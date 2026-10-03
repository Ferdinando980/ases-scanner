from __future__ import annotations
from pathlib import Path
import re
from .filesystem import iter_owned_files
from .common import line_of
from ..source_roles import classify_source
from ..model import FactGraph, Node, Edge, Evidence

SCRIPT_EXTS={'.js','.jsx','.ts','.tsx','.vue','.svelte'}
TEMPLATE_EXTS={'.html','.htm','.jsp','.hbs','.ejs','.pug','.twig'}


def scan_frontend(root: Path) -> FactGraph:
    graph=FactGraph(); modules={}; records=[]
    for p in iter_owned_files(root):
        rel=p.relative_to(root).as_posix(); meta=classify_source(rel, root)
        if meta['scope']!='frontend' or meta['role']!='OWNED_SOURCE': continue
        ext=p.suffix.lower()
        if ext not in SCRIPT_EXTS|TEMPLATE_EXTS: continue
        text=p.read_text(encoding='utf-8',errors='ignore')
        if (root/'angular.json').is_file() and p.name.endswith('.routes.ts'):
            for route in re.finditer(r'(?<!\w)path\s*:\s*["\']([^"\']*)["\']',text):
                declared=route.group(1)
                ev=[f'{rel}:{line_of(text,route.start())}']
                graph.add_node(Node(f'frontend-route:{rel}:{line_of(text,route.start())}:{route.start()}',
                    'frontend_route',declared or '/',rel,{
                        'scope':'frontend','framework':'Angular','declared_path':declared,
                        'source_role':meta['role']},Evidence(evidence=ev)))
        if ext in TEMPLATE_EXTS:
            nid=f'frontend-template:{rel}'
            graph.add_node(Node(nid,'frontend_template',p.stem,rel,{
                'scope':'frontend','source_role':meta['role'],
                'framework':'Thymeleaf' if re.search(r'\bth:[\w-]+=',text) else ('Angular' if (root/'angular.json').is_file() and rel.startswith('src/app/') else 'template')
            },Evidence(evidence=[rel])))
            _form_calls(graph,rel,text,nid)
            continue

        kind=_script_kind(p,text)
        nid=f'frontend:{kind}:{rel}'
        graph.add_node(Node(nid,kind,p.stem,rel,{
            'scope':'frontend','source_role':meta['role'],'lines':text.count('\n')+1,
            'framework':'Angular' if (root/'angular.json').is_file() and rel.startswith('src/app/') else None,
            'has_state':bool(re.search(r'\b(useState|useReducer|createStore|writable\s*\(|ref\s*\(|reactive\s*\()',text)),
            'has_validation':bool(re.search(r'(?i)\b(validate|validation|required|invalid|errorMessage|errors\b)',text)),
        },Evidence(evidence=[rel])))
        modules[p.stem.lower()]=nid; records.append((p,rel,text,nid,kind))
        _script_calls(graph,rel,text,nid)

    # Lightweight service/import relationships; no bundler-specific resolver.
    service_by_stem={n.name.lower():n.id for n in graph.nodes if n.kind=='frontend_service'}
    for p,rel,text,nid,kind in records:
        for imp in re.findall(r'(?:from\s+|require\s*\()\s*["\']([^"\']+)',text):
            stem=Path(imp).name.lower()
            for suffix in ('.tsx','.jsx','.ts','.js'):
                if stem.endswith(suffix):
                    stem=stem[:-len(suffix)]
                    break
            target=service_by_stem.get(stem)
            if target:
                graph.add_edge(Edge(nid,target,'depends_on',[rel]))
    return graph


def _script_kind(path: Path,text: str) -> str:
    stem=path.stem.lower()
    if any(x in stem for x in ('service','api','client','gateway')) and _has_remote(text): return 'frontend_service'
    if any(x in stem for x in ('store','state')) and re.search(r'(?i)redux|zustand|pinia|createStore|writable\s*\(',text): return 'frontend_store'
    if path.suffix.lower() in {'.jsx','.tsx','.vue','.svelte'} or re.search(r'@Component\b|\bReact\.Component\b|\bfunction\s+[A-Z]\w*\s*\([^)]*\)\s*{[^{}]{0,800}return\s*\(',text,re.S):
        return 'frontend_component'
    return 'frontend_module'


def _has_remote(text:str)->bool:
    return bool(re.search(r'\bfetch\s*\(|\baxios\.|\bXMLHttpRequest\b|\$\.ajax\s*\(|\bHttpClient\b',text))


def _script_calls(graph,rel,text,owner):
    seen=set()
    patterns=[]

    for m in re.finditer(r'\bfetch\s*\(\s*["\']([^"\']+)["\'](?P<tail>.{0,260}?)\)',text,re.S):
        meth=re.search(r'(?i)\bmethod\s*:\s*["\'](GET|POST|PUT|PATCH|DELETE)["\']',m.group('tail') or '')
        patterns.append((m, meth.group(1).upper() if meth else 'GET', m.group(1)))

    patterns += [(m, m.group(1).upper(), m.group(2)) for m in re.finditer(r'\baxios\.(get|post|put|patch|delete)\s*\(\s*["\']([^"\']+)["\']',text,re.I)]
    patterns += [(m, m.group(1).upper(), m.group(2)) for m in re.finditer(r'\b(?:this\.)?http\s*\.\s*(get|post|put|patch|delete)(?:<[^\n]{0,160}?>)?\s*\(\s*["\']([^"\']+)["\'](?!\s*\+)',text,re.I)]
    for m,method,path in patterns:
        key=(method,path,m.start())
        if key in seen: continue
        seen.add(key); _add_call(graph,rel,text,owner,method,path,m.start(),'script')

    for m in re.finditer(r'\$\.ajax\s*\(\s*\{([^}]{0,1200})\}',text,re.S):
        body=m.group(1); u=re.search(r'url\s*:\s*["\']([^"\']+)["\']',body); meth=re.search(r'(?:type|method)\s*:\s*["\']([^"\']+)["\']',body,re.I)
        if u: _add_call(graph,rel,text,owner,(meth.group(1).upper() if meth else 'GET'),u.group(1),m.start(),'ajax')


def _form_calls(graph,rel,text,owner):
    for m in re.finditer(r'<form\b([^>]*)>',text,re.I|re.S):
        attrs=m.group(1); action=re.search(r'\baction\s*=\s*["\']([^"\']+)["\']',attrs,re.I); method=re.search(r'\bmethod\s*=\s*["\']([^"\']+)["\']',attrs,re.I)
        if action:
            value=action.group(1)
            if value.startswith('@{'):
                value=value[2:].split('(',1)[0].rstrip('}')
            if not value.startswith(('${','#')) and value:
                _add_call(graph,rel,text,owner,(method.group(1).upper() if method else 'GET'),value,m.start(),'form')


def _add_call(graph,rel,text,owner,method,path,pos,source):
    external=bool(re.match(r'https?://',path,re.I))
    cid=f'frontend-call:{method}:{path}:{rel}:{line_of(text,pos)}'
    ev=[f'{rel}:{line_of(text,pos)}']
    graph.add_node(Node(cid,'frontend_api_call',f'{method} {path}',rel,{
        'scope':'frontend','http_method':method,'path':path,'external':external,'source':source,'owner':owner
    },Evidence(evidence=ev)))
    graph.add_edge(Edge(owner,cid,'calls_api',ev))

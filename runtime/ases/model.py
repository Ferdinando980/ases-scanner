from __future__ import annotations
from dataclasses import dataclass, asdict, field
from typing import Any

@dataclass
class Evidence:
    state: str = "OBSERVED"
    confidence: str = "high"
    evidence: list[str] = field(default_factory=list)

@dataclass
class Node:
    id: str
    kind: str
    name: str
    path: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    provenance: Evidence = field(default_factory=Evidence)

@dataclass
class Edge:
    source: str
    target: str
    relation: str
    evidence: list[str] = field(default_factory=list)

@dataclass
class FactGraph:
    nodes: list[Node] = field(default_factory=list)
    edges: list[Edge] = field(default_factory=list)

    def add_node(self, node: Node) -> None:
        if all(existing.id != node.id for existing in self.nodes):
            self.nodes.append(node)

    def add_edge(self, edge: Edge) -> None:
        key = edge.source, edge.target, edge.relation
        if all((existing.source, existing.target, existing.relation) != key for existing in self.edges):
            self.edges.append(edge)

    def merge(self, other: "FactGraph") -> "FactGraph":
        for n in other.nodes:
            self.add_node(n)
        for e in other.edges:
            self.add_edge(e)
        return self

    def to_dict(self) -> dict:
        return {
            "nodes": [asdict(n) for n in self.nodes],
            "edges": [asdict(e) for e in self.edges],
        }

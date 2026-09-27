# Recovered SDD — Progetto-JustInTime

> Evidence-based reconstruction of the current implementation.

## Architecture overview
### Class
- JustInTimeApplicationTests — OBSERVED / high / ProgettoIs JustInTime/src/test/java/com/justInTime/demo/JustInTimeApplicationTests.java:6
- FeedBackServiceTest — OBSERVED / high / ProgettoIs JustInTime/src/test/java/com/justInTime/Service/FeedBackServiceTest.java:19
- PartitaConfigServiceTest — OBSERVED / high / ProgettoIs JustInTime/src/test/java/com/justInTime/Service/PartitaConfigServiceTest.java:36
- UtenzaServiceTest — OBSERVED / high / ProgettoIs JustInTime/src/test/java/com/justInTime/Service/UtenzaServiceTest.java:28
- SpringBootJspApplication — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/SpringBootJspApplication.java:9
- SessionUtil — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/SessionUtil.java:9
- FullPlayerDataDTO — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/DTO/FullPlayerDataDTO.java:5
- FullPlayerDataDTOPsw — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/DTO/FullPlayerDataDTOPsw.java:5
- LoginResponse — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/DTO/LoginResponse.java:3
- paeseUtenzaDTO — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/DTO/paeseUtenzaDTO.java:3
- PlayerRecord — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/DTO/PlayerRecord.java:4
- SinglePlayerDataDTO — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/DTO/SinglePlayerDataDTO.java:4
- Carta — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/Carta.java:6
- Mazzo — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/Mazzo.java:6
- MazzoFactory — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/MazzoFactory.java:3
- MazzoPesca — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/MazzoPesca.java:11
- MazzoScarto — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/MazzoScarto.java:7
### Component
- EndGameState — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/EndGameState.java:16
- PauseState — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/PauseState.java:11
- StartGameState — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/StartGameState.java:9
- TurnState — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/TurnState.java:16
### Configuration
- AsyncConfig — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/config/AsyncConfig.java:6
### Controller
- AuthController — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/AuthController.java:16
- ClassificaController — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/ClassificaController.java:15
- FeedbackController — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/FeedbackController.java:18
- PagesController — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:11
- PartitaConfigController — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:25
- PartitaController — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:21
- PlayerController — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PlayerController.java:18
- UtenzaController — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:22
### Repository
- FeedbackRepository — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/repository/FeedbackRepository.java:9
- PlayerRepository — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/repository/PlayerRepository.java:14
- UtenzaRepository — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/repository/UtenzaRepository.java:13
### Service
- ClassificaService — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/service/ClassificaService.java:17
- FeedbackService — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/service/FeedbackService.java:11
- MazzoPescaService — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/service/MazzoPescaService.java:10
- MazzoScartoService — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/service/MazzoScartoService.java:8
- PartitaConfigService — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/service/PartitaConfigService.java:24
- PartitaService — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/service/PartitaService.java:26
- PlayerService — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/service/PlayerService.java:11
- UtenzaPlayerService — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/service/UtenzaPlayerService.java:11
- UtenzaService — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/service/UtenzaService.java:18

## Persistence / data
- Achievements — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/Achievements.java:14
- Feedback — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/Feedback.java:12
- Partita — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/Partita.java:20
- Player — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/Player.java:20
- Utente — OBSERVED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/model/Utente.java:9

## Trust boundaries
- External caller → application HTTP boundary — INFERRED / high / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/AuthController.java:31, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/AuthController.java:55, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/AuthController.java:82, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/AuthController.java:91, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/ClassificaController.java:26, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/ClassificaController.java:33, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/ClassificaController.java:38, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/FeedbackController.java:33, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/FeedbackController.java:45, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:100, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:108, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:116, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:124, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:132, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:14, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:140, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:22, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:30, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:40, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:48, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:71, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:76, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:84, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:92, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:110, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:137, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:151, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:38, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:54, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:71, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:76, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:86, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:107, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:129, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:145, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:168, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:189, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:215, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:245, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:282, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:38, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:61, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:94, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PlayerController.java:36, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PlayerController.java:49, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:32, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:40, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:46, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:55, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:60, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:66, ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:82

## Conflicts and unknowns
- Original stakeholder intent is not recoverable from code alone.

# Recovered RAD — Progetto-JustInTime

> Recovered requirements describe current observed/inferred behavior, not original stakeholder intent unless explicitly confirmed.

## Actors
- External caller — INFERRED / medium / ProgettoIs JustInTime/src/main/java/com/justInTime/controller/AuthController.java:31

## Recovered functional behavior
### POST //registrazione
- State: OBSERVED
- Actor: External caller
- Trigger: POST //registrazione
- Main flow: route:POST://registrazione:com.justInTime.controller.AuthController#registraUtente → method:com.justInTime.controller.AuthController#registraUtente:31 → type:com.justInTime.service.UtenzaService → method-name:UtenzaService#registerUser → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/AuthController.java:31

### POST //login
- State: OBSERVED
- Actor: External caller
- Trigger: POST //login
- Main flow: route:POST://login:com.justInTime.controller.AuthController#login → method:com.justInTime.controller.AuthController#login:55 → type:com.justInTime.service.UtenzaService → method-name:UtenzaService#login → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/AuthController.java:55

### GET //logout
- State: OBSERVED
- Actor: External caller
- Trigger: GET //logout
- Main flow: route:GET://logout:com.justInTime.controller.AuthController#logout → method:com.justInTime.controller.AuthController#logout:82
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/AuthController.java:82

### POST //resetIsPageOpen
- State: OBSERVED
- Actor: External caller
- Trigger: POST //resetIsPageOpen
- Main flow: route:POST://resetIsPageOpen:com.justInTime.controller.AuthController#resetIsPageOpen → method:com.justInTime.controller.AuthController#resetIsPageOpen:91
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/AuthController.java:91

### GET /classifica/locale
- State: OBSERVED
- Actor: External caller
- Trigger: GET /classifica/locale
- Main flow: route:GET:/classifica/locale:com.justInTime.controller.ClassificaController#getClassificaLocale → method:com.justInTime.controller.ClassificaController#getClassificaLocale:26 → type:com.justInTime.service.ClassificaService → method-name:ClassificaService#getClassificaLocale → type:com.justInTime.repository.PlayerRepository
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/ClassificaController.java:26

### GET /classifica
- State: OBSERVED
- Actor: External caller
- Trigger: GET /classifica
- Main flow: route:GET:/classifica:com.justInTime.controller.ClassificaController#getClassifica → method:com.justInTime.controller.ClassificaController#getClassifica:33 → type:com.justInTime.service.ClassificaService → method-name:ClassificaService#getClassifica → type:com.justInTime.repository.PlayerRepository
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/ClassificaController.java:33

### GET /classifica/singlePlayerData
- State: OBSERVED
- Actor: External caller
- Trigger: GET /classifica/singlePlayerData
- Main flow: route:GET:/classifica/singlePlayerData:com.justInTime.controller.ClassificaController#getSinglePlayerRecord → method:com.justInTime.controller.ClassificaController#getSinglePlayerRecord:38 → type:com.justInTime.service.ClassificaService → method-name:ClassificaService#getSinglePlayer → type:com.justInTime.repository.PlayerRepository
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/ClassificaController.java:38

### GET /feedback
- State: OBSERVED
- Actor: External caller
- Trigger: GET /feedback
- Main flow: route:GET:/feedback:com.justInTime.controller.FeedbackController#getAllFeedback → method:com.justInTime.controller.FeedbackController#getAllFeedback:33 → type:com.justInTime.service.FeedbackService → method-name:FeedbackService#getAllFeedback → type:com.justInTime.repository.FeedbackRepository
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/FeedbackController.java:33

### POST /feedback
- State: OBSERVED
- Actor: External caller
- Trigger: POST /feedback
- Main flow: route:POST:/feedback:com.justInTime.controller.FeedbackController#creaFeedback → method:com.justInTime.controller.FeedbackController#creaFeedback:45 → type:com.justInTime.service.FeedbackService → method-name:FeedbackService#creaFeedback → type:com.justInTime.repository.FeedbackRepository
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/FeedbackController.java:45

### GET /
- State: OBSERVED
- Actor: External caller
- Trigger: GET /
- Main flow: route:GET:/:com.justInTime.controller.PagesController#viewHome → method:com.justInTime.controller.PagesController#viewHome:14
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:14

### GET /login
- State: OBSERVED
- Actor: External caller
- Trigger: GET /login
- Main flow: route:GET:/login:com.justInTime.controller.PagesController#login → method:com.justInTime.controller.PagesController#login:22
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:22

### GET /registrazione
- State: OBSERVED
- Actor: External caller
- Trigger: GET /registrazione
- Main flow: route:GET:/registrazione:com.justInTime.controller.PagesController#register → method:com.justInTime.controller.PagesController#register:30
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:30

### GET /achievements
- State: OBSERVED
- Actor: External caller
- Trigger: GET /achievements
- Main flow: route:GET:/achievements:com.justInTime.controller.PagesController#achievements → method:com.justInTime.controller.PagesController#achievements:40
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:40

### GET /prepartita
- State: OBSERVED
- Actor: External caller
- Trigger: GET /prepartita
- Main flow: route:GET:/prepartita:com.justInTime.controller.PagesController#prepartita → method:com.justInTime.controller.PagesController#prepartita:48
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:48

### GET /rules
- State: OBSERVED
- Actor: External caller
- Trigger: GET /rules
- Main flow: route:GET:/rules:com.justInTime.controller.PagesController#rules → method:com.justInTime.controller.PagesController#rules:71
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:71

### GET /classificaGlobale
- State: OBSERVED
- Actor: External caller
- Trigger: GET /classificaGlobale
- Main flow: route:GET:/classificaGlobale:com.justInTime.controller.PagesController#classificaGlobale → method:com.justInTime.controller.PagesController#classificaGlobale:76
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:76

### GET /classificaLocale
- State: OBSERVED
- Actor: External caller
- Trigger: GET /classificaLocale
- Main flow: route:GET:/classificaLocale:com.justInTime.controller.PagesController#classificaLocale → method:com.justInTime.controller.PagesController#classificaLocale:84
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:84

### GET /consultazioneProfilo
- State: OBSERVED
- Actor: External caller
- Trigger: GET /consultazioneProfilo
- Main flow: route:GET:/consultazioneProfilo:com.justInTime.controller.PagesController#consultazioneProfilo → method:com.justInTime.controller.PagesController#consultazioneProfilo:92
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:92

### GET /userHomepage
- State: OBSERVED
- Actor: External caller
- Trigger: GET /userHomepage
- Main flow: route:GET:/userHomepage:com.justInTime.controller.PagesController#userHomepage → method:com.justInTime.controller.PagesController#userHomepage:100
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:100

### GET /modifyaccount
- State: OBSERVED
- Actor: External caller
- Trigger: GET /modifyaccount
- Main flow: route:GET:/modifyaccount:com.justInTime.controller.PagesController#modifyaccount → method:com.justInTime.controller.PagesController#modifyaccount:108
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:108

### GET /endmatch
- State: OBSERVED
- Actor: External caller
- Trigger: GET /endmatch
- Main flow: route:GET:/endmatch:com.justInTime.controller.PagesController#endmatch → method:com.justInTime.controller.PagesController#endmatch:116
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:116

### GET /match
- State: OBSERVED
- Actor: External caller
- Trigger: GET /match
- Main flow: route:GET:/match:com.justInTime.controller.PagesController#match → method:com.justInTime.controller.PagesController#match:124
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:124

### GET /startmatch
- State: OBSERVED
- Actor: External caller
- Trigger: GET /startmatch
- Main flow: route:GET:/startmatch:com.justInTime.controller.PagesController#startmatch → method:com.justInTime.controller.PagesController#startmatch:132
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:132

### GET /feedbacks
- State: OBSERVED
- Actor: External caller
- Trigger: GET /feedbacks
- Main flow: route:GET:/feedbacks:com.justInTime.controller.PagesController#feedback → method:com.justInTime.controller.PagesController#feedback:140
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PagesController.java:140

### POST /api/game-config/add-player-login
- State: OBSERVED
- Actor: External caller
- Trigger: POST /api/game-config/add-player-login
- Main flow: route:POST:/api/game-config/add-player-login:com.justInTime.controller.PartitaConfigController#addPlayerLogin → method:com.justInTime.controller.PartitaConfigController#addPlayerLogin:38 → type:com.justInTime.service.PartitaConfigService → method-name:PartitaConfigService#aggiungiGiocatoreConfig → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.UtenzaService → type:com.justInTime.service.PlayerService → type:com.justInTime.service.PartitaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:38

### GET /api/game-config/getSessionUser
- State: OBSERVED
- Actor: External caller
- Trigger: GET /api/game-config/getSessionUser
- Main flow: route:GET:/api/game-config/getSessionUser:com.justInTime.controller.PartitaConfigController#getSessionUser → method:com.justInTime.controller.PartitaConfigController#getSessionUser:54
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:54

### GET /api/game-config/path
- State: OBSERVED
- Actor: External caller
- Trigger: GET /api/game-config/path
- Main flow: route:GET:/api/game-config/path:com.justInTime.controller.PartitaConfigController#getMethodName → method:com.justInTime.controller.PartitaConfigController#getMethodName:71
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:71

### DELETE /api/game-config/remove-player
- State: OBSERVED
- Actor: External caller
- Trigger: DELETE /api/game-config/remove-player
- Main flow: route:DELETE:/api/game-config/remove-player:com.justInTime.controller.PartitaConfigController#removePlayer → method:com.justInTime.controller.PartitaConfigController#removePlayer:76 → type:com.justInTime.service.PartitaConfigService → method-name:PartitaConfigService#rimuoviGiocatore → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.UtenzaService → type:com.justInTime.service.PlayerService → type:com.justInTime.service.PartitaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:76

### GET /api/game-config/players
- State: OBSERVED
- Actor: External caller
- Trigger: GET /api/game-config/players
- Main flow: route:GET:/api/game-config/players:com.justInTime.controller.PartitaConfigController#getConfiguredPlayers → method:com.justInTime.controller.PartitaConfigController#getConfiguredPlayers:86 → type:com.justInTime.service.PartitaConfigService → method-name:PartitaConfigService#getGiocatoriInConfigurazione → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.UtenzaService → type:com.justInTime.service.PlayerService → type:com.justInTime.service.PartitaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:86

### POST /api/game-config/create-and-start
- State: OBSERVED
- Actor: External caller
- Trigger: POST /api/game-config/create-and-start
- Main flow: route:POST:/api/game-config/create-and-start:com.justInTime.controller.PartitaConfigController#createAndStartGame → method:com.justInTime.controller.PartitaConfigController#createAndStartGame:110 → type:com.justInTime.service.PartitaConfigService → method-name:PartitaConfigService#creaPartita → type:com.justInTime.service.PartitaService → method-name:PartitaService#iniziaPartitaAsync → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.UtenzaService → type:com.justInTime.service.PlayerService → type:com.justInTime.model.GameState → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:110

### GET /api/game-config/match-status
- State: OBSERVED
- Actor: External caller
- Trigger: GET /api/game-config/match-status
- Main flow: route:GET:/api/game-config/match-status:com.justInTime.controller.PartitaConfigController#getPartitaStatus → method:com.justInTime.controller.PartitaConfigController#getPartitaStatus:137 → type:com.justInTime.service.PartitaService → method-name:PartitaService#isFinished → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:137

### POST /api/game-config/play-again
- State: OBSERVED
- Actor: External caller
- Trigger: POST /api/game-config/play-again
- Main flow: route:POST:/api/game-config/play-again:com.justInTime.controller.PartitaConfigController#playAgain → method:com.justInTime.controller.PartitaConfigController#playAgain:151 → type:com.justInTime.service.PartitaConfigService → method-name:PartitaConfigService#creaNuovaPartitaDaPartitaPrecedente → type:com.justInTime.service.PartitaService → method-name:PartitaService#iniziaPartita → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.UtenzaService → type:com.justInTime.service.PlayerService → type:com.justInTime.model.GameState → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaConfigController.java:151

### POST /game/play-card/{cartaIndex}
- State: OBSERVED
- Actor: External caller
- Trigger: POST /game/play-card/{cartaIndex}
- Main flow: route:POST:/game/play-card/{cartaIndex}:com.justInTime.controller.PartitaController#playCard → method:com.justInTime.controller.PartitaController#playCard:38 → type:com.justInTime.service.PartitaService → method-name:PartitaService#getPartita → method-name:PartitaService#giocaCarta → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:38

### POST /game/pesca-carta
- State: OBSERVED
- Actor: External caller
- Trigger: POST /game/pesca-carta
- Main flow: route:POST:/game/pesca-carta:com.justInTime.controller.PartitaController#pescaCarta → method:com.justInTime.controller.PartitaController#pescaCarta:61 → type:com.justInTime.service.PartitaService → method-name:PartitaService#getPartita → method-name:PartitaService#pescaCarta → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:61

### POST /game/termina-partita
- State: OBSERVED
- Actor: External caller
- Trigger: POST /game/termina-partita
- Main flow: route:POST:/game/termina-partita:com.justInTime.controller.PartitaController#terminaPartita → method:com.justInTime.controller.PartitaController#terminaPartita:94 → type:com.justInTime.service.PartitaService → method-name:PartitaService#getPartita → method-name:PartitaService#terminaPartita → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:94

### POST /game/playerMano
- State: OBSERVED
- Actor: External caller
- Trigger: POST /game/playerMano
- Main flow: route:POST:/game/playerMano:com.justInTime.controller.PartitaController#getGiocatoreCorrenteMano → method:com.justInTime.controller.PartitaController#getGiocatoreCorrenteMano:107 → type:com.justInTime.service.PartitaService → method-name:PartitaService#getPartita → method-name:PartitaService#getGiocatoreCorrenteMano → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:107

### POST /game/nextPlayerReady
- State: OBSERVED
- Actor: External caller
- Trigger: POST /game/nextPlayerReady
- Main flow: route:POST:/game/nextPlayerReady:com.justInTime.controller.PartitaController#nextPlayerReady → method:com.justInTime.controller.PartitaController#nextPlayerReady:129 → type:com.justInTime.service.PartitaService → method-name:PartitaService#getPartita → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:129

### POST /game/PlayerReady
- State: OBSERVED
- Actor: External caller
- Trigger: POST /game/PlayerReady
- Main flow: route:POST:/game/PlayerReady:com.justInTime.controller.PartitaController#PlayerReady → method:com.justInTime.controller.PartitaController#PlayerReady:145 → type:com.justInTime.service.PartitaService → method-name:PartitaService#getPartita → method-name:PartitaService#playerReady → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:145

### GET /game/timer
- State: OBSERVED
- Actor: External caller
- Trigger: GET /game/timer
- Main flow: route:GET:/game/timer:com.justInTime.controller.PartitaController#getTimerPlayer → method:com.justInTime.controller.PartitaController#getTimerPlayer:168 → type:com.justInTime.service.PartitaService → method-name:PartitaService#getPartita → method-name:PartitaService#getCurrentPlayerTimer → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:168

### GET /game/nameIndexPlayer
- State: OBSERVED
- Actor: External caller
- Trigger: GET /game/nameIndexPlayer
- Main flow: route:GET:/game/nameIndexPlayer:com.justInTime.controller.PartitaController#getNameINdexPlayer → method:com.justInTime.controller.PartitaController#getNameINdexPlayer:189 → type:com.justInTime.service.PartitaService → method-name:PartitaService#getPartita → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:189

### GET /game/last-discarded-card
- State: OBSERVED
- Actor: External caller
- Trigger: GET /game/last-discarded-card
- Main flow: route:GET:/game/last-discarded-card:com.justInTime.controller.PartitaController#lastDiscardedCard → method:com.justInTime.controller.PartitaController#lastDiscardedCard:215 → type:com.justInTime.service.PartitaService → method-name:PartitaService#getPartita → method-name:PartitaService#getLastCardScarto → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:215

### POST /game/nextPlayer
- State: OBSERVED
- Actor: External caller
- Trigger: POST /game/nextPlayer
- Main flow: route:POST:/game/nextPlayer:com.justInTime.controller.PartitaController#goNextPlayer → method:com.justInTime.controller.PartitaController#goNextPlayer:245 → type:com.justInTime.service.PartitaService → method-name:PartitaService#getPartita → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:245

### POST /game/nextPlayer2
- State: OBSERVED
- Actor: External caller
- Trigger: POST /game/nextPlayer2
- Main flow: route:POST:/game/nextPlayer2:com.justInTime.controller.PartitaController#goNextPlayer2 → method:com.justInTime.controller.PartitaController#goNextPlayer2:282 → type:com.justInTime.service.PartitaConfigService → method-name:PartitaConfigService#getGiocatoriInConfigurazione → type:com.justInTime.repository.PartitaRepository → type:com.justInTime.service.UtenzaService → type:com.justInTime.service.PlayerService → type:com.justInTime.service.PartitaService → type:com.justInTime.model.GameState → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService → type:com.justInTime.service.MazzoScartoService → type:com.justInTime.service.MazzoPescaService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PartitaController.java:282

### GET /giocatore/{playerId}
- State: OBSERVED
- Actor: External caller
- Trigger: GET /giocatore/{playerId}
- Main flow: route:GET:/giocatore/{playerId}:com.justInTime.controller.PlayerController#trovaGiocatore → method:com.justInTime.controller.PlayerController#trovaGiocatore:36 → type:com.justInTime.service.PlayerService → method-name:PlayerService#trovaGiocatore → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService → type:com.justInTime.repository.UtenzaRepository
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PlayerController.java:36

### GET /giocatore/tutti
- State: OBSERVED
- Actor: External caller
- Trigger: GET /giocatore/tutti
- Main flow: route:GET:/giocatore/tutti:com.justInTime.controller.PlayerController#trovaTuttiGiocatori → method:com.justInTime.controller.PlayerController#trovaTuttiGiocatori:49 → type:com.justInTime.service.PlayerService → method-name:PlayerService#trovaTuttiGiocatori → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService → type:com.justInTime.repository.UtenzaRepository
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/PlayerController.java:49

### POST /utenze
- State: OBSERVED
- Actor: External caller
- Trigger: POST /utenze
- Main flow: route:POST:/utenze:com.justInTime.controller.UtenzaController#creaUtenza → method:com.justInTime.controller.UtenzaController#creaUtenza:32 → type:com.justInTime.service.UtenzaService → method-name:UtenzaService#creaUtente → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:32

### GET /utenze/trovaUtenza
- State: OBSERVED
- Actor: External caller
- Trigger: GET /utenze/trovaUtenza
- Main flow: route:GET:/utenze/trovaUtenza:com.justInTime.controller.UtenzaController#trovaUtenza → method:com.justInTime.controller.UtenzaController#trovaUtenza:40 → type:com.justInTime.service.UtenzaService → method-name:UtenzaService#trovaUtenteNoPsw → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:40

### GET /utenze/trovaUtenzaPsw
- State: OBSERVED
- Actor: External caller
- Trigger: GET /utenze/trovaUtenzaPsw
- Main flow: route:GET:/utenze/trovaUtenzaPsw:com.justInTime.controller.UtenzaController#trovaUtenzaPsw → method:com.justInTime.controller.UtenzaController#trovaUtenzaPsw:46 → type:com.justInTime.service.UtenzaService → method-name:UtenzaService#trovaUtenteConPsw → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:46

### GET /utenze/trovaUtenzaPaese
- State: OBSERVED
- Actor: External caller
- Trigger: GET /utenze/trovaUtenzaPaese
- Main flow: route:GET:/utenze/trovaUtenzaPaese:com.justInTime.controller.UtenzaController#trovaUtenzaPaese → method:com.justInTime.controller.UtenzaController#trovaUtenzaPaese:55 → type:com.justInTime.service.UtenzaService → method-name:UtenzaService#trovaUtentePaese → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:55

### GET /utenze/trovaTutteUtenze
- State: OBSERVED
- Actor: External caller
- Trigger: GET /utenze/trovaTutteUtenze
- Main flow: route:GET:/utenze/trovaTutteUtenze:com.justInTime.controller.UtenzaController#trovaTutteUtenze → method:com.justInTime.controller.UtenzaController#trovaTutteUtenze:60 → type:com.justInTime.service.UtenzaService → method-name:UtenzaService#trovaTutteUtenze → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:60

### PUT /utenze/modificautenza
- State: OBSERVED
- Actor: External caller
- Trigger: PUT /utenze/modificautenza
- Main flow: route:PUT:/utenze/modificautenza:com.justInTime.controller.UtenzaController#aggiornaUtenza → method:com.justInTime.controller.UtenzaController#aggiornaUtenza:66 → type:com.justInTime.service.UtenzaService → method-name:UtenzaService#aggiornaUtente → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:66

### DELETE /utenze/rimuoviUtenza
- State: OBSERVED
- Actor: External caller
- Trigger: DELETE /utenze/rimuoviUtenza
- Main flow: route:DELETE:/utenze/rimuoviUtenza:com.justInTime.controller.UtenzaController#eliminaUtenza → method:com.justInTime.controller.UtenzaController#eliminaUtenza:82 → type:com.justInTime.service.UtenzaService → method-name:UtenzaService#eliminaUtente → type:com.justInTime.repository.UtenzaRepository → type:com.justInTime.service.PlayerService → type:com.justInTime.repository.PlayerRepository → type:com.justInTime.service.UtenzaPlayerService
- Evidence: ProgettoIs JustInTime/src/main/java/com/justInTime/controller/UtenzaController.java:82

## Unknown original requirements
- Original stakeholder intent is not recoverable from code alone.

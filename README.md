# tatum24
 # Autenticazione e Profilo Utente
L'applicazione permette l'accesso a tre tipologie di utenti: utente non registrato, utente registrato (normale) e moderatore (sottoclasse di utente registrato).

- Un utente registrato potrà aggiungere nuovi snippet, modificare i propri, salvarli (attraverso un meccanismo che sfrutta i segnalibri) e mettere like o dislike.
- Un utente moderatore avrà la possibilità di controllare il comportamento degli utenti che accedono all'applicazione. Ad esempio, potrà eliminare o modificare qualsiasi snippet.
- Un utente non registrato potrà solo visionare gli snippet esistenti.

# Gestione degli Snippet
Gli snippet di codice creati dagli utenti registrati potranno essere visionati, con _syntax highlighting_ in base al linguaggio di programmazione utilizzato. Il sito web disporrà di una sezione per visionare tutti gli snippet creati, con una funzione di ricerca per "titolo". Inoltre, gli snippet verranno catalogati solo per linguaggio di programmazione. I linguaggi di programmazione sono statici e immutabili, solo un amministratore (dalla rispettiva interfaccia) potrà aggiungerne o modificarli.

# Visualizzazione delle Statistiche
Tutti gli utenti devono poter visualizzare due liste: la prima relativa agli **autori che hanno scritto più snippet** e la seconda relativa ai **linguaggi di programmazione più frequenti**.

# Gestione dei Segnalibri
Gli **utenti registrati** potranno **modificare** i propri **segnalibri** (relativi a snippet) e **vedere** i propri **segnalibri** (snippet salvati). Un qualsiasi utente potrà visualizzare una classifica generale degli snippet più salvati.

# Valutazione degli Snippet (Rating System)
Gli utenti registrati devono poter **valutare (like/dislike)** gli snippet di codice. Verrà generata una classifica dei **Top-Rated Snippet**. Non si intende valutare gli snippet di codice tra di loro, la funzione di rating inserita (like/dislike) permetterà agli utenti di avere una valutazione qualitativa immediata (garantita dal numero di like) sulla correttezza e efficienza del codice.

**Ulteriore implementazione: funzionalità per commenti sotto gli snippet?**


pip install pigments
pip install markdown

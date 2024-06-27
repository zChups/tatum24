# tatum24
 



\section*{Autenticazione e Profilo Utente}
L'applicazione permette l'accesso a tre tipologie di utenti: utente non registrato, utente registrato (normale) e moderatore (sottoclasse di utente registrato).
\begin{itemize}
    \item Un utente registrato potrà aggiungere nuovi snippet, modificare i propri, salvarli (attraverso un meccanismo che sfrutta i segnalibri) e mettere like o dislike. 
    \item Un utente moderatore avrà la possibilità di controllare il comportamento degli utenti che accedono all'applicazione. Ad esempio, potrà eliminare o modificare qualsiasi snippet.
    \item Un utente non registrato potrà solo visionare gli snippet esistenti.
\end{itemize}

\section*{Gestione degli Snippet}
Gli snippet di codice creati dagli utenti registrati potranno essere visionati, con \textit{syntax highlighting} in base al linguaggio di programmazione utilizzato. Il sito web disporrà di una sezione per visionare tutti gli snippet creati, con una funzione di ricerca per "titolo". Inoltre, gli snippet verranno catalogati solo per linguaggio di programmazione. I linguaggi di programmazione sono statici e immutabili, solo un amministratore (dalla rispettiva interfaccia) potrà aggiungerne o modificarli.

\section*{Visualizzazione delle Statistiche}
Tutti gli utenti devono poter visualizzare due liste: la prima relativa agli \textbf{autori che hanno scritto più snippet} e la seconda relativa ai \textbf{linguaggi di programmazione più frequenti}.

\section*{Gestione dei Segnalibri}
Gli \textbf{utenti registrati} potranno \textbf{modificare} i propri \textbf{segnalibri} (relativi a snippet) e \textbf{vedere} i propri \textbf{segnalibri} (snippet salvati). Un qualsiasi utente potrà visualizzare una classifica generale degli snippet più salvati.

\section*{Valutazione degli Snippet (Rating System)}
Gli utenti registrati devono poter \textbf{valutare (like/dislike)} gli snippet di codice. Verrà generata una classifica dei \textbf{Top-Rated Snippet}. Non si intende valutare gli snippet di codice tra di loro, la funzione di rating inserita (like/dislike) permetterà agli utenti di avere una valutazione qualitativa immediata (garantita dal numero di like) sulla correttezza e efficienza del codice.\\\textbf{Ulteriore implementazione: funzionalità per commenti sotto gli snippet?}



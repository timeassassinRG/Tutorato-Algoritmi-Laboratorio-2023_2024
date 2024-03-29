1. **Dijkstra**
   - **Limiti applicativi**: L'algoritmo di Dijkstra funziona su grafi con pesi non negativi. Non può essere utilizzato per grafi con archi aventi peso negativo poiché potrebbe non terminare o dare risultati errati.
   - **Complessità asintotica**:
     - Con **matrice di adiacenza**: \(O(V^2)\), dove \(V\) è il numero di vertici.
     - Con **lista di adiacenza** e coda con priorità (heap binario): \(O((V + E) \log V)\), dove \(E\) è il numero di archi.

2. **Bellman-Ford**
   - **Limiti applicativi**: L'algoritmo di Bellman-Ford gestisce pesi negativi e può rilevare cicli di peso negativo nel grafo. È più versatile rispetto a Dijkstra ma generalmente più lento.
   - **Complessità asintotica**:
     - Sia con **matrice di adiacenza** che con **lista di adiacenza**: \(O(V*E)\).

3. **DAG Shortest Path**
   - **Limiti applicativi**: Questo algoritmo si applica solo ai grafi diretti aciclici (DAG). È molto efficiente in questo contesto poiché sfrutta l'assenza di cicli per ottimizzare il calcolo dei cammini minimi.
   - **Complessità asintotica**:
     - Sia con **matrice di adiacenza** che con **lista di adiacenza**: \(O(V+E)\), che deriva dal fatto che ogni vertice e ogni arco viene esplorato una sola volta.

4. **Algoritmo A***
   - **Limiti applicativi**: Utilizzato per la ricerca del cammino minimo in spazi di ricerca grafici ponderati e diretti con l'ausilio di euristiche per guidare la ricerca. È efficace in presenza di una buona euristica, riducendo il numero di esplorazioni. Non è propriamente un algoritmo per il cammino minimo classico, ma può essere adattato per questo scopo.
   - **Complessità asintotica**: La complessità è fortemente dipendente dall'euristica usata; nel caso peggiore, può degenerare a \(O(E)\), ma con buone euristiche può essere molto efficiente.


   Certamente, esaminiamo più da vicino gli algoritmi di Dijkstra, Bellman-Ford e il metodo per i cammini minimi in grafi diretti aciclici (DAG).

### 1. Algoritmo di Dijkstra

L'algoritmo di Dijkstra è un metodo per trovare il cammino minimo da un vertice sorgente a tutti gli altri vertici in un grafo ponderato con pesi non negativi sugli archi. Si basa su un'idea semplice: mantenere un insieme di vertici per cui i cammini minimi sono già stati trovati e espandere questo insieme un vertice alla volta, selezionando il vertice più vicino non ancora elaborato.

- **Funzionamento**: 
  - Inizia con l'inizializzazione di una distanza per ogni vertice: zero per il vertice sorgente e infinito per tutti gli altri.
  - A ogni passo, sceglie il vertice \(u\) non ancora elaborato con la distanza minima dalla sorgente, lo marca come elaborato, e per ogni suo vicino \(v\) non ancora elaborato, se il cammino attraverso \(u\) migliora la distanza di \(v\) dalla sorgente, aggiorna la distanza di \(v\).

- **Complessità asintotica** migliora utilizzando una coda di priorità (heap minimo) per selezionare efficientemente il prossimo vertice da elaborare, risultando in \(O((V + E) \log V)\) con liste di adiacenza.

### 2. Algoritmo di Bellman-Ford

L'algoritmo di Bellman-Ford estende la capacità di trovare cammini minimi ai grafi con pesi degli archi negativi, a differenza di Dijkstra. Può anche rilevare cicli di peso negativo, i quali rendono indefinito il concetto di cammino minimo.

- **Funzionamento**:
  - Inizializza le distanze come per Dijkstra.
  - Ripetutamente aggiorna la stima della distanza per ogni arco, considerando se passare per un altro vertice riduce la distanza complessiva. Questo passo viene ripetuto \(V - 1\) volte, dove \(V\) è il numero dei vertici.
  - Infine, esegue un'ulteriore iterazione per verificare se ci sono cicli di peso negativo, controllando se le distanze possono essere ridotte ulteriormente.

- **Complessità asintotica**: \(O(V \cdot E)\), rendendolo meno efficiente di Dijkstra per grafi senza pesi negativi ma indispensabile quando tali pesi sono presenti.

### 3. DAG Shortest Path

Questo metodo specifico si applica ai grafi diretti aciclici (DAG), sfruttando l'assenza di cicli per ottimizzare il calcolo dei cammini minimi. In un DAG, è possibile ordinare i vertici linearmente in modo tale che tutti gli archi vadano da un vertice precedente a uno successivo in questo ordine (ordinamento topologico).

- **Funzionamento**:
  - Si inizia con l'esecuzione di un ordinamento topologico del DAG.
  - Poi, i vertici vengono visitati nell'ordine dato dall'ordinamento topologico, e per ciascun vertice \(u\), si rilassa ogni arco \(u \rightarrow v\) aggiornando la distanza di \(v\) se il passaggio attraverso \(u\) la riduce.

- **Complessità asintotica**: \(O(V+E)\), perché l'ordinamento topologico può essere eseguito in \(O(V+E)\) e ogni arco viene considerato una sola volta.
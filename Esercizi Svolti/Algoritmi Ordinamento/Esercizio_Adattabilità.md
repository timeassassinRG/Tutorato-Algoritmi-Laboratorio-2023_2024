Per svolgere l'esercizio, analizzeremo passo dopo passo come Insertion Sort e Bubble Sort operano sull'insieme di dati parzialmente ordinato \(A = [2, 3, 5, 7, 8, 6, 4, 9]\) per dimostrare la loro adattività. Calcoleremo il numero di confronti e scambi effettuati da ciascun algoritmo.

### Parte 1: Insertion Sort

**Procedimento**:
- Inizia da `i = 1` (secondo elemento dell'array), poiché il primo elemento è considerato già ordinato.
- Confronta l'elemento corrente con quelli prima di esso, spostandoli di una posizione verso sinistra finché non trova la posizione corretta per l'elemento corrente.
- Ripete il processo per ogni elemento fino alla fine dell'array.

**Analisi Passo-Passo**:

- \(A = [2, 3, 5, 7, 8, 6, 4, 9]\) - inizio, nessun confronto/scambio per il primo elemento.
- \(A = [2, 3, 5, 7, 8, 6, 4, 9]\) - \(3\) viene confrontato con \(2\), posizione corretta (1 confronto)
- \(A = [2, 3, 5, 7, 8, 6, 4, 9]\) - \(5\) viene confrontato con \(3\), posizione corretta (1 confronto)
- \(A = [2, 3, 5, 7, 8, 6, 4, 9]\) - \(7\) viene confrontato con \(8\), posizione corretta (1 confronto)
- \(A = [2, 3, 5, 7, 8, 6, 4, 9]\) - \(8\) viene confrontato con \(7\), posizione corretta (1 confronto)
- \([2, 3, 5, 7, 8, 6, 4, 9]\) - \(6\) è confrontato con \(8\), poi con \(7\), \(5\) (3 confronti, 2 scambi) fino ad essere inserito nella posizione corretta.
- \([2, 3, 5, 6, 7, 8, 4, 9]\) - \(4\) è confrontato con \(8\), poi con \(7\), \(6\), \(5\), e \(3\) (5 confronti, 4 scambi) fino ad essere inserito nella posizione corretta.
- \([2, 3, 4, 5, 6, 7, 8, 9]\) - \(9\) è confrontato solo con \(8\) (1 confronto, 0 scambi) e lasciato nella sua posizione.

**Calcolo dei Confronti e Scambi**:
- **Confronti**: \(13\)
- **Scambi**: \(6\)

### Parte 2: Bubble Sort

**Procedimento**:
- Confronta ogni coppia di elementi adiacenti e li scambia se sono in ordine sbagliato.
- Ripete il processo per l'intero array fino a quando non viene effettuato nessuno scambio, indicando che l'array è ordinato.

**Analisi Passo-Passo**:

1. Primo passaggio attraverso l'array:
    - \([2, 3, 5, 7, 8, 6, 4, 9]\) - scambia \(8\) e \(6\) (1 scambio), poi \(8\) e \(4\) (1 scambio).
2. Secondo passaggio:
    - \([2, 3, 5, 7, 6, 4, 8, 9]\) - scambia \(7\) e \(6\) (1 scambio), poi \(7\) e \(4\) (1 scambio), nessun scambio per \(8\) e \(9\), indicando che l'array è ora ordinato fino a \(8\).
3. Terzo passaggio:
    - \([2, 3, 5, 6, 4, 7, 8, 9]\) - scambia \(6\) e \(4\) (1 scambio), nessun scambio ulteriore necessario per ordinare completamente l'array.

**Calcolo dei Confronti e Scambi**:
- Dato che ogni passaggio attraverso l'array richiede un confronto per ogni coppia adiacente:
    - **Confronti totali**: il numero di confronti in Bubble Sort dipende dal numero di passaggi necessari. Per ogni passaggio attraverso l'array di \(n\) elementi, si effettuano \(n-1\) confronti. Nel nostro caso, i passaggi effettivi con confronti sono 3, quindi \(7+6+5=18\) confronti.
    - **Scambi totali**: \(2 + 2 + 1 = 5\) scambi.

### Conclusione

**Insertion Sort** ha mostrato un'efficienza notevole in termini di adattabilità con meno confronti e scambi su un insieme

 di dati parzialmente ordinato rispetto a **Bubble Sort**, che ha richiesto più confronti per raggiungere l'ordinamento completo. Questo evidenzia come Insertion Sort sia particolarmente efficace ed adattivo su insiemi di dati che presentano una certa pre-ordinazione, rendendolo una scelta più efficiente per insiemi di dati piccoli o parzialmente ordinati.
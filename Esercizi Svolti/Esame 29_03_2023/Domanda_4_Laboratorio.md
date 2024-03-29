### HeapSort

HeapSort è un algoritmo di ordinamento basato sulla struttura dati dell'heap (un particolare tipo di albero binario). Si compone di due fasi principali: la costruzione di un heap e il processo di estrazione dei massimi per ottenere l'array ordinato.

#### Pseudocodice

```c
// Procedura per costruire un heap da un array
HEAPIFY(A, i, heapSize) {
    left = 2*i
    right = 2*i + 1
    largest = i
    
    if left < heapSize and A[left] > A[largest]
        largest = left
    if right < heapSize and A[right] > A[largest]
        largest = right
    
    if largest != i {
        swap(A[i], A[largest])
        HEAPIFY(A, largest, heapSize) // Elemento di ricorsione
    }
}

// Procedura principale di HeapSort
HEAPSORT(A) {
    heapSize = length(A)
    
    // Costruzione dell'heap
    for i = heapSize / 2 - 1 downto 0 // BuildMaxHeap(A)
        HEAPIFY(A, i, heapSize)
    
    // Estrazione degli elementi dall'heap 
    for i = heapSize - 1 downto 1 {
        swap(A[0], A[i])    //Extract-Max
        HEAPIFY(A, 0, i)
    }
}
```

#### Complessità Computazionale

- **Costruzione dell'heap**: \(O(n log n)\), dove \(n\) è il numero di elementi nell'array.
- **Estrazione degli elementi dall'heap**: \(O(n \log n)\) perché per ciascuno degli \(n-1\) elementi si effettua una chiamata a `HEAPIFY`, che ha complessità \(O(\log n)\).
- **Complessità totale**: \(O(n \log n)\).

La complessità di `HEAPIFY` è \(O(\log n)\) poiché è limitata dall'altezza dell'albero (heap). L'operazione di costruzione dell'heap è lineare rispetto al numero di elementi, e l'ordinamento stesso avviene in tempo \(O(n \log n)\).

### CountingSort

CountingSort è un algoritmo di ordinamento non comparativo che funziona contando il numero di oggetti che hanno ciascun valore distintivo. È efficiente quando la variazione dei valori degli elementi è limitata.

#### Pseudocodice

```c
COUNTINGSORT(A, B, k) {
    // A è l'array di input
    // B è l'array di output
    // k è il valore massimo in A
    C = array di dimensione k+1, inizializzato a 0
    
    // Conta le occorrenze di ogni elemento
    for i = 0 to length(A)-1
        C[A[i]] = C[A[i]] + 1
    
    // Aggiorna C per contenere la posizione effettiva nell'array di output
    for i = 1 to k
        C[i] = C[i] + C[i-1]
    
    // Costruisce l'array di output
    for i = length(A)-1 downto 0
        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]] - 1
}
```

#### Complessità Computazionale

- **Complessità temporale**: \(O(n+k)\), dove \(n\) è il numero di elementi nell'array e \(k\) è l'intervallo di valori. La complessità deriva dalla necessità di inizializzare e aggiornare l'array di conteggio `C` e dall'elaborazione dell'array di input `A`.
  
CountingSort è particolarmente efficiente quando \(k = O(n)\), il che significa che l'intervallo di valori degli elementi è non molto più grande del numero di elementi da ordinare. In tale scenario, l'algoritmo può offrire prestazioni significativamente migliori rispetto agli algoritmi di ordinamento comparativo come HeapSort, particolarmente per grandi volumi di dati con un ristretto intervallo di valori.
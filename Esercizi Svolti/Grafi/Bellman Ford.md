L'algoritmo di Bellman-Ford è un algoritmo utilizzato per trovare il percorso più breve in un grafo orientato ponderato che può contenere archi con peso negativo. A differenza dell'algoritmo di Dijkstra, Bellman-Ford è in grado di gestire questi casi, ma è leggermente meno efficiente per i grafi senza pesi negativi.

L'algoritmo di Bellman-Ford procede rilassando ripetutamente tutti gli archi e aggiornando il costo per raggiungere ogni vertice se viene trovato un percorso più breve. L'algoritmo esegue questo processo per `V-1` volte, dove `V` è il numero di vertici nel grafo. Questo perché il percorso più breve in un grafo può avere al massimo `V-1` archi. Inoltre, l'algoritmo può rilevare cicli di peso negativo nel grafo.

Ecco il pseudocodice dell'algoritmo di Bellman-Ford, seguito da una spiegazione dettagliata:

```plaintext
BellmanFord(grafo, sorgente):
    Inizializza distanze[v] = infinito per ogni vertice v nel grafo, tranne distanze[sorgente] = 0
    Per i da 1 a V-1:
        Per ogni arco (u, v) nel grafo:
            Se distanze[u] + peso(u, v) < distanze[v]:
                distanze[v] = distanze[u] + peso(u, v)

    // Verifica l'esistenza di cicli di peso negativo
    Per ogni arco (u, v) nel grafo:
        Se distanze[u] + peso(u, v) < distanze[v]:
            Restituisci "Esiste un ciclo di peso negativo"
    
    Restituisci distanze
```

**Spiegazione:**

- **Inizializzazione:** All'inizio, l'algoritmo inizializza la distanza da raggiungere per ogni vertice come infinito, tranne che per il vertice sorgente, la cui distanza da se stesso è ovviamente 0. Questo prepara il terreno per l'aggiornamento delle distanze.

- **Rilassamento degli archi:** L'algoritmo itera poi su tutti gli archi del grafo per `V-1` volte, dove `V` è il numero di vertici nel grafo. Per ogni arco, se la somma della distanza memorizzata per il vertice di partenza dell'arco e il peso dell'arco è inferiore alla distanza memorizzata per il vertice di arrivo, allora la distanza per il vertice di arrivo viene aggiornata. Questo processo è noto come "rilassamento" dell'arco.

- **Rilevamento di cicli di peso negativo:** Dopo `V-1` iterazioni, tutti i percorsi più brevi sono stati trovati a meno che non ci siano cicli di peso negativo. Per verificare ciò, l'algoritmo esegue un'altra iterazione su tutti gli archi. Se in questa fase si trova un arco che può essere rilassato, significa che esiste un ciclo di peso negativo, poiché un percorso più breve non dovrebbe essere trovabile dopo `V-1` iterazioni.

Se non viene rilevato alcun ciclo di peso negativo, l'algoritmo restituisce le distanze calcolate dai vertici sorgente a tutti gli altri vertici nel grafo. In caso contrario, segnala l'esistenza di un ciclo di peso negativo.
Nell'ottimizzazione della moltiplicazione di catene di matrici, l'obiettivo è trovare il modo più efficiente di moltiplicare una serie di matrici insieme. Il problema non è il calcolo del prodotto in sé, ma piuttosto come parentesizzare il prodotto in modo tale da minimizzare il numero totale di operazioni scalari.

L'esercizio fa uso di una matrice triangolare superiore \( M \), dove \( M[i, j] \) rappresenta il numero minimo di moltiplicazioni scalari necessarie per moltiplicare la catena di matrici dalla i-esima alla j-esima. Per riempire questa matrice, viene usata una formula ricorsiva basata sulla posizione k della parentesi che divide la catena di matrici in due sottocatene più piccole. La formula considera tutti i possibili valori di k per trovare il costo minimo di moltiplicazione tra la i-esima e la j-esima matrice.

la sequenza di dimensioni delle matrici è data come \( <2, 2, 5, 3, 3, 2> \), che corrisponde a matrici con dimensioni 2x2, 2x5, 5x3, 3x3, e 3x2. L'obiettivo è trovare la parentesizzazione ottimale per moltiplicare queste matrici insieme con il minimo numero di moltiplicazioni scalari.

La soluzione è costruita progressivamente calcolando il numero minimo di moltiplicazioni necessarie per tutte le possibili catene di lunghezza 2, poi di lunghezza 3, e così via fino alla lunghezza completa della catena. Questo viene fatto utilizzando la seguente formula ricorsiva:

$$
\[
M[i,j] = \min_{i \leq k < j} (M[i,k] + M[k+1,j] + p_{i-1} \cdot p_k \cdot p_j)
\]
$$

dove \( p_i \) è la dimensione delle righe della i-esima matrice e \( p_j \) è la dimensione delle colonne della j-esima matrice nella catena di moltiplicazione.
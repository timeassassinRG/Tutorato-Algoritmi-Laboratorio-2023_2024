# scrivi il codice python di bellmanford

import numpy as np
#bellmanford
def bellmanford(W, s):
    n = W.shape[0]
    D = np.full(n, np.inf)
    D[s] = 0
    for nodo in range(n-1):
        for u in range(n):
            for v in range(n):
                D[v] = min(D[v], D[u] + W[u, v])
    return D

#write an example
inf = np.inf
W = np.array([
    [0, 3 ,8, inf, -4],
    [inf, 0, inf, 1, 7],
    [inf, 4, 0, inf, inf],
    [2, inf, -5, 0, inf],
    [inf, inf, inf, 6, 0]
])

result = bellmanford(W, 0)
print(result)


# write bellman ford that find negative cycle
def bellmanford(W, s):
    n = W.shape[0]
    D = np.full(n, np.inf)
    D[s] = 0
    for nodo in range(n-1):
        for u in range(n):
            for v in range(n):
                D[v] = min(D[v], D[u] + W[u, v])
    for u in range(n):
        for v in range(n):
            if D[v] > D[u] + W[u, v]:
                return "negative cycle"
    return D

#write an example with a negative cycle
inf = np.inf
W = np.array([
    [0, -3 ,-8, inf, -4],
    [inf, 0, -1, -1, -7],
    [inf, -4, 0, inf, inf],
    [-2, inf, -5, 0, inf],
    [inf, inf, inf, -6, 0]
])

result = bellmanford(W, 0)
print(result)
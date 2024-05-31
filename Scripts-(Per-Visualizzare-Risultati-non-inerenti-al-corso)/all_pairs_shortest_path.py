import numpy as np

def extend_shortest_paths(L, W):
    n = L.shape[0]
    L_prime = np.full((n, n), np.inf)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                L_prime[i, j] = min(L_prime[i, j], L[i, k] + W[k, j])
    return L_prime

def slow_all_pairs_shortest_paths(W):
    n = W.shape[0]
    L = [None] * n
    L[0] = W
    for m in range(1, n):
        L[m] = extend_shortest_paths(L[m-1], W)
    return L[-1]

def faster_all_pairs_shortest_paths(W):
    n = W.shape[0]
    L = [None] * (n+1)
    L[1] = W
    m = 1
    while m < n - 1:
        L[2 * m] = extend_shortest_paths(L[m], L[m])
        m *= 2
    return L[m]


inf = np.inf

# Example usage
W = np.array([
    [0, 3, 8, inf, -4],
    [inf, 0, inf, 1, 7],
    [inf, 4, 0, inf, inf],
    [2, inf, -5, 0, inf],
    [inf, inf, inf, 6, 0]
])

slow_result = slow_all_pairs_shortest_paths(W)
print("Slow All-Pairs Shortest Paths Result:")
print(slow_result)

faster_result = faster_all_pairs_shortest_paths(W)
print("Faster All-Pairs Shortest Paths Result:")
print(faster_result)
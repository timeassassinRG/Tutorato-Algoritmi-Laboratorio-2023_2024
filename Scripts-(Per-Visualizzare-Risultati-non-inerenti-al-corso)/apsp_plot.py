import numpy as np
import matplotlib.pyplot as plt
import time
from tqdm import tqdm

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
    L = [None] * (2 * n)
    L[1] = W
    m = 1
    while m < n - 1:
        L[2 * m] = extend_shortest_paths(L[m], L[m])
        m *= 2
    return L[m] if m < 2 * n else L[m // 2]

def floyd_warshall(W):
    n = W.shape[0]
    D = np.array(W)  # Initialize D^(0) with the weight matrix W
    for k in range(n):
        D_new = np.copy(D)
        for i in range(n):
            for j in range(n):
                D_new[i, j] = min(D[i, j], D[i, k] + D[k, j])
        D = D_new  # Update D to D_new for the next iteration
    return D

def generate_random_matrix(n, density=0.5):
    W = np.random.rand(n, n) * 10
    W[np.random.rand(n, n) > density] = np.inf
    np.fill_diagonal(W, 0)
    return W

# Setup for the plot
sizes = range(6, 20)
slow_times = []
faster_times = []
floyd_times = []

for n in tqdm(sizes, desc="Processing algorithms for different matrix sizes"):
    W_random = generate_random_matrix(n)

    # Measure time for slow algorithm
    start_time = time.time()
    slow_all_pairs_shortest_paths(W_random)
    slow_times.append(time.time() - start_time)

    # Measure time for faster algorithm
    start_time = time.time()
    faster_all_pairs_shortest_paths(W_random)
    faster_times.append(time.time() - start_time)

    # Measure time for Floyd-Warshall algorithm
    start_time = time.time()
    floyd_warshall(W_random)
    floyd_times.append(time.time() - start_time)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(sizes, slow_times, label='Slow All-Pairs Shortest Paths (Θ(n^4))', color='blue', marker='o')
plt.plot(sizes, faster_times, label='Faster All-Pairs Shortest Paths (Θ(n^(3) log n))', color='green', marker='o')
plt.plot(sizes, floyd_times, label='Floyd-Warshall (O(n^3))', color='red', marker='o')
plt.xlabel('Matrix Size n')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Matrix Size for Various Algorithms')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import time
import matplotlib.pyplot as plt

# Definizione dell'algoritmo Insertion Sort (adattivo)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Definizione dell'algoritmo Quick Sort (non adattivo)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Funzione per generare array parzialmente ordinati
def generate_partially_sorted_array(size, disorder_level):
    arr = np.arange(size)
    disorder_count = int(size * disorder_level)
    for _ in range(disorder_count):
        idx1, idx2 = np.random.randint(0, size, 2)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return list(arr)

# Parametri dell'esperimento
sizes = np.arange(100, 5001, 100) # Da 100 a 10000 con step 100
disorder_level = 0
n_experiments = 1 # Numero di esperimenti per dimensione

# Variabili per memorizzare i risultati
insertion_sort_times = []
quick_sort_times = []

# Esecuzione degli esperimenti
for size in sizes:
    insertion_sort_avg_time = 0
    quick_sort_avg_time = 0
    print("esperimento",int(size/100) ," di ", len(sizes))
    for _ in range(n_experiments):
        arr = generate_partially_sorted_array(size, disorder_level)
        
        # Misurazione Insertion Sort
        start_time = time.time()
        insertion_sort(arr.copy())
        insertion_sort_avg_time += (time.time() - start_time)
        
        # Misurazione Quick Sort
        start_time = time.time()
        quick_sort(arr.copy())
        quick_sort_avg_time += (time.time() - start_time)
    
    insertion_sort_avg_time /= n_experiments
    quick_sort_avg_time /= n_experiments
    
    insertion_sort_times.append(insertion_sort_avg_time)
    quick_sort_times.append(quick_sort_avg_time)

# Creazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_sort_times, label='Insertion Sort', marker='o', color='blue')
plt.plot(sizes, quick_sort_times, label='Quick Sort', marker='s', color='red')
plt.xlabel('Dimensione dell\'input')
plt.ylabel('Tempo medio (secondi)')
plt.title(f'Confronto delle performance: Insertion Sort vs Quick Sort, percentuale di disordine dell input:' + str(disorder_level*100) + '%' )
plt.legend()
plt.grid(True)
plt.show()
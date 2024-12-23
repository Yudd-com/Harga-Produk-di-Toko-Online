# %% [markdown]
# # **Pencarian Harga Produk di Toko Online**

# %% [markdown]
# **Import Library**

# %%
import time
import matplotlib.pyplot as plt
import random

# %% [markdown]
# **Implementasi Linear Search Iteratif**
# 
# mencari elemen dalam array secara iteratif dari awal hingga akhir.
# 

# %%
# Implementasi Linear Search Iteratif
def linear_search_iterative(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1  # Target not found

# %% [markdown]
# **Implementasi Binary Search Rekursif**
# 
# Fungsi ini mencari elemen dalam array yang sudah terurut dengan membagi array menjadi dua bagian.

# %%
# Implementasi Binary Search Rekursif
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


# %% [markdown]
# **Fungsi untuk mengukur waktu eksekusi**
# 
# untuk mencatat waktu yang dibutuhkan oleh algoritma untuk menyelesaikan tugasnya.

# %%
#Fungsi untuk mengukur waktu eksekusi
def measure_execution_time(func, arr, target):
    start_time = time.time()
    func(arr, target)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Konversi ke milliseconds

# %%
# Fungsi untuk membuat dataset dengan ukuran berbeda
def generate_dataset(size):
    return [random.randint(1, 10000) for _ in range(size)]

# %%
# Ukuran dataset yang akan diuji
sizes = [1, 10, 100, 1000, 5000, 10000]
linear_times = []
binary_times = []

# %% [markdown]
# # Pengujian untuk setiap ukuran dataset

# %%
# Pengujian untuk setiap ukuran
for size in sizes:
    # Generate dataset
    unordered_data = generate_dataset(size)
    ordered_data = sorted(unordered_data)
    target = random.choice(ordered_data)

    # Ukur waktu untuk Linear Search (Iterative)
    linear_time = measure_execution_time(
        lambda x, y: linear_search_iterative(x, y),
        unordered_data,
        target
    )
    linear_times.append(linear_time)

    # Ukur waktu untuk Binary Search
    binary_time = measure_execution_time(
        lambda x, y: binary_search_recursive(x, y),
        ordered_data,
        target
    )
    binary_times.append(binary_time)

    print(f"\nUkuran Dataset: {size}")
    print(f"Waktu Linear Search: {linear_time:.6f} ms")
    print(f"Waktu Binary Search: {binary_time:.6f} ms")

# %% [markdown]
# **Import Library**

# %%
import time
import matplotlib.pyplot as plt
import random

# %% [markdown]
# Implementasi Linear Search Iteratif Dan Implementasi Binary Search Rekursif

# %%
# Implementasi Linear Search Iteratif
def linear_search_iterative(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1  # Target not found

# Implementasi Binary Search Rekursif
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# %% [markdown]
# untuk mengukur waktu eksekusi

# %%
# Fungsi untuk mengukur waktu eksekusi
def measure_execution_time(func, arr, target):
    start_time = time.time()
    func(arr, target)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Konversi ke milliseconds

# Fungsi untuk membuat dataset dengan ukuran berbeda
def generate_dataset(size):
    return [random.randint(1, 10000) for _ in range(size)]


# %%
# Ukuran dataset yang akan diuji
sizes = [1, 10, 100, 1000, 5000, 10000]
linear_times = []
binary_times = []

# %% [markdown]
# # Pengujian untuk setiap ukuran Dan visualisasi (grafik).

# %%
for size in sizes:
    # Generate dataset
    unordered_data = generate_dataset(size)
    ordered_data = sorted(unordered_data)
    target = random.choice(ordered_data)

    # Ukur waktu untuk Linear Search (Iterative)
    linear_time = measure_execution_time(
        lambda x, y: linear_search_iterative(x, y),
        unordered_data,
        target
    )
    linear_times.append(linear_time)

    # Ukur waktu untuk Binary Search
    binary_time = measure_execution_time(
        lambda x, y: binary_search_recursive(x, y),
        ordered_data,
        target
    )
    binary_times.append(binary_time)

    print(f"\nUkuran Dataset: {size}")
    print(f"Waktu Linear Search: {linear_time:.6f} ms")
    print(f"Waktu Binary Search: {binary_time:.6f} ms")

# Plotting hasil
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, 'r-o', label='Linear Search (O(n))')
plt.plot(sizes, binary_times, 'b-x', label='Binary Search (O(log n))')
plt.xlabel("Ukuran Dataset")
plt.ylabel("Waktu Eksekusi (ms)")
plt.title("Perbandingan Waktu Eksekusi Linear Search dan Binary Search")
plt.legend()
plt.grid(True)
plt.show()

# %% [markdown]
# 

# %%

import time
import matplotlib.pyplot as plt
import random
import numpy as np

# Implementasi Linear Search Iteratif
def linear_search_iterative(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1  # Target not found

# Implementasi Linear Search Rekursif
def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1  # Target not found
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

# Implementasi Binary Search Rekursif
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# Fungsi untuk mengukur waktu eksekusi
def measure_execution_time(func, arr, target):
    start_time = time.time()
    func(arr, target)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Konversi ke milliseconds

# Fungsi untuk membuat dataset dengan ukuran berbeda
def generate_dataset(size):
    return [random.randint(1, 10000) for _ in range(size)]

# Ukuran dataset yang akan diuji
sizes = [1, 10, 100, 1000, 5000, 10000]
linear_iterative_times = []
linear_recursive_times = []
binary_times = []

# Pengujian untuk setiap ukuran
for size in sizes:
    # Generate dataset
    unordered_data = generate_dataset(size)
    ordered_data = sorted(unordered_data)
    target = random.choice(ordered_data)

    # Ukur waktu untuk Linear Search (Iterative)
    linear_iter_time = measure_execution_time(
        lambda x, y: linear_search_iterative(x, y),
        unordered_data,
        target
    )
    linear_iterative_times.append(linear_iter_time)

    # Ukur waktu untuk Linear Search (Recursive)
    linear_rec_time = measure_execution_time(
        lambda x, y: linear_search_recursive(x, y),
        unordered_data,
        target
    )
    linear_recursive_times.append(linear_rec_time)

    # Ukur waktu untuk Binary Search
    binary_time = measure_execution_time(
        lambda x, y: binary_search_recursive(x, y),
        ordered_data,
        target
    )
    binary_times.append(binary_time)

    print(f"\nUkuran Dataset: {size}")
    print(f"Waktu Linear Search (Iterative): {linear_iter_time:.6f} ms")
    print(f"Waktu Linear Search (Recursive): {linear_rec_time:.6f} ms")
    print(f"Waktu Binary Search: {binary_time:.6f} ms")

# Plotting hasil dengan penjelasan detail
plt.figure(figsize=(12, 8))
plt.plot(sizes, linear_iterative_times, 'r-o', label='Linear Search Iterative (O(n))', linewidth=2)
plt.plot(sizes, linear_recursive_times, 'g-s', label='Linear Search Recursive (O(n))', linewidth=2)
plt.plot(sizes, binary_times, 'b-x', label='Binary Search (O(log n))', linewidth=2)

plt.xlabel('Ukuran Dataset (n)', fontsize=12)
plt.ylabel('Waktu Eksekusi (ms)', fontsize=12)
plt.title('Perbandingan Waktu Eksekusi\nLinear Search (Iterative & Recursive) vs Binary Search', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)

# Menambahkan anotasi
plt.annotate('Linear Growth (Iterative)',
            xy=(sizes[-2], linear_iterative_times[-2]),
            xytext=(sizes[-2]-2000, linear_iterative_times[-2]+1),
            arrowprops=dict(facecolor='red', shrink=0.05))

plt.annotate('Linear Growth (Recursive)',
            xy=(sizes[-2], linear_recursive_times[-2]),
            xytext=(sizes[-2]-2000, linear_recursive_times[-2]+0.5),
            arrowprops=dict(facecolor='green', shrink=0.05))

plt.annotate('Logarithmic Growth',
            xy=(sizes[-2], binary_times[-2]),
            xytext=(sizes[-2]-2000, binary_times[-2]+0.3),
            arrowprops=dict(facecolor='blue', shrink=0.05))

plt.show()


# %% [markdown]
# 

# %%
import time
import matplotlib.pyplot as plt
import random

# Implementasi Linear Search Iteratif
def linear_search_iterative(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1  # Target not found

# Implementasi Binary Search Rekursif
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# Fungsi untuk mengukur waktu eksekusi
def measure_execution_time(func, arr, target, repetitions=10):
    total_time = 0
    for _ in range(repetitions):
        start_time = time.perf_counter()  # Gunakan perf_counter untuk akurasi tinggi
        func(arr, target)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    return (total_time / repetitions) * 1000  # Rata-rata waktu dalam milidetik

# Fungsi untuk membuat dataset dengan ukuran berbeda
def generate_dataset(size):
    return [random.randint(1, 10000) for _ in range(size)]

# Ukuran dataset yang akan diuji (gunakan dataset yang lebih besar)
sizes = [1000, 5000, 10000, 50000, 100000]
linear_times = []
binary_times = []

# Pengujian untuk setiap ukuran
for size in sizes:
    # Generate dataset
    unordered_data = generate_dataset(size)
    ordered_data = sorted(unordered_data)
    target = random.choice(ordered_data)

    # Ukur waktu untuk Linear Search (Iterative)
    linear_time = measure_execution_time(
        lambda x, y: linear_search_iterative(x, y),
        unordered_data,
        target
    )
    linear_times.append(linear_time)

    # Ukur waktu untuk Binary Search
    binary_time = measure_execution_time(
        lambda x, y: binary_search_recursive(x, y),
        ordered_data,
        target
    )
    binary_times.append(binary_time)

    print(f"\nUkuran Dataset: {size}")
    print(f"Waktu Linear Search: {linear_time:.6f} ms")
    print(f"Waktu Binary Search: {binary_time:.6f} ms")

# Visualisasi hasil running time
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, label="Linear Search (Iterative)", marker='o')
plt.plot(sizes, binary_times, label="Binary Search (Recursive)", marker='s')
plt.title("Analisis Waktu Algoritma Pencarian")
plt.xlabel("Dataset Size")
plt.ylabel("Time (ms)")
plt.grid(True)
plt.legend()
plt.show()




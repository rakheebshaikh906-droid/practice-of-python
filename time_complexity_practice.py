# Time Complexity Practice Examples


# O(1) - Constant Time
def constant_time(arr):
    print(arr[0])   # always 1 operation


# O(n) - Linear Time
def linear_time(arr):
    for i in arr:
        print(i)


# O(n^2) - Quadratic Time
def quadratic_time(arr):
    for i in arr:
        for j in arr:
            print(i, j)


# O(log n) - Logarithmic Time (Binary Search idea)
def log_time(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# O(n log n) - Efficient sorting (Python sort)
def nlogn_time(arr):
    arr.sort()
    print(arr)


# Test data
arr = [5, 2, 9, 1, 6]

print("O(1):")
constant_time(arr)

print("\nO(n):")
linear_time(arr)

print("\nO(n^2):")
quadratic_time(arr)

print("\nO(log n):")
sorted_arr = sorted(arr)
print("Index:", log_time(sorted_arr, 6))

print("\nO(n log n):")
nlogn_time(arr)

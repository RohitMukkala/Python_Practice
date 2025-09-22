def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


input_list = input("Enter a list of numbers separated by spaces: ").split()
arr = [int(x) for x in input_list]

sorted_arr = quick_sort(arr)
print(f"Sorted array: {sorted_arr}")

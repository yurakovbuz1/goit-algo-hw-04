import random
import timeit

arr_random = [random.randint(0, 100000) for _ in range(10000)]
arr_sorted = list(range(10000))
arr_reversed = list(range(10000, 0, -1))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst



time_merge_random = timeit.timeit(
    stmt=lambda: merge_sort(arr_random.copy()),
    number=10
)

time_merge_sorted = timeit.timeit(
    stmt=lambda: merge_sort(arr_sorted.copy()),
    number=10
)

time_merge_reversed = timeit.timeit(
    stmt=lambda: merge_sort(arr_reversed.copy()),
    number=10
)

time_insertion_random = timeit.timeit(
    stmt=lambda: insertion_sort(arr_random.copy()),
    number=10
)

time_insertion_sorted = timeit.timeit(
    stmt=lambda: insertion_sort(arr_sorted.copy()),
    number=10
)

time_insertion_reversed = timeit.timeit(
    stmt=lambda: insertion_sort(arr_reversed.copy()),
    number=10
)

time_sorted_random = timeit.timeit(
    stmt=lambda: sorted(arr_random.copy()),
    number=10
)

time_sorted_sorted = timeit.timeit(
    stmt=lambda: sorted(arr_sorted.copy()),
    number=10
)

time_sorted_reversed = timeit.timeit(
    stmt=lambda: sorted(arr_reversed.copy()),
    number=10
)



print(f"\nMerge sort tests:\nRandom array: {time_merge_random}s\n"
      + f"Sorted array: {time_merge_sorted}s\nReversed array: {time_merge_reversed}s\n")
print(f"Insertion sort tests:\nRandom array: {time_insertion_random}s\n"
      + f"Sorted array: {time_insertion_sorted}s\nReversed array: {time_insertion_reversed}s\n")
print(f"Timsort sort tests:\nRandom array: {time_sorted_random}s\n"
      + f"Sorted array: {time_sorted_sorted}s\nReversed array: {time_sorted_reversed}s\n")
print("Conclusion:\nBased on the results, Timsort (which is used in Python by default) is most efficient in all three cases.\n At the same time the results show that Merge sort is a number of times more efficient compared to Insertion sort except for the case with an already sorted array, as it still needs to divide the subsets and merge them back.")
# TO-DO: complete the helper function below to merge 2 sorted arrays
# [5, 9 , 3, 7, 2, 8, 1, 6]
# [5, 9, 3, 7] [2, 8, 1, 6]
# [5, 9] [3, 7] [2, 8] [1, 6]
# [5] [9] [3] [7] [2] [8] [1] [6] these are individually sorted

# i = [9]
# j = [5]
# [5, 9]

# i = [3]
# j = [7]
# [3, 7]

# i = [2]
# j = [8]
# [2, 8]

# i = [1]
# j = [6]
# [1, 6]

# [5, 9] [3, 7] [2, 8] [1, 6] # subarrays are individually sorted

# [5, 9]
# i = 5 --> i = 5 --> i = 9 --> i = 9
# [3]     [3, 5]      [3, 5, 7]   [3, 5, 7, 9]
# j = 3 --> j = 7 --> j = 7 --> j = None
# [3, 7]

# [2, 8]
# i = 2 --> i = 2 --> i = 8 --> i = 8
# [1]     [1, 2]      [1, 2, 6]   [1, 2, 6, 8]
# j = 1 --> j = 6 --> j = 6 --> j = None
# [1, 6]

# [3, 5, 7, 9] [1, 2, 6, 8] # subarrays are individually sorted

# [3, 5, 7, 9]
# i = 3 -> i = 3 -> i = 3 -> i = 5 -> i = 7 -> i = 7 -> i = 9 -> i = None

# [0, 0, 0, 0, 0, 0, 0, 0]
#  k
# [1, 0, 0, 0, 0, 0, 0, 0]
#     k
# [1, 2, 0, 0, 0, 0, 0, 0]
#        k
# [1, 2, 3, 0, 0, 0, 0, 0]
#           k
# [1, 2, 3, 5, 0, 0, 0, 0]
#              k
# [1, 2, 3, 5, 6, 0, 0, 0]
#                 k
# [1, 2, 3, 5, 6, 7, 0, 0]
#                    k
# [1, 2, 3, 5, 6, 7, 8, 0]
#                       k
# [1, 2, 3, 5, 6, 7, 8, 9]

# [1, 2, 6, 8]
# j = 1 -> j = 2 -> j = 6 -> j = 6 -> j = 6 -> j = 8 -> j = 8 -> j = None


# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements

#     # Your code here
#     a = 0
#     k = 0
#     b = 0

#     for k in range(0, elements):
#         # if a is out of range, push b and iterate
#         if a >= len(arrA):
#             merged_arr[k] = arrB[b]
#             b += 1
#         # if b is out of range, push a and iterate
#         elif b >= len(arrB):
#             merged_arr[k] = arrA[a]
#             a += 1
#         # if a is smaller, put it in array and iterate
#         elif arrA[a] < arrB[b]:
#             merged_arr[k] = arrA[a]
#             a += 1
#         # if b is smaller, put it in array and iterate
#         else:
#             merged_arr[k] = arrB[b]
#             b += 1

#     return merged_arr

def merge(arrA, arrB):
    merged_arr = []
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    while i < len(arrA):
        merged_arr.append(arrA[i])
        i += 1

    while j < len(arrB):
        merged_arr.append(arrB[j])
        j += 1

    return merged_arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    return arr
# TO-DO: implement the Merge Sort function below USING RECURSION


# def merge_sort(arr):
#     # Your code here
#     if len(arr) > 1:
#         # get midpoint
#         mid = len(arr) // 2
#         # recursively call merge_sort on LHS
#         left = merge_sort(arr[:mid])
#         # recursively call merge_sort on RHS
#         right = merge_sort(arr[mid:])
#         # merge left and right
#         arr = merge(left, right)

#     # merge sorted pieces

#     return arr


print(merge_sort([3, 4, 6, 1, 2, 5]))

# implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1
    # If the direct merge is already sorted
    if arr[mid] <= arr[start2]:
        return
    # two pointers to maintain start of both arrays to merge
    while start <= mid and start2 <= end:
        # if element 1 is in the right place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            # Shift all the elements between element 1 and element 2, right by 1
            while index is not start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all pointers
            start += 1
            mid += 1
            start2 += 1

    return arr

# l is for left index and r is right index of the sub-array of arr to be sorted


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        mid = l + (r - l) // 2
        # Sort first and second halves
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        # merge them
        merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

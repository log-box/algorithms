# https://pythonru.com/osnovy/top-5-algoritmov-sortirovki-na-python

# def selection_sort(alist):
#     for i in range(len(alist)):
#         smallest = i
#         for j in range(i + 1, len(alist)):
#             if alist[j] < alist[smallest]:
#                 smallest = j
#         alist[i], alist[smallest] = alist[smallest], alist[i]
#         print(alist)
#     return alist


a = [1, 23, 3, 43534, 55, 5, 3, 4, 3, 434, 43, 4, 4343, 4]
# print(selection_sort(a))


# def insertions_sort(array):
#     for i in range(len(array)):
#         cursor = array[i]
#         pos = i
#         while array[pos-1] > cursor and pos > 0:
#             array[pos] = array[pos - 1]
#             pos -= 1
#         array[pos] = cursor


# insertions_sort(a)

# def bubble_sort(arr):
#     n = 1
#     while n < len(arr):
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#         n+=1
#     return arr


# print(bubble_sort(a))
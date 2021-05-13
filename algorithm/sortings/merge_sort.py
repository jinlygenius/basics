'''
Merge sort takes advantage of the ease of merging already sorted lists into a new sorted list. It starts by comparing every two elements (i.e., 1 with 2, then 3 with 4...) and swapping them if the first should come after the second. It then merges each of the resulting lists of two into lists of four, then merges those lists of four, and so on; until at last two lists are merged into the final sorted list.
O(nlogn) algorithms
'''

from utils.my_decorators import timeit


# def merge_sort(data):
#     if len(data) <= 1:
#         return data
#     middle_index = len(data) / 2
#     # print middle_index

#     data1 = merge_sort(data[:middle_index:])
#     data2 = merge_sort(data[middle_index::])
#     data = merge(data1, data2)
#     return data


def merge_sort(data, left_index, right_index):
    if left_index >= right_index - 1:
        return data
    middle_index = left_index + (right_index - left_index) / 2
    merge_sort(data, left_index, middle_index)
    merge_sort(data, middle_index, right_index)
    data[left_index:right_index] = merge(data[left_index:middle_index], data[middle_index:right_index])
    return data


def merge(data1, data2):
    '''merge 2 ordered data array'''
    aa = 0
    bb = 0
    new_data = []

    while aa < len(data1) and bb < len(data2):
        if data1[aa] <= data2[bb]:
            new_data.append(data1[aa])
            aa += 1
        else:
            new_data.append(data2[bb])
            bb += 1

        if aa == len(data1):
            new_data.extend(data2[bb:])
            break

        if bb == len(data2):
            new_data.extend(data1[aa:])
            break

    return new_data

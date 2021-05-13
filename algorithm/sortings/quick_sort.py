'''Quicksort is a divide and conquer algorithm which relies on a partition operation: to partition an array an element called a pivot is selected
quick sort is not stable - the order may changes
O(nlogn) algorithms
'''

from utils.my_decorators import timeit


def quick_sort(data, low_index, high_index):

    if low_index >= high_index:
        return data

    aa = low_index
    bb = high_index - 1

    pivot = data[aa]

    while aa < bb:
        while aa < bb and data[bb] >= pivot:
            bb -= 1
        while aa < bb and data[aa] <= pivot:
            # import pdb; pdb.set_trace()
            aa += 1
        data[aa], data[bb] = data[bb], data[aa]

    data[low_index], data[aa] = data[aa], data[low_index]

    quick_sort(data, low_index, aa)
    quick_sort(data, aa + 1, high_index)
    
    return data


def quick_sort(data, low_index, high_index):
    if low_index >= high_index:
        return data
    aa = low_index
    bb = high_index
    pivot = data[aa]
    while aa < bb:
        while aa < bb and data[bb] >= pivot:
            bb -= 1
        while aa < bb and data[aa] <= pivot:
            # import pdb; pdb.set_trace()
            aa += 1
        data[aa], data[bb] = data[bb], data[aa]
    data[low_index], data[aa] = data[aa], data[low_index]
    quick_sort(data, low_index, aa - 1)
    quick_sort(data, aa + 1, high_index)
    return data


# class QuickSorter(object):
#     """docstring for QuickSorter"""
#     def __init__(self, data):
#         super(QuickSorter, self).__init__()
#         self.data = data

#     def quick_sorting(self, left_indicator, right_indicator):

#         if left_indicator > right_indicator:
#             return None

#         temp_value = data[left_indicator]
#         i = left_indicator
#         j = right_indicator

#         while i != j:

#             while data[j] >= temp_value and i < j:
#                 j -= 1

#             while data[i] <= temp_value and i < j:
#                 i += 1

#             if i < j:
#                 temp = data[i]
#                 data[i] = data[j]
#                 data[j] = temp

#         data[left_indicator] = data[i]
#         data[i] = temp_value

#         # -1 +1 is key point!!!
#         self.quick_sorting(left_indicator, i-1)
#         self.quick_sorting(i+1, right_indicator)


# if __name__ == '__main__':
#     data = [3, 2, 5, 8, 9, 4, 6, 1, 10, 7]
#     quicker = QuickSorter(data)
#     quicker.quick_sorting(0, 9)

#     print quicker.data

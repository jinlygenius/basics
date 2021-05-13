'''
Heapsort is a much more efficient version of selection sort. It also works by determining the largest (or smallest) element of the list, placing that at the end (or beginning) of the list, then continuing with the rest of the list, but accomplishes this task efficiently by using a data structure called a heap, a special type of binary tree.
O(nlogn) Algorithm
'''

from utils.my_decorators import timeit

@timeit
def heap_sort(data):

    build_max_heap(data)
    # import pdb; pdb.set_trace()

    length = len(data)

    # swap first and last to get the largest
    for index in range(length - 1, -1, -1):
        data[0], data[index] = data[index], data[0]
        max_heapify(data, 0, index - 1)

    return data


def max_heapify(data, begin_index, end_index):
    # import pdb; pdb.set_trace()
    if begin_index >= end_index:
        return data

    root_index = begin_index
    child1_index = root_index * 2 + 1
    child2_index = root_index * 2 + 2

    if child1_index > end_index:
        return data
    elif child2_index > end_index:
        max_index = child1_index
    else:
        max_index = child1_index if data[child1_index] >= data[child2_index] else child2_index
    if data[root_index] < data[max_index]:
        data[root_index], data[max_index] = data[max_index], data[root_index]
        # import pdb; pdb.set_trace()
        max_heapify(data, max_index, end_index)


def build_max_heap(data):
    '''start from the last leaf'''
    for index in range(len(data)-1,-1,-1):
        max_heapify(data, index, len(data) - 1)
    return data

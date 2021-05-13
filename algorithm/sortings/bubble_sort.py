'''
The algorithm works by comparing each item in the list with the item next to it, and swapping them if required. In other words, the largest element has bubbled to the top of the array. The algorithm repeats this process until it makes a pass all the way through the list without swapping any items.
O(n2) algorithms
'''
from utils.my_decorators import timeit


@timeit
def bubble_sort(data):
    for i in range(len(data)):
        # import pdb; pdb.set_trace()
        for index, value in enumerate(data[:len(data) - i:]):  # cannot use -i because i will = 0
            # import pdb; pdb.set_trace()
            if index == 0:
                continue
            if value < data[index - 1]:
                data[index], data[index - 1] = data[index - 1], data[index]
    return data

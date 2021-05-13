'''
you look through the entire array for the smallest element, once you find it you swap it (the smallest element) with the first element of the array. Then you look for the smallest element in the remaining array (an array without the first element) and swap it with the second element. Then you look for the smallest element in the remaining array (an array without first and second elements) and swap it with the third element, and so on.
O(n2) algorithms
'''

from utils.my_decorators import timeit


# @timeit
# def selection_sort(data):
#     final_data = []
#     data_length = len(data)
#     for i in range(data_length):
#         for index, value in enumerate(data):
#         # for index, value in enumerate(data[:len(data) - i:]):
#             if index == 0:
#                 (min_index, min_value) = (0, value)
#                 continue
#             if min_value > value:
#                 (min_index, min_value) = (index, value)
#             # import pdb; pdb.set_trace()
#         final_data.append(data[min_index])
#         data.pop(min_index)
#     return final_data


@timeit
def selection_sort(data):
    data_length = len(data)
    for i in range(data_length):
        for index, value in enumerate(data[i:data_length:]):
            index += i
            if index == i:
                (min_index, min_value) = (index, value)
                continue
            if min_value > value:
                (min_index, min_value) = (index, value)
        data[i], data[min_index] = data[min_index], data[i]
    return data

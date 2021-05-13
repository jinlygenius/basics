'''To sort unordered list of elements, we remove its entries one at a time and then insert each of them into a sorted part (initially empty)
O(n2) algorithms
'''

from utils.my_decorators import timeit


# @timeit
# def insertion_sort(data):
#     final_data = []

#     for value in data:

#         if len(final_data) == 0:
#             final_data.append(value)
#             continue

#         for i in range(len(final_data)):
#             if i == 0 and value < final_data[i]:
#                 # import pdb; pdb.set_trace()
#                 final_data.insert(i, value)
#                 break

#             if i == len(final_data) - 1 and value >= final_data[i]:
#                 final_data.append(value)
#                 break

#             if final_data[i] <= value < final_data[i + 1]:
#                 final_data.insert(i + 1, value)
#                 break

#     return final_data


@timeit
def insertion_sort(data):
    for index, value in enumerate(data):
        if index == 0:
            continue

        i = index
        while (value < data[i - 1]):
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
            else:
                break
    return data

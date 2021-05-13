
'''
O(n) algorithms
'''
from utils.my_decorators import timeit


@timeit
def bucket_sort(data):

    positive_bucket = [0] * 101  # max value in array (list)!
    negative_bucket = [0] * 101

    for item in data:
        # import pdb; pdb.set_trace()
        if item >= 0:
            positive_bucket[item] += 1
        else:
            negative_bucket[abs(item)] += 1

    final_data = []
    for index, value in enumerate(negative_bucket):
        if value > 0:
            final_data.append(-abs(index))
    final_data[:] = final_data[::-1]

    for index, value in enumerate(positive_bucket):
        if value > 0:
            final_data.append(index)

    return final_data

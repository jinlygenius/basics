
import os
import sys
import time

BASE_DIR = '/Users/ella/Dropbox/Study/basics'
# BASE_DIR = '/Users/shs/Dropbox/Study/basics'
sys.path.insert(0, BASE_DIR)

import random
from bucket_sort import bucket_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort
from merge_sort import merge_sort, merge
from heap_sort import heap_sort, max_heapify, build_max_heap
from shell_sort import shell_sort
from utils.my_decorators import timeit


if __name__ == '__main__':

    random_items = [random.randint(-50, 100) for c in range(32)]

    print(random_items)
    print(len(random_items))

    # aaa = [9, 11, 27, 83, 96]
    # result = build_max_heap(aaa)

    # result = heap_sort(random_items)

    time1 = time.time()
    # result = merge_sort(random_items, 0, len(random_items))
    result = shell_sort(random_items)
    time2 = time.time()
    print('took: %2.6f sec' % (time2-time1))

    print(result)
    print(len(result))

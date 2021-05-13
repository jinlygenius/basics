# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        time1 = time.time()
        result = func(*args, **kwargs)
        time2 = time.time()
        print 'func:%r took: %2.6f sec' % (func.__name__, time2-time1)
        return result
    return wrapper

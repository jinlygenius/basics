
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            pass
            # if want to run init every time
            # cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]

# python2
# class Logger(object):
#     __metaclass__ = Singleton


# python3
class Logger(metaclass=Singleton):
    pass


import os
import sys

BASE_DIR = '/Users/ella/Dropbox/Study/basics'
# BASE_DIR = '/Users/shs/Dropbox/Study/basics'
sys.path.insert(0, BASE_DIR)

if __name__ == '__main__':
    x = Logger()
    print(x)

    y = Logger()
    print(y)

    z = Logger()
    print(z)

    print(type(Singleton))

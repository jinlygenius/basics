
from random import randint


class Heap():

    def __init__(self, arr):
        super(Heap, self).__init__()
        self.arr = arr
        self.end_index = len(arr) - 1

    def shift_down(self, current_index):
        # 构建最大堆，小元素下沉
        root_index = current_index
        lchild_index = root_index * 2 + 1
        rchild_index = root_index * 2 + 2
        max_index = root_index

        if root_index >= self.end_index:
            return
        elif lchild_index > self.end_index:
            return
        elif rchild_index > self.end_index:
            if self.arr[lchild_index] > self.arr[max_index]:
                max_index = lchild_index
        else:
            if self.arr[lchild_index] > self.arr[max_index]:
                max_index = lchild_index
            if self.arr[rchild_index] > self.arr[max_index]:
                max_index = rchild_index
        if max_index != root_index:
            # swap
            self.arr[root_index], self.arr[max_index] = self.arr[max_index], self.arr[root_index]
            # re-adjust changed elements
            return self.shift_down(max_index)
        return

    def build(self):
        # 构建最大堆
        for i in range(len(self.arr)-1, -1, -1):
            self.shift_down(i)
        print(f'after build: {self.arr}')


if __name__ == '__main__':
    length = randint(10,20)
    arr = [randint(1,100) for x in range(length)]
    print(f'arr={arr}')
    print(f'length={length}')

    k = randint(5, length)
    print(f'k={k}')

    # 构造一个k的最大堆，是整体arr中最小的k个
    # 取任一元素如果比top更大，直接跳过
    # 如果比最大小，替换top元素，然后shift down

    hh = Heap(arr[:k])
    # 构造一个k的最大堆，是整体arr中最小的k个
    # O(klogk)
    hh.build()
    current_index = k
    # O((n-k)logk)
    while True:
        if current_index >= length:
            # 遍历结束
            break
        if arr[current_index] > hh.arr[0]:
            # 取任一元素如果比top更大，直接跳过
            current_index += 1
            continue
        # 如果比最大小，替换top元素，然后shift down
        hh.arr[0] = arr[current_index]
        hh.shift_down(0)
        current_index += 1
    print(f'最小的k个:{hh.arr}')
    # 总复杂度 nlogk
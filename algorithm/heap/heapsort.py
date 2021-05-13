from pdb import main
import pdb
import random


class Heap(object):

    myarr = []
    end_index = None # last index

    def __init__(self, myarr):
        super().__init__()
        self.myarr = myarr
        self.end_index = len(self.myarr) - 1

    def _shift_down(self, current_index):
        # root_index 和 min_index 的元素swap交换
        if current_index >= self.end_index:
            return

        root_index = current_index
        left_index = root_index * 2 + 1
        right_index = root_index * 2 + 2
        min_index = root_index

        if right_index <= self.end_index:
            # root, left, right 三个元素都存在
            if self.myarr[left_index] < self.myarr[min_index]:
                min_index = left_index
            if self.myarr[right_index] < self.myarr[min_index]:
                min_index = right_index
        elif left_index <= self.end_index:
            # right 元素不存在，root和left存在
            if self.myarr[left_index] < self.myarr[root_index]:
                min_index = left_index
        else:
            # 只有root元素存在
            return
        if root_index != min_index:
            # 如果产生了swap交换，需要调整交换后index开始的子树
            self.myarr[root_index], self.myarr[min_index] = self.myarr[min_index], self.myarr[root_index]
            self._shift_down(min_index)
        else:
            return

    def _shift_up(self, current_index):
        # import pdb; pdb.set_trace()
        if current_index > self.end_index:
            return
        while True:
            # 把current_index 的元素 shift up 到它应该在的最小的位置
            parent_index = int((current_index - 1)/2)
            if parent_index < 0:
                break
            if self.myarr[parent_index] > self.myarr[current_index]:
                self.myarr[parent_index], self.myarr[current_index] = self.myarr[current_index], self.myarr[parent_index]
                current_index = parent_index
            else:
                break

    def build_min_heap(self):
        # 因为堆是一个完全二叉树，所以从最后一位开始调整
        for index in range(len(self.myarr)-1, -1, -1):
            self._shift_down(index)
        print(self.myarr)
    
    def insert(self, value):
        self.myarr.append(value)
        self.end_index = len(self.myarr) - 1
        self._shift_up(self.end_index)
    
    def replace_top(self, value):
        top_value = self.myarr[0]
        self.myarr[0] = value
        self._shift_down(0)
        return top_value

    def bottom_to_top(self):
        # top_value 可能是None，不管。用bottom取代top并shift_down
        if not self.myarr:
            return
        if self.end_index <= 0:
            return
        top_value = self.myarr[0]
        bottom_value = self.myarr[self.end_index]
        self.myarr[0] = bottom_value
        self.end_index -= 1
        self._shift_down(0)
        return top_value
    
    def desc(self):
        # 用最小堆重排为myarr从大到小
        while True:
            # import pdb; pdb.set_trace()
            if self.end_index <= 0:
                break
            self.myarr[self.end_index], self.myarr[0] = self.myarr[0], self.myarr[self.end_index]
            self.end_index -= 1
            self._shift_down(0)
            
        # 全部排序之后，记得恢复self.end_index
        print(self.myarr)
        self.end_index = len(self.myarr) - 1


def heap_sort(myarr):
    # 从小到大排序
    result = []
    hh = Heap(myarr)
    hh.build_min_heap()
    for i in range(len(myarr)):
        result.append(hh.myarr[0])
        hh.bottom_to_top()
    print(result)
    return result


if __name__ == '__main__':
    myarr = [1,5,8,3,10,5,2]
    print(myarr)
    # hh = Heap(myarr)
    # hh.build_min_heap()
    # # import pdb; pdb.set_trace()
    # print(hh.myarr)
    # hh.insert(4)
    # print(hh.myarr)
    # top = hh.replace_top(7)
    # print(f'poped out {top}')
    # print(hh.myarr)

    # 堆排序
    # heap_sort(myarr)
    hh = Heap(myarr)
    hh.build_min_heap()
    hh.desc()


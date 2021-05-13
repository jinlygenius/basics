'''
It improves upon bubble sort and insertion sort by moving out of order elements more than one position at a time. One implementation can be described as arranging the data sequence in a two-dimensional array and then sorting the columns of the array using insertion sort.
O(nlogn) algorithms
'''


def shell_sort(data, gap=6):
    if gap < 1:
        return data
    length = len(data)
    for iii in range(0, gap):
        for nnn in range(length / gap, -1, -1):
            for jjj in range(nnn, 0, -1):
                if jjj * gap + iii >= length:
                    continue
                if data[jjj * gap + iii] < data[(jjj - 1) * gap + iii]:
                    data[jjj * gap + iii], data[(jjj - 1) * gap + iii] = data[(jjj - 1) * gap + iii], data[jjj * gap + iii]
    # import pdb; pdb.set_trace()
    gap = gap / 8
    shell_sort(data, gap)
    return data

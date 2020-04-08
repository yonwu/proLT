from sortarray import *


def insertion_sort(sa):
    for index in range(1, sa.getSize()):

        position = index

        while position > 0:
            if sa.cmp(position - 1, index) > 0:
                sa.swap(position - 1, index)
                index = index - 1
            position = position - 1


def quick_sort(sa):
    quick_sort_helper(sa, 0, sa.getSize() - 1)


def quick_sort_helper(sa, first, last):

    if first < last:
        splitpoint = partition(sa, first, last)

        quick_sort_helper(sa, first, splitpoint - 1)
        quick_sort_helper(sa, splitpoint + 1, last)


def partition(sa, first, last):
    pivot_position = first

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and sa.cmp(left_mark, pivot_position) <= 0:
            left_mark = left_mark + 1
        while sa.cmp(right_mark, pivot_position) >= 0 and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            sa.swap(left_mark, right_mark)
    sa.swap(first, right_mark)

    return right_mark


def selectionSort(sa):
    for i in range(0, sa.getSize() - 1):
        min = i
        for j in range(i + 1, sa.getSize()):
            if sa.cmp(j, min) < 0:
                min = j
        sa.swap(i, min)


debug = True

print("-----------------------------------------------------------------------------")
print("test of quick sort")
sa = SortArray()
for size in range(10, 51, 20):
    print("SIZE: ", size)

    for method in ["shuffle"]:
        print("METHOD: ", method)

        sa.reset(size, method)

        if debug:
            print("before: ")
            sa.printList()

        # selectionSort(sa)
        quick_sort(sa)
        # insertion_sort(sa)

        if debug:
            print("after: ")
            sa.printList()

        sa.printInfo()

    print()
print("-----------------------------------------------------------------------------")

print("-----------------------------------------------------------------------------")
print("test of insertion  sort")
sa = SortArray()
for size in range(10, 51, 20):
    print("SIZE: ", size)

    for method in ["shuffle"]:
        print("METHOD: ", method)

        sa.reset(size, method)

        if debug:
            print("before: ")
            sa.printList()

        # selectionSort(sa)
        # quick_sort(sa)
        insertion_sort(sa)

        if debug:
            print("after: ")
            sa.printList()

        sa.printInfo()

    print()
print("-----------------------------------------------------------------------------")

print("-----------------------------------------------------------------------------")
print("test of selection  sort")
sa = SortArray()
for size in range(10, 51, 20):
    print("SIZE: ", size)

    for method in ["shuffle"]:
        print("METHOD: ", method)

        sa.reset(size, method)

        if debug:
            print("before: ")
            sa.printList()

        selectionSort(sa)

        if debug:
            print("after: ")
            sa.printList()

        sa.printInfo()

    print()

from sortarray import *


def selectionSort(sa):
    for i in range(0, sa.getSize()-1):
        min = i
        for j in range(i+1, sa.getSize()):
            if sa.cmp(j,min) < 0:
                min = j
        sa.swap(i,min)


debug = False

sa = SortArray()
for size in range(10, 51, 20):
    print ("SIZE: ", size)

    for method in ["shuffle", "miniShuffle", "reverse"]:
        print ("METHOD: ", method)

        sa.reset(size, method)

        if debug:
            print ("before: ")
            sa.printList()
        
        selectionSort(sa)

        if debug:
            print ("after: ")
            sa.printList()

        sa.printInfo()
    
    print()

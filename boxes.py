class Box:

    def __init__(self, capacity):
        self.capacity = capacity
        self.item_list = []

    def add(self, item):
        item_size = check_item_size(item)
        if self.free() >= item_size:
            self.item_list.append(item)
            return True
        else:
            return "Fail"

    def empty(self):
        item_in_box = []
        item_in_box.extend(self.item_list)
        self.item_list.clear()
        return item_in_box

    def count(self):
        return len(self.item_list)

    def free(self):
        free_space = self.capacity
        free_space = free_space - self.occupied_space()
        return free_space

    def occupied_space(self):
        occupied_space = 0
        for x in self.item_list:
            occupied_space = occupied_space + check_item_size(x)
        return occupied_space

    def size(self):
        return self.capacity


class IntBox(Box):
    def add(self, item):
        item_size = check_item_size(item)
        if self.free() >= item_size and isinstance(item, int):
            self.item_list.append(item)
            return True
        else:
            return "Fail"


def check_item_size(item):
    if hasattr(item, '__len__'):
        return len(item)
    elif hasattr(item, 'size'):
        return item.size()
    else:
        return 1


def repack(boxes):
    item_all = []
    boxes_regular = []
    boxes_int = []
    item_regular = []
    item_int = []
    for box in boxes:
        item_all.extend(box.empty())
        if isinstance(box, IntBox):
            boxes_int.append(box)
        else:
            boxes_regular.append(box)
    boxes_rearrange = boxes_regular + boxes_int
    for item in item_all:
        if isinstance(item, int):
            item_int.append(item)
        else:
            item_regular.append(item)
    print(item_regular)
    print(item_int)
    item_rearrange = item_regular + item_int
    print(item_rearrange)
    for box in boxes_rearrange:
        items_remian = item_rearrange
        for item in items_remian:
            if box.add(item):
                item_rearrange.remove(item)


if __name__ == "__main__":
    b = Box(5)
    print(b.add([10, 11, 12]))
    print(b.add('abc'))
    print(b.add(9))
    print(b.add('x'))
    print(b.empty())
    b1 = IntBox(2)
    print(b1.add('1'))
    print(b1.add(1))
    print(b1.add(2))
    print(b1.empty())

    b2 = Box(5)
    print(b2.add([10, 11, 12]))
    print(b2.add(9))
    print(b2.add('x'))
    b3 = IntBox(2)
    print(b3.add(1))
    print(b3.add(2))
    b4 = Box(5)
    print(b4.add('abc'))
    print(b4.add(9))
    print(b4.add('x'))

    list_of_box = [b2, b3, b4]
    print('Try to repack the list of boxes')
    repack(list_of_box)
    print("Check what's in every boxes in the list now")
    print('b =', b2.empty())
    print('bb =', b3.empty())
    print('bbb =', b4.empty())

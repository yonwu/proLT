class Box:

    def __init__(self, capacity):
        self.capacity = capacity
        self.item_list = []

    def add(self, item):
        item_size = check_item_size(item)
        if self.free_space() >= item_size:
            self.item_list.append(item)
            return True
        else:
            return False

    def empty(self):
        item_in_box = []
        item_in_box.extend(self.item_list)
        self.item_list.clear()
        return item_in_box

    def count(self):
        return len(self.item_list)

    def free_space(self):
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
        if self.free_space() >= item_size and isinstance(item, int):
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
    item_rearrange = item_regular + item_int
    print(item_rearrange)
    print(item_rearrange[:])
    for box in boxes_rearrange:
        for item in item_rearrange[:]:
            if box.free_space() >= check_item_size(item):
                box.add(item)
                item_rearrange.remove(item)
            else:
                continue


if __name__ == "__main__":
    b2 = Box(2)
    b2.add(1)

    b3 = IntBox(1)
    b3.add(2)

    b4 = Box(1)
    b4.add('a')

    list_of_box = [b2, b3, b4]
    print('Try to repack the list of boxes')
    repack(list_of_box)
    print("Check what's in every boxes in the list now")
    print('b2 =', b2.empty())
    print('b3 =', b3.empty())
    print('b4 =', b4.empty())

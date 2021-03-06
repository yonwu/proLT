class Node:

    def __init__(self, word):
        self._word = word
        self._frequency = 1
        self._next = None

    def get_word(self):
        return self._word

    def set_word(self, new_word):
        self._word = new_word

    def get_frequency(self):
        return self._frequency

    def set_frequency(self, new_frequency):
        self._frequency = new_frequency

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next


class FreqLinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head
        while current:
            print(current.get_word(), current.get_frequency())
            current = current.get_next()

    def search_and_modify_frequency(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_word() == item:
                found = True
                current.set_frequency(current.get_frequency() + 1)
            else:
                if current.get_word() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def addWord(self, item):
        current = self.head
        previous = None
        stop = False
        found = self.search_and_modify_frequency(item)

        while current is not None and not stop:
            if current.get_word() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        if not found:
            temp = Node(item)
            if previous is None:
                temp.set_next(self.head)
                self.head = temp
            else:
                temp.set_next(current)
                previous.set_next(temp)

    def filterWords(self, frequency):
        current = self.head
        previous = None
        while current:
            if current.get_frequency() < frequency:
                if previous is None:
                    self.head = current.get_next()
                    current = self.head
                else:
                    previous.set_next(current.get_next())
                    current = previous.get_next()
            else:
                previous = current
                current = current.get_next()






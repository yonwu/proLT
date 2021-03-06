from collections import deque
from timeit import default_timer as timer

SORTED_WORD_LIST = [line.rstrip('\n') for line in open('./sortedWordList.txt')]
TO_SEARCH_LIST = [line.rstrip('\n') for line in open('./toSearchFor.txt')]
SORTED_WORD_DEQUE = deque(line.rstrip('\n') for line in open('./sortedWordList.txt'))
SORTED_WORD_DIC = {}
for index, item in enumerate(SORTED_WORD_LIST):
    SORTED_WORD_DIC[item] = index


def sequential_search_index(word_list, word):
    for i in range(0, len(word_list)):
        if word_list[i] == word:
            return i
    return -1


def sequential_search_enumerate(word_list, word):
    for i, w in enumerate(word_list):
        if w == word:
            return i
    return -1


def binary_search(word_list, item):
    if binary_check(word_list, item):
        return word_list.index(item)
    else:
        return -1


def binary_check(word_list, word):
    first = 0
    last = len(word_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if word_list[midpoint] == word:
            found = True
        else:
            if word < word_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def search_in_dic(word_list, word):
    for key, value in word_list.items():
        if key == word:
            return value
        else:
            return -1
'''
print("search in dictionary")
start = timer()
for word in TO_SEARCH_LIST:
    search_in_dic(SORTED_WORD_DIC, word)
end = timer()
print(end - start)

print("search in list uses indexing")
start = timer()
for word in TO_SEARCH_LIST:
    sequential_search_index(SORTED_WORD_LIST, word)
end = timer()
print(end - start)

print("search in list using enumerate")
start = timer()
for word in TO_SEARCH_LIST:
    sequential_search_enumerate(SORTED_WORD_LIST, word)
end = timer()
print(end - start)


print("search in deque")
start = timer()
for word in TO_SEARCH_LIST:
    binary_search(SORTED_WORD_LIST, word)
end = timer()
print(end - start)
'''

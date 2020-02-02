import unittest

from boxes import Box


class TestBoxes(unittest.TestCase):

    def test_creating(self):
        b = Box(10)
        self.assertEqual(b.capacity, 10)

    def test_adding_number(self):
        b = Box(10)
        number = 17
        b.add(number)
        self.assertEqual(b.free_space(), 9)

    def test_adding_string(self):
        b = Box(20)
        word = 'hello'
        b.add(word)
        self.assertEqual(b.free_space(), 20 - len(word))

    # What is added should get out in the same order
    def test_order(self):
        b = Box(100)
        items = [313, True, 17, (1, 2)]
        for i in items:
            b.add(i)
        self.assertEqual(b.empty(), items)

    def test_doesnt_fit(self):
        b = Box(5)
        self.assertTrue(b.add(2))
        self.assertFalse(b.add('abcde'))
        self.assertEqual(b.free_space(), 4)


if __name__ == '__main__':
    unittest.main()

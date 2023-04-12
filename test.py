import unittest
from whiteboard import solution

class WhiteboardTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution('xyaabbbccccdefww', 'xxxxyyyyabklmopq'), 'abcdefklmopqwxy')

    def test_2(self):
        self.assertEqual(solution('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz'), 'abcdefghijklmnopqrstuvwxyz')

    def test_3(self):
        self.assertEqual(solution('aaaaaaaab', 'c'), 'abc')

    def test_4(self):
        self.assertEqual(solution('lnadflnfdsnfnfvlalhjfds', 'knacsdcdlnjafanfj'), 'acdfhjklnsv' )

    def test_5(self):
        self.assertEqual(solution('a', 'a'), 'a')

    def test_6(self):
        self.assertEqual(solution('qwerty', 'asdfgh'), 'adefghqrstwy')

    def test_7(self):
        self.assertEqual(solution('', ''), '')

if __name__ == '__main__':
    unittest.main()
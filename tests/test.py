import unittest
from lab import format


class TestLab4(unittest.TestCase):
    def test1(self):
        self.assertEqual(format('+7(912)123-12-12'), '+1 912-123-1212')

    def test2(self):
        self.assertEqual(format('+7 (999) 99-9-99-99'), '+1 999-999-9999')

    def test3(self):
        self.assertEqual(format('+7  999 999-9999'), '+1 999-999-9999')
        
    def test4(self):
        self.assertEqual(format('+7 (999) 999-99-99'), '+1 999-999-9999')

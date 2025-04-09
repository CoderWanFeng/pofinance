import unittest

from pofinance import t0


class TestT(unittest.TestCase):

    def test_t0(self):
        print(t0(112.23565656565, 112.36, 700))

import unittest

from pofinance import t0, t1


class TestT(unittest.TestCase):

    def test_t0(self):
        logger.info(t0(112.23565656565, 112.36, 700))

    def test_t1(self):
        print(t1(112.23565656565, 112.36, 700))

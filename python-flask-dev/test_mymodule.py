'''Tests for mymodule.py'''

import unittest

from mymodule import square, doubler

class TestMyModule(unittest.TestCase):
    '''Class for testing the functions of mymodule.py.'''

    def test_square(self):
        '''Tests if function square is operating as it should.'''

        self.assertEqual(square(2), 4)

    def test_doubler(self):
        '''Tests if doubler is operating as it should.'''

        self.assertEqual(doubler(0), 0)

if __name__ == '__main__':
    unittest.main()

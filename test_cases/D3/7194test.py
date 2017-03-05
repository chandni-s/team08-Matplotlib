import unittest
import matplotlib.pyplot as plt
from matplotlib import figure

class TestingIssue7194(unittest.TestCase):


    '''(TestingIssue7194) -> None
    Test if adding a subplot to the AxesStack with a positive key
    '''
    def test_adding_subplot_with_positive_key(self):
        a = figure.AxesStack()
        try:
            a.add('123',plt.figure().add_subplot(111))
            a.add('123',plt.figure().add_subplot(111))
            self.assertTrue(True)
        except:
            self.assertTrue(False)

    '''(TestingIssue7194) -> None
    Test if adding a subplot to the AxesStack with a positive key
    that is not 3 digits long. All keys must be 3 digits as per
    matplotlib implementation.
    '''
    def test_adding_subplot_with_positive_key_not_three_digits(self):
        a = figure.AxesStack()
        with self.assertRaises(ValueError):
            a.add('123',plt.figure().add_subplot(11))


    '''(TestingIssue7194) -> None
    Test if adding a subplot to the AxesStack with a negative key
    '''
    def test_adding_subplot_with_negative_key(self):
        a = figure.AxesStack()
        with self.assertRaises(ValueError):
            a.add('123',plt.figure().add_subplot(-111))


    '''(TestingIssue7194) -> None
    Test if adding a subplot to the AxesStack with a zero key
    '''
    def test_adding_subplot_with_zero_key(self):
        a = figure.AxesStack()
        with self.assertRaises(ValueError):
            a.add('123',plt.figure().add_subplot(0))

if __name__ == '__main__':
    unittest.main()

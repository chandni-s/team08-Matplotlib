import unittest
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero
import matplotlib.axis as axis

class TestingIssue7617(unittest.TestCase):

    # Create the new subplot and pull the AxisArtists out
    def setUp(self):
        fig = plt.figure()
        ax = SubplotZero(fig, 111)
        _ = fig.add_subplot(ax)
        self.XArtist = ax.axis["xzero"]
        self.YArtist = ax.axis["yzero"]

    # Test if the axis are of the correct type
    def test_axistype(self):
        self.assertTrue(isinstance(self.XArtist.axis, axis.XAxis))
        self.assertTrue(isinstance(self.YArtist.axis, axis.YAxis))

    # Test if the labels are being set
    def test_label(self):
        plt.xlabel("xTest")
        plt.ylabel("yTest")
        self.assertEqual(self.XArtist.axis.label.get_text(), "xTest")
        self.assertEqual(self.YArtist.axis.label.get_text(), "yTest")

    # as the axis_direction is what defines whether what type of axis is created
    # we should confirm that value is correct as well
    def test_axis_direction(self):
        self.assertEqual(self.XArtist._axis_direction, "bottom")
        self.assertEqual(self.YArtist._axis_direction, "left")

if __name__ == '__main__':
    unittest.main()
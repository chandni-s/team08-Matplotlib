import unittest
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import numpy as np

class TestAxisArtistRotation(unittest.TestCase):

    def test_set_rotation(self):
        host = host_subplot(111, axes_class=AA.Axes)
        plt.subplots_adjust(bottom=0.15)
        host.plot(10, 10)
        host.set_xticks([10.2, 10.4, 10.6])
        host.set_xticklabels(['A', 'B', 'C'], rotation=45)
        ticks = host.get_xmajorticklabels()
        self.assertEquals(len(ticks), 3)
        self.assertEqual(ticks[0].get_rotation(), 45)
        self.assertEqual(ticks[1].get_rotation(), 45)
        self.assertEqual(ticks[2].get_rotation(), 45)

    def test_set_rotation_ninety(self):
        host = host_subplot(111, axes_class=AA.Axes)
        plt.subplots_adjust(bottom=0.15)
        host.plot(10, 10)
        host.set_xticks([10.2, 10.4, 10.6])
        host.set_xticklabels(['A', 'B', 'C'], rotation=90)
        ticks = host.get_xmajorticklabels()
        self.assertEquals(len(ticks), 3)
        self.assertEqual(ticks[0].get_rotation(), 90)
        self.assertEqual(ticks[1].get_rotation(), 90)
        self.assertEqual(ticks[2].get_rotation(), 90)

    def test_set_rotation_one_eighty(self):
        host = host_subplot(111, axes_class=AA.Axes)
        plt.subplots_adjust(bottom=0.15)
        host.plot(10, 10)
        host.set_xticks([10.2, 10.4, 10.6])
        host.set_xticklabels(['A', 'B', 'C'], rotation=180)
        ticks = host.get_xmajorticklabels()
        self.assertEquals(len(ticks), 3)
        self.assertEqual(ticks[0].get_rotation(), 180)
        self.assertEqual(ticks[1].get_rotation(), 180)
        self.assertEqual(ticks[2].get_rotation(), 180)

    def test_set_rotation_text(self):
        host = host_subplot(111, axes_class=AA.Axes)
        plt.subplots_adjust(bottom=0.15)
        host.plot(10, 10)
        host.set_xticks([10.2, 10.4, 10.6])
        host.set_xticklabels(['A', 'B', 'C'], rotation="horizontal")
        ticks = host.get_xmajorticklabels()
        self.assertEquals(len(ticks), 3)
        self.assertEqual(ticks[0].get_rotation(), 180)
        self.assertEqual(ticks[1].get_rotation(), 180)
        self.assertEqual(ticks[2].get_rotation(), 180)

    def test_set_rotation_text(self):
        host = host_subplot(111, axes_class=AA.Axes)
        plt.subplots_adjust(bottom=0.15)
        host.plot(10, 10)
        host.set_xticks([10.2, 10.4, 10.6])
        host.set_xticklabels(['A', 'B', 'C'], rotation="vertical")
        ticks = host.get_xmajorticklabels()
        self.assertEquals(len(ticks), 3)
        self.assertEqual(ticks[0].get_rotation(), 90)
        self.assertEqual(ticks[1].get_rotation(), 90)
        self.assertEqual(ticks[2].get_rotation(), 90)

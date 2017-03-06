import unittest
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import RRuleLocator 

class testing_8089(unittest.TestCase):

	def test_tickertooHigh(self):
		try:
			locator = mpl.dates.MinuteLocator(interval=1)
			x = []
			x = range(1,2000)
			locator.raise_if_exceeds(x)
			self.assertTrue(True)
		except:
			self.assertTrue(False)
	def test_tickerTooLow(self):
		try:
			locator = mpl.dates.MinuteLocator(interval=1)
			x = []
			x = range(1,500)
			locator.raise_if_exceeds(x)
			self.assertTrue(True)
		except:
			self.assertTrue(False)

if __name__=='__main__':
	unittest.main()
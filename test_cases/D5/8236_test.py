import unittest
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerAnnotation
from matplotlib.offsetbox import DrawingArea
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import ArrowStyle
from matplotlib.text import Text

class Test8236(unittest.TestCase):

    # Test if label gets added for a line with arrows (special case) <-->
    def test_add_legend_arrow_line(self):
        fig, ax = plt.subplots(1)
        ax.annotate("",
                    xy=(0.4, 1.0),
                    xytext=(0.4, 0.0),
                    arrowprops={'arrowstyle': '<->', 'color': 'C7'},
                    label='distance')
        ax.legend()

        handles, labels = ax.get_legend_handles_labels()
        self.assertTrue('distance' in labels)

    # labels should not have 'distance' as it is initiating with underscore
    def test_add_legend_underscore(self):
        fig, ax = plt.subplots(1)
        ax.annotate("",
                    xy=(0.4, 1.0),
                    xytext=(0.4, 0.0),
                    arrowprops={'arrowstyle': '<->', 'color': 'C7'},
                    label='_distance')
        ax.legend()

        handles, labels = ax.get_legend_handles_labels()
        self.assertFalse('distance' in labels)

    # adding integer as legend, should raise TypeError
    def test_add_legend_integer(self):
        fig, ax = plt.subplots(1)
        ax.annotate("",
                    xy=(0.4, 1.0),
                    xytext=(0.4, 0.0),
                    arrowprops={'arrowstyle': '<->', 'color': 'C7'},
                    label='distance')
        with self.assertRaises(TypeError):
            ax.legend(1)

    # adding integer as label, should raise TypeError
    # def test_add_label_integer(self):
    #     fig, ax = plt.subplots(1)
    #     ax.annotate("",
    #                     xy=(0.4, 1.0),
    #                     xytext=(0.4, 0.0),
    #                     arrowprops={'arrowstyle': '<->', 'color': 'C7'},
    #                     label=1)

    #     with self.assertRaises(TypeError):
    #         ax.legend()

    # only annotation has legend - should have no user warning
    def test_annotation_only(self):
        fig, ax = plt.subplots(1)
        ax.plot([1, 2, 3])
        ax.annotate("",
                    xy=(0.4, 1.0),
                    xytext=(0.4, 0.0),
                    arrowprops={'arrowstyle': '<->', 'color': 'C7'},
                    label='distance')
        ax.legend()
        handles, labels = ax.get_legend_handles_labels()
        self.assertIn('distance', labels)

    #test the newly created handler with a full annotation
    def test_handler_full_annotation(self):
        fig, ax = plt.subplots(1)
        anno = ax.annotate("test",
                    xy=(0.4, 1.0),
                    xytext=(0.4, 0.0),
                    arrowprops={'arrowstyle': '<->', 'color': 'C7'},
                    label='distance')
        legend = ax.legend()
        draw = DrawingArea(20.0,7.0, 0.0, 0.0)
        handle = HandlerAnnotation()
        artists = handle.create_artists(legend,anno,0.0,0.0,20.0,7.0, 10.0, draw)
        self.assertEqual(len(artists), 2)
        self.assertTrue(isinstance(artists[0],FancyArrowPatch))
        self.assertTrue(isinstance(artists[1], Text))
        self.assertTrue(isinstance(artists[0]._arrow_transmuter, ArrowStyle.CurveAB))
        self.assertEqual(artists[1].get_text(), "Aa")

    # test the newly created handler with an annotation with only text
    def test_handler_only_text_annotation(self):
        fig, ax = plt.subplots(1)
        anno = ax.annotate("test",
                           xy=(0.4, 1.0),
                           xytext=(0.4, 0.0),
                           label='distance')
        legend = ax.legend()
        draw = DrawingArea(20.0, 7.0, 0.0, 0.0)
        handle = HandlerAnnotation()
        artists = handle.create_artists(legend, anno, 0.0, 0.0, 20.0, 7.0, 10.0, draw)
        self.assertEqual(len(artists), 1)
        self.assertTrue(isinstance(artists[0], Text))
        self.assertEqual(artists[0].get_text(), "Aa")

    #test the newly created handler with an annotation with only an arrow
    def test_handler_arrow_annotation(self):
        fig, ax = plt.subplots(1)
        anno = ax.annotate("",
                    xy=(0.4, 1.0),
                    xytext=(0.4, 0.0),
                    arrowprops={'arrowstyle': '->', 'color': 'C7'},
                    label='distance')
        legend = ax.legend()
        draw = DrawingArea(20.0,7.0, 0.0, 0.0)
        handle = HandlerAnnotation()
        artists = handle.create_artists(legend,anno,0.0,0.0,20.0,7.0, 10.0, draw)
        self.assertEqual(len(artists), 2)
        self.assertTrue(isinstance(artists[0],FancyArrowPatch))
        self.assertTrue(isinstance(artists[1], Text))
        self.assertTrue(isinstance(artists[0]._arrow_transmuter, ArrowStyle.CurveB))
        self.assertEqual(artists[1].get_text(), "")

    #test the newly created handler with neither text or an arrow
    def test_handler_empty_annotation(self):
        fig, ax = plt.subplots(1)
        anno = ax.annotate("",
                    xy=(0.4, 1.0),
                    xytext=(0.4, 0.0),
                    label='distance')
        legend = ax.legend()
        draw = DrawingArea(20.0,7.0, 0.0, 0.0)
        handle = HandlerAnnotation()
        artists = handle.create_artists(legend,anno,0.0,0.0,20.0,7.0, 10.0, draw)
        self.assertEqual(len(artists), 1)
        self.assertTrue(isinstance(artists[0], Text))
        self.assertEqual(artists[0].get_text(), "")

if __name__ == '__main__':
    unittest.main()

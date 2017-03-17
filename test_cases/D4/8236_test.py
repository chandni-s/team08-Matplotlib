import unittest
import matplotlib.pyplot as plt


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
    def test_add_label_integer(self):
        fig, ax = plt.subplots(1)
        ax.annotate("",
                        xy=(0.4, 1.0),
                        xytext=(0.4, 0.0),
                        arrowprops={'arrowstyle': '<->', 'color': 'C7'},
                        label=1)

        with self.assertRaises(TypeError):
            ax.legend()

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

if __name__ == '__main__':
    unittest.main()

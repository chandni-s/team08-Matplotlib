'''Acceptance test for issue 8236
Originally tried to test following test_legend.py method in using image_comparison.
Did not work as wanted. Need to figure out how to use image_comparison for our
case. Attempted code has been commented out. Currently, acceptance test needs to be
run manually by passing in 'show' parameter in main to 'True'.
'''


# from __future__ import (absolute_import, division, print_function,
#                        unicode_literals)
# import matplotlib.pylab as plt
# from matplotlib.testing.decorators import image_comparison

# try:
#    # mock in python 3.3+
#    from unittest import mock
# except ImportError:
#    import mock


def plot_annotations(style, show=False):
    fig, ax = plt.subplots(1)
    ax.plot([0, 1], [0, 0], label='line1')
    ax.plot([0, 1], [1, 1], label='line2')
    ax.annotate("",
                xy=(0.4, 1.0),
                xytext=(0.4, 0.0),
                arrowprops={'arrowstyle': style, 'color': 'C7'},
                label='annotation')
    ax.legend()
    plt.show()

def plot_annotations_no_style(prop, show=False):
	fig, ax = plt.subplots(1)
    ax.plot([0, 1], [0, 0], label='line1')
    ax.plot([0, 1], [1, 1], label='line2')
    ax.annotate("",
                xy=(0.4, 1.0),
                xytext=(0.4, 0.0),
                arrowprops={prop: 20, 'color': 'C7'},
                label='annotation')
    ax.legend()
    plt.show()

# @image_comparison(baseline_images=['Dash'], remove_text=True)
def test_annotation_dash(show=False):
    if show:
        plot_annotations('-', show)


# @image_comparison(baseline_images=['Right_arrow'], remove_text=True)
def test_annotation_right_arrow(show=False):
    if show:
        plot_annotations('->', show)


# @image_comparison(baseline_images=['Right_bracket'], remove_text=True)
def test_annotation_right_bracket(show=False):
    if show:
        plot_annotations('-[', show)


# @image_comparison(baseline_images=['Flat_ends'], remove_text=True)
def test_annotation_flat_ends(show=False):
    if show:
        plot_annotations('|-|', show)


# @image_comparison(baseline_images=['Right_solid_arrow'], remove_text=True)
def test_annotation_right_solid_arrow(show=False):
    if show:
        plot_annotations('-|>', show)


# @image_comparison(baseline_images=['Left_arrow'], remove_text=True)
def test_annotation_left_arrow(show=False):
    if show:
        plot_annotations('<-', show)


# @image_comparison(baseline_images=['Both_arrow'], remove_text=True)
def test_annotation_both_arrow(show=False):
    if show:
        plot_annotations('<->', show)


# @image_comparison(baseline_images=['Left_solid_arrow'], remove_text=True)
def test_annotation_left_solid_arrow(show=False):
    if show:
        plot_annotations('<|-', show)


# @image_comparison(baseline_images=['Both_solid_arrow'], remove_text=True)
def test_annotation_both_soild_arrow(show=False):
    if show:
        plot_annotations('<|-|>', show)


# @image_comparison(baseline_images=['Both_solid_arrow'], remove_text=True)
def test_annotation_fancy(show=False):
    if show:
        plot_annotations('fancy', show)


# @image_comparison(baseline_images=['Both_solid_arrow'], remove_text=True)
def test_annotation_simple(show=False):
    if show:
        plot_annotations('simple', show)


# @image_comparison(baseline_images=['Wedge'])
def test_annotation_wedge(show=False):
    if show:
        plot_annotations('wedge', show)

# @image_comparison(baseline_images=['Width_20'], remove_text=True)
def test_annotation_width(show=False):
    if show:
	   plot_annotations_no_style('width', show)

# @image_comparison(baseline_images=['Headwidth_20'], remove_text=True)
def test_annotation_width(show=False):
    if show:
	   plot_annotations_no_style('headwidth', show)

# @image_comparison(baseline_images=['Headlength_20'], remove_text=True)
def test_annotation_width(show=False):
    if show:
	   plot_annotations_no_style('headlength', show)	


if __name__ == '__main__':
    test_annotation_wedge()
    test_annotation_fancy()
    test_annotation_simple()
    test_annotation_both_soild_arrow()
    test_annotation_left_solid_arrow()
    test_annotation_both_arrow()
    test_annotation_left_arrow()
    test_annotation_right_solid_arrow()
    test_annotation_flat_ends()
    test_annotation_right_bracket()
    test_annotation_right_arrow()
    test_annotation_dash()
    test_annotation_width()
    test_annotation_headwidth()
    test_annotation_headlength()
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.stats.kde import gaussian_kde
import numpy as np

def kde2d(x, y, color="C0", linewidths=1, axes=None, axis=None, **kwargs):
    """Make a 2d plot of scattered points and their 1d KDE on the sides of the plot.

    Only works with matplotlib 2.0+

    Parameters
    ----------
    x : array
        x data
    y : array
        y data
    color : str
        matplotlib color
    linewidths : float
        width of KDE lines
    axes : 3-element list of axes
        preformatted axes for each subplot (order=[scatter, xkde, ykde])
    axis : 4 element list
        axis for scatter plot

    Keyword args get passed

    Returns
    -------
    fig : Figure object
        matplotlib Figure object
    axes : 3 element list
        axes for each subplot (order=[scatter, xkde, ykde])
    """
    if axes == None:
        fig = plt.figure(figsize=(7,7))
        gs = gridspec.GridSpec(4, 4)
        gs.update(hspace=0.3, wspace=0.3)

        base = plt.subplot(gs[1:,0:3])
        xkde = plt.subplot(gs[0:1,:3], sharex=base)
        ykde = plt.subplot(gs[1:, 3:], sharey=base)
        axes=[base, xkde, ykde]
    else:
        base, xkde, ykde = axes
        fig = axes[0].get_figure()

    xkd = gaussian_kde(x)
    ykd = gaussian_kde(y)

    xx = np.linspace(min(x), max(x), 1000)
    yy = np.linspace(min(y), max(y), 1000)
    px = xkd.pdf(xx)
    py = ykd.pdf(yy)
    px = px/sum(px)
    py = py/sum(py)

    # Set up base figure
    base.plot(x,y, marker="o", linewidth=0, color=color, **kwargs)
    base.spines["right"].set_visible(False)
    base.spines["top"].set_visible(False)
    if axis is not None:
        base.axis(axis)

    xkde.plot(xx, px, color=color, linewidth=linewidths)
    xkde.spines["right"].set_visible(False)
    xkde.spines["top"].set_visible(False)
    plt.setp(xkde.get_xticklabels(), visible=False)

    ykde.plot(py, yy, color=color, linewidth=linewidths)
    ykde.spines["right"].set_visible(False)
    ykde.spines["top"].set_visible(False)
    plt.setp(ykde.get_yticklabels(), visible=False)

    return fig, axes

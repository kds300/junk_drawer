"""Spectral Analysis helper code
"""

import numpy as np
import matplotlib.pyplot as plt


def specshow(spec:np.ndarray, ax=None, **kwargs):
    """Use plt.imshow to plot the provided spectrogram, with the following
    modified default parameters:

    origin = 'lower'
    aspect = 'auto'
    cmap = 'jet'
    interpolation = 'none'
    """
    if ax is None:
        ax = plt.gca()
    origin = kwargs.pop('origin', 'lower')
    aspect = kwargs.pop('aspect', 'auto')
    cmap = kwargs.pop('cmap', 'jet')
    interpolation = kwargs.pop('interpolation', 'none')
    ax.imshow(
        spec,
        origin=origin, cmap=cmap, aspect=aspect, interpolation=interpolation,
        **kwargs
    )


def format_yaxis_kHz(ax=None):
    """Reformat y-axis showing frequency to display in kHz.
    """
    if ax is None:
        ax = plt.gca()

    yticks = ax.get_yticks()

    ax.set_yticks(
        yticks,
        [tick / 1000 for tick in yticks],
    )
    ax.set_ylabel('Frequency (kHz)')

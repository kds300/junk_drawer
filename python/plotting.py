"""Plotting functions
"""

import matplotlib.pyplot as plt


def remove_borders(borders=['top', 'right'], ax=None):
    """ Removes the specified borders of the axes.

    Default borders are top and right.
    """
    if ax is None:
        ax = plt.gca()
    ax.spines[borders].set_visible(False)


def plot_event_label_boundaries(
    events:list, boundary_kwargs:dict={}, text_kwargs:dict={}, ax=None,
):
    """Plots boundaries and labels for events defined by a start time, stop
    time, and label.
    
    Parameters
    ----------
    events: list
        List of events [start_time, stop_time, label] for plotting.
    bound_kwargs: dict
        Keyword arguments for plotting the event boundaries (plt.axvline)
    text_kwargs: dict
        Keyword arguments for plotting the event labels (plt.text)
    """
    # get current axes if None supplied
    if not ax:
        ax = plt.gca()
    # default kwargs for boundaries and text
    _boundary_kwargs = {
        'linestyle': 'dashed',
        'color': 'gray',
        'zorder': 0
    }
    _text_kwargs = {
        'y': 0.01,
        'ha': 'center',
        'bbox': {
            'alpha': 0.8,
            'color': 'white',
            'boxstyle': 'Round4, pad=0.0'
        },
        'transform': ax.get_xaxis_transform()
    }

    # update with supplied args
    _boundary_kwargs.update(boundary_kwargs)
    _text_kwargs.update(text_kwargs)

    xi, xf = ax.get_xlim()
    for start_time, stop_time, label in events:
        if start_time <= xf:
            ax.axvline(start_time, **_boundary_kwargs)
        if stop_time >= xi:
            ax.axvline(stop_time, **_boundary_kwargs)
        if xi <= (start_time + stop_time) / 2 <= xf:
            ax.text(x=(start_time + stop_time) / 2, s=label, **_text_kwargs)

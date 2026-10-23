"""
signal_filter.py

A module for basic time-series signal processing operations.
"""

import numpy as np

def moving_average(data: list, window_size: int) -> list:
    """
    Calculates the moving average of a 1D time-series signal to smooth out short-term fluctuations.

    Args:
        data (list): A sequence of numerical values representing the raw signal.
        window_size (int): The number of consecutive data points to include in the rolling window.

    Returns:
        list: A new list containing the smoothed signal data.

    Raises:
        ValueError: If the window_size is less than 1 or exceeds the length of the data array.
    """
    if window_size < 1 or window_size > len(data):
        raise ValueError("Window size must be between 1 and the length of the data.")
    
    window = np.ones(int(window_size)) / float(window_size)
    smoothed = np.convolve(data, window, 'valid')
    return smoothed.tolist()
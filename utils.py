"""
This file has common functions
"""
# Define new functions
import math


def protectedDiv(numerator, denominator,):
    """
    Returns the division between the numerator and denominator, unless the denominator is zero then returns 1
    :param numerator:
    :param denominator:
    :return:
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        if numerator is type(int):
            return 1
        else:
            return 1.0



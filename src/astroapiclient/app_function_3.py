'''This module contains functions that generate long(er) term compatibility.'''

## importing necessary libraries
import pandas as pd
import numpy as np

# importing build_dataset module
from astroapiclient import build_dataset as bd

# get df of astrological data
df = bd.df
df['Compatibility'] = df['Compatibility'].str.lower()

def best_compatibility(sign):
    '''
    This functions returns the best compatible sign. 

    Parameters:
    -----------
        sign: a string, the zodiac sign

    Returns:
    --------
        The return value is the most frequent sign that pairs with the given zodiac sign.

    Example:
    --------
    >>>> best_compatibility('capricorn')
    'scorpio'
        '''
    assert type(sign) == str, "sign must be a valid zodiac sign"
    lst = list(df[df['Sun Sign'] == sign]['Compatibility']) + list(df[df['Compatibility'] == sign]['Sun Sign'])
    return max(lst, key=lst.count)
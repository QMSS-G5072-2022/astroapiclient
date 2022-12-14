'''This module contains functions that generate key trends/words based on the description column values.'''

## importing necessary libraries 
import pandas as pd 
import numpy as np
from itertools import compress
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import contractions

# importing build_dataset module
import build_dataset as bd

# get df of astrological data
df = bd.df

# separate contractions
df['temp'] = [contractions.fix(x) for x in df['Description']]
# split each sentence into a list of words to work witj
df['temp'] = [i.split() for i in df['temp']]
# detect which words are important/meaningful
df['key_words_bool'] = [list(map(lambda x: x.lower() not in ENGLISH_STOP_WORDS, i)) for i in df['temp']]
# get the final key words for each day
df['Key Words'] = [list(compress(df['temp'][i],df['key_words_bool'][i])) for i in range(len(df))]
# get long term key words 
results = df[['Sun Sign', 'Key Words']].groupby('Sun Sign').sum()

def key_words(sign):
    '''This function, key_words, takes in a string, the zodiac sign.
    The return value is the most popular key word used in the horoscopes. (Generates a theme.)'''
    assert type(sign) == str, "sign must be a valid zodiac sign"
    all_key_words = results.loc[sign][0]
    return max(all_key_words, key=all_key_words.count)


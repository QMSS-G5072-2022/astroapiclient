'''This module contains functions that generate trends for the remaining columns.'''

# importing necessary libraries
import pandas as pd
import numpy as np
import re

# import build_dataset module
from astroapiclient import build_dataset as bd

# get df of astrological data
df = bd.df

def overall(var, sign):
	'''
	This function generates key trends based on what the user wants to know about over a long(er)
	term period.

	Parameters:
	-----------
		var: a string that represents the column in which the user wants to know about
		sign: a string, the zodiac sign

	Returns:
	--------
	The return value is the most prominent column value over the 3 day period.
	
	Example:
	--------
	>>>> overall('Color', 'capricorn')
	'Brown'
	'''
	assert type(sign) == str, "sign must be a valid zodiac sign"
	assert type(var) == str, "var must be a valid data name"
	temp = df.groupby('Sun Sign')[var].apply(list)
	lst = temp[sign]
	return max(lst, key=lst.count)


'''This module contains functions to build and clean a dataset from the generate_data file.'''

## importing necessary libraries
import pandas as pd
import numpy as np  
import re

# importing generate_data module
import generate_data as gd

# generating data
today_lst = gd.today_data()
yesterday_lst = gd.yesterday_data()
tomorrow_lst = gd.tomorrow_data()

# extract date from each lst
def extract_date(txt):
	date = re.findall(r'"current_date":\s"(.+[0-9]{4})', txt)
	return date

def date_for_each():
	lst = yesterday_lst + today_lst + tomorrow_lst 
	lst_dates = []
	for i in lst:
		lst_dates.append(extract_date(i.text)[0])
	return lst_dates

# extract description from each lst
def extract_description(txt):
	date = re.findall(r'"description":\s"(.+\.)', txt)
	return date

def description_for_each():
	lst = yesterday_lst + today_lst + tomorrow_lst 
	lst_description = []
	for i in lst:
		lst_description.append(extract_description(i.text)[0])
	return lst_description

# extract compatibility from each lst
def extract_compatibility(txt):
	date = re.findall(r'"compatibility":\s"([A-z]{3,11})', txt)
	return date

def compatibility_for_each():
	lst = yesterday_lst + today_lst + tomorrow_lst 
	lst_compatibility = []
	for i in lst:
		lst_compatibility.append(extract_compatibility(i.text)[0])
	return lst_compatibility

# extract mood from each lst
def extract_mood(txt):
	date = re.findall(r'"mood":\s"([A-z]+)', txt)
	return date

def mood_for_each():
	lst = yesterday_lst + today_lst + tomorrow_lst 
	lst_mood = []
	for i in lst:
		lst_mood.append(extract_mood(i.text)[0])
	return lst_mood

# extract color from each lst
def extract_color(txt):
	date = re.findall(r'"color":\s"([A-z]+?\s?[A-z]+)', txt)
	return date

def color_for_each():
	lst = yesterday_lst + today_lst + tomorrow_lst 
	lst_color = []
	for i in lst:
		lst_color.append(extract_color(i.text)[0])
	return lst_color

# extract lucky_number from each lst
def extract_lucky_number(txt):
	lucky_number = re.findall(r'"lucky_number":\s"([0-9]+)', txt)
	return lucky_number

def lucky_number_for_each():
	lst = yesterday_lst + today_lst + tomorrow_lst 
	lst_lucky_number = []
	for i in lst:
		lst_lucky_number.append(extract_lucky_number(i.text)[0])
	return lst_lucky_number

# extract lucky_time from each lst
def extract_lucky_time(txt):
	lucky_time = re.findall(r'"lucky_time":\s"([0-9apm]+)', txt)
	return lucky_time

def lucky_time_for_each():
	lst = yesterday_lst + today_lst + tomorrow_lst 
	lst_lucky_time = []
	for i in lst:
		lst_lucky_time.append(extract_lucky_time(i.text)[0])
	return lst_lucky_time

lst = gd.lst_sun_signs * 3
df = pd.DataFrame({
	'Sun Sign': lst,
	'Date': date_for_each(),
	'Description': description_for_each(),
	'Compatibility': compatibility_for_each(),
	'Mood': mood_for_each(),
	'Color': color_for_each(),
	'Lucky Number': lucky_number_for_each(),
	'Lucky Time': lucky_time_for_each()
	
})
'''This module contains functions that query the Aztro rapid API developed my Sameer Kumar.
Each function generates data for each day avaliable (today, yesterday, tomorrow).'''

## importing necessary libraries
import requests

# base url for API
url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

# API Key + Host
headers = {
	"X-RapidAPI-Key": "4b129e1208msh33e49a5cb1bd56bp1deaf8jsn9d67d65fa24e",
	"X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
}

lst_sun_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius']

def today_data():
	'''generates today's horoscope data for each zodiac sign'''
	lst_response = []
	for sign in lst_sun_signs:
		querystring = {'sign': sign, 'day':'today'}
		response = requests.request("POST", url, headers=headers, params=querystring)
		lst_response.append(response)
	return lst_response

def yesterday_data():
	'''generates yesterday's horoscope data for each zodiac sign'''
	lst_response = []
	for sign in lst_sun_signs:
		querystring = {'sign': sign, 'day':'yesterday'}
		response = requests.request("POST", url, headers=headers, params=querystring)
		lst_response.append(response)
	return lst_response

def tomorrow_data():
	'''generates tomorrow's horoscope data for each zodiac sign'''
	lst_response = []
	for sign in lst_sun_signs:
		querystring = {'sign': sign, 'day':'tomorrow'}
		response = requests.request("POST", url, headers=headers, params=querystring)
		lst_response.append(response)
	return lst_response
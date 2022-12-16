'''This module contains functions that automate the process of obtaining daily horoscope of 
today, yesterday, and tomorrow based on the sun sign inputed.'''

## importing necessary libraries 
import requests 

# base url for API
url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

# API Key + Host
headers = {
	"X-RapidAPI-Key": "4b129e1208msh33e49a5cb1bd56bp1deaf8jsn9d67d65fa24e",
	"X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
}

def horoscope(sign, day):
	'''
	The function returns horoscope information for a given sign and day. 

	Parameters:
	-----------
		sign: string, the zodiac sign
		day: string; yesterday, today, or tomorrow

	Returns:
	--------
		The return value is null as a string with the horoscope information is printed.
	
	Example:
	--------
	>>>> horoscope(sign='capricorn', day='today')
	{"date_range": "Dec 22 - Jan 19", "current_date": "December 16, 2022", "description": 
	"If you don't feel comfortable knowing that you've been giving in to a certain person about 
	financial matters, then it's time to stop. If anyone is intellectually on top of things, it's you. 
	Go with your gut.", "compatibility": "Libra", "mood": "Confidence", "color": "Brown", 
	"lucky_number": "95", "lucky_time": "11pm"}
	'''
	assert type(sign) == str, "sign must be a valid zodiac sign"
	assert type(day) == str, "day must be yesterday, today, or tomorrow"
	querystring = {'sign': sign, 'day': day}
	response = requests.request("POST", url, headers=headers, params=querystring)
	print(response.text)
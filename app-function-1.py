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
	'''This function, horoscope, takes in a string, the zodiac sign, and another string, what day.
	The return value is null as a string with the horoscope information is printed.'''
	assert type(sign) == str, "sign must be a valid zodiac sign"
	assert type(day) == str, "day must be yesterday, today, or tomorrow"
	querystring = {'sign': sign, 'day': day}
	response = requests.request("POST", url, headers=headers, params=querystring)
	print(response.text)
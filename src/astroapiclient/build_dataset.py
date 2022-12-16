'''This module contains functions to build and clean a dataset from the generate_data file.'''

## importing necessary libraries
import pandas as pd
import numpy as np  
import re

# importing generate_data module
from astroapiclient import generate_data as gd

# generating data
today_lst = gd.today_data()
yesterday_lst = gd.yesterday_data()
tomorrow_lst = gd.tomorrow_data()

# extract date from each lst
def extract_date(txt):
	'''
	This function extracts date from each horoscope text.

	Parameters:
	-----------
		txt: a string of the text of the response object

	Returns:
	--------
		A string with the date information

	Example:
	--------
	>>>> extract_date('{"date_range": "Mar 21 - Apr 20", "current_date": "December 16, 2022", 
	"description": "A relationship with someone you've been trying to get 
	close to is finally taking off -- not in a mad, passionate way, but in a comfortable, 
	pleasant, long-lasting way. Have a chat tonight.", "compatibility": "Scorpio", "mood": 
	"Sincere", "color": "Brown", "lucky_number": "68", "lucky_time": "8am"}')
	'December 16, 2022'
	'''
	d = re.findall(r'"current_date":\s"(.+[0-9]{4})', txt)
	return d

def date_for_each():
	'''
	This function applies the extract_date function to all items within the list of response objects. 

	Parameters:
	-----------
		none

	Returns:
	---------
		A list of dates

	Example:
	>>>> date_for_each()
	['December 15, 2022',
	'December 15, 2022',
	'December 15, 2022',
	'December 15, 2022',
	'December 15, 2022',
	'December 15, 2022',
	'December 15, 2022',
	'December 15, 2022',
	'December 15, 2022',
	'December 15, 2022',
	'December 15, 2022',
	'December 16, 2022',
	'December 16, 2022',
	'December 16, 2022',
	'December 16, 2022',
	'December 16, 2022',
	'December 16, 2022',
	'December 16, 2022',
	'December 16, 2022',
	'December 16, 2022',
	'December 16, 2022',
	'December 16, 2022',
	'December 17, 2022',
	'December 17, 2022',
	'December 17, 2022',
	'December 17, 2022',
	'December 17, 2022',
	'December 17, 2022',
	'December 17, 2022',
	'December 17, 2022',
	'December 17, 2022',
	'December 17, 2022',
	'December 17, 2022']
	'''
	lst = today_lst+yesterday_lst+tomorrow_lst
	lst_dates = []
	for i in lst:
		lst_dates.append(extract_date(i.text)[0])
	return lst_dates

# extract description from each lst
def extract_description(txt):
	'''
	This function extracts description from each horoscope text.

	Parameters:
	-----------
		txt: a string of the text of the response object

	Returns:
	--------
		A string with the description horoscope information

	Example:
	--------
	>>>> extract_date('{"date_range": "Mar 21 - Apr 20", "current_date": "December 16, 2022", 
	"description": "A relationship with someone you've been trying to get 
	close to is finally taking off -- not in a mad, passionate way, but in a comfortable, 
	pleasant, long-lasting way. Have a chat tonight.", "compatibility": "Scorpio", "mood": 
	"Sincere", "color": "Brown", "lucky_number": "68", "lucky_time": "8am"}')
	'A relationship with someone you've been trying to get 
	close to is finally taking off -- not in a mad, passionate way, but in a comfortable, 
	pleasant, long-lasting way. Have a chat tonight.'
	'''
	d = re.findall(r'"description":\s"(.+\.)', txt)
	return d

def description_for_each():
	'''
	This function applies the extract_description function to all items within the list of response objects. 

	Parameters:
	-----------
		none

	Returns:
	---------
		A list of dates

	Example:
	>>>> description_for_each()
	["Taking orders is never easy, but sometimes it's easier than giving them. Think about that before you give the person in charge a hard time, even if you're less than tickled with the way they're handling themselves.",
"Still wondering what to do about some information that's been recently -- and quite surreptitiously -- conveyed to you? Follow your instincts, especially if they tell you to just keep it under wraps.",
"You're tempted to go overboard to let someone you love know how grateful you are for what they've done for you. Say thank you, certainly, but don't get crazy.",
"After days of feeling that something is about to turn around, you'll suddenly find that you're right. It's all over. Or, depending on your perspective, it may be just beginning. Until it really gets rolling, sit tight.",
"Get in touch with that higher-up you've always thought of as a surrogate parent of sorts. They'll be happy to help. Besides, they probably know more about what you need right now than you do.",
"A money matter is about to come to the surface, but you won't mind at all. This is probably something you've been trying to uncover for some time. Your relief may actually be mixed with a bit of excitement.",
"Stop daydreaming. You've been so good with your budget and now it's time to have a little fun. Call the airlines, then decide on a hotel. Take someone along, if you like. It's time for a change of scenery.",
'If someone offers you the chance to show off your hobby, take it. It would be fun to see your creations on display, and you never know -- this could soon become a profitable and enjoyable source of part-time income.',
"There's no use trying to hide anything. The full Moon will expose all your feelings to the world. Fortunately, you're more than ready to let them be told. Smile pretty and primp for the cameras.",
"You want to show someone how much you care, and with the mood you're in, the sky's the limit. Think about holding back just a tiny bit. Not to be selfish -- but just in case you need it.",
"You've been known to enjoy a formal evening out, especially if your companion enjoys the opera, the theater or the symphony. Tonight would be a fine night to indulge in those elegant pastimes.",
"A relationship with someone you've been trying to get close to is finally taking off -- not in a mad, passionate way, but in a comfortable, pleasant, long-lasting way. Have a chat tonight.",
"The Moon will be full when you open your eyes, a heavenly event that can't help but put you in the mood to state a case -- probably with regard to a business situation -- with amazing logic and persuasion.",
"The truth about a friend will surface now. That doesn't mean it will be a truth you're uncomfortable with, or that you'll be unhappy with the news. In fact, this is the type of surprise you can definitely live with.",
"If you feel stalled, especially when it comes to a relationship matter, you'll have one major consolation: You're not alone. That may not make it any easier to deal with, but at least you'll be able to commiserate.",
"You've done everything you can in a situation like this. Your mission now is to look forward even as you're realizing that there are all kinds of wonderful lessons to be learned from the past.",
"Getting your travel plans together may be easier said than done now, but if you plan and prepare, you'll be fine. Be sure that Plan B is ready to put into action at a moment's notice.",
"You're not usually prone to taking time off, but you can occasionally be persuaded, as you will be now, by a family member who's determined to drag you away from duty, even if it's just for one evening.",
"Your health and physical appearance are on your mind now, which certainly explains your recent fascination with mirrors. Well, get used to it. The person who's made you so self-aware isn't going anywhere for a while.",
"Things are at a standstill regarding any joint finances. When you're ready -- and don't be in a hurry -- you should seek out the advice and counsel of someone who legitimately cares about what happens to you.",
"If you don't feel comfortable knowing that you've been giving in to a certain person about financial matters, then it's time to stop. If anyone is intellectually on top of things, it's you. Go with your gut.",
"If you didn't get a chance to enjoy the full Moon with someone special, it's not too late. You'll be especially energetic, so sitting up late for a long, lovely chat won't be a problem, especially if it turns romantic.",
"You've never been known for being shy, retiring or unavailable to the ones you love, and that goes double now. You'll happily burn the candle at both ends if it means being able to mingle with new, interesting people.",
"If you need the advice of an authority figure, stop pretending you don't know who to turn to. You'll be pleased to know that the higher-up you've always thought of in warm, friendly terms feels the same about you.",
"You're feeling spontaneous, generous and willing to extend a hand to anyone who needs it. That goes double for the one you love, who'll be able to get you to do their bidding with just one little glance.",
"You're in the mood to do some seriously hard work, and since you're rarely lazy, that's saying something. Rest assured that your efforts will be noticed -- soon -- by the powers that be.",
"Everything's in flux at the moment, which can seem unsettling but actually puts you in an excellent position. Watch for a certain discovery, and steer all the changes in a positive direction.",
"A seemingly irresistible attraction -- whether to a person or a pair of shoes -- is, in fact, fully resistible. And if you're smart, you will resist -- at least your first wild impulse.",
"The soundtrack of your life's been rocking lately, but now it screeches to a halt. The sudden silence is a little unsettling. Take it as a cue to quickly, quietly help someone else out.",
"You've always thought of your coworkers as part of your extended family, and you've just hoped that they felt the same. Well, lucky you. You're about to be shown just how right you are.",
"A family member's spontaneous and unpretentious actions now will demonstrate the depth of their love for and loyalty to you. You may not say a word about it, but you'll be truly touched.",
"If anyone has earned the right to travel at a moment's notice, it's you, especially since you've done everything you can to be reliable, trustworthy, and dependable. You should definitely have your passport ready.",
'An out-of-towner with a terrific accent and an even more exotic attitude is about to cross your path, ready, willing and eager to charge into your life and help you to make some much needed changes.']
	'''
	lst = today_lst+yesterday_lst+tomorrow_lst
	lst_description = []
	for i in lst:
		lst_description.append(extract_description(i.text)[0])
	return lst_description

# extract compatibility from each lst
def extract_compatibility(txt):
	'''
	This function extracts compatibility from each horoscope text.

	Parameters:
	-----------
		txt: a string of the text of the response object

	Returns:
	--------
		A string with the compatibility information

	Example:
	--------
	>>>> extract_date('{"date_range": "Mar 21 - Apr 20", "current_date": "December 16, 2022", 
	"description": "A relationship with someone you've been trying to get 
	close to is finally taking off -- not in a mad, passionate way, but in a comfortable, 
	pleasant, long-lasting way. Have a chat tonight.", "compatibility": "Scorpio", "mood": 
	"Sincere", "color": "Brown", "lucky_number": "68", "lucky_time": "8am"}')
	'Scorpio'
	'''
	d = re.findall(r'"compatibility":\s"([A-z]{3,11})', txt)
	return d

def compatibility_for_each():
	'''
	This function applies the extract_compatibility function to all items within the list of response objects. 

	Parameters:
	-----------
		none

	Returns:
	---------
		A list of zodiac signs

	Example:
	>>>> description_for_each()
	['Gemini',
	'Capricorn',
	'Pisces',
	'Gemini',
	'Libra',
	'Capricorn',
	'Capricorn',
	'Cancer',
	'Leo',
	'Virgo',
	'Leo',
	'Scorpio',
	'Aquarius',
	'Libra',
	'Aries',
	'Capricorn',
	'Scorpio',
	'Cancer',
	'Leo',
	'Capricorn',
	'Libra',
	'Gemini',
	'Sagittarius',
	'Aries',
	'Scorpio',
	'Libra',
	'Aquarius',
	'Sagittarius',
	'Sagittarius',
	'Taurus',
	'Gemini',
	'Gemini',
	'Libra']
	'''
	lst = today_lst+yesterday_lst+tomorrow_lst
	lst_compatibility = []
	for i in lst:
		lst_compatibility.append(extract_compatibility(i.text)[0])
	return lst_compatibility

# extract mood from each lst
def extract_mood(txt):
	'''
	This function extracts mood from each horoscope text.

	Parameters:
	-----------
		txt: a string of the text of the response object

	Returns:
	--------
		A string with the mood information

	Example:
	--------
	>>>> extract_date('{"date_range": "Mar 21 - Apr 20", "current_date": "December 16, 2022", 
	"description": "A relationship with someone you've been trying to get 
	close to is finally taking off -- not in a mad, passionate way, but in a comfortable, 
	pleasant, long-lasting way. Have a chat tonight.", "compatibility": "Scorpio", "mood": 
	"Sincere", "color": "Brown", "lucky_number": "68", "lucky_time": "8am"}')
	'Sincere'
	'''
	d = re.findall(r'"mood":\s"([A-z]+)', txt)
	return d

def mood_for_each():
	'''
	This function applies the extract_mood function to all items within the list of response objects. 

	Parameters:
	-----------
		none

	Returns:
	---------
		A list of moods 

	Example:
	>>>> mood_for_each()
	['Humble',
'Mellow',
'Grateful',
'Cautious',
'Successful',
'Lucky',
'Fun',
'Creative',
'Attractive',
'Thoughtful',
'Sweet',
'Sincere',
'Successful',
'Surprised',
'Warm',
'Focus',
'Relaxed',
'Surprised',
'Attractive',
'Peaceful',
'Confidence',
'Energetic',
'Happy',
'Charming',
'Thoughtful',
'Focus',
'Hopeful',
'Cool',
'Thoughtful',
'Warm',
'Touched',
'Relaxed',
'Creative']
	'''
	lst = today_lst+yesterday_lst+tomorrow_lst
	lst_mood = []
	for i in lst:
		lst_mood.append(extract_mood(i.text)[0])
	return lst_mood

# extract color from each lst
def extract_color(txt):
	'''
	This function extracts color from each horoscope text.

	Parameters:
	-----------
		txt: a string of the text of the response object

	Returns:
	--------
		A string with the color information

	Example:
	--------
	>>>> extract_date('{"date_range": "Mar 21 - Apr 20", "current_date": "December 16, 2022", 
	"description": "A relationship with someone you've been trying to get 
	close to is finally taking off -- not in a mad, passionate way, but in a comfortable, 
	pleasant, long-lasting way. Have a chat tonight.", "compatibility": "Scorpio", "mood": 
	"Sincere", "color": "Brown", "lucky_number": "68", "lucky_time": "8am"}')
	'Brown'
	'''
	d = re.findall(r'"color":\s"([A-z]+?\s?[A-z]+)', txt)
	return d

def color_for_each():
	'''
	This function applies the extract_color function to all items within the list of response objects. 

	Parameters:
	-----------
		none

	Returns:
	---------
		A list of colors 

	Example:
	>>>> color_for_each()
	['Teal',
'Red',
'Peach',
'Brown',
'Brown',
'Blue',
'Brown',
'Brown',
'Blue',
'Navy',
'Yellow',
'Brown',
'Rose',
'Peach',
'Navy',
'Blue',
'Pink',
'Pink',
'Copper',
'Brown',
'Brown',
'Blue',
'Blue',
'Silver',
'Copper',
'Navy',
'Shadow',
'Teal',
'Yellow',
'Pink',
'Spring',
'Orchid',
'Red']
	'''
	lst = today_lst+yesterday_lst+tomorrow_lst
	lst_color = []
	for i in lst:
		lst_color.append(extract_color(i.text)[0])
	return lst_color

# extract lucky_number from each lst
def extract_lucky_number(txt):
	'''
	This function extracts lucky number from each horoscope text.

	Parameters:
	-----------
		txt: a string of the text of the response object

	Returns:
	--------
		A string with the lucky number information

	Example:
	--------
	>>>> extract_date('{"date_range": "Mar 21 - Apr 20", "current_date": "December 16, 2022", 
	"description": "A relationship with someone you've been trying to get 
	close to is finally taking off -- not in a mad, passionate way, but in a comfortable, 
	pleasant, long-lasting way. Have a chat tonight.", "compatibility": "Scorpio", "mood": 
	"Sincere", "color": "Brown", "lucky_number": "68", "lucky_time": "8am"}')
	'68'
	'''
	lucky_number = re.findall(r'"lucky_number":\s"([0-9]+)', txt)
	return lucky_number

def lucky_number_for_each():
	'''
	This function applies the extract_lucky_number function to all items within the list of response objects. 

	Parameters:
	-----------
		none

	Returns:
	---------
		A list of lucky numbers 

	Example:
	>>>> lucky_number_for_each()
	['54',
'62',
'24',
'41',
'8',
'12',
'16',
'57',
'51',
'42',
'53',
'68',
'34',
'35',
'49',
'31',
'33',
'25',
'87',
'5',
'95',
'66',
'79',
'65',
'93',
'97',
'33',
'8',
'95',
'96',
'75',
'63',
'11']
	'''
	lst = today_lst+yesterday_lst+tomorrow_lst
	lst_lucky_number = []
	for i in lst:
		lst_lucky_number.append(extract_lucky_number(i.text)[0])
	return lst_lucky_number

# extract lucky_time from each lst
def extract_lucky_time(txt):
	'''
	This function extracts lucky time from each horoscope text.

	Parameters:
	-----------
		txt: a string of the text of the response object

	Returns:
	--------
		A string with the lucky time information

	Example:
	--------
	>>>> extract_date('{"date_range": "Mar 21 - Apr 20", "current_date": "December 16, 2022", 
	"description": "A relationship with someone you've been trying to get 
	close to is finally taking off -- not in a mad, passionate way, but in a comfortable, 
	pleasant, long-lasting way. Have a chat tonight.", "compatibility": "Scorpio", "mood": 
	"Sincere", "color": "Brown", "lucky_number": "68", "lucky_time": "8am"}')
	'8am'
	'''
	lucky_time = re.findall(r'"lucky_time":\s"([0-9apm]+)', txt)
	return lucky_time

def lucky_time_for_each():
	'''
	This function applies the extract_lucky_time function to all items within the list of response objects. 

	Parameters:
	-----------
		none

	Returns:
	---------
		A list of lucky times 

	Example:
	>>>> lucky_time_for_each()
	['6am',
	'6pm',
	'12pm',
	'2pm',
	'8pm',
	'8pm',
	'8am',
	'12am',
	'12pm',
	'4am',
	'12pm',
	'8am',
	'9pm',
	'6am',
	'4pm',
	'5pm',
	'3am',
	'1am',
	'11am',
	'4pm',
	'11pm',
	'1pm',
	'1pm',
	'3am',
	'2am',
	'4pm',
	'1am',
	'6am',
	'10am',
	'9am',
	'8pm',
	'8pm',
	'3pm']
	'''
	lst = today_lst+yesterday_lst+tomorrow_lst
	lst_lucky_time=[]
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
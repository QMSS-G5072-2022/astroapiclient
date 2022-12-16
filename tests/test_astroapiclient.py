from astroapiclient import astroapiclient
import pytest 
from astroapiclient	 import build_dataset as bd

@pytest.mark.parametrize("example_text, expected_date",
	[('{"date_range": "Mar 21 - Apr 20", "current_date": "December 16, 2022",' , 'December 16, 2022')])
def test_extract_date(example_text, expected_date):
	result = bd.extract_date(example_text)
	assert result[0] == expected_date

@pytest.mark.parametrize("example_text, expected_description",
	[("{\"date_range\": \"Mar 21 - Apr 20\", \"current_date\": \"December 16, 2022\", \"description\": \"A relationship with someone you've been trying to get close to is finally taking off -- not in a mad, passionate way, but in a comfortable, pleasant, long-lasting way. Have a chat tonight.\", \"compatibility\":",
	"A relationship with someone you've been trying to get close to is finally taking off -- not in a mad, passionate way, but in a comfortable, pleasant, long-lasting way. Have a chat tonight.")])
def test_extract_description(example_text, expected_description):
	result = bd.extract_description(example_text)
	assert result[0] == expected_description # since result is returned as a list of the actual result value

@pytest.mark.parametrize("example_text, expected_compatibility",
	[(" \"compatibility\": \"Scorpio\", ", "Scorpio")])
def test_extract_compatibility(example_text, expected_compatibility):
	result = bd.extract_compatibility(example_text)
	assert result[0] == expected_compatibility

@pytest.mark.parametrize("example_text, expected_mood", 
	[(" \"mood\": \"Sincere\" ", "Sincere")])
def test_extract_mood(example_text, expected_mood):
	result = bd.extract_mood(example_text)
	assert result[0] == expected_mood

@pytest.mark.parametrize("example_text, expected_color", 
	[(" , \"color\": \"Brown\", ", "Brown")])
def test_extract_color(example_text, expected_color):
	result = bd.extract_color(example_text)
	assert result[0] == expected_color

@pytest.mark.parametrize("example_text, expected_lucky_number",
	[(" \"lucky_number\": \"68\" ", "68")])
def test_extract_lucky_number(example_text, expected_lucky_number):
	result = bd.extract_lucky_number(example_text)
	assert result[0] == expected_lucky_number

@pytest.mark.parametrize("example_text, expected_lucky_time", 
	[(" \"lucky_number\": \"68\", \"lucky_time\": \"8am\"} ", "8am")])
def test_extract_lucky_time(example_text, expected_lucky_time):
	result = bd.extract_lucky_time(example_text)
	assert result[0] == expected_lucky_time
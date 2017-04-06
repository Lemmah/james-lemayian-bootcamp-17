import requests
import json

def consume_api():
	movie_query = raw_input('Enter movie name to search: \n')
	api_key = 'ee58a870044d3b4369b90a9b1a906e57'

	api_response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=%s&language=en-US&query=%s&page=1&include_adult=false' % (api_key,movie_query))

	print('\n These are the movies results: \n')
	print(api_response.json())
consume_api()	
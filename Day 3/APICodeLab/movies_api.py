import requests
import json

def moviedb_api():
	movie_query = raw_input('Enter movie name to search: \n')
	api_key = 'ee58a870044d3b4369b90a9b1a906e57'

	api_response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=%s&language=en-US&query=%s&page=1&include_adult=false' % (api_key,movie_query))
	movies_json = api_response.json()
	print('\n These are the movies results: \n')
	print(movies_json)
moviedb_api()	
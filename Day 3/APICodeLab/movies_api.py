import requests

def consume_api():
	movie_name = raw_input('Enter movie name to search: \n')
	my_api_key = 'ee58a870044d3b4369b90a9b1a906e57'

	api_response = requests.get('https://api.themoviedb.org/3/movie/550?api_key=ee58a870044d3b4369b90a9b1a906e57')

	print('\n These are the movies results: \n')
	print(api_response.json())
consume_api()
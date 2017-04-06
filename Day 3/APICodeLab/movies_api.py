import requests
import json

def moviedb_api():
	movie_query = raw_input('Enter movie name to search: \n')
	api_key = 'ee58a870044d3b4369b90a9b1a906e57'

	api_response = requests.get('https://api.themoviedb.org/3/search/movie?api_key=%s&language=en-US&query=%s&page=1&include_adult=false' % (api_key,movie_query))
	movies_json = api_response.json()
	movies_results = movies_json['results']
	if len(movies_results) != 0:
		movies_results_dict = movies_results[0]
		print('\n These are the movies results: \n')
		print('Number of movies found is %s but I currently can\'t print all the results.\n' % movies_json['total_results'])
		print('The first pick is:\n')
		# print(movies_json)
		for key, value in movies_results_dict.iteritems(): 
			detail = key.upper()
			info = value
			print('%s : %s' % (detail, info))
	else:
		print 'There are no movies that match that name.'
moviedb_api()	
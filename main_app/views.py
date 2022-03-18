from django.shortcuts import render
import requests

def main_page(request):
	search_query = request.GET.get('SearchQuery')
	context = {}
	main_list = []
	if search_query is not None:
		response = requests.get(f' https://api.github.com/users/{search_query}')
		main_response = response.json()
		main_list.append(main_response)
		context['main_user'] = main_list
	return render(request, 'index.html', context)
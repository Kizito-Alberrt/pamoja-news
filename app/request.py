from app import app
import urllib.request,json
from .models import news

News = news.News
api_key = app.config['MOVIE_API_KEY']

base_url = app.config["MOVIE_API_BASE_URL"]

def get_news(category):
    '''
    function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        overview = news_item.get('overview')
        poster = news_item.get('poster_path')
        Author = news_item.get('Author')
        Content = news_item.get('Content')

        if poster:
            news_object = News(id,title,overview,poster,Author,Content)
            news_results.append(news_object)
    

def get_news(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            title = news_details_response.get('original_title')
            overview = news_details_response.get('overview')
            poster = news_details_response.get('poster_path')
            vote_average = news_details_response.get('vote_average')
            vote_count = news_details_response.get('vote_count')

            news_object = news(id,title,overview,poster,vote_average,vote_count)
    

def search_news(news_name):
    search_news_url = 'https://newsapi.org/register/success?api_key={}&query={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results
    
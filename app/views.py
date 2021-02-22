from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_news,search_news


@app.route('/news/<int:id>')
def news(id):

    '''
    View root page function that returns the index page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html', title =title, news =news)
    # Getting popular news
    popular_news = get_news('popular')
    print(popular_news)
    upcoming_news = get_news('upcoming')
    now_trending_news = get_news('now_trending')

    title = 'Home - Welcome to The best news Review Website Online'

    return render_template('index.html', title = title,popular = popular_news, upcoming = upcoming_news, trending = now_trending_news)

    # search_news = request.args.get('news_query')

    # if search_news:
    #     return redirect(url_for('search',news_name=search_news))
    # else:
    #     return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news )
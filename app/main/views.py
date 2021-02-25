from flask import render_template,request
from . import main
from ..request import get_news


@main.route('/')
def news():

    '''
    View root page function that returns the index page and its data
    '''
    name = get_news(id) 
    title = 'pamoja'

    return render_template('index.html', title = title, news =name)
   
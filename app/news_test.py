import unittest
from models import news
News =news.News

class NewsTest(unittest.TestCase):
    '''
    test class to test the behaviour of our news class
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_news = News('id', 'title', 'articles', 'vote_average','vote_count')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()

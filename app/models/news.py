class News:
    '''
    news class to define news objects
    '''

    def __init__(self,id,title, articles,vote_average,vote_count):
        self.id =id
        self.title = title
        self.aticles = articles
        self.vote_average = vote_average
        self.vote_count = vote_count



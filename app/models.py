class News:
    '''
    news class to define news objects
    '''

    def __init__(self,id,name,title,description,urlToImage,publishedAt):
        self.id =id
        self.title = title
        self.name = name
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt



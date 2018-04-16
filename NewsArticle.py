class NewsArticle:
	#Initializes standard parameters for the date object
	def __init__(self, aTitle = None, aTags = None, aDate = None, aSource = None,
				 aUrl = None, aAuthor = None, aText = None, aImage_desc = None):
		self.title = aTitle #string - The title of the article
		self.tags = aTags #list of strings - The category tags on the article
		self.date = aDate #datetime - The date the article was released
		self.source = aSource #string - The source of the article
		self.url = aUrl #string - Permanent link to the article
		self.author = aAuthor #string - The author of the article as a tuple (last, first)
		self.text = aText #string - The text body of the article
		self.image_desc = aImage_desc #string - A list of image descriptions - one entry per image

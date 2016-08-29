import re

class CardData():

	def __init__(self, data):
		self.data = data
		self.name = data['name'].lower()
		if 'text' in data:
			self.text = data['text'].lower() 
		else:
			self.text = None

		
	'''
	Card Data functions
	'''
	def count_keywords(self, keywords, clean=False):
		'''
		Counts all occurrences of each keyword in keywords within text
		Params: String text - text to be counted from
				List keywords - list of keywords to count
		'''
		kw = {}
		for keyword in keywords:
			# the 'meld' requirement here is a hack to avoid Midnight Scavengers
			# making 'Scavenge' show up as an EMN keyword'
			if keyword in self.text and keyword not in self.name and 'meld' not in self.text:
				kw[keyword] = self.text.count(keyword)
		return kw

	def has_text(self):
		return not self.text == None

	def get_text(self, clean=False):
		if not self.has_text():
			return ""
		if clean:
			return self.clean_text(self.text)
		else:
			return self.text

	def wordcount(self, clean=False):
		if not self.has_text():
			return 0
		return len(self.get_text(clean=clean))

	def name(self):
		return self.name

	'''
	Text cleanup functions
	'''
	def remove_reminder_text(self, text):
		'''
		Removes all substrings that are enclosed by parentheses, including the parentheses
		Params: String text - text to be changed
		'''
		text_no_reminder = re.sub('\(.*\)', '', text)
		return text_no_reminder

	def remove_unicode_chars(self, text):
		'''
		Removes all relevant unicode characters, in this case long dash, bullet and ae/AE
		Params: String text - text to be changed
		'''
		clean_text = re.sub(ur'[\u2014\u2022\u00E6\u00C6]','',text)
		return clean_text

	def remove_numeric_chars(self, text):
		'''
		Removes all numeric chars (0-9) from text (i.e. the 1 in Modular 1)
		Params: String text - text to be changed
		'''
		clean_text = re.sub(' \d+','',text)
		return clean_text

	def clean_text(self, text):
		'''
		Invokes the above three text functions
		Params: String text - text to be changed
		'''
		clean_text = self.remove_reminder_text(
						self.remove_unicode_chars(
							self.remove_numeric_chars(text)))
		return clean_text.lower()
import re

class CardData():

	def __init__(self, data):
		self.data = data
		self.Name = data['name']
		if 'text' in data:
			self.text = data['text']
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
		return self.Name

	def has_color(self):
		if 'colors' in self.data:
			return True
		return False

	def colors(self):
		if not self.has_color():
			return 'C'
		color_map = {'White':'W', 'Blue':'U','Black':'B','Red':'R','Green':'G'}
		color_symbols = []
		for color in self.data['colors']:
			color_symbols.append(color_map[color])
		return ''.join(color_symbols)

	def has_coloridentity(self):
		if 'colorIdentity' in self.data:
			return True
		return False

	def coloridentity(self):
		if not self.has_coloridentity():
			return 'C'
		return ''.join(self.data['colorIdentity'])

	def types(self):
		return ' '.join(self.data['types'])

	def full_type(self):
		ft = self.data['type']
		full_type = ft.replace('\u2014','&mdash;').replace('\u00E6','&#230;')
		return full_type

	def rarity(self):
		return self.data['rarity']

	def cmc(self):
		if 'cmc' in self.data:
			return self.data['cmc']
		return 0

	def mana_cost(self):
		if 'manaCost' in self.data:
			return self.data['manaCost']
		return 0

	def modern_text(self):
		return self.data['text'].replace(u'\u2014','&mdash;').replace(u'\u00E6','&#230;')

	def original_text(self):
		if 'originalText' in self.data:
			return self.data['originalText'].replace(u'\2014', '&mdash;').replace(u'\u00E6', '&#230;')
		return self.modern_text()

	def artist(self):
		return self.data['artist']

	def reserved(self):
		if 'reserved' in self.data:
			return self.data['reserved']
		return False 

	def has_flavor(self):
		if 'flavor' in self.data:
			return True
		return False

	def flavor_text(self):
		return self.data['flavor'].replace(u'\u2014','&mdash;').replace(u'\u00E6','&#230;')

	def has_power(self):
		if 'power' in self.data:
			return True
		return False

	def power(self):
		if self.has_power():
			return self.data['power']
		return None

	def has_toughness(self):
		if 'toughness' in self.data:
			return True
		return False

	def has_loyalty(self):
		if 'loyalty' in self.data:
			return True
		return False

	def loyalty(self):
		if self.has_loyalty():
			return self.data['loyalty']
		return None

	def toughness(self):
		if self.has_toughness():
			return self.data['toughness']
		return None

	def legality(self):
		legalities = {}
		for legality in self.data['legalities']:
			format = legality['format']
			legal = legality['legality']
			legalities[format] = legal
		return legalities

	def original_type(self):
		if 'originalType' in self.data:
			ot = self.data['originalType']
			original_type = ot.replace('\u2014','&mdash;').replace('\u00E6','&#230;')
			return original_type
		return self.full_type()

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
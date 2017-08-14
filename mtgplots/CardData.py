import re

class CardData():

	def __init__(self, data):
		self.data = data
		
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

	#def has_text(self):
	#	return not self.text == None

	def text(self, clean=False):
		if 'text' not in self.data:
			return None
		else:
			return self.clean_text(self.data['text']) if clean else self.data['text']

	def wordcount(self, clean=False):
		text = self.text()
		return len(self.text(clean=clean)) if text else 0

	def name(self):
		return self.data['name']

	def colored(self):
		return 'colors' in self.data

	def colors(self):
		if not self.colored():
			return 'C'
		color_map = {'White':'W', 'Blue':'U','Black':'B','Red':'R','Green':'G'}
		color_symbols = []
		for color in self.data['colors']:
			color_symbols.append(color_map[color])
		return ''.join(color_symbols)

	def coloredidentity(self):
		return 'colorIdentity' in self.data

	def coloridentity(self):
		return ''.join(self.data['colorIdentity']) if self.coloredidentity() else 'C'

	def typeslist(self):
		return self.data['types']

	def types(self):
		return ' '.join(self.typeslist())

	def subtypeslist(self):
		return self.data['subtypes'] if 'subtypes' in self.data else None

	def subtypes(self):
		subtypes = self.subtypeslist()
		return ' '.join(subtypes) if subtypes else None

	def typesstring(self):
		return ' '.join(self.typeslist())

	def fulltype(self):
		ft = self.data['type']
		full_type = remove_unicode_characters(ft)
		return full_type

	def supertypes(self):
		return self.data['supertypes'] if 'supertypes' in self.data else None

	def rarity(self):
		return self.data['rarity']

	def cmc(self):
		return self.data['cmc'] if 'cmc' in self.data else 0

	def manacost(self):
		return self.data['manaCost'] if 'manaCost' in self.data else None

	def moderntext(self):
		text = self.text()
		if text:
			return self.remove_unicode_characters(text)
		return None

	def originaltext(self):
		if 'originalText' in self.data:
			return self.remove_unicode_characters(self.data['originalText'])
		return self.modern_text()

	def artist(self):
		return self.remove_unicode_characters(self.data['artist'])

	def reserved(self):
		return 'reserved' in self.data

	def flavortext(self):
		if 'flavor' in self.data:
			return self.remove_unicode_characters(self.data['flavor'])
		return None

	def power(self):
		return self.data['power'] if 'power' in self.data else None

	def toughness(self):
		return self.data['toughness'] if 'toughness' in self.data else None

	def loyalty(self):
		return self.data['loyalty'] if 'loyalty' in self.data else None

	def legality(self):
		legalities = {}
		for legality in self.data['legalities']:
			format = legality['format']
			legal = legality['legality']
			legalities[format] = legal
		return legalities

	def originaltype(self):
		if 'originalType' in self.data:
			ot = self.data['originalType']
			original_type = ot.replace('\u2014','&mdash;').replace('\u00E6','&#230;')
			return original_type
		return self.fulltype()

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

	def remove_unicode_characters(self, text):
		'''
		Removes all relevant unicode characters, in this case long dash, bullet and ae/AE
		Params: String text - text to be changed
		'''
		clean_text = re.sub(ur'[\u2014\u2022\u00E6\u00C6]','',text)
		clean_text = re.sub(ur'\xe4', 'a', clean_text)
		clean_text = re.sub(ur'\xf5', 'o', clean_text)
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
						self.remove_unicode_characterss(
							self.remove_numeric_chars(text)))
		return clean_text.lower()
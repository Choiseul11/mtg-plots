
class SetData():

	def __init__(self, data):
		self.data = data
		self.name = data['name']
		self.code = data['code']

	def set_name(self):
		return self.name

	def set_code(self):
		return self.code

	def num_cards(self):
		return len(self.data['cards'])

	def cards(self):
		return self.data['cards']
	
	def releasedate(self):
		return self.data['releaseDate']

	def has_booster(self):
		return 'booster' in self.data

	def booster(self):
		if not self.has_booster():
			return None
		return self.data['booster']

class SetData():

	def __init__(self, data):
		self.data = data

	def name(self):
		return self.data['name']

	def code(self):
		return self.data['code']

	def gatherercode(self):
		return self.data['gathererCode'] if 'gathererCode' in self.data else self.code()

	def oldcode(self):
		return self.data['oldCode'] if 'oldCode' in self.data else self.code()

	def magiccardsinfocode(self):
		if 'magicCardsInfoCode' in self.data:
			return self.data['magicCardsInfoCode']
		return None

	def releasedate(self):
		return self.data['releaseDate']

	def border(self):
		return self.data['border']
	
	def settype(self):
		return self.data['type']

	def block(self):
		return self.data['block']

	def onlineOnly(self):
		return 'onlineOnly' in self.data

	def booster(self):
		return self.data['booster'] if 'booster' in self.data else None

	def cards(self):
		return self.data['cards']

	def size(self):
		return len(self.cards())
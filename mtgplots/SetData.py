 
 class SetData():

 	def __init__(self, data):
 		self.data = data

 	def set_name(self):
 		return self.data['name']

 	def set_code(self):
 		return self.data['code']

 	def num_cards(self):
 		return len(self.data['cards'])

 	def get_cards(self):
 		return self.data['cards']
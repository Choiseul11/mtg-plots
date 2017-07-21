'''
This class provides a convenient interface to the Magic: the Gathering
data provided at http://mtgjson.com/, specifically the All Sets + Extras
data. I am in no way affiliated with MTG JSON, Wizards of the Coast, or
any other entity that this data may belong to.
'''

import json, re
from itertools import permutations
import operator
import Constants

class MagicData():
	# Member variables
	data = None
	sets = []

	def __init__(self):
		return
	'''
	Data loading functions
	'''
	def loaddata(self, path):
		'''
		Reads in JSON data file containing card/set data 
		Params: String path - path to data file
		'''
		self.datapath = path
		with open(self.datapath,'r') as f:
			try:
				self.data = json.load(f)
			except Exception as e:
				self.data = None

	def loadsets(self, s):
		'''
		Params: List s - List of set codes to load
		'''	
		self.sets += s

	def unloadsets(self):
		self.sets = []

	'''
	Total Dataset Functions
	'''

	def allsets(self):
		return self.data.keys()

	def loadedsets(self):
		return self.sets

	def oneset(self, code):
		return self.data[code] if code in self.data else None
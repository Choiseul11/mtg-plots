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
	'''
	Static Data
	'''
	colorids = ['W','U','B','R','G',\
				'WU','WB','WR','WG','UB','UR','UG','BR','BG','RG',\
				'WUB','WUR','WUG','WBR','WBG','WRG','UBR','UBG','URG','BRG',\
				'WUBR','WUBG','WURG','WBRG','UBRG',\
				'WUBRG']
	# Member variables
	data = None
	sets = []

	def __init__(self, path):
		self.json_path = path

	'''
	Data loading functions
	'''
	def load_json(self):
		'''
		Reads in JSON data file containing card/set data 
		Params: String path - path to data file
		'''
		with open(self.json_path,'r') as f:
			self.data = json.load(f)

	def load_keywords(self, path):
		'''
		Reads in new-line separated keywords files and converts to list with newlines stripped
		Params: String path - path to keywords file
		'''
		with open(path,'r') as f:
			keywords = f.readlines()
		keywords = [keyword.strip() for keyword in keywords]
		self.keywords = keywords

	def load_sets(self, s):
		'''
		Params: List s - List of set codes to load
		'''	
		self.sets += s

	'''
	Total Dataset Functions
	'''

	def get_all_sets(self):
		return self.data.keys()

	def get_relevant_sets(self):
		sts = [st for st in self.data if st in self.sets]
		return sts

	def get_set(self, code):
		if code in self.data:
			return self.data[code]
		return None
import json
import matplotlib.pyplot as plt
from itertools import permutations

def get_json(path):
	'''
	Reads in JSON data file containing card/set data 
	Params: String path - path to data file
	'''
	with open(path,'r') as f:
		data = json.load(f)
	return data
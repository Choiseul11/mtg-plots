import json
import re
import matplotlib.pyplot as plt
import operator
from mtgplots import MagicData 
from mtgplots import CardData
from mtgplots import SetData

def calculate_set_data(data, sets, keywords):
	'''
	Given JSON set data, determines keyword counts, total cards, name/code, total keywords/words
	Params: Dict data - JSON dict containing set data
			List sets - list of sets to operate on
			List keywords - list of keywords to count
	'''
	set_data = {}
	for st in sets:
		sd = SetData(data[st])
		set_data[st] = {'keywords':{}, 'words':0, 'total_keywords':0}
		for card in sd.get_cards():
			cd = CardData(card)
			# Skip card if it has no rules text
			if cd.has_text():
				txt = cd.text(clean=True)
				# Add all words on current card to total word count
				set_data[st]['words'] += cd.wordcount(clean=True)
				# Get individual keyword counts from rules text
				kw = cd.count_keywords(keywords, clean=True)
				# Increment per-set keyword counts from above data
				for k in kw:
					set_data[st]['total_keywords'] += kw[k]
					if k in set_data[st]['keywords']:
						set_data[st]['keywords'][k] += kw[k]
					else:
						set_data[st]['keywords'][k] = 1
		set_data[st]['cards'] = sd.num_cards()
		set_data[st]['name'] = sd.set_name()
		set_data[st]['code'] = sd.set_code()
	return set_data

def label_bars(rects):
	'''
	Places labels above bars in bar chart
	Params: List rects - list of pyplot rect objects 
	'''
	for rect in rects:
		height = rect.get_height()
		x = rect.get_x()+rect.get_width()/4. if len(str(height))<2 else rect.get_x()
		plt.text(x, max(1.03*height,height+1), '%d' % int(height))

def plot_set(set_data):
	'''
	Creates bar graph detailing keyword counts and stats
	Params: Dict set_data - dictionary containing data relevant to given set
	'''
	# Sort keywords dict biggest to smallest
	sorted_keywords = sorted(set_data['keywords'].items(), key=operator.itemgetter(1), reverse=True)
	labels = [x[0] for x in sorted_keywords]
	sizes = [x[1] for x in sorted_keywords]
	points = range(len(labels))
	# Create bar graph, saving rects to add text to
	rects = plt.bar([x+.25 for x in points], sizes, 0.5, color='black')
	plt.xticks([x+.5 for x in points], labels,rotation='vertical')
	# Plot text/labels
	plt.title(set_data['name']+' - Keyword Density')
	plt.xlabel('Keyword')
	plt.ylabel('Occurrences')
	plt.text(0.75, 0.79, 'Total Unique Keywords: ' + str(len(set_data['keywords'])), ha='center', va='center', transform=plt.gca().transAxes)
	plt.text(0.75, 0.75, 'Total Keyword Occurences: ' + str(set_data['total_keywords']), ha='center', va='center', transform=plt.gca().transAxes)
	plt.text(0.75, 0.71, 'Total Words: ' + str(set_data['words']), ha='center', va='center', transform=plt.gca().transAxes)
	plt.text(0.75, 0.67, 'Avg. KW/Card: %.1f' % float(float(set_data['total_keywords'])/set_data['cards']), ha='center', va='center', transform=plt.gca().transAxes)
	plt.text(0.75, 0.63, 'Most Common Keyword: ' + sorted_keywords[-1][0], ha='center', va='center', transform=plt.gca().transAxes)
	plt.text(0.75, 0.59, 'Least Common Keyword: ' + sorted_keywords[0][0], ha='center', va='center', transform=plt.gca().transAxes)
	plt.text(0.75, 0.55, 'Total Cards: ' + str(set_data['cards']), ha='center', va='center', transform=plt.gca().transAxes)
	# Numbers above bars
	label_bars(rects)
	#adjust ylim so there's space above bars
	if plt.gca().get_ylim()[1]-sorted_keywords[0][1] < 5:
		plt.gca().set_ylim((0, plt.gca().get_ylim()[1]+5))
	plt.savefig('plots/'+set_data['code']+'-keyword-density.png',bbox_inches='tight')
	plt.clf()

def main():
	# Getting data from files, specifically: keywords, card JSON data
	# NOTE: if you place these files somewhere different, you will need to change these paths
	md = MagicData('../common/AllSets-x.json')
	md.load_keywords('keywords.txt')
	# Variables for storing relevant set codes
	md.load_sets('../common/core_sets.txt') + get_sets('../common/expansion_sets.txt')

	# Variables for storing processed data from each card/set
	# Structure: Dict - Set:
	#						Keywords:
	#							Keyword: INT
	#						Total Words: INT
	#						Total Keywords: INT
	#						Cards: INT
	set_data = calculate_set_data(md.data, md.sets, md.keywords)
	# Create and save figures for each set
	for st in set_data:
		plot_set(set_data[st])
	

if __name__ == "__main__":
	main()

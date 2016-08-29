import json
import re
import matplotlib.pyplot as plt
import operator

def get_keywords(path):
	'''
	Reads in new-line separated keywords files and converts to list with newlines stripped
	Params: String path - path to keywords file
	'''
	with open(path,'r') as f:
		keywords = f.readlines()
	keywords = [keyword.strip() for keyword in keywords]
	return keywords

def get_json(path):
	'''
	Reads in JSON data file containing card/set data 
	Params: String path - path to data file
	'''
	with open(path,'r') as f:
		data = json.load(f)
	return data

def get_sets(path):
	'''
	Reads in new-line separated sets file and converts to list with newlines stripped
	Params: String path - path to sets file
	'''
	with open(path, 'r') as f:
		sets = f.readlines()
	sets = [st.strip() for st in sets]
	return sets

def remove_reminder_text(text):
	'''
	Removes all substrings that are enclosed by parentheses, including the parentheses
	Params: String text - text to be changed
	'''
	text_no_reminder = re.sub('\(.*\)', '', text)
	return text_no_reminder

def remove_unicode_chars(text):
	'''
	Removes all relevant unicode characters, in this case long dash, bullet and ae/AE
	Params: String text - text to be changed
	'''
	clean_text = re.sub(ur'[\u2014\u2022\u00E6\u00C6]','',text)
	return clean_text

def remove_numeric_chars(text):
	'''
	Removes all numeric chars (0-9) from text (i.e. the 1 in Modular 1)
	Params: String text - text to be changed
	'''
	clean_text = re.sub(' \d+','',text)
	return clean_text

def clean_text(text):
	'''
	Invokes the above three text functions
	Params: String text - text to be changed
	'''
	clean_text = remove_reminder_text(
					remove_unicode_chars(
						remove_numeric_chars(text)))
	return clean_text

def count_keywords(text,name,keywords):
	'''
	Counts all occurrences of each keyword in keywords within text
	Params: String text - text to be counted from
			List keywords - list of keywords to count
	'''
	kw = {}
	for keyword in keywords:
		# the 'meld' requirement here is a hack to avoid Midnight Scavengers
		# making 'Scavenge' show up as an EMN keyword'
		if keyword in text and keyword not in name.lower() and 'meld' not in text:
			kw[keyword] = text.count(keyword)
	return kw

def calculate_set_data(data, sets, keywords):
	'''
	Given JSON set data, determines keyword counts, total cards, name/code, total keywords/words
	Params: Dict data - JSON dict containing set data
			List sets - list of sets to operate on
			List keywords - list of keywords to count
	'''
	set_data = {}
	for st in sets:
		set_data[st] = {'name':None, 'code':None, 'keywords':{}, 'words':0, 'total_keywords':0, 'cards':0}
		set_data[st]['name'] = data[st]['name']
		set_data[st]['code'] = data[st]['code']
		for card in data[st]['cards']:
			set_data[st]['cards'] += 1
			# Skip card if it has no rules text
			if 'text' in card:
				txt = clean_text(card['text']).lower()
			else:
				continue	
			# Add all words on current card to total word count
			set_data[st]['words'] += len(txt)
			# Get individual keyword counts from rules text
			kw = count_keywords(txt, card['name'], keywords)
			# Increment per-set keyword counts from above data
			for k in kw:
				set_data[st]['total_keywords'] += kw[k]
				if k in set_data[st]['keywords']:
					set_data[st]['keywords'][k] += kw[k]
				else:
					set_data[st]['keywords'][k] = 1
	'''
	# Print tabulated data for each set1
	for s in set_data:
		print clean_text(set_data[s]['name'])
		print 'Words: ' + str(set_data[s]['words'])
		print 'Keywords: ' + str(set_data[s]['total_keywords'])
		print 'Cards: ' + str(set_data[s]['cards'])
		for i in set_data[s]['keywords']:
			print i + ': ' + str(set_data[s]['keywords'][i])
		print ''
	'''
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
	plt.text(0.75, 0.63, 'Most Common Keyword: ' + sorted_keywords[0][0], ha='center', va='center', transform=plt.gca().transAxes)
	plt.text(0.75, 0.59, 'Least Common Keyword: ' + sorted_keywords[-1][0], ha='center', va='center', transform=plt.gca().transAxes)
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
	keywords = get_keywords('keywords.txt')
	data = get_json('../common/AllSets-x.json')
	
	# Variables for storing relevant set codes
	sets = get_sets('../common/core_sets.txt') + get_sets('../common/expansion_sets.txt')

	# Variables for storing processed data from each card/set
	# Structure: Dict - Set:
	#						Keywords:
	#							Keyword: INT
	#						Total Words: INT
	#						Total Keywords: INT
	#						Cards: INT
	set_data = calculate_set_data(data, sets, keywords)
	# Create and save figures for each set
	for st in set_data:
		plot_set(set_data[st])
	

if __name__ == "__main__":
	main()

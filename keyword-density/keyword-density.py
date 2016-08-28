import json
import re
import matplotlib.pyplot as plt

def get_keywords(path):
	with open(path,'r') as f:
		keywords = f.readlines()
	keywords = [keyword.strip() for keyword in keywords]
	return keywords

def get_json(path):
	with open(path,'r') as f:
		data = json.load(f)
	return data

def remove_reminder_text(text):
	text_no_reminder = re.sub('\(.*\)', '', text)
	return text_no_reminder

def remove_unicode_chars(text):
	clean_text = re.sub(ur'[\u2014\u2022\u00E6\u00C6]','',text)
	return clean_text

def remove_numeric_chars(text):
	clean_text = re.sub(' \d+','',text)
	return clean_text

def clean_text(text):
	clean_text = remove_reminder_text(
					remove_unicode_chars(
						remove_numeric_chars(text)))
	return clean_text

def get_sets(path):
	with open(path, 'r') as f:
		sets = f.readlines()
	sets = [st.strip() for st in sets]
	return sets

def count_keywords(text,keywords):
	kw = {}
	for keyword in keywords:
		if keyword in text:
			kw[keyword] = text.count(keyword)
	return kw

def calculate_set_data(data, sets, keywords):
	set_data = {}
	for st in sets:
		set_data[st] = {'name':None, 'code':None, 'keywords':{}, 'words':0, 'total_keywords':0, 'cards':0}
		set_data[st]['name'] = data[st]['name']
		set_data[st]['code'] = data[st]['code']
		for card in data[st]['cards']:
			if 'text' in card:
				txt = clean_text(card['text']).lower()
			else:
				continue	
			set_data[st]['words'] += len(txt)
			set_data[st]['cards'] += 1
			kw = count_keywords(txt, keywords)
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

def plot_set(set_data):
	labels = sorted(set_data['keywords'])
	sizes = [set_data['keywords'][x] for x in labels]
	#sizes = [float(x/set_data['EXO']['keywords']) for x in sizes]
	rects = plt.bar([x+.25 for x in range(len(labels))], sizes, 0.5, color='black')
	plt.xticks([x+.5 for x in range(len(labels))], labels,rotation='vertical')
	# Plot total kewyords line
	plt.plot([0, plt.gca().get_xlim()[1]], [set_data['total_keywords'],set_data['total_keywords']],'k--',label='Total Keywords')
	# Plot text/labels
	plt.title('Keyword Density')
	plt.xlabel('Keyword')
	plt.ylabel('Occurrences')
	plt.legend()
	plt.show()

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
	plot_set(set_data['EXO'])

if __name__ == "__main__":
	main()

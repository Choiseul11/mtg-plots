from mtgplots import MagicData, SetData, CardData

def update_dict(d, k):
	if k in d:
		d[k] += 1
	else:
		d[k] = 1

def print_set_data(d):
	for s in d:
		print d[s]['name'].upper() + ' (' + s.upper() +')'
		print 'Total Cards: ' + str(d[s]['cards'])
		print 'Release Date: ' + d[s]['releasedate']
		for item in d[s]:
			if item == 'name' or item == 'cards' or item == 'releasedate':
				continue
			else:
				print '  ' + item.upper()
				for i in d[s][item]:
					print '    ' + str(i).upper() + ': ' + str(d[s][item][i])

def main():
	# Static variables
	set_dicts = ['colors', 'coloridentities', 'types', 'rarities', 'cmc']
	# load JSON data
	md = MagicData.MagicData('../common/AllSets-x.json')
	md.load_json()
	# load core and expansion sets
	md.load_sets('../common/core_sets.txt')
	md.load_sets('../common/expansion_sets.txt')

	set_data = {}
	for st in md.get_relevant_sets():
		sd = SetData.SetData(md.get_set(st))
		# Create dict for set
		sdict = {}
		# Create sub-dicts for set items
		for item in set_dicts:
			sdict[item] = {}
		# iterate over cards to fill out set items
		sdict['name'] = sd.set_name()
		sdict['cards'] = sd.num_cards()
		sdict['releasedate'] = sd.releasedate()
		for card in sd.cards():
			cd = CardData.CardData(card)
			if cd.has_color():
				update_dict(sdict['colors'], cd.colors())
			if cd.has_coloridentity():
				update_dict(sdict['coloridentities'], cd.coloridentity())
			update_dict(sdict['types'], cd.types())
			update_dict(sdict['rarities'], cd.rarity())
			update_dict(sdict['cmc'], cd.cmc())
		set_data[sd.set_code()] = sdict
	print_set_data(set_data)


if __name__ == '__main__':
	main()
import json, sys
from itertools import permutations
from mtgplots import Constants
from mtgplots import MagicData
from mtgplots import SetData
from mtgplots import CardData

DATAPATH = './AllSets-x.json'

def type_breakdown(cards):
	type_dict = {}
	for card in cards:
		cd = CardData.CardData(card)
		types = cd.types()
		if types in type_dict:
			type_dict[types] += 1
		else:
			type_dict[types] = 1
	return type_dict

def color_breakdown(cards):
	color_map = {'White':'W', 'Blue':'U','Black':'B','Red':'R','Green':'G', 'C': 'C'}
	color_dict = {}
	for card in cards:
		cd = CardData.CardData(card)
		color = cd.colors()
		if color in color_dict:
			color_dict[color] += 1
		else:
			color_dict[color] = 1
	return color_dict

def colorid_breakdown(cards):
	colorid_possible = ['C', 'W','U','B','R','G',\
					'WU','WB','WR','WG','UB','UR','UG','BR','BG','RG',\
					'WUB','WUR','WUG','WBR','WBG','WRG','UBR','UBG','URG','BRG',\
					'WUBR','WUBG','WURG','WBRG','UBRG',\
					'WUBRG']
	col_perms = {}
	for ids in colorid_possible:
		perms = [''.join(p) for p in permutations(ids)]
		for perm in perms:
			col_perms[perm] = ids
	colorid_dict = {}
	for card in cards:
		cd = CardData.CardData(card)
		colors = cd.coloridentity()
		cid = col_perms[colors]
		if cid in colorid_dict:
			colorid_dict[cid] += 1
		else:
			colorid_dict[cid] = 1
	return colorid_dict

def rarity_breakdown(cards):
	rarity_dict = {}
	for card in cards:
		cd = CardData.CardData(card)
		rarity = cd.rarity()
		if rarity in rarity_dict:
			rarity_dict[rarity] += 1
		else:
			rarity_dict[rarity] = 1
	return rarity_dict

def cmc_breakdown(cards):
	cmc_dict = {}
	for card in cards:
		cd = CardData.CardData(card)
		cmc = cd.cmc()
		if cmc in cmc_dict:
			cmc_dict[cmc] += 1
		else:
			cmc_dict[cmc] = 1
	return cmc_dict

def legendary_breakdown(cards):
	legendaries = 0
	for card in cards:
		cd = CardData.CardData(card)
		supertypes = cd.supertypes()
		if supertypes and 'Legendary' in supertypes:
			legendaries += 1
	return legendaries

def count_nonbasic_lands(cards):
	nblands = 0
	for card in cards:
		cd = CardData.CardData(card)
		supertypes = cd.supertypes()
		if 'Land' in cd.typeslist() and (not supertypes or 'Basic' not in supertypes):
			nblands += 1
	return nblands

def get_creature_types(cards):
	type_dict = {}
	for card in cards:
		cd = CardData.CardData(card)
		subtypes = cd.subtypes()
		if subtypes and 'Creature' in cd.types():
			if subtypes in type_dict:
				type_dict[subtypes] += 1
			else:
				type_dict[subtypes] = 1
	return type_dict

def get_artifact_types(cards):
	type_dict = {}
	for card in cards:
		cd = CardData.CardData(card)
		subtypes = cd.subtypes()
		if subtypes and 'Artifact' in cd.types():
			if subtypes in type_dict:
				type_dict[subtypes] += 1
			else:
				type_dict[subtypes] = 1
	return type_dict

def get_artists(cards):
	artist_dict = {}
	for card in cards:
		cd = CardData.CardData(card)
		artist = cd.artist()
		if artist in artist_dict:
			artist_dict[artist] += 1
		else:
			artist_dict[artist] = 1
	return artist_dict

def main():
	s = sys.argv[1]
	md = MagicData.MagicData()
	md.loaddata(DATAPATH)
	sd = SetData.SetData(md.oneset(s))
	cards = sd.cards()

	out = {}
	out['typeBreakdown'] = type_breakdown(cards)
	out['colorBreakdown'] = color_breakdown(cards)
	out['coloridBreakdown'] = colorid_breakdown(cards)
	out['rarityBreakdown'] = rarity_breakdown(cards)
	out['cmcBreakdown'] = cmc_breakdown(cards)
	out['legendaries'] = legendary_breakdown(cards)
	out['nonbasicLands'] = count_nonbasic_lands(cards)
	out['creatureTypes'] = get_creature_types(cards)
	out['artifactTypes'] = get_artifact_types(cards)
	out['artists'] = get_artists(cards)
	out['totalCards'] = sd.size()
	print 'Total Cards: ' + str(out['totalCards'])
	print 'Legendary Cards: ' + str(out['legendaries'])
	print 'Nonbasic Lands: ' + str(out['nonbasicLands'])
	print '\n\n'

	for item in [x for x in out if x not in ['legendaries', 'nonbasicLands', 'totalCards']]:
		print item.upper()
		print "---"
		for i in out[item]:
			print str(i) + ' : ' + str(out[item][i])
		print "\n\n"

	#with open('../data/'+s+'/breakdown.json','w') as f:
	#	json.dump(out, f)

if __name__ == "__main__":
	main()
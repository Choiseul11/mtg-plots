import json, sys, re
from itertools import permutations
from mtgplots import Constants
from mtgplots import MagicData
from mtgplots import SetData
from mtgplots import CardData

DATAPATH = 'AllSets-x.json'

def increment_dict(k, d):
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
    return d

def remove_unicode_characters(text):
    '''
    Removes all relevant unicode characters, in this case long dash, bullet and ae/AE
    Params: String text - text to be changed
    '''
    clean_text = re.sub(ur'[\u2014\u2022\u00E6\u00C6]','',text)
    clean_text = re.sub(ur'\xe4', 'a', clean_text)
    clean_text = re.sub(ur'\xf5', 'o', clean_text)
    return clean_text

def is_cat(card):
    cd = CardData.CardData(card)
    if cd.subtypeslist() and  'Cat' in cd.subtypeslist():
        return True
    return False

def contains_cat(card):
    cd = CardData.CardData(card)
    if not cd.text():
        return False
    text = cd.text()
    cats = ['Cat ', 'cat ', 'Cats ', 'cats ', 'Cat,', 'cat,', 'Cats,', 'cats,', 'Cat.', 'cat.']
    for cat in cats:
        if cat in text:
            return True
    return False

def main():
    md = MagicData.MagicData()
    md.loaddata(DATAPATH)
    sets = set(Constants.CORE_SETS + Constants.EXPANSION_SETS + Constants.STARTER_SETS + Constants.COMMANDER_SETS + Constants.CONSPIRACY_SETS + Constants.UN_SETS)
    md.loadsets(sets)

    setsWithCats = {}
    blocksWithCats = {}
    cardsWithCats = set()
    countsWithCats = {}
    colorsOfCats = {}
    colorsOfCatsBySet = {}
    coloridsOfCats = {}
    coloridsOfCatsBySet = {}
    artistsOfCats = {}
    artistsOfCatsBySet = {}
    subtypesOfCats = {}
    subtypesOfCatsBySet = {}
    legendaryCats = []
    legendaryCatsBySet = {}
    cmcsOfCats = {}
    cmcsOfCatsBySet = {}
    raritiesOfCats = {}
    raritiesOfCatsBySet = {}

    for s in md.loadedsets():
        sd = SetData.SetData(md.oneset(s))
        cats = []
        cards = sd.cards()
        for card in cards:
            if is_cat(card) or contains_cat(card):
                cd = CardData.CardData(card)
                if s not in colorsOfCatsBySet:
                    colorsOfCatsBySet[s] = {}
                if s not in coloridsOfCatsBySet:
                    coloridsOfCatsBySet[s] = {}
                if s not in artistsOfCatsBySet:
                    artistsOfCatsBySet[s] = {}
                if s not in subtypesOfCatsBySet:
                    subtypesOfCatsBySet[s] = {}
                if s not in cmcsOfCatsBySet:
                    cmcsOfCatsBySet[s] = {}
                if s not in raritiesOfCatsBySet:
                    raritiesOfCatsBySet[s] = {}

                colorsOfCatsBySet[s] = increment_dict(cd.colors(), colorsOfCatsBySet[s])
                coloridsOfCatsBySet[s] = increment_dict(cd.coloridentity(), coloridsOfCatsBySet[s])
                artistsOfCatsBySet[s] = increment_dict(remove_unicode_characters(cd.artist()), artistsOfCatsBySet[s])
                cmcsOfCatsBySet[s] = increment_dict(cd.cmc(), cmcsOfCatsBySet[s])
                raritiesOfCatsBySet[s] = increment_dict(cd.rarity(), raritiesOfCatsBySet[s])
                if 'Creature' in cd.typeslist():
                    subtypesOfCatsBySet[s] = increment_dict(cd.subtypes(), subtypesOfCatsBySet[s])
                if cd.supertypes() and 'Legendary' in cd.supertypes():
                    if s not in legendaryCatsBySet:
                        legendaryCatsBySet[s] = []
                    legendaryCatsBySet[s].append(cd.name())

                if cd.name() not in cardsWithCats:
                    colorsOfCats = increment_dict(cd.colors(), colorsOfCats)
                    coloridsOfCats = increment_dict(cd.coloridentity(), coloridsOfCats)
                    cmcsOfCats = increment_dict(cd.cmc(), cmcsOfCats)
                    raritiesOfCats = increment_dict(cd.rarity(), raritiesOfCats)
                    artistsOfCats = increment_dict(remove_unicode_characters(cd.artist()), artistsOfCats)
                    if 'Creature' in cd.typeslist():
                        subtypesOfCats = increment_dict(cd.subtypes(), subtypesOfCats)
                    if cd.supertypes() and 'Legendary' in cd.supertypes():
                        legendaryCats.append(cd.name())

                cats.append(card)
                cardsWithCats.add(cd.name())

        #if len(cats)>0:
        setsWithCats[s] = cats
        if sd.block():
            if sd.block() not in blocksWithCats:
                blocksWithCats[sd.block()] = 0
            blocksWithCats[sd.block()] += len(cats)
        countsWithCats[s] = len(cats)

    avgCatsPerSet = 0.0
    for i in countsWithCats:
        avgCatsPerSet += countsWithCats[i]
    avgCatsPerSet /= len(countsWithCats)
 
    with open('cats.txt', 'w') as f:
        f.write('Sets with cats: ' + str(len(setsWithCats)) + '/' + str(len(md.loadedsets())) + '\n')
        f.write('Total cats: ' + str(len(cardsWithCats)) + '\n')
        f.write('Average cats per set: ' + str(avgCatsPerSet) + '\n\n')

        catsets = [(x,len(setsWithCats[x])) for x in setsWithCats]
        catsets.sort(key = lambda x: x[1], reverse=True)
        f.write('Cats per Set:\n')
        for i in catsets:
            f.write('\t' + i[0] + ' : ' + str(i[1]) + '\n')

        f.write('Colors of cats:\n')
        for i in colorsOfCats:
            f.write('\t' + i + ' : ' + str(colorsOfCats[i]) + '\n')
        f.write('Colors of Cats by Set:\n')
        for i in colorsOfCatsBySet:
            f.write('\t'+ i + ' : ' + '; '.join(colorsOfCatsBySet[i]) + '\n')
        f.write('\n')
        f.write('Color Identities of Cats')
        for i in coloridsOfCats:
            f.write('\t' + i + ' : ' + str(coloridsOfCats[i]) + '\n')
        f.write('Color Identities of Cats by Set:\n')
        for i in coloridsOfCatsBySet:
            f.write('\t'+ i + ' : ' + '; '.join(coloridsOfCatsBySet[i]) + '\n')
        f.write('\n')
        f.write('Raritiess of Cats')
        for i in raritiesOfCats:
            f.write('\t' + i + ' : ' + str(raritiesOfCats[i]) + '\n')
        f.write('Rarities of Cats by Set:\n')
        for i in raritiesOfCatsBySet:
            f.write('\t'+ i + ' : ' + '; '.join(raritiesOfCatsBySet[i]) + '\n')
        f.write('\n')
        f.write('CMCs of Cats\n')
        for i in cmcsOfCats:
            f.write('\t' + str(i) + ' : ' + str(cmcsOfCats[i]) + '\n')
        f.write('CMCs of Cats by Set:\n')
        for i in cmcsOfCatsBySet:
            f.write('\t'+ str(i) + ' : ' + '; '.join(str(cmcsOfCatsBySet[i])) + '\n')
        f.write('\n')
        artists = artistsOfCats.items()
        artists.sort(key = lambda x: x[1], reverse=True)
        f.write('Artists of cats:\n')
        for i in artists:
            f.write('\t'+ i[0] + ' : ' + str(i[1]) + '\n')
        f.write('Artists of Cats by Set:\n')
        for i in artistsOfCatsBySet:
            f.write('\t'+ i + ' : ' + '; '.join(artistsOfCatsBySet[i]) + '\n')
        f.write('\n')

        f.write('Subtypes of cats:\n')
        for i in subtypesOfCats:
            f.write('\t' + i + ' : ' + str(subtypesOfCats[i]) + '\n')
        f.write('Subtypes of cats by Set:\n')
        for i in subtypesOfCatsBySet:
            f.write('\t' + i + ' : ' + '; '.join(subtypesOfCatsBySet[i]) + '\n')
        f.write('\n')
        f.write('Legendary cats:\n')
        for i in legendaryCats:
            f.write('\t' + i + '\n')
        f.write('Legendary cats by Set:\n')
        for i in legendaryCatsBySet:
            f.write('\t' + i + ' : ' + '; '.join(legendaryCatsBySet[i]) + '\n')

        f.write('CATS PER BLOCK:\n')
        for i in blocksWithCats:
            f.write('\t' + i + ' : ' + str(blocksWithCats[i]) + '\n')

if __name__ == "__main__":
    main()
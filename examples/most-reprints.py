import json
from mtgplots import Constants
from mtgplots import MagicData
from mtgplots import SetData
from mtgplots import CardData


DATAPATH = 'AllSets-x.json'

def main():
    md = MagicData.MagicData()
    md.loaddata(DATAPATH)
    sets = Constants.ALL_SETS
    md.loadsets(sets)
    cards = {}
    EXCLUDES = ['Plains', 'Island', 'Swamp', 'Mountain', 'Forest']

    for s in md.loadedsets():
        sd = SetData.SetData(md.oneset(s))
        for c in sd.cards():
            n = c['name']
            if n not in EXCLUDES:
                if n in cards:
                    cards[n] += 1
                else:
                    cards[n] = 1

    cards_sorted = cards.items()
    cards_sorted.sort(key=lambda x: x[1], reverse=True)

    print 'ALL SETS'
    for i in cards_sorted[0:50]:
        print i[0] + ' : ' + str(i[1])
    print '\n\n'

    md.unloadsets()
    sets = Constants.CORE_SETS + Constants.EXPANSION_SETS
    md.loadsets(sets)
    cards.clear()
    for s in md.loadedsets():
        sd = SetData.SetData(md.oneset(s))
        for c in sd.cards():
            n = c['name']
            if n not in EXCLUDES:
                if n in cards:
                    cards[n] += 1
                else:
                    cards[n] = 1

    cards_sorted = cards.items()
    cards_sorted.sort(key=lambda x: x[1], reverse=True)

    print 'STANDARD ONLY'
    for i in cards_sorted[0:175]:
        print i[0] + ' : ' + str(i[1])

if __name__ == "__main__":
    main()
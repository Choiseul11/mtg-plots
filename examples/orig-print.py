import json, sys
from mtgplots import Constants
from mtgplots import MagicData
from mtgplots import SetData
from mtgplots import CardData

DATAPATH = ''

def main():
    s = sys.argv[1]
    md = MagicData.MagicData()
    md.loaddata(DATAPATH)
    sd = SetData.SetData(md.oneset(s))
    cards = sd.cards()
    printings = {}

    for card in cards:
        op = card['printings'][0]
        if op in printings:
            printings[op] += 1
        else:
            printings[op] = 1
    for p in printings:
        print p + ' : ' + str(printings[p])


if __name__ == "__main__":
    main()
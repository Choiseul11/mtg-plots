import re

class CardData():

    def __init__(self, data):
        self.data = data
        
    '''
    Card Data functions - JSON getters
    '''

    def id(self):
        return self.data['id']

    def layout(self):
        return self.data['layout']

    def name(self):
        return self.data['name']

    def names(self):
        if 'names' in self.data:
            return self.data['names']
        return [self.data['name']]

    def manacost(self):
        return self.data['manaCost'] if 'manaCost' in self.data else None

    def cmc(self):
        return self.data['cmc'] if 'cmc' in self.data else 0

    def colors(self):
        return self.data['colors'] if 'colors' in self.data else None

    def colorIdentity(self):
        return self.data['colorIdentity'] if 'colorIdentity' in self.data else None

    #Name deviates from data field due to 'type' being reserved
    def cardtype(self):
        return self.data['type']

    def supertypes(self):
        return self.data['supertypes'] if 'supertypes' in self.data else None

    def types(self):
        return self.data['types']

    def subtypes(self):
        return self.data['subtypes'] if 'subtypes' in self.data else None

    def rarity(self):
        return self.data['rarity']

    def text(self):
        return self.data['text'] if 'text' in self.data else None

    def flavor(self):
        return self.data['flavor'] if 'flavor' in self.data else None

    def artist(self):
        return self.data['artist']

    def number(self):
        return self.data['number']

    def power(self):
        return self.data['power'] if 'power' in self.data else None

    def toughness(self):
        return self.data['toughness'] if 'toughness' in self.data else None

    def loyalty(self):
        return self.data['loyalty'] if 'loyalty' in self.data else None

    def multiverseId(self):
        return self.data['multiverseid'] if 'multiverseid' in self.data else None

    def variations(self):
        return self.data['variations'] if 'variations' in self.data else None

    def imageName(self):
        return self.data['imageName']

    def watermark(self):
        return self.data['watermark'] if 'watermark' in self.data else None

    def border(self):
        return self.data['border'] if 'border' in self.data else None

    def timeshifted(self):
        return self.data['timeshifted'] if 'timeshifted' in self.data else None

    def hand(self):
        return self.data['hand'] if 'hand' in self.data else None

    def life(self):
        return self.data['life'] if 'life' in self.data else None

    def reserved(self):
        return self.data['reserved'] if 'reserved' in self.data else None

    def releaseDate(self):
        return self.data['releaseDate'] if 'releaseDate' in self.data else None

    def starter(self):
        return self.data['starter'] if 'starter' in self.data else None

    def mciNumber(self):
        return self.data['mciNumber']

    def rulings(self):
        return self.data['rulings'] if 'rulings' in self.data else None

    def foreignNames(self):
        return self.data['foreignNames'] if 'foreignNames' in self.data else None

    def printings(self):
        return self.data['printings']

    def originalText(self):
        return self.data['originalText'] if 'originalText' in self.data else None

    def originalType(self):
        return self.data['originalType'] if 'originalType' in self.data else None

    def legalities(self):
        return self.data['legalities']

    def source(self):
        return self.data['source'] if 'source' in self.data else None
 
    '''
    Additional data
    '''


    '''
    Analytics functions
    '''
    def powerToughnessRatio(self):
        if self.power() and self.toughness():
            power = float(self.power())
            toughness = float(self.toughness())
            return power/toughness
        return None

    def toughnessPowerRatio(self):
        if self.power() and self.toughness():
            power = float(power())
            toughness = float(toughness())
            return toughness/power
        return None
    
    def count_keywords(self, keywords, clean=False):
        '''
        Counts all occurrences of each keyword in keywords within text
        Params: String text - text to be counted from
                List keywords - list of keywords to count
        '''
        if not self.text():
            return None
        text = self.text()
        kw = {}
        for keyword in keywords:
            # the 'meld' requirement here is a hack to avoid Midnight Scavengers
            # making 'Scavenge' show up as an EMN keyword'
            if keyword in text and keyword not in self.name() and 'meld' not in text:
                kw[keyword] = text.count(keyword)
        return kw

    def cleanText(self):
        text = self.text()
        if not text:
            return None
        return self.clean_text(text)

    def wordcount(self, clean=False):
        text = self.text()
        if clean:
            return len(cleanText(text).split(' '))
        return len(text.split(' '))

    def colored(self):
        if self.colored():
            return True
        return False

    def coloredidentity(self):
        if self.coloredidentity():
            return True
        return False

    def colorLetters(self):
        colors = self.colors()
        if not colors:
            return 'C'
        color_map = {'White':'W', 'Blue':'U','Black':'B','Red':'R','Green':'G'}
        color_symbols = []
        for color in colors:
            color_symbols.append(color_map[color])
        return ''.join(color_symbols)

    def coloridentity(self):
        colorIdentity = self.coloridentity()
        if not colorIdentity:
            return 'C'
        return ''.join(colorIdentity)

    def typesString(self):
        return ' '.join(self.types())

    def subtypesString(self):
        subtypes = self.subtypes()
        if not subtypes:
            return None
        return ' '.join(subtypes)

    def artist(self):
        artist = self.artist()
        return self.remove_unicode_characters(artist)

    '''
    Text cleanup functions
    '''
    def remove_reminder_text(self, text):
        '''
        Removes all substrings that are enclosed by parentheses, including the parentheses
        Params: String text - text to be changed
        '''
        text_no_reminder = re.sub('\(.*\)', '', text)
        return text_no_reminder

    def remove_unicode_characters(self, text):
        '''
        Removes all relevant unicode characters, in this case long dash, bullet and ae/AE
        Params: String text - text to be changed
        '''
        clean_text = re.sub(ur'[\u2014\u2022\u00E6\u00C6]','',text)
        clean_text = re.sub(ur'\xe4', 'a', clean_text)
        clean_text = re.sub(ur'\xf5', 'o', clean_text)
        return clean_text

    def remove_numeric_chars(self, text):
        '''
        Removes all numeric chars (0-9) from text (i.e. the 1 in Modular 1)
        Params: String text - text to be changed
        '''
        clean_text = re.sub(' \d+','',text)
        return clean_text

    def clean_text(self, text):
        '''
        Invokes the above three text functions
        Params: String text - text to be changed
        '''
        clean_text = self.remove_reminder_text(
                        self.remove_unicode_characterss(
                            self.remove_numeric_chars(text)))
        return clean_text.lower()
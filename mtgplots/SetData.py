import datetime

class SetData():

    def __init__(self, data):
        self.data = data

    '''
    Set Data functions - JSON getters
    '''
    def name(self):
        return self.data['name']

    def code(self):
        return self.data['code']

    def gatherercode(self):
        return self.data['gathererCode'] if 'gathererCode' in self.data else None

    def oldcode(self):
        return self.data['oldCode'] if 'oldCode' in self.data else None

    def magiccardsinfocode(self):
        return self.data['magicCardsInfoCode'] lif 'magicCardsInfoCode' in self.data else None

    def releasedate(self):
        return self.data['releaseDate']

    def border(self):
        return self.data['border']
    
    def type(self):
        return self.data['type']

    def block(self):
        return self.data['block'] if 'block' in self.data else None

    def onlineOnly(self):
        return 'onlineOnly' in self.data

    def booster(self):
        return self.data['booster'] if 'booster' in self.data else None

    def cards(self):
        return self.data['cards']


    '''
    Analytics functions
    '''
    def size(self):
        return len(self.cards())

    def releaseDate(self):
        date = self.releasedate().split('-')
        date = [int(x) for x in date]
        try:
            return datetime.datetime(d[0], d[1], d[2])
        except:
            return None

class Booster():

    def __init__(self, data):
        self.data = data

    def contents(self):
        return self.data

    def size(self):
        return len(self.contents())
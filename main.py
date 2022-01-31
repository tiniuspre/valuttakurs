from requests import get, post
import urllib3


class Valutta:
    def __init__(self):
        self.url = "https://api.coinbase.com/v2/"

    def getValutta(self, valutta="EUR", til='NOK', mengde=100):
        return float(get(self.url+"exchange-rates?currency="+valutta).json()['data']['rates'][til]) * float(mengde)

    def getAll(self):
        return get(self.url+"exchange-rates").json()['data']['rates']

    def getValuttaList(self, valutta="EUR", mengde=100):
        return [self.getValutta(valutta, til, mengde) for til in self.getAll()]



if __name__ == "__main__":
    for valutta in Valutta().getAll():
        print(valutta)

class Deck:
    def __init__(self, cards):
        super().__init__()
        self.cards = cards

    def addCardToDeck(self, card):
        self.cards.append(card)

    def removeCardFromDeck(self, card):
        self.cards.remove(card)

    # def addAllCardsToDeck(self):
    # CardRank.addRanks(CardRank,CardRank.ranks)
    # CardSuit.addSuits(CardSuit, CardSuit.suits)

    def isEmpty(self):
        if not self.cards:
            return True
        else:
            return False

    def getDeckOfCards(self):
        return self.cards

    def setDeckOfCards(self, cards):
        self.cards = cards

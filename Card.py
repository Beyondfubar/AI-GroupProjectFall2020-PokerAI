class Card:

    def __init__(self, rank, suit):
        # super().__init__()
        self.rank = rank
        self.suit = suit

    def toString(self):
        print("Rank: " + str(self.rank) + ", Suit: " + str(self.suit))

    def getRank(self):
        return self.rank

    def setRank(self, rank):
        self.rank = rank

    def getSuit(self):
        return self.suit

    def setSuit(self, suit):
        self.suit = suit

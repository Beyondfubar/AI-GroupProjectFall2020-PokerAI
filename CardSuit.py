class CardSuit:

    def __init__(self, suits):
        super().__init__()
        self.suits = suits

    def addSuits(self):
        self.suits.append("Hearts")
        self.suits.append("Clubs")
        self.suits.append("Spades")
        self.suits.append("Diamonds")

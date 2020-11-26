class CardRank:

    def __init__(self, ranks):
        super().__init__()
        self.ranks = ranks

    def addRanks(self, ranks):
        self.ranks["Two"] = 2
        self.ranks["Three"] = 3
        self.ranks["Four"] = 4
        self.ranks["Five"] = 5
        self.ranks["Six"] = 6
        self.ranks["Seven"] = 7
        self.ranks["Eight"] = 8
        self.ranks["Nine"] = 9
        self.ranks["Ten"] = 10
        self.ranks["Jack"] = 11
        self.ranks["Queen"] = 12
        self.ranks["King"] = 13
        self.ranks["Ace"] = 14

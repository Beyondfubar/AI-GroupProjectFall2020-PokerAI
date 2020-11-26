# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from enum import IntEnum, Enum


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class CardValues(IntEnum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


class Suits(Enum):
    Hearts = 'hearts'
    Diamonds = 'diamonds'
    Clubs = 'clubs'
    Spades = 'spades'


class PlayingCards:
    def __init__(self, CardValues, Suits):
        self.CardValue = CardValues
        self.Suit = Suits


deck = []


def creatDeck():
    for suit in Suits:
        for CardValue in CardValues:
            deck.append(PlayingCards(CardValue), Suits(suit))
    return deck

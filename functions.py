import random
from collections import defaultdict 
import sys

def calcFrequency(hand):
    freqDict = {}
    
    # Mark all array elements as not  visited
    visited = [False for i in range(len(hand))]
        
    #Traverse through array elements
    #and count frequencies

    for i in range(len(hand)):
        #Skip this element if already processed
        if visited[i] == True:
            continue
        
        #Count frequency
        count = 1
        for j in range (i + 1, len(hand), 1):
            if hand[i] == hand[j]:
                visited[j]  = True
                count += 1
        freqDict[hand[i]] = count
        
        print(hand[i], count)


################ Dealer Functions ################
def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

def dealHoleCards(deck, players):
    for x in range(2):
        for player in players:
            player.append(deck[x])

def dealFlopCards(deck):
    for x in range(3):
        flop[x] = deck[x]
    return flop

def dealBurnCard(deck):
    burnCard = deck.pop()
    return burnCard


def dealTurnCard(deck):
    turnCard = deck.pop()
    return turnCard


def dealRiverCard(deck):
    riverCard = deck.pop()
    return riverCard

    



################ AI Functions ################

def waitForNextRound():
    print("AI will wait for next round")

def leaveTable():
    print("AI left the table")
    sys.exit(0)

def bind():
    print("AI has entered the round")

def determineHandStrength(deck, possibleCardsInDeck, removedCardFromDeck, hand):
    hand.sort()

    winningChance = 0
    ######

    return winningChance

def distanceBetweenCards(card1Rank, card2Rank):
    cardDifference = 0

    if card1Rank > card2Rank:
        cardDifference = card1Rank - card2Rank
    elif card2Rank > card1Rank:
        cardDifference = card2Rank - card1Rank
    else:
        print("cards have the same rank")



def twoCardsSameRank(possibleCardsInDeck, hand):
    freqDict = {}
    freqDict = calcFrequency(hand)
    cardsWithPairs = []
    pairCount = 0
    pairPercentage = 0

    #Traverse through dictionary and check if there is a pair 
    for key in freqDict:
        if freqDict[key] == 2:
            print("This card has a pair of two")
            #add this card rank to an array
            cardsWithPairs.append(key)
    for card in range(len(cardsWithPairs)):
        if card in possibleCardsInDeck:
            pairCount = possibleCardsInDeck.count(card)
    
    pairPercentage = pairCount/len(possibleCardsInDeck)

    return pairPercentage


def twoDifferentPairs(possibleCardsInDeck, hand):



def threeOfAKindProb(possibleCardsInDeck, hand):
    freqDict = {}
    freqDict = calcFrequency(hand)
    cardsWithPairs = []
    pairCount = 0
    threeOfKindPct = 0
    card1 = hand[0]
    card2 = hand[1]

    #Traverse through dictionary and check if there is a pair 
    for key in freqDict:
        if freqDict[key] == 3:
            print("This card has a pair of three")
            #add this card rank to an array
            cardsWithPairs.append(key)
    for card in range(len(cardsWithPairs)):
        if card in possibleCardsInDeck:
            pairCount = possibleCardsInDeck.count(card)
    
    if card1 and card2 in possibleCardsInDeck:
        threeOfKindPct = (possibleCardsInDeck.count(card1) + possibleCardsInDeck.count(card2))/len(possibleCardsInDeck)

    return threeOfKindPct




def fullHouseProb(possibleCardsInDeck, hand):
    fullHouseProb = 0
    fullHouseProb = threeOfAKindProb(possibleCardsInDeck, hand) * twoCardsSameRank(possibleCardsInDeck, hand)
    return fullHouseProb

def fiveCardsInSequenceProb(possibleCardsInDeck, hand):
    card1 = hand[0]
    card2 = hand[1]
    straightPercentage = 0

    cardDifference = distanceBetweenCards(card1.rank, card2.rank)

    if cardDifference <= 5:
        ("There is a possibility for a straight")    

    #straightPercentage = (number possibleValues left in deck by array/deckRemaingSize)

def fiveCardsSameSuitProb(possibleCardsInDeck, hand):
    card1 = hand[0]
    card2 = hand[1]

    card1Suit = card1.suit
    card2Suit = card2.suit
    card1Count = 0
    card2Count = 0

    flushPct = 0

    for card in possibleCardsInDeck:
        if card.suit == card1Suit:
            card1Count += 1
        if card.suit == card2Suit:
            card2Count += 1

    flushPct = max((card1Count/len(possibleCardsInDeck)), (card2Count/len(possibleCardsInDeck)))

    return flushPct
    
    



def threeOfKindWithPairProb(possibleCardsInDeck, hand):
    fullHouseProb = 0
    fullHouseProb = threeOfAKindProb(possibleCardsInDeck, hand) * twoCardsSameRank(possibleCardsInDeck, hand)
    return fullHouseProb

def fourOfAKindProb(possibleCardsInDeck, hand):
    

def fiveCardsInSqeuenceSameSuitProb():
    straightFlush = fiveCardsSameSuitProb * fiveCardsInSequenceProb
    return straightFlush

def royalFlushProb(possibleCardsInDeck, hand):
    card1 = hand[0]
    card2 = hand[1]

    part1Pct = 0
    part2Pct = 0

    numOf10InDeck = numOfRankInDeck(possibleCardsInDeck, 10)
    numOfJInDeck = numOfRankInDeck(possibleCardsInDeck, 11)
    numOfQInDeck = numOfRankInDeck(possibleCardsInDeck, 12)
    numOfKInDeck = numOfRankInDeck(possibleCardsInDeck, 13)
    numOfAInDeck = numOfRankInDeck(possibleCardsInDeck, 14)
    deckRemainingSize = len(possibleCardsInDeck)



    if card1.rank >= 10 or card2.rank >= 10:
        if isRankInDeck(possibleCardsInDeck, 10) and isRankInDeck(possibleCardsInDeck, 11) and isRankInDeck(possibleCardsInDeck, 12) and isRankInDeck(possibleCardsInDeck, 13) and isRankInDeck(possibleCardsInDeck, 14):
            part1Pct = (numOf10InDeck/deckRemainingSize * (numOfJInDeck/deckRemainingSize-1) * (numOfQInDeck/deckRemainingSize-2) * (numOfKInDeck/deckRemainingSize -3) * (numOfAInDeck/deckRemainingSize - 4)
        
        else:
            part1Pct = 0


        if isAllCardsSameSuit(possibleCardsInDeck, card10, cardJ, cardQ, cardK, cardA):
            part2Pct = (1/deckRemainingSize) * (1/deckRemainingSize - 1) * (1/deckRemainingSize - 2) * (1/deckRemainingSize - 3) * (1/deckRemainingSize - 4)
        else:
            part2Pct = 0

        
        royalSraightFlushPct = part1Pct * part2Pct 

        return royalSraightFlushPct
        


def numOfRankInDeck(deck, rank):
    count = 0

    for card in deck:
        if card.rank == rank:
            count += 1

    return count

def isRankInDeck(deck, rank):

    for card in deck:
        if rank in deck:
            return True
    return False

def isAllCardsSameSuit (deck, card1, card2, card3, card4, card5):
    allCardsInDeck = False

    if isRankInDeck(deck, card1.rank) and isRankInDeck(deck, card2.rank) and isRankInDeck(deck, card3.rank) and isRankInDeck(deck, card4.rank) and isRankInDeck(deck, card5.rank):

        if card1.suit == card2.suit and card2.suit == card3.suit and card3.suit == card4.suit and card4.suit == card5.suit:
            return True

        else:
            return False



def bet(winningChance):
    if winningChance >= 0.65:
        print("AI Will put more money in the pot")
    else:
        print("AI will not be this round")


     

def check(winningChance):
    if winningChance >= 0.40:
        print("AI can choose to check and bet zero")
    else:
        return






def revealHand(players):
    for player in players:
        for card in player.hand:
            print(card)


   





    








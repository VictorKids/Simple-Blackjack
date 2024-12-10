import random

class Deck:
    def __init__(self):
        self.deck = ["A-Hearts"  , "2-Hearts"  , "3-Hearts"  , "4-Hearts"  , "5-Hearts"  , "6-Hearts"  , "7-Hearts"  , "8-Hearts"  , "9-Hearts"  , "10-Hearts"  , "J-Hearts"  , "Q-Hearts"  , "K-Hearts",
                     "A-Spades"  , "2-Spades"  , "3-Spades"  , "4-Spades"  , "5-Spades"  , "6-Spades"  , "7-Spades"  , "8-Spades"  , "9-Spades"  , "10-Spades"  , "J-Spades"  , "Q-Spades"  , "K-Spades",
                     "A-Diamonds", "2-Diamonds", "3-Diamonds", "4-Diamonds", "5-Diamonds", "6-Diamonds", "7-Diamonds", "8-Diamonds", "9-Diamonds", "10-Diamonds", "J-Diamonds", "Q-Diamonds", "K-Diamonds",
                     "A-Clubs"   , "2-Clubs"   , "3-Clubs"   , "4-Clubs"   , "5-Clubs"   , "6-Clubs"   , "7-Clubs"   , "8-Clubs"   , "9-Clubs"   , "10-Clubs"   , "J-Clubs"   , "Q-Clubs"   , "K-Clubs"]

    def getCardValue(self, card):
        cardNumber = card[0]
        if (cardNumber == "K" or cardNumber == "Q" or cardNumber == "J" or cardNumber == "1"):
            return 10
        if (cardNumber == "A"):
            return 11
        return int(cardNumber)

    def getOneCard(self):
        chosenCard = random.choice(self.deck)
        self.deck.remove(chosenCard)
        return chosenCard

class Player:
        def __init__(self, _name):
            self.cards = []
            self.totalPoints = 0
            self.name = _name

        def getCards(self):
            return self.cards

        def addCard(self, card, value):
            self.cards.append(card)
            self.totalPoints += value
            print("\n", self.name , " hand:\n" , self.cards)
            print("Current points: " , self.totalPoints, "\n")

        def getPoints(self):
            return self.totalPoints

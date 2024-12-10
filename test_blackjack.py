import unittest
from blackjack_obj import Deck, Player

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
    
    def test_getCardValue(self):
        valueOfK  = self.deck.getCardValue("K-Spades")
        self.assertEqual(valueOfK, 10)

        valueOfQ  = self.deck.getCardValue("Q-Spades")
        self.assertEqual(valueOfQ, 10)

        valueOfJ  = self.deck.getCardValue("J-Spades")
        self.assertEqual(valueOfJ, 10)

        valueOfA  = self.deck.getCardValue("A-Spades")
        self.assertEqual(valueOfA, 11)

        valueOf10 = self.deck.getCardValue("10-Spades")
        self.assertEqual(valueOf10,10)

        valueOf2  = self.deck.getCardValue("2-Spades")
        self.assertEqual(valueOf2,  2)

    def test_getOneCard(self):
        myCard = self.deck.getOneCard()
        self.assertNotIn(myCard,self.deck.deck)

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("test_player")

    def test_addCard(self):
        self.player.addCard("A-Hearts", 11)
        self.assertEqual(self.player.cards[0], "A-Hearts")
        self.assertEqual(self.player.totalPoints, 11)

    def test_getCards(self):
        self.player.cards.append("Q-Clubs")
        self.assertEqual(self.player.cards, ["Q-Clubs"])

    def test_getPoints(self):
        self.player.totalPoints += 21
        self.assertEqual(self.player.totalPoints, 21)

if __name__ == '__main__':
    unittest.main()
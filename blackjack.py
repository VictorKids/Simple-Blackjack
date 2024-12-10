import blackjack_obj

# game loop
print("\n***********************************************************************\n")
print(" (*_._*) Dealer: Hello! Welcome to my Casino. Let's play some Blackjack?!\n   /|\\\n   / \\")
print("\n***********************************************************************")

replayFlag = True
while(replayFlag):

    # init
    deck    = blackjack_obj.Deck()
    player  = blackjack_obj.Player("Player")
    dealer  = blackjack_obj.Player("Dealer")
    gameoverFlag = False

    # generate initial board state on player side
    card1 = deck.getOneCard()
    card2 = deck.getOneCard()
    player.addCard(card1, deck.getCardValue(card1))
    player.addCard(card2, deck.getCardValue(card2))

    # generate initial board state on dealer side
    card3 = deck.getOneCard()
    dealer.addCard(card3, deck.getCardValue(card3))

    # check if players opening hand is an autoWin
    if(deck.getCardValue(card1) + deck.getCardValue(card2) == 21):
        gameoverFlag = True
        print("YOU WON THE GAME WITH A BLACKJACK!")

    # player draw phase
    if gameoverFlag == False:
        MoreCardsPlz = True
        while(MoreCardsPlz and not gameoverFlag):
            newCardQuestion = input("\n (*_._*) Dealer: Do you want one more card? (type n to No or any other thing to Yes).\n   /|\\\n   / \\\n\n")
            if newCardQuestion == "n":
                MoreCardsPlz = False
            else:
                newCard = deck.getOneCard()
                player.addCard(newCard, deck.getCardValue(newCard))
                if player.getPoints() > 21:
                    gameoverFlag = True
                    print("\n (*_._*) Dealer: You bypassed the points limit!\n   /|\\\n   / \\\n")
                    print("You have lost...")
        
    # dealer draw phase
    if gameoverFlag == False:
        dealerStopFlag = False
        # dealer decision logic to draw a new card or stop
        while(not (dealer.getPoints() >= 17 and dealerStopFlag) and not gameoverFlag):
            newCard = deck.getOneCard()
            dealer.addCard(newCard, deck.getCardValue(newCard))
            if dealer.getPoints() > 21:
                print(" (*_._*) Dealer: Oh no, I bypassed the points limit! You won...\n   /|\\\n   / \\\n")
                gameoverFlag = True
            elif dealer.getPoints() >= player.getPoints():
                dealerStopFlag = True

    # game results
    if gameoverFlag == False:
        playerFinalScore = player.getPoints()
        dealerFinalScore = dealer.getPoints()
        if playerFinalScore > dealerFinalScore:
            print("YOU WON THE GAME!")
        elif playerFinalScore == dealerFinalScore:
            print("It's a draw.")
        else:
            print("You have lost...")

    # replay?
    userInput = input("\n (*_._*) Dealer: Do you want to play again? (type n to No or any other thing to Yes).\n   /|\\\n   / \\\n\n")
    if userInput == "n":
        replayFlag = False
    print("\n********************************************************************************************************************\n")


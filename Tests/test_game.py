import sys
sys.path.append(".")
import unittest
import unittest.mock
from unittest.mock import patch, call
from GameMechanics import Game as gameClass
from CardMechanics import Card, Deck
from Players import Intelligence as intellClass

class testRegularGame(unittest.TestCase):
    card = Card.Card()
    deck = Deck.Deck(card)
    ai = intellClass.Intelligence(deck.shuffleDeck, 400)

    # TODO regularGame()

    def testAiHasEnoughBalanceYes(self):
        betAmount = 50
        aiBalance = 100

        testVar = 50
        returnedVar = gameClass.Game.aiHasEnoughBalance(betAmount, aiBalance)
        self.assertEqual(testVar, returnedVar)

    def testAiHasEnoughBalanceNo(self):
        betAmount = 50
        aiBalance = 10

        testVar = 10
        returnedVar = gameClass.Game.aiHasEnoughBalance(betAmount, aiBalance)
        self.assertEqual(testVar, returnedVar)

    
    def testWhosCardIsHigherPlayerWins(self):
        playerName = "Test"
        playerHand = ("9 of Diamonds", 9)
        aiHand = ("6 of Clubs", 6)
        playerBalance = 670
        aiBalance = 400
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 3

        testVar = (720, 350, True, 3)
        returnedVar = gameClass.Game.whosCardIsHigher(playerName, playerHand, aiHand, playerBalance, aiBalance, betAmount, difficulty, testRegularGame.ai, aiDecision)

        self.assertEqual(testVar, returnedVar)

    def testWhosCardIsHigherAiWins(self):
        playerName = "Test"
        playerHand = ("2 of Diamonds", 2)
        aiHand = ("6 of Clubs", 6)
        playerBalance = 670
        aiBalance = 400
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 3

        testVar = (620, 450, False, 3)
        returnedVar = gameClass.Game.whosCardIsHigher(playerName, playerHand, aiHand, playerBalance, aiBalance, betAmount, difficulty, testRegularGame.ai, aiDecision)

        self.assertEqual(testVar, returnedVar)
    
    def testWhosCardIsHigherTie(self):
        playerName = "Test"
        playerHand = ("2 of Diamonds", 2)
        aiHand = ("2 of Clubs", 2)
        playerBalance = 670
        aiBalance = 400
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 4

        testVar = (745.0, 375.0, "Draw", 1)
        returnedVar = gameClass.Game.whosCardIsHigher(playerName, playerHand, aiHand, playerBalance, aiBalance, betAmount, difficulty, testRegularGame.ai, aiDecision)

        self.assertEqual(testVar, returnedVar)
        
    def testTiePlayerNotEnoughBalance(self):
        playerName = "Test"
        playerHand = ("2 of Diamonds", 2)
        aiHand = ("2 of Clubs", 2)
        playerBalance = 40
        aiBalance = 400
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 4

        testVar = (15.0, 375.0, "Draw", 1)
        returnedVar = gameClass.Game.tie(playerName, betAmount, playerBalance, aiBalance, difficulty, testRegularGame.ai, aiDecision)
        self.assertEqual(testVar, returnedVar)

    def testTieAiNotEnoughBalance(self):
        playerName = "Test"
        playerHand = ("2 of Diamonds", 2)
        aiHand = ("2 of Clubs", 2)
        playerBalance = 100
        aiBalance = 40
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 4

        testVar = (75.0, 20.0, "Draw", 1)
        returnedVar = gameClass.Game.tie(playerName, betAmount, playerBalance, aiBalance, difficulty, testRegularGame.ai, aiDecision)
        self.assertEqual(testVar, returnedVar)
    
    def testStartGameAgainYes(self):
        testVar = "New Game selected!"
        returnedVar = gameClass.Game.startGameAgain()
        self.assertEqual(testVar, returnedVar)
    
    def testStartGameAgainNo(self):
        testVar = "No New Game!"
        returnedVar = gameClass.Game.startGameAgain()
        self.assertEqual(testVar, returnedVar)
        




if __name__ == '__main__':
    unittest.main()
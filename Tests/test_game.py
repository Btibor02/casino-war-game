# flake8: noqa

"""Tests -> test_game."""

import sys

import unittest
import unittest.mock
from GameMechanics import Game as gameClass
from CardMechanics import Card, Deck
from Players import Intelligence as intellClass

sys.path.append(".")


"""Guide TestGame.:

1. 1
2. Test
3. 1
4. 40
5. 0
6. 4
7. N
8. Y
9. 4
10. Surrend
11. War
12. Surrend
13. War
14. War
"""


class testRegularGame(unittest.TestCase):
    """testRegularGame class."""

    card = Card.Card()
    deck = Deck.Deck(card)
    ai = intellClass.Intelligence(deck.shuffleDeck, 400)

    def testRegularGame(self):
        """Test RegularGame."""
        testVar = "regularGame works!"
        returnedVar = gameClass.Game.regularGame()

        self.assertEqual(testVar, returnedVar)

    def testAiHasEnoughBalanceYes(self):
        """Test aiHasEnoughBalance.
        
        Check if true.
        """
        betAmount = 50
        aiBalance = 100

        testVar = 50
        returnedVar = gameClass.Game.aiHasEnoughBalance(betAmount, aiBalance)
        self.assertEqual(testVar, returnedVar)

    def testAiHasEnoughBalanceNo(self):
        """Test aiHasEnoughBalance.
        
        Check if false.
        """
        betAmount = 50
        aiBalance = 10

        testVar = 10
        returnedVar = gameClass.Game.aiHasEnoughBalance(betAmount, aiBalance)
        self.assertEqual(testVar, returnedVar)

    def testWhosCardIsHigherPlayerWins(self):
        """Test whosCardIsHigher.
        
        Player wins.
        """
        playerName = "Test"
        playerHand = ("9 of Diamonds", 9)
        aiHand = ("6 of Clubs", 6)
        playerBalance = 670
        aiBalance = 400
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 3

        testVar = (720, 350, True, 3)
        returnedVar = gameClass.Game.whosCardIsHigher(
            playerName,
            playerHand,
            aiHand,
            playerBalance,
            aiBalance,
            betAmount,
            difficulty,
            testRegularGame.ai,
            aiDecision,
        )

        self.assertEqual(testVar, returnedVar)

    def testWhosCardIsHigherAiWins(self):
        """Test whosCardIsHigher.
        
        Ai wins.
        """
        playerName = "Test"
        playerHand = ("2 of Diamonds", 2)
        aiHand = ("6 of Clubs", 6)
        playerBalance = 670
        aiBalance = 400
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 3

        testVar = (620, 450, False, 3)
        returnedVar = gameClass.Game.whosCardIsHigher(
            playerName,
            playerHand,
            aiHand,
            playerBalance,
            aiBalance,
            betAmount,
            difficulty,
            testRegularGame.ai,
            aiDecision,
        )

        self.assertEqual(testVar, returnedVar)

    def testWhosCardIsHigherTie(self):
        """Test whosCardIsHigher.
        
        Tie.
        """
        playerName = "Test"
        playerHand = ("2 of Diamonds", 2)
        aiHand = ("2 of Clubs", 2)
        playerBalance = 670
        aiBalance = 400
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 4

        testVar = (745.0, 375.0, "Draw", 1)
        returnedVar = gameClass.Game.whosCardIsHigher(
            playerName,
            playerHand,
            aiHand,
            playerBalance,
            aiBalance,
            betAmount,
            difficulty,
            testRegularGame.ai,
            aiDecision,
        )

        self.assertEqual(testVar, returnedVar)

    def testTiePlayerNotEnoughBalance(self):
        """Test tie.
        
        Player has not enough balance.
        """
        playerName = "Test"
        playerBalance = 40
        aiBalance = 400
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 4

        testVar = (15.0, 375.0, "Draw", 1)
        returnedVar = gameClass.Game.tie(
            playerName,
            betAmount,
            playerBalance,
            aiBalance,
            difficulty,
            testRegularGame.ai,
            aiDecision,
        )
        self.assertEqual(testVar, returnedVar)

    def testTieAiNotEnoughBalance(self):
        """Test tie.
        
        Ai has not enough balance.
        """
        playerName = "Test"
        playerBalance = 100
        aiBalance = 40
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 4

        testVar = (75.0, 20.0, "Draw", 1)
        returnedVar = gameClass.Game.tie(
            playerName,
            betAmount,
            playerBalance,
            aiBalance,
            difficulty,
            testRegularGame.ai,
            aiDecision,
        )
        self.assertEqual(testVar, returnedVar)

    def testTieWar(self):
        """Test tie.
        
        Tie occur.
        """
        playerName = "Test"
        playerBalance = 100
        aiBalance = 400
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 7

        testVar = (200, 300, True, 0)
        returnedVar = gameClass.Game.tie(
            playerName,
            betAmount,
            playerBalance,
            aiBalance,
            difficulty,
            testRegularGame.ai,
            aiDecision,
        )
        self.assertEqual(testVar, returnedVar)

    def testTieSurrend(self):
        """Test tie.
        
        Surrend.
        """
        playerName = "Test"
        playerBalance = 100
        aiBalance = 400
        betAmount = 50
        difficulty = "Easy"
        aiDecision = 5

        testVar = (75.0, 475.0, "Draw", 0)
        returnedVar = gameClass.Game.tie(
            playerName,
            betAmount,
            playerBalance,
            aiBalance,
            difficulty,
            testRegularGame.ai,
            aiDecision,
        )
        self.assertEqual(testVar, returnedVar)

    def testStartGameAgainYes(self):
        """Test startGameAgain.
        
        Yes.
        """
        testVar = "New Game selected!"
        returnedVar = gameClass.Game.startGameAgain()
        self.assertEqual(testVar, returnedVar)

    def testStartGameAgainNo(self):
        """Test startGameAgain.
        
        No.
        """
        testVar = "No New Game!"
        returnedVar = gameClass.Game.startGameAgain()
        self.assertEqual(testVar, returnedVar)

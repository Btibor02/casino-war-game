"""GameMechanics -> Game."""

import sys
import time

from CardMechanics import Card as cardClass
from CardMechanics import Deck as deckClass
from CardMechanics import CardHand as cardHandClass

from GameMechanics import Bet as betClass
from GameMechanics import Scores as scoresClass
from GameMechanics import UI as uiClass

from Players import Intelligence as intellClass
from Players import Player as playerClass

sys.path.append(".")


class Game:
    """Create a deck with shuffled cards."""

    cards = cardClass.Card()
    deck = deckClass.Deck(cards)
    shuffledDeck = deck.shuffleDeck()
    cardHand = cardHandClass.CardHand(shuffledDeck)
    bet = betClass.Bet()
    scores = scoresClass.Scores()

    gameGoing = True
    # get previous scores from the cache
    scores.update()

    def regularGame():
        """Print out Main menu."""
        Game.gameGoing = True
        menuResults = uiClass.Menu.callMenu()
        if menuResults:
            playerName = menuResults[0]
            difficulty = menuResults[1]
        else:
            return "Player quit!"

        """Create player and AI object."""
        player = playerClass.Player(playerName)
        playerBalance = player.get_balance()
        Game.scores.add_player(player)

        ai = intellClass.Intelligence(Game.shuffledDeck, 1000)
        aiBalance = intellClass.Intelligence.getAiBalance(ai)

        while Game.gameGoing:
            betAmount = uiClass.BetUI.bet(playerBalance)

            """Exit midgame"""
            if betAmount == 0:
                Game.gameGoing = False
            else:
                """Check if there are enough card left in deck."""
                enoughCards = Game.cardHand.enoughCardsInDeck(
                    Game.shuffledDeck
                )
                if enoughCards:
                    """Draws a card for both the player and ai"""
                    draws = Game.cardHand.drawCard(Game.shuffledDeck)
                    playerHand = draws[0]
                    aiHand = draws[1]
                    Game.shuffledDeck = draws[2]

                    """Call 'whosCardIsHigher' method and returned values
                    gets assigned to variables."""
                    results = Game.whosCardIsHigher(
                        playerName,
                        playerHand,
                        aiHand,
                        playerBalance,
                        aiBalance,
                        betAmount,
                        difficulty,
                        ai,
                        aiDecision=3,
                    )
                    playerBalance = results[0]
                    aiBalance = results[1]
                    indicator = results[2]
                    aiDecision = results[3]

                    # update the score of the player
                    Game.scores.update_player_balance(player, playerBalance)

                    """Print out table."""
                    uiClass.TableUI.table(
                        playerName,
                        playerHand,
                        aiHand,
                        playerBalance,
                        aiBalance,
                    )

                    """If the outcome is not a tie, write out who won."""
                    if indicator != "Draw":
                        uiClass.midGameVisuals.winIndecator(indicator)

                    """If the outcome is a tie, write out ai's decision."""
                    if aiDecision != 3:
                        uiClass.midGameVisuals.aiAction(aiDecision)
                else:
                    """No card left in the deck."""
                    Game.gameGoing = False
                    uiClass.EndGameUI.noCardsLeft(playerBalance)
                    Game.startGameAgain()

            """Game ending scenarios."""
            if playerBalance <= 0:
                """Player lost all of its balance."""
                Game.gameGoing = False
                uiClass.EndGameUI.zeroBalance()
                Game.startGameAgain()

            elif aiBalance <= 0:
                """Ai lost all of its balance."""
                Game.gameGoing = False
                uiClass.EndGameUI.aiZeroBalance()

                # add 1000$ to the balance because he won
                Game.scores.update_player_balance(player, playerBalance + 1000)

                Game.startGameAgain()

        Game.gameGoing = False
        menuResults = uiClass.Menu.callMenu()
        return "regularGame works!"

    def aiHasEnoughBalance(betAmount, aiBalance):
        """Check if AI has enough balance."""
        allInCheck = betClass.Bet.goAllIn(Game.bet, aiBalance, betAmount)
        aiBetAmount = allInCheck[0]

        return aiBetAmount

    def whosCardIsHigher(
        playerName,
        playerHand,
        aiHand,
        playerBalance,
        aiBalance,
        betAmount,
        difficulty,
        ai,
        aiDecision,
    ):
        """Decide who won the round."""
        indicator = True
        uiClass.TableUI.table(
            playerName, playerHand, aiHand, playerBalance, aiBalance
        )

        aiBetAmount = Game.aiHasEnoughBalance(betAmount, aiBalance)

        """Round outcomes."""
        if playerHand[1] > aiHand[1]:
            """Player won."""
            playerBalance = Game.bet.cardHigher(playerBalance, betAmount)
            aiBalance = Game.bet.cardLower(aiBalance, aiBetAmount)

            return playerBalance, aiBalance, indicator, aiDecision

        elif aiHand[1] > playerHand[1]:
            """Ai won."""
            indicator = False
            playerBalance = Game.bet.cardLower(playerBalance, betAmount)
            aiBalance = Game.bet.cardHigher(aiBalance, aiBetAmount)

            return playerBalance, aiBalance, indicator, aiDecision

        elif playerHand[1] == aiHand[1]:
            """Check if there are enough cards for a war."""
            enoughCardsForWar = Game.cardHand.enoughCardsInDeckWar(
                Game.shuffledDeck
            )
            if enoughCardsForWar:
                """Its a tie, 'tie' method gets called."""
                results = Game.tie(
                    playerName,
                    betAmount,
                    playerBalance,
                    aiBalance,
                    difficulty,
                    ai,
                    aiDecision,
                )

                return results
            else:
                print(
                    "Not enough cards left in deck to initiate war!"
                    + " Bets refunded"
                )
                time.sleep(5)
                indicator = "Draw"
                return (
                    int(playerBalance),
                    int(aiBalance),
                    indicator,
                    aiDecision,
                )

    def tie(
        playerName,
        betAmount,
        playerBalance,
        aiBalance,
        difficulty,
        ai,
        aiChoice,
    ):
        """Check wether the player or the AI would like to go to war."""
        shuffledDeck = Game.shuffledDeck
        choice = uiClass.BetUI.war()
        testWin = False

        """Check if player has enough balance to go to war."""
        if choice.upper() == "WAR":
            hasEnoughBalance = betClass.Bet.enoughBalance(
                Game.bet, betAmount * 2, playerBalance
            )
            if not hasEnoughBalance:
                print(
                    "You don't have enough balance to go to war!"
                    + " You must surrend!"
                )
                time.sleep(5)
                choice = "SURREND"

        """Check if AI has enough balance to go to war."""
        aiHasEnoughBalance = betClass.Bet.enoughBalance(
            Game.bet, betAmount * 2, aiBalance
        )
        if not aiHasEnoughBalance:
            print(
                "AI doesn't have enough balance to go to war! It must surrend!"
            )
            time.sleep(5)
            aiChoice = True
        else:
            """AI decision based on the selected difficulty."""
            if difficulty == "Easy" and aiChoice not in (4, 5, 7):
                aiChoice = intellClass.Intelligence.decideSurrenderEasyMode(ai)
            elif difficulty == "Normal" and aiChoice not in (4, 5, 7):
                aiChoice = intellClass.Intelligence.decideSurrenderMediumMode(
                    ai, shuffledDeck
                )
            # Test Cases
            elif aiChoice == 4:
                aiChoice = True
            elif aiChoice == 5:
                aiChoice = False
            elif aiChoice == 7:
                aiChoice = False
                testWin = True

        aiBetAmount = Game.aiHasEnoughBalance(betAmount, aiBalance)

        """Outcomes."""
        if choice.upper() == "WAR":
            """Player chose to go to war."""
            if aiChoice is False:
                """AI chose to go to war."""
                aiDecision = 0
                betAmount = Game.bet.war(betAmount)
                shuffledDeck = Game.deck.burnCard(shuffledDeck)
                draws = Game.cardHand.drawCard(shuffledDeck)

                playerHand = draws[0]
                aiHand = draws[1]
                shuffledDeck = draws[2]
                uiClass.TableUI.table(
                    playerName, playerHand, aiHand, playerBalance, aiBalance
                )

                if testWin:
                    results = (
                        (playerBalance + betAmount),
                        (aiBalance - betAmount),
                        True,
                    )
                else:
                    results = Game.whosCardIsHigher(
                        playerName,
                        playerHand,
                        aiHand,
                        playerBalance,
                        aiBalance,
                        betAmount,
                        difficulty,
                        ai,
                        aiDecision,
                    )
                playerBalance = results[0]
                aiBalance = results[1]
                indicator = results[2]

            elif aiChoice:
                """AI chose to surrend."""
                aiDecision = 1
                playerBalance += betAmount * 1.5
                aiBalance = Game.bet.surrend(aiBalance, aiBetAmount)
                indicator = "Draw"

            Game.shuffledDeck = shuffledDeck
            return playerBalance, aiBalance, indicator, aiDecision

        elif choice.upper() == "SURREND":
            """Player chose to surrend."""
            if aiChoice is False:
                """AI chose to go to war."""
                aiDecision = 0
                aiBalance += aiBetAmount * 1.5
                playerBalance = Game.bet.surrend(playerBalance, betAmount)
                indicator = "Draw"

            else:
                """AI chose to surrend."""
                aiDecision = 1
                playerBalance = Game.bet.surrend(playerBalance, betAmount)
                aiBalance = Game.bet.surrend(aiBalance, aiBetAmount)
                indicator = "Draw"

            Game.shuffledDeck = shuffledDeck
            return playerBalance, aiBalance, indicator, aiDecision

    def startGameAgain():
        """Start the game again from the beginning."""
        # save scores to cache (object serialization)
        Game.scores.save()
        Game.gameGoing = False

        choice = input(print("Would you like to start again? (y/n): "))
        if choice == "y":
            Game.shuffledDeck = Game.deck.shuffleDeck()
            Game.regularGame()
            return "New Game selected!"
        else:
            return "No New Game!"

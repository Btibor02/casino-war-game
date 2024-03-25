# flake8: noqa

"""GameMechanics -> UI."""

import os
import sys

from GameMechanics import Bet as betClass
from GameMechanics import Scores as scoresClass

sys.path.append(".")


class MenuUI:
    """Print out Menu uis."""

    def logo():
        """Print out logo."""
        os.system("cls||clear")
        print(
            """.------..------..------..------..------..------.     .------..------..------.
|C.--. ||A.--. ||S.--. ||I.--. ||N.--. ||O.--. |.-.  |W.--. ||A.--. ||R.--. |
| :/\: || (\/) || :/\: || (\/) || :(): || :/\: ((5)) | :/\: || (\/) || :(): |
| :\/: || :\/: || :\/: || :\/: || ()() || :\/: |'-.-.| :\/: || :\/: || ()() |
| '--'C|| '--'A|| '--'S|| '--'I|| '--'N|| '--'O| ((1)) '--'W|| '--'A|| '--'R|
`------'`------'`------'`------'`------'`------'  '-'`------'`------'`------'"""
        )

    def mainMenu():
        """Print out main menu."""
        MenuUI.logo()
        print(f'{"Main menu":.^77}')
        print(f'\n{"1. New Game":^77}')
        print(f'{"2. Leaderboard":^80}')
        print(f'{"3. Rules":^74}')
        print(f'{"4. Exit":^73}')

    def playerNameSelector():
        """Print out player name selector."""
        MenuUI.logo()
        print(f'{"Player name selector":.^77}')
        playerName = input(f'\n{"Enter your name: "}')
        return playerName

    def difficultySelector():
        """Print out difficulty selector."""
        MenuUI.logo()
        print(f'{"Difficulty selector":.^77}')
        print(f'\n{"1. Easy":^77}')
        print(f'{"2. Normal":^80}')

    def rules():
        """Print out the rules for the game."""
        MenuUI.logo()
        print(f'{"Rules":.^77}')
        print("\nEach player starts with a balance of a 1000.")
        print("One card each is dealt to the players.")
        print("Card ranks (High -> Low): A K Q J 10 9 8 7 6 5 4 3 2")
        print(
            "Whoever has the higher card win the wager they bet."
            + " One with a smaller card \nloses their bet."
        )
        print(
            "\nA tie occurs when the players each have cards of the same rank."
            + " In a tie the \nplayers have two options: \n1. A player can " 
            + " surrender, in which case the player loses half the bet.\n2."
            + " A player can go to war,"
            + " in which case the player must double their stake."
        )
        print(
            "\nIf one of the players chose to go to war, but the other"
            + " surrends, the \nplayer who chose to go to war gets "
            + " 1.5x they bet back."
        )
        print(
            "In a war, the computer burns three cards before dealing each of them"
            + " \nan additional card and the game continues as normal."
        )
        print(
            "\nA player wins if the other player runs out of their balance,"
            + " \nor can leave at anytime by writing '0' in the bet window. "
        )


"""Print out Table uis."""


class TableUI:
    """Table Uis."""

    def cardSymbol(hand):
        """Print out the right card symbol."""
        match hand:
            case "Spades":
                print(f'{"*"} {"| :/⧹: |":^73} {"*"}')
                print(f'{"*"} {"| (⧹/) |":^73} {"*"}')

            case "Clubs":
                print(f'{"*"} {"| :(): |":^73} {"*"}')
                print(f'{"*"} {"| ()() |":^73} {"*"}')

            case "Diamonds":
                print(f'{"*"} {"| :/⧹: |":^73} {"*"}')
                print(f'{"*"} {"| :⧹/: |":^73} {"*"}')

            case "Hearts":
                print(f'{"*"} {"| (⧹/) |":^73} {"*"}')
                print(f'{"*"} {"| :⧹/: |":^73} {"*"}')

    def table(playerName, playerHand, aiHand, playerBalance, aiBalance):
        """Print out table."""
        os.system("cls||clear")
        # Table Header
        print(f'{"":*^77}')

        """Print out AI's card."""
        print(f'{"*"} {"AI’s balance: %d" % (aiBalance) :^73} {"*"}')
        print(f'{"*"} {"AI’s hand: %s" % (aiHand[0]) :^73} {"*"}')
        print(f'{"*"} {".------." :^73} {"*"}')
        print(f'{"*"} {"|%s.--. |" % (aiHand[0].split(" ")[0][0]) :^73} {"*"}')
        TableUI.cardSymbol(aiHand[0].split(" ")[2])
        print(f'{"*"} {"| `--’%s|" % (aiHand[0].split(" ")[0][0]) :^73} {"*"}')
        print(f'{"*"} {"`------’":^73} {"*"}')

        for x in range(3):
            print(f'{"*"} {"":^73} {"*"}')

        """Print out Player's card."""
        print(f'{"*"} {".------.":^73} {"*"}')
        print(
            f'{"*"} {"|%s.--. |" % (playerHand[0].split(" ")[0][0]) :^73} {"*"}'
        )
        TableUI.cardSymbol(playerHand[0].split(" ")[2])
        print(
            f'{"*"} {"| `--’%s|" % (playerHand[0].split(" ")[0][0]) :^73} {"*"}'
        )
        print(f'{"*"} {"`------’":^73} {"*"}')
        print(
            f'{"*"} {"%s’s hand: %s" % (playerName, playerHand[0]) :^73} {"*"}'
        )
        print(
            f'{"*"} {"%s’s balance: %d" % (playerName, playerBalance) :^73} {"*"}'
        )
        print(f'{"":*^77}')


"""Print out Bet uis."""


class BetUI:
    """Bet UIs."""

    def bet(balance):
        """Ask the player how much they want to bet."""
        betSelf = betClass.Bet
        hasEnoughBalance = False

        """Check if the input is a number."""
        while not hasEnoughBalance:
            try:
                """Check if the user has enough balance for the bet."""

                userInput = input(
                    f'\n{"How much would you like to bet? (0 - Quit) (Current ammount: %d):  " % balance}'
                )

                # look if user typed "cheat"
                if isinstance(userInput, str) and userInput.lower() == "cheat":
                    balance = BetUI.cheat()

                betAmount = int(userInput)

                hasEnoughBalance = betSelf.enoughBalance(
                    betSelf, betAmount, balance
                )
                if not hasEnoughBalance:
                    print("You don't have enough balance to make that bet!")
            except ValueError:
                hasEnoughBalance = False

        return betAmount

    def cheat():
        """Return enormous sum."""
        return 100000

    def war():
        """Ask the player is they want to go to war or not."""
        choice = ""

        """Check if the input is equal to 'war' or to 'surrend'."""
        while choice not in ("WAR", "SURREND"):
            choice = input(
                "Would you like to go to war or surrend? (War/Surrend) "
            )
            choice = choice.upper()

        return choice


"""Prints out Leaderboard ui"""


class LeaderboardUI:
    """Leaderboard UIs."""

    def leaderboard():
        """Print out leaderboard."""
        MenuUI.logo()
        print(f'{"Leaderboard":.^77}')

        scores = scoresClass.Scores()
        scores.update()

        print(scores)


"""Print out EndGame uis."""


class EndGameUI:

    def zeroBalance():
        """Happen when player has zero or less balance."""
        MenuUI.logo()
        print(f'{"You lost all your money. Better luck next time!":.^77}')

    def aiZeroBalance():
        """Happen when the AI has zero or less balance."""
        MenuUI.logo()
        print(f'{"Congratulation! The AI lost all its money.":.^77}')
        print(f'{"+1000 points have been added to your score": ^77}')

    def noCardsLeft(playerBalance):
        """Happen when there is no more card left in the deck."""
        MenuUI.logo()
        print(f'{"Game ended! No more cards left in the deck":.^77}')
        print(f'{"Your final balance: %d " % (playerBalance) :.^77}')


"""Print out MidGame uis."""


class midGameVisuals:

    def aiAction(aiDecision):
        """Print out AI's decision."""
        notSurrend = "Ai decided not to surrend"
        surrend = "Ai decided to surrend"
        print(surrend if aiDecision else notSurrend)

    def winIndecator(indicator):
        """Print out whether the player won or lost."""
        win = "You won this round!"
        lose = "You lost this round!"
        print(win if indicator else lose)


"""Handle Menu"""


class Menu:
    def callMenu():
        """Call menu."""
        menu = MenuUI
        keepMenu = True

        """Check if input is a number."""
        while keepMenu:
            menu.mainMenu()
            try:
                choiceMenu = int(input("\n>>>>>> "))

                menuResults = Menu.options(choiceMenu)
                if menuResults in (
                    "Leaderboard works!",
                    "Rules works!",
                    "Wrong char",
                ):
                    keepMenu = True
                elif menuResults == "Quit":
                    keepMenu = False
                else:
                    keepMenu = False
                    return menuResults

            except ValueError:
                keepMenu = True

    def options(choice):
        """Option."""
        menu = MenuUI
        leaderboard = LeaderboardUI

        if choice == 1:
            """Game start."""
            playerName = menu.playerNameSelector()
            keepDiffMenu = True
            while keepDiffMenu:
                """Check if the input is a number."""
                menu.difficultySelector()
                try:
                    difficultyChoice = int(input("\n>>>>>> "))
                    if difficultyChoice == 1:
                        difficulty = "Easy"
                    elif difficultyChoice == 2:
                        difficulty = "Normal"
                    keepDiffMenu = False

                    return playerName, difficulty
                except ValueError:
                    keepDiffMenu = True

        elif choice == 2:
            """Leaderboard shown."""
            keepLeaderboard = True
            while keepLeaderboard:
                leaderboard.leaderboard()
                print("Press '0' to go back")

                try:
                    keepLeaderboard = False
                    choiceLeaderboard = int(input("\n>>>>>> "))
                    if choiceLeaderboard == 0:
                        return "Leaderboard works!"
                    else:
                        keepLeaderboard = True
                except ValueError:
                    keepLeaderboard = True

        elif choice == 3:
            keepRules = True
            while keepRules:
                menu.rules()
                print("\nPress '0' to go back")

                try:
                    keepRules = False
                    choiceRules = int(input("\n>>>>>> "))
                    if choiceRules == 0:
                        return "Rules works!"
                    else:
                        keepRules = True
                except ValueError:
                    keepRules = True

        elif choice == 4:
            return "Quit"

        else:
            return "Wrong char"

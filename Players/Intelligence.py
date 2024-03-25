"""Players -> Intelligence."""

import sys
import random

from CardMechanics import CardHand as cardHandClass
from CardMechanics import Deck as deckClass
from collections import defaultdict

sys.path.append(".")


class Intelligence(cardHandClass.CardHand, deckClass.Deck):
    """Intelligence class."""

    def __init__(self, deck, aiBalance):
        """Initialize Ai player object."""
        self.deck = deck
        self.aiBalance = aiBalance

    def getAiBalance(self):
        """Return Ai Balance."""
        return self.aiBalance

    def getOccurrences(self, currentDeck):
        """Get occurrences of each rank in the deck."""
        # initiate default dictionary to provide a default value for key
        # what hasnt been seen before
        occurrences = defaultdict(int)
        # loop through the currentDeck and add one everytime the value occurs
        for card in currentDeck:
            # Get the rank from the dictionary value
            rank = currentDeck[card]
            # append number of occurrences as value
            occurrences[rank] += 1
        return occurrences

    def calculateProbabilities(self, occurrences, currentDeck):
        """Calculate probability of drawing each rank from the deck."""
        # get occurrences
        totalCardscurrentDeck = len(currentDeck)
        # calculate probabilities of each rank being drawn from the currentDeck
        # save each rank and probability as a key, value pair in a dictionary
        probabilities = {}
        for rank, countOfOccurences in occurrences.items():
            probabilities[rank] = countOfOccurences / totalCardscurrentDeck
        return probabilities

    def calculateTieProbability(self, currentDeck):
        """Calculate probability of a tie."""
        # get occurrences
        occurrences = self.getOccurrences(currentDeck)
        # get probabilities of each outcome
        probabilities = self.calculateProbabilities(occurrences, currentDeck)
        # calculate tie probability
        tieProbability = 0
        for rank in probabilities:
            # formula: each outcome probability squared and sumed together
            tieProbability += probabilities[rank] ** 2
        return tieProbability

    def calculateHigherCardProbability(self, currentDeck):
        """Calculate probability of drawing a higher card then the opponent."""
        # formula: (100 - tieProbability)/2
        higherCardProbability = (
            100 - self.calculateTieProbability(currentDeck)
        ) / 2
        return higherCardProbability

    def decideSurrenderEasyMode(self):
        """Easy mode: randomize surrender decision."""
        surrender = random.choice([True, False])
        return surrender

    def decideSurrenderMediumMode(self, deck):
        """Medium difficulty mode:.

        Base surrender decision on probability of drawing higher card.
        """
        surrender = False
        surrenderThreshold = 30
        # get current deck
        currentDeck = deck
        # calculate probability of a higher card:
        # (100 - probability of a tie)/2
        higherCardProbablity = self.calculateHigherCardProbability(currentDeck)
        # if probability of drawing higher > probability of drawing
        # lower => surrender False, else True
        if higherCardProbablity > surrenderThreshold:
            surrender = False
        else:
            surrender = True
        return surrender

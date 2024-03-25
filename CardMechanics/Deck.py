"""CardMechanics -> Deck."""
import random
import sys

from CardMechanics import Card as cardClass
sys.path.append(".")


class Deck(cardClass.Card):
    """Deck class."""

    def __init__(self, card):
        """Initialize Deck object."""
        self.deck = {}
        self.shuffledDeck = {}

        self.cards = card.cards
        self.suits = card.suits

    def createDeck(self):
        """Create deck."""
        for cardName, cardValue in self.cards.items():
            for suit in self.suits:
                self.deck[cardName + " of " + suit] = cardValue
        return self.deck

    def shuffleDeck(self):
        """Shuffle deck."""
        deck = self.createDeck()
        listDeck = list(deck.items())

        random.shuffle(listDeck)
        self.shuffledDeck = dict(listDeck)
        return self.shuffledDeck

    def burnCard(self, currentDeck):
        """Burn three cards."""
        for x in range(3):
            currentDeck.popitem()
        return currentDeck

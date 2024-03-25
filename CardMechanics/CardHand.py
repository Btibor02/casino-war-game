"""CardMechanics -> CardHand."""
import sys
from CardMechanics import Deck as deckClass

sys.path.append(".")


class CardHand(deckClass.Deck):
    """CardHand class."""

    def __init__(self, deck):
        """Initialize CardHand object."""
        self.playerHand = {}
        self.aiHand = {}
        self.shuffledDeck = deck

    """Draw one card for the player and one for the AI and removes those
    cards from the deck"""

    def drawCard(self, deck):
        """Return playerHand, aiHand and currentDeck."""
        self.playerHand = deck.popitem()
        self.aiHand = deck.popitem()
        currentDeck = deck

        return self.playerHand, self.aiHand, currentDeck

    def enoughCardsInDeck(self, currentDeck):
        """Check if enough cards in the deck to continue playing."""
        if len(currentDeck) < 2:
            # not enough cards in deck
            return False
        else:
            return True

    def enoughCardsInDeckWar(self, currentDeck):
        """Check if enough cards in the deck for a war."""
        if len(currentDeck) < 5:
            return False
        else:
            return True

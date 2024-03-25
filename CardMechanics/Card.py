"""CardMechanics -> Card."""


class Card(object):
    """Card class."""

    def __init__(self):
        """Initialize Card object."""
        self.cards = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "Jack": 11,
            "Queen": 12,
            "King": 13,
            "Ace": 14,
        }
        self.suits = ["Diamonds", "Hearts", "Clubs", "Spades"]

    def getCards(self):
        """Return the cards."""
        return self.cards

    def getSuits(self):
        """Return the suits."""
        return self.suits

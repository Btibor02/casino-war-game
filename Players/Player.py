"""Players -> Player."""

import sys

sys.path.append(".")


class Player:
    """Player has a name and a balance."""

    def __init__(self, nickname, balance=1000):
        """Initialise player object."""
        self.nickname = nickname
        self.balance = balance

    def __str__(self):
        """Return a string containg the name and the score of the player."""
        return f"{self.nickname} -- {int(self.balance):,d}$"

    def __eq__(self, other):
        """Check if player is already exists."""
        if isinstance(other, Player):
            return (
                self.nickname == other.nickname
                and self.balance == other.balance
            )
        return False

    def update_balance(self, new_balance):
        """Set new balance."""
        self.balance = new_balance

    def get_balance(self):
        """Get balance."""
        return self.balance

    def get_name(self):
        """Get name."""
        return self.nickname

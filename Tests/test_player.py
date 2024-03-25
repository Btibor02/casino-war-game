"""Tests -> test_player."""

import sys
import unittest

from Players.Player import Player

sys.path.append(".")


class TestPlayer(unittest.TestCase):
    """TestPlayer class."""

    def test_init_default_object(self):
        """Testing the constructor of the Player class."""
        player = Player("player1")

        res = player
        exp = Player
        self.assertIsInstance(res, exp)

    def test_str_method(self):
        """Test the __str__() method from the Player class."""
        player = Player("player1")

        res = str(player)
        exp = f"player1 -- {1000:,d}$"
        self.assertEqual(res, exp)

    def test_update_balance(self):
        """Test the update_balance() method from the Player class."""
        player = Player("player1")

        player.update_balance(500)

        res = player.get_balance()
        exp = 500
        self.assertEqual(res, exp)

    def test_get_name(self):
        """Test the get_name() method from the Player class."""
        player = Player("player1")

        res = player.get_name()
        exp = "player1"
        self.assertEqual(res, exp)

    def test_get_balance(self):
        """Test the get_balance() method from the Player class."""
        player = Player("player1")

        res = player.get_balance()
        exp = 1000
        self.assertEqual(res, exp)

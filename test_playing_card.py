#/usr/bin/python3

import unittest
from itertools import product
from playing_card import PlayingCardDeck, PlayingCard

class TestPlayingCard(unittest.TestCase):

    def test_compare_two_cards(self):
        """
        Tests the comparison function by comparing the numeral value
        of the card by drawing two cards and do manual comparison within this.
        The result is compared to the is_high_card function.
        """
        deck = PlayingCardDeck()
        first_card = PlayingCard(deck)
        second_card = PlayingCard(deck)

        value = None
        if first_card.num_value > second_card.num_value:
            value = 1
        elif first_card.num_value <second_card.num_value:
            value = -1
        else:
            value = 0
        
        self.assertEqual(first_card.is_higher_card(second_card), value)

    def test_string_value(self):
        """
        Tests the formatting functionality to human-readable form to make sure
        that it meets the expected format (e.g., Eight of Heart)
        """        
        deck = PlayingCardDeck()
        card = PlayingCard(deck)
        self.assertEqual(card.get_string_value(), "%s of %s" % (card.str_value, card.suit))

    def test_get_num_cards_left(self):
        """
        Tests the card drawing functionality by creating a card from the deck.
        There should only be 51 cards left
        """
        deck = PlayingCardDeck()
        PlayingCard(deck)  
        self.assertEqual(deck.get_num_card_left(), 51) 

    def test_draw_all_cards(self):
        """
        This tests the functionality where an assertion error is thrown when
        the deck is out of card.
        """
        deck = PlayingCardDeck()
        with self.assertRaises(AssertionError):
            for i in range(53):
                PlayingCard(deck)

    def test_shuffle(self):
        """
        This test the shuffle functionality by creating a new
        deck that is not shuffled and comparing to make sure
        it is not equal to the deck that has been shuffled
        """
        SUIT_MAP = ["Heart", "Spade", "Club", "Diamond"]
        VALUE_MAP = {
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
            "Six": 6,
            "Seven": 7,
            "Eight": 8,
            "Nine": 9,
            "Ten": 10,
            "Jack": 11,
            "Queen": 12,
            "King": 13,
            "Ace": 14,
        }
        unshuffled_deck = list(product(SUIT_MAP, VALUE_MAP))
        deck = PlayingCardDeck().get_string_value()

        self.assertNotEqual(unshuffled_deck, deck)
        
if __name__ == '__main__':
    unittest.main()
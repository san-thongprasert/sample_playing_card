#/usr/bin/python3

import random
from itertools import product

class PlayingCardDeck(object):
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

    def __init__(self, value=None, suit=None):
        """
        This initializes and create a new deck by doing
        product calculation to get all of the suit and values.
        """
        self.deck = list(product(self.SUIT_MAP, self.VALUE_MAP))
        self.shuffle()

    def get_string_value(self):
        return str(self.deck)
                
    def shuffle(self):
        """
        This shuffles the whole deck using random generator to randomize indexes
        and use the randomized index to reorder the list.
        """
        shuffled_list = random.sample(range(0, len(self.deck)), len(self.deck))
        shuffled_deck = []
        for ran_index in shuffled_list:
            shuffled_deck.append(self.deck[ran_index])

        self.deck = shuffled_deck

    def deal_one_card(self):
        """
        Deals one card from the deck and remove it from the list.
        """
        if len(self.deck) == 0:
            return 0
        else:
            return self.deck.pop()

    def get_num_card_left(self):
        return len(self.deck)

class PlayingCard(PlayingCardDeck):
    def __init__(self, deck):
        """
        Initializing the PlayingCard object by dealing one card
        from the deck. If the deck is empty, we should exit the app.
        """
        self.card = deck.deal_one_card()
        if self.card == 0:
            raise AssertionError("End of the deck, terminating program")
        self.suit = self.card[0]
        self.str_value = self.card[1]
        self.num_value = self.VALUE_MAP.get(self.str_value)

    def get_string_value(self):
        """
        Returns the human readable version of the card
        (i.e., Eight of Heart, Ace of Spade, etc.)
        """
        return "%s of %s" % (self.str_value, self.suit)

    def is_higher_card(self, second_card):
        """
        Runs a comparison to determine if the card being compared
        is higher, lower or equal. If higher, returns 1, if lower
        returns -1, and if equal returns 0.
        """
        if self.num_value > second_card.num_value:
            return 1
        elif self.num_value == second_card.num_value:
            return 0
        else:
            return -1


if __name__ == "__main__":
    print("This should not be used as main. Implement with another ")
    pass

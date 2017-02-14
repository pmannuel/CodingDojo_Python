import random
from random import shuffle

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck(object):
    def __init__(self):
        self.deck = []
        self.createDeck()

    def createDeck(self):
        suits = ["heart", "spade", "club", "diamond"]
        ranks = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        for s in range(0, 4):
            for r in range(0, 13):
                card = Card(suits[s], ranks[r])
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def flipCard(self):
        return self.deck.pop()

    def reset(self):
        self.deck = []
        self.createDeck()

    # def __repr__(self):
    #     return ("Suit: %r Rank: %r") %(self.suit, self.rank)

my_deck = Deck().deck
my_shuffled_deck = Deck().shuffle()
flipped_card = Deck().flipCard()

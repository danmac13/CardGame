# Card Deck Base
# Dan MacDonald

import random

'''Creates the card object'''


class Card(object):
    def __init__(self, suit, v):
        self.suit = suit
        self.value = v

    def show(self):
        print("{} of {}".format(self.value, self.suit))


'''generates the deck of cards'''


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()


'''creates object for Players'''


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def showHand(self):
        print(self.name, "hand")
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


'''Driver for card game'''


def main():
    deck = Deck()
    deck.shuffle()

    dan = Player("Dan")
    dan.draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck).draw(deck)
    dan.showHand()


main()

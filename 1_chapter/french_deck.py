import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]



deck = FrenchDeck()
# #
# print(len(deck))
# #
# print(deck[0])
# print(deck[-1])
# #
# print(choice(deck))
# #
# print(deck[:3])
# print(deck[4:7])
# print(deck[12::13])
# #
# for card in deck:
#     print(card)
# #
# for card in reversed(deck):
#     print(card)
# #
# print(Card('Q', 'hearts') in deck)
# print(Card('1', 'hearts') in deck)
# print(Card('2', 'spades') in deck)
# print(id(deck[0]))
# print(id(Card('2', 'spades')))
# print(deck[0] == Card('2', 'spades'))
#
# print(FrenchDeck.ranks)
# print(FrenchDeck.suits)
#
suit_values = dict(spades=3, diamonds=2, clubs=1, hearts=0)


def spades_hight(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    priority = rank_value * len(suit_values) + suit_values[card.suit]
    print(priority)
    return priority


for card in sorted(deck, key=spades_hight):
    print(card)

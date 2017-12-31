from collections import Counter

class Card:
    ranks = "23456789TJQKA"

    def __init__(self, s):
        self.printable_rank = s[0]
        self.rank = self.ranks.find(s[0])
        self.suit = s[1]

class Hand:
    rules = [
        # Royal flush is special case of straight flush 
        {'desc': "Straight Flush", 'straight': True, 'flush': True, 'n0': 1, 'n1': 1},
        {'desc': "Four of a Kind", 'straight': False, 'flush': False, 'n0': 4, 'n1': 1},
        {'desc': "Full House", 'straight': False, 'flush': False, 'n0': 3, 'n1': 2},
        {'desc': "Flush", 'straight': False, 'flush': True, 'n0': 1, 'n1': 1},
        {'desc': "Straight", 'straight': True, 'flush': False, 'n0': 1, 'n1': 1},
        {'desc': "Three of a Kind", 'straight': False, 'flush': False, 'n0': 3, 'n1': 1},
        {'desc': "Two Pair", 'straight': False, 'flush': False, 'n0': 2, 'n1': 2},
        {'desc': "One Pair", 'straight': False, 'flush': False, 'n0': 2, 'n1': 1},
        {'desc': "High Card", 'straight': False, 'flush': False, 'n0': 1, 'n1': 1},
    ]

    def __init__(self, s):
        self.cards = [Card(c) for c in s.split(" ")]
        self.cards.sort(key = lambda card: card.rank)
        
        flush = all(self.cards[i].suit == self.cards[i+1].suit for i in range(0,4))
        straight = all(self.cards[i].rank + 1 == self.cards[i+1].rank for i in range(0,4))
        counter = Counter(card.rank for card in self.cards)
        n_of_a_kind = counter.most_common(2)

        for i in range(len(self.rules)):
            rule = self.rules[i]
            if (rule['flush'] == flush 
                    and rule['straight'] == straight 
                    and rule['n0'] == n_of_a_kind[0][1]
                    and rule['n1'] == n_of_a_kind[1][1]):
                self.hand_strength = 9 - i
                if rule['n0'] >= 2:
                    # tiebreaker for n of a kind is rank of the pair/3/4 
                    if rule['n1'] == 2: # special case for two pair - make sure you get the higher pair
                        self.type_rank = max(n_of_a_kind[0][0], n_of_a_kind[1][0])
                    else:
                        self.type_rank = n_of_a_kind[0][0]
                else:
                    # tiebreaker for others is the high card
                    self.type_rank = self.cards[4].rank

                break

    def comparison_tuple(self):
        return (self.hand_strength, self.type_rank) + tuple(card.rank for card in self.cards[::-1])

    def __lt__(self, other):
        return self.comparison_tuple() < other.comparison_tuple()

    def __str__(self):
        return "%s %d" % (self.hand_strength, self.type_rank)

def gen():
    f = open("p054_poker.txt")
    for line in f:
        hand1 = Hand(line[0:14])
        hand2 = Hand(line[15:])
        yield (hand1, hand2)

print(sum(1 for (hand1, hand2) in gen() if hand1 > hand2))

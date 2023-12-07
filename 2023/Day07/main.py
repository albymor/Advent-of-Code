from collections import Counter

with open('input.txt', 'r') as f:
    data = f.read()

class Hand():
    def __init__(self, line):
        self.cards , self.points = line.split()
        self.points = int(self.points)

        self.card_counts = Counter(self.cards)

        self.mapping = {
            'A':12, 'K':11, 'Q':10, 'J':9, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0
        }

        l = list(self.card_counts.values())

        if max(l) == 5:
            self.hand_type = 6 #'five of a kind'
        elif max(l) == 4:
            self.hand_type = 5 #'four of a kind'
        elif max(l) == 3:
            if min(l) == 2:
                self.hand_type = 4 #'full house'
            else:
                self.hand_type = 3 #'three of a kind'
        elif max(l) == 2:
            if l.count(2) == 2:
                self.hand_type = 2 #'two pairs'
            else:
                self.hand_type = 1 #'one pair'
        else:
            self.hand_type = 0 #'high card'


    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        else:
            for my_card, other_card in zip(self.cards, other.cards):
                if self.mapping[my_card] < self.mapping[other_card]:
                    return True
                elif self.mapping[my_card] > self.mapping[other_card]:
                    return False
                
            return False  
    
    def __repr__(self):
        return f'{self.cards} {self.points}'


test = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""   

def get_part_one(data):
    lines = data.split('\n')

    hands = []

    for line in lines:
        hands.append(Hand(line))
    
    sorted_hands = sorted(hands)

    total = 0

    for i, hand in enumerate(sorted_hands):
        total += hand.points * (i+1)
        

    return total

assert get_part_one(test) == 6440
print(f'Part 1: {get_part_one(data)}')


class Hand2():
    def __init__(self, line):
        self.cards , self.points = line.split()
        self.points = int(self.points)

        num_j = self.cards.count('J')
        tmp = self.cards.replace('J', '')

        self.card_counts = Counter(tmp)

        self.mapping = {
            'A':12, 'K':11, 'Q':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1, 'J':0
        }

        l = list(self.card_counts.values())

        #if all cards are all J
        if len(l) == 0:
            l.append(0)

        if max(l) + num_j == 5:
            self.hand_type = 6 #'five of a kind'
        elif max(l) + num_j == 4:
            self.hand_type = 5 #'four of a kind'
        elif max(l) + num_j == 3:
            if min(l) == 2:
                self.hand_type = 4 #'full house'
            else:
                self.hand_type = 3 #'three of a kind'
        elif max(l) + num_j == 2:
            if l.count(2) == 2:
                self.hand_type = 2 #'two pairs'
            else:
                self.hand_type = 1 #'one pair'
        else:
            self.hand_type = 0 #'high card'


    def __lt__(self, other):
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        else:
            for my_card, other_card in zip(self.cards, other.cards):
                if self.mapping[my_card] < self.mapping[other_card]:
                    return True
                elif self.mapping[my_card] > self.mapping[other_card]:
                    return False
                
            return False        

    def __repr__(self):
        return f'{self.cards} {self.points}'
    
# part 2 
def get_part_two(data):
    lines = data.split('\n')

    hands = []

    for line in lines:
        hands.append(Hand2(line))
    
    sorted_hands = sorted(hands)

    total = 0

    for i, hand in enumerate(sorted_hands):
        total += hand.points * (i+1)
        

    return total

assert get_part_two(test) == 5905
print(f'Part 2: {get_part_two(data)}')


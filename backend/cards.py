import random
class Card:
    def __init__(self, number, suit, prev=None):
        self.number = number
        self.suit = suit
        self.prev = prev

    def __str__(self):
        numbers = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        return f"{numbers[self.number]} of {self.suit}"

    def valid(self,other):
        valid = False
        num = self.number
        other_num = other.number

        if num == 2 or num == 10 or num == 9 or num == 7:
            valid = True
            
        if other_num == 9:
            other_num = other.prev.number

        if other_num == 7:
            if num <= 7:
                valid = True
        elif other_num == 2 or other_num == 10:
            valid = True
        else:
            if num >= other_num:
                valid = True

        return valid

class Deck:
    def __init__(self, cards=None):
        if cards == None:
            cards = []
            for num in range(2,15):
                for suit in ["spades", "clubs", "hearts", "diamonds"]:
                    cards.append(Card(num, suit))
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

    def play(self, card):
        self.cards.append(card)

    def deal(self, count, decks):
        for i in range(count):
            for deck in decks:
                deck.append(self.cards.pop())
        return decks

    def __str__(self):
        card_list = []
        for i in self.cards:
            card_list.append(str(i))
        return "\n".join(card_list)
            


deck = Deck()
deck.shuffle()
print(deck)
print("\n")
print(deck.draw())
print("\n")
print(deck)

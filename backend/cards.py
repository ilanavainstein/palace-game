import random

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.value = number
        self.suit = suit
        

    def __str__(self):
        numbers = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        return f"{numbers[self.number]} of {self.suit}"

    def valid(self,other):
        valid = False
        value = self.value
        other_num = other.number

        if value == 2 or value == 10 or value == 9 or value == 7:
            valid = True

        if other_num == 7:
            if value <= 7:
                valid = True
        elif other_num == 2 or other_num == 10:
            valid = True
        else:
            if value >= other_num:
                valid = True

        return valid

class Deck:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards

    def reset_full(self):
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

    def add(self, card):
        self.cards.append(card)

    def deal(self, num_players, count):
        decks = []
        for j in range(num_players):
            decks.append(Deck())
        for i in range(count):
            for j in range(num_players):
                decks[j].add(self.draw())
        return decks

    def __str__(self):
        card_list = []
        for i in self.cards:
            card_list.append(str(i))
        return "\n".join(card_list)

    def __len__(self):
        return len(self.cards)
            




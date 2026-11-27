import random

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        numbers = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        return f"{numbers[self.number]} of {self.suit}"

class Deck:
    def __init__(self, cards=None, value=0, repeats=0):
        if cards is None:
            cards = []
        self.cards = cards
        self.value = value # only useful for the discard pile
        self.repeats = repeats # only useful for the discard pile

    def shuffle(self):
        random.shuffle(self.cards)
        self.update_value()
        
    def draw(self):
        if len(self.cards) == 0:
            return None
        card = self.cards.pop()
        self.update_value()
        return card

    def add(self, card):
        if isinstance(card, Card):
            self.cards.append(card)
        elif isinstance(card, Deck):
            for i in card.cards:
                self.cards.append(i)
        self.update_value()

    def reset_full(self):
        for num in range(2,15):
            for suit in ["spades", "clubs", "hearts", "diamonds"]:
                self.add(Card(num, suit))
        self.update_value()

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

    def update_value(self):
        self.value = 0
        for card in reversed(self.cards):
            if card.number != 9:
                if card.number not in (2,10):
                    self.value = card.number
                break
            
import random

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        numbers = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        return f"{numbers[self.number]} of {self.suit}"

    def __eq__(self, card):
        return self.number == card.number and self.suit == card.suit

class Deck:
    def __init__(self, cards=None, value=0, repeats=0):
        if cards is None:
            cards = []
        self.cards = cards
        self.value = value # only useful for the discard pile
        if cards is not None:
            self.update_value()
        self.repeats = repeats # only useful for the discard pile

    def shuffle(self):
        random.shuffle(self.cards)
        self.update_value()
        
    def draw(self,card=None):
        if len(self.cards) == 0:
            raise ValueError("deck is empty")
        if card is None:
            card = self.cards.pop()
        else:
            if isinstance(card,Card):
                if card not in self.cards:
                    raise ValueError(f"{card} not in deck")
                self.cards.remove(card)
            elif isinstance(card,Deck):
                for i in card.cards:
                    self.draw(i)
        
        self.update_value()
        return card


    def add(self, card):
        if len(self) == 0: top = 0
        else: top = self.cards[-1].number
        if isinstance(card, Card):
            self.cards.append(card)
            if top not in (0,2,10) and top == card.number:
                self.repeats = self.repeats + 1
            else:
                self.repeats = 0
        elif isinstance(card, Deck):
            for i in card.cards:
                self.cards.append(i)
            for i in card.cards:
                if top not in (0,2,10) and top == i.number:
                    self.repeats += 1
                else:
                    break
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

    def __eq__(self, other): # checks of two Decks with unique cards have the same cards
        if len(self) != len(other):
            return False
        for card in self.cards:
            if card not in other.cards:
                return False
        return True

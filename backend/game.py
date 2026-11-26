from cards import Card
from cards import Deck

class Player:
    def __init__(self, hand=None, face_up=None, face_down=None):
        if hand is None:
            hand = Deck()
        self.hand = hand
        if face_up is None:
            face_up = Deck()
        self.face_up = face_up
        if face_down is None:
            face_down = Deck()
        self.face_down = face_down

class State:
    def __init__(self,players,draw_pile,discard_pile=None,bomb_pile=None,turn=0,winner=None):
        self.players = players
        self.draw_pile = draw_pile
        if discard_pile is None:
            discard_pile = Deck()
        self.discard_pile = discard_pile
        if bomb_pile is None:
            bomb_pile = Deck()
        self.bomb_pile = bomb_pile
        self.turn = turn
        self.winner = winner

def new_game(num_players):
    players = []
    for i in range(num_players):
        players.append(Player())

    full_deck = Deck()
    full_deck.reset_full()
    full_deck.shuffle()
    face_downs = full_deck.deal(num_players, 3)
    for i in range(len(players)):
        players[i].face_down = face_downs[i]
    hands = full_deck.deal(num_players, 6)
    for i in range(len(players)):
        players[i].hand = hands[i]

    return State(players, full_deck)
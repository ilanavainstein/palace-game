from cards import Card
from cards import Deck
from collections import defaultdict
import itertools

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
    def __init__(self,players,draw_pile,discard_pile=None,bomb_pile=None,turn=0,winner=None,phase="setup"):
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
        self.phase = phase

    def top_card(self):
        if len(self.discard_pile) == 0:
            return None
        else:
            return self.discard_pile.cards[-1]

def new_game(num_players):
    if num_players not in range(2,5):
        raise ValueError("must be between 2 - 4 players")
    
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

def set_face_up(state,pick):
    player = state.turn
    if state.phase != "setup":
        raise ValueError("not in setup")
    hand = state.players[player].hand
    face_up = state.players[player].face_up
    if len(face_up) == 3:
        raise ValueError("face-up full")
    if any(i not in hand.cards for i in pick.cards):
        raise ValueError("at least one card not an option")
    hand.draw(pick)
    face_up.add(pick)
    
    state.turn = (state.turn+1) % len(state.players)
    if all(len(i.face_up)==3 for i in state.players):
        state.phase="play"

def can_play(state, card):
    if card.number in (2,10,7,9):
        return True
    else:
        deck_value = state.discard_pile.value
        if deck_value == 7:
            return card.number <= 7
        else:
            return card.number >= deck_value

def legal_moves(state):
    player = state.players[state.turn]
    if state.winner is not None:
        return []
    if state.phase == "setup":
        moves = []
        for combo in itertools.combinations(player.hand.cards,3):
            moves.append(Deck(list(combo)))
        return moves
    zone = Deck()
    if len(player.hand) > 0:
        zone = player.hand
    elif len(player.face_up) > 0:
        zone = player.face_up
    elif len(player.face_down) > 0:
        zone = player.face_down
    else:
        return []

    moves = []
    options = [n for n in zone.cards if can_play(state,n)]
    groups = defaultdict(list)
    for n in options:
        groups[n.number].append(n)
    for repeat in groups.values():
       for j in range(1,len(repeat)+1):
           for combo in itertools.combinations(repeat,j):
               moves.append(Deck(list(combo)))
    return moves
    
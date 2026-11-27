from cards import Card, Deck
from game import Player, State, new_game

def test_3_players():
    state = new_game(3)
    assert len(state.players) == 3

def test_num_zones():
    state = new_game(3)
    for i in state.players:
        assert len(i.hand) == 6
        assert len(i.face_down) == 3

def test_left_in_draw():
    state = new_game(3)
    assert len(state.draw_pile) == 52 - len(state.players) * 9

def test_start_discard():
    state = new_game(3)
    assert isinstance(state.discard_pile, Deck)
    assert len(state.discard_pile) == 0

def test_no_repeats():
    state = new_game(3)
    cards = Deck()
    for player in state.players:
        cards.add(player.hand)
        cards.add(player.face_up)
        cards.add(player.face_down)
    cards.add(state.draw_pile)
    cards.add(state.discard_pile)
    cards.add(state.bomb_pile)

    cards_list = []
    for i in cards.cards:
        cards_list.append(str(i))
    cards_set = set()
    for i in cards_list:
        cards_set.add(i)

    assert len(cards_list) == len(cards_set)

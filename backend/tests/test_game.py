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


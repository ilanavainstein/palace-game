from cards import Card, Deck
from game import Player, State, new_game, can_play, set_face_up, legal_moves

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

def test_can_play():
    draw = Deck()
    deck = Deck()
    deck.add(Card(6,"spades"))
    state = State(2,draw,discard_pile=deck)
    assert can_play(state,Card(8,"spades")) == True
    assert can_play(state,Card(5,"hearts")) == False
    assert can_play(state,Card(10,"clubs")) == True
    
    deck.add(Card(7,"hearts"))
    state.discard_pile = deck
    assert can_play(state,Card(5,"hearts")) == True
    assert can_play(state,Card(8,"spades")) == False

    deck.add(Card(9,"spades"))
    state.discard_pile = deck
    assert can_play(state,Card(5,"hearts")) == True
    assert can_play(state,Card(8,"spades")) == False

    deck.add(Card(10,"diamonds"))
    state.discard_pile = deck
    assert can_play(state,Card(3,"hearts")) == True

def test_face_up():
    state = new_game(2)
    pick = state.players[0].hand.cards[2]
    set_face_up(state,pick)
    assert len(state.players[0].hand) == 5
    assert isinstance(state.players[0].face_up,Deck)
    assert len(state.players[0].face_up) == 1
    assert state.players[0].face_up.draw() == pick

def test_setup_next_turn():
    state = new_game(2)
    pick = Deck()
    for i in range(3):
        card = state.players[0].hand.cards[0]
        pick.add(card)
    set_face_up(state,pick)
    assert state.turn == 1
    assert state.phase == "setup"

def test_setup_complete():
    state = new_game(2)
    pick1 = Deck()
    for i in range(3):
        card = state.players[0].hand.cards[0]
        pick1.add(card)
    set_face_up(state,pick1)
    pick2 = Deck()
    for i in range(3):
        card = state.players[1].hand.cards[0]
        pick2.add(card)
    set_face_up(state,pick2)
    assert state.phase == "play"

def test_setup_complete_num():
    state = new_game(2)
    pick1 = Deck()
    for i in range(3):
        card = state.players[0].hand.cards[0]
        pick1.add(card)
    set_face_up(state,pick1)
    pick2 = Deck()
    for i in range(3):
        card = state.players[1].hand.cards[0]
        pick2.add(card)
    set_face_up(state,pick2)

    total = 0
    for player in state.players:
        for deck in (player.hand, player.face_up, player.face_down):
            total += len(deck)
    for deck in (state.discard_pile, state.draw_pile, state.bomb_pile):
        total += len(deck)
    assert total == 52

def test_legal_moves():
    players = [Player(), Player()]
    draw_pile = Deck()
    draw_pile.reset_full()
    players[0].hand.add(Deck([Card(5,"hearts"),Card(5,"spades"),Card(13,"clubs")]))
    draw_pile.draw(Deck([Card(5,"hearts"),Card(5,"spades"),Card(13,"clubs")]))
    state = State(players,draw_pile,phase="play")
    moves = legal_moves(state)
    assert len(moves) == 4
    assert isinstance(moves[0],Deck)

    state.players[0].hand.add(Card(5,"clubs"))
    state.draw_pile.draw(Card(5,"clubs"))
    moves = legal_moves(state)
    assert len(moves) == 8
    
    discard_pile = Deck()
    discard_pile.add(Card(6,"spades"))
    draw_pile.draw(Card(6,"spades"))
    state.discard_pile = discard_pile
    moves = legal_moves(state)
    assert len(moves) == 1


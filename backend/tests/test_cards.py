from cards import Card, Deck

def test_full_deck_52_cards():
    deck = Deck()
    deck.reset_full()
    assert len(deck) == 52

def test_draw_shrinks():
    deck = Deck()
    deck.reset_full()
    length = len(deck)
    card = deck.draw()
    new_length = len(deck)
    assert length == new_length+1

def test_draw_returns_card():
    deck = Deck()
    deck.reset_full()
    card = deck.draw()
    assert isinstance(card,Card)

def test_deal_num_cards():
    deck = Deck()
    deck.reset_full()
    decks = deck.deal(2,3)
    assert len(decks[0]) == 3

def test_deal_returns_decks():
    deck = Deck()
    deck.reset_full()
    decks = deck.deal(2,3)
    assert isinstance(decks[0],Deck)

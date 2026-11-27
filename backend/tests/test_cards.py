from cards import Card, Deck

def test_full_deck_52_cards():
    deck = Deck()
    deck.reset_full()
    assert len(deck) == 52

# draw
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

#add
def test_add_deck():
    deck = Deck()
    cards = Deck()
    cards.add(Card(9,"hearts"))
    cards.add(Card(10,"spades"))
    cards.add(Card(11,"clubs"))
    deck.add(cards)
    assert deck.cards[-1].number == 11

#deal
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

def test_correct_length():
    deck = Deck()
    deck.reset_full()
    assert len(deck) == len(deck.cards)

#value
def test_value_full():
    deck = Deck()
    deck.reset_full()
    deck.shuffle()
    value = deck.value
    card = deck.cards[-1]
    while card.number == 9:
        draw = deck.draw()
        card = deck.cards[-1]
    if card.number in (2,10):
        assert value == 0
    elif card.number != 9:
        assert value == card.number

def test_value_empty():
    deck = Deck()
    assert deck.value == 0

def test_value_add():
    deck = Deck()
    deck.add(Card(5,"hearts"))
    assert deck.value == 5

def test_value_nine():
    deck = Deck()
    deck.add(Card(5,"hearts"))
    deck.add(Card(9,"hearts"))
    deck.add(Card(9,"spades"))
    assert deck.value == 5

def test_value_all_nines():
    deck = Deck()
    deck.add(Card(9,"hearts"))
    deck.add(Card(9,"spades"))
    assert deck.value == 0

def test_value_ten_nine():
    deck = Deck()
    deck.add(Card(10,"hearts"))
    deck.add(Card(9,"spades"))
    assert deck.value == 0

def test_value_draw():
    deck = Deck()
    deck.add(Card(5,"hearts"))
    deck.add(Card(6,"spades"))
    deck.draw()
    assert deck.value == 5


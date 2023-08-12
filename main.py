# Enum Class from enum import Enum
from enum import Enum

class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Stack(Enum):
    ROYAL_STRAGHT_FLUSH = 1
    STRAGHT_FLUSH = 2
    QUADS = 3
    FULL_HOUSE = 4
    FLUSH = 5
    STRAGHT = 6
    THREE = 7
    TWO_PAIR = 8
    ONE_PAIR = 9
    HIGH_CARD = 10

class Suit(Enum):
    HEART = 'H'
    DIAMOND = 'D'
    CLUB = 'C'
    SPADE = 'S'

class Phase(Enum):
    PRE_FLOP = 0
    FLOP = 1
    TURN = 2
    RIVER = 3

class Color(Enum):
    BLACK = "⚫"
    RED = "🔴"

class Action(Enum):
    FOLD = 0
    CHECK = 1
    RISE = 2
    CALL = 3
    ALL_IN = 4

# Base Game
class Poker:
    def __init__(self, players, deck):
        self.player = players
        self.deck = deck
        self.pot = 0
        self.current_phase = Phase.PRE_FLOP
        self.community_card = []

    def generate_chips(number):
        pass

    def deal_cards():
        pass

    def betting_round():
        pass

    def change_phase():
        pass

    def determind_winner():
        pass

    def payout():
        pass

    def game_over():
        pass

class Player:
    def __init__(self, id, chips, hand):
        self.id = id
        self.chips = chips
        self.hand = hand
        self.current_bet = 0
        self.has_folded = False

    def make_bet(action):
        pass

class Hand:
    def __init__(self):
        self.hand = []

    def evaluate_cards(commu_cards):
        pass

    def add_cards(cards):
        pass

    def clear_hand():
        pass

class Deck:
    def __init__(self, cards = []):
        self.cards = cards

    def shuffle(self):
        pass

    def draw(self):
        pass

    def is_empty(self):
        pass

    def append_card(self, card):
        self.cards.append(card)
    
    def print_cards(self):
        for card in self.cards:
            print(card)

class Card:
    def __init__(self, rank, suit, color):
       self.rank = rank
       self.suit = suit
       self.color = color

    def __str__(self):
        suit_symbol = self.suit.value
        rank_symbol = self.rank.name if self.rank.value >= 11 else str(self.rank.value)
    
        available_space = 17
        rank_space = ' ' * ((available_space - len(rank_symbol)) // 2)
    
        card_lines = [
            "+-----------------+",
            "|                 |",
            f"|{' '*6}{suit_symbol} {self.color.value}{' '*7}|",
            f"|{rank_space}{rank_symbol}{' ' if len(rank_symbol) % 2 == 0 else ''}{rank_space}|",
            "|                 |",
            "+-----------------+"
        ]
        return "\n".join(card_lines)
# Initial Game

# create cards
deck = Deck()
for rank in Rank:
    for suit in Suit:
        for color in Color:
            card = Card(rank=rank,suit=suit,color=color)
            deck.append_card(card)

deck.print_cards()

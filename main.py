from enum import Enum
from typing import List, Union
import random

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
class Card:
    def __init__(self, rank, suit, color) -> None:
        self.rank: Rank = rank
        self.suit: Suit = suit
        self.color: Color = color

    def __str__(self) -> str:
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

class Deck:
    def __init__(self, cards=None) -> None:
        if cards is None:
            cards = []
        self.cards: List[Card] = cards

    def shuffle(self) -> None:
        temp = None
        for i in range(len(self.cards)-1, -1, -1):
            swap_index = random.randint(0, i)
            temp = self.cards[swap_index]
            self.cards[swap_index] = self.cards[i]
            self.cards[i] = temp
            temp = None

    def draw(self, draw_number: int) -> List[Card]:
        cards = []
        for _ in range(draw_number):
            if self.is_empty():
                print('Card is out of Deck!')
            else:
                cards.append(self.cards.pop())
        return cards

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def append_card(self, card) -> None:
        self.cards.append(card)
    
    def print_cards(self) -> None:
        for card in self.cards:
            print(card)

class Hand:
    def __init__(self, cards=None) -> None:
        if cards is None:
            cards = []
        self.cards: List[Card] = cards

    def evaluate_cards(self, commu_cards: List[Card]) -> None:
        pass

    def add_cards(self, cards: List[Card]) -> None:
        self.cards.extend(cards)

    def clear_hand(self) -> None:
        self.cards.clear()

class Player:
    def __init__(self, id, chips, hand, next_player = None) -> None:
        self.id: int = id
        self.chips: int = chips
        self.hand: Hand = hand
        self.current_bet: int = 0
        self.has_folded: bool = False
        self.next_player: Union[Player, None] = next_player

    def make_bet(self, action: Action) -> None:
        pass

class Poker:
    def __init__(self, player, deck) -> None:
        self.first_player: Player = player
        self.deck: Deck = deck
        self.pot: int = 0
        self.current_phase: Phase = Phase.PRE_FLOP
        self.community_card: List[Card] = []

    def generate_chips(self, number: int) -> None:
        pass

    def deal_cards(self) -> None:
        pass

    def betting_round(self) -> None:
        pass

    def change_phase(self) -> None:
        pass

    def determind_winner(self) -> None:
        pass

    def payout(self) -> None:
        pass

    def game_over(self) -> None:
        pass


#################################### Initial Poker Game ####################################

# create cards
deck = Deck()
for rank in Rank:
    for suit in Suit:
        color = Color.BLACK
        if suit.name == 'HEART' or suit.name == 'DIAMOND':
            color = Color.RED
        card = Card(rank=rank, suit=suit, color=color)
        deck.append_card(card)

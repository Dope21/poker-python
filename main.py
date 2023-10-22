from enum import Enum
import itertools
from typing import List, Union
import itertools 
import random

class Rank(Enum):
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
    ACE = 14

class Stack(Enum):
    ROYAL_FLUSH = 10
    STRAIGHT_FLUSH = 9
    QUADS = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    TRIPS = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

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
    BLACK = "\033[30m"
    RED = "\033[91m"

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
    
        return f"{self.color.value}{suit_symbol}\033[0m {rank_symbol}"

class Deck:
    def __init__(self, cards=None) -> None:
        if cards is None:
            cards = []
        self.cards: List[Card] = cards

    def fisher_shuffle(self) -> None:
        temp = None
        for i in range(len(self.cards)-1, -1, -1):
            swap_index = random.randint(0, i)
            temp = self.cards[swap_index]
            self.cards[swap_index] = self.cards[i]
            self.cards[i] = temp
            temp = None

    def riffle_shuffle(self) -> None:
        split_index = random.randint(24, 28)
        q1 = self.cards[:split_index]
        q2 = self.cards[split_index:]
        shuffle_deck = []
        while len(q1) or len(q2):
            if len(q1): shuffle_deck.append(q1.pop(0))
            if len(q2): shuffle_deck.append(q2.pop(0))
        self.cards = shuffle_deck

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
        self.stack: Stack = Stack.HIGH_CARD
        self.best_cards: List[Card] = []

    def evaluate_cards(self, cards: List[Card]) -> Stack:
        suits = { "H": 0, "D": 0, "S": 0, "C": 0 }
        ranks = [0] * 13
        
        for card in cards:
            suits[card.suit.value] += 1
            ranks[card.rank.value - 2] += 1

        if 1 in ranks:
            first_i = ranks.index(1) 
            low_ace_indicatior = all(value == 1 for value in ranks[:4] + [ranks[-1]])
            ranks_part = ranks[first_i:first_i+5]
            consecutive = len(ranks_part) == 5 and all(n == 1 for n in ranks_part)
        else:
            first_i = None
            low_ace_indicatior = False
            consecutive = False

        flush = any(value >= 5 for value in suits.values())
        trips = 3 in ranks
        pairs = ranks.count(2)

        if (consecutive or low_ace_indicatior) and flush:
            if first_i == 8: return Stack.ROYAL_FLUSH
            return Stack.STRAIGHT_FLUSH
        if 4 in ranks: return Stack.QUADS
        if trips and pairs: return Stack.FULL_HOUSE
        if flush: return Stack.FLUSH
        if consecutive: return Stack.STRAIGHT
        if trips: return Stack.TRIPS
        if pairs == 2: return Stack.TWO_PAIR
        if pairs: return Stack.ONE_PAIR
        return Stack.HIGH_CARD

    def find_best_hande(self, commnu_cards: List[Card]) -> None: 
        all_cards = self.cards + commnu_cards
       
        best_hand = []
        hit_rank = Stack.HIGH_CARD

        if len(all_cards) >= 5:
            combinations = list(itertools.combinations(all_cards, 5))

            for combo in combinations:
                combo_list = list(combo) # convert from tuple
                new_rank = self.evaluate_cards(combo_list)

                if hit_rank is None:
                    hit_rank = new_rank 
                    best_hand = combo_list
                    continue
                if hit_rank.value < new_rank.value:
                    hit_rank = new_rank 
                    best_hand = combo_list

        else:
            best_hand = all_cards
            hit_rank = self.evaluate_cards(all_cards)

        self.best_cards = best_hand
        self.stack = hit_rank

    def sort_cards(self, cards: List[Card]):
        if len(cards) <= 1: return cards
        for current in range(1, len(cards)):
            temp = cards[current]
            previous = current - 1

            while previous >= 0 and cards[previous].rank.value > temp.rank.value:
                cards[previous + 1] = cards[previous] 
                previous -= 1

            cards[previous + 1] = temp
        return cards

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

deck = Deck()
for rank in Rank:
    for suit in Suit:
        color = Color.BLACK
        if suit.name == 'HEART' or suit.name == 'DIAMOND':
            color = Color.RED
        card = Card(rank=rank, suit=suit, color=color)
        deck.append_card(card)

ryf = [
    Card(rank=Rank.ACE, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.KING, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.QUEEN, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.JACK, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.TEN, suit=Suit.HEART, color=Color.RED)
]

hand_cards = []

hand = Hand()
hand.cards = hand_cards

deck.riffle_shuffle()
deck.fisher_shuffle()
deck.riffle_shuffle()

for c in deck.cards:
    print(c)

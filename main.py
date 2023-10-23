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
    FLOP = 3
    TURN = 1
    RIVER = 1

class Color(Enum):
    BLACK = "\033[30m"
    RED = "\033[91m"

class Action(Enum):
    FOLD = 0
    CHECK = 1
    RISE = 2
    CALL = 3
    ALL_IN = 4

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
        if draw_number == 0: return []
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

    def find_best_hand(self, commnu_cards: List[Card]) -> None: 
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

    def display_hand(self) -> None:
        for c in self.cards:
            print(c, end=", ")
        print()

    def display_best_cards(self) -> None:
        for c in self.best_cards:
            print(c, end=", ")
        print()

class Player:
    def __init__(self, id, hand, next_player = None) -> None:
        self.id: int = id
        self.chips: int = 0
        self.hand: Hand = hand
        self.current_bet: int = 0
        self.has_folded: bool = False
        self.next_player: Union[Player, None] = next_player

    def make_bet(self, action: Action) -> None:
        pass

class Poker:
    def __init__(self, player) -> None:
        self.deck: Deck = Deck()
        self.first_player: Player = player
        self.pot: int = 0
        self.current_phase: Phase = Phase.PRE_FLOP
        self.community_card: List[Card] = []

        # Create cards
        for rank in Rank:
            for suit in Suit:
                color = Color.BLACK
                if suit.name == 'HEART' or suit.name == 'DIAMOND':
                    color = Color.RED
                card = Card(rank=rank, suit=suit, color=color)
                self.deck.append_card(card)
        self.deck.riffle_shuffle()
        self.deck.fisher_shuffle()

    def generate_chips(self, amount: int) -> None:
        player = self.first_player
        while player:
            player.chips = amount
            player = player.next_player
            if player == self.first_player: break

    def deal_cards(self) -> None:
        player = self.first_player
        while player:
            first_hand = self.deck.draw(2) 
            player.hand.cards = first_hand
            player = player.next_player
            if player == self.first_player: break

    def draw_community_cards(self, phase: Phase) -> None:
        cards = self.deck.draw(phase.value)
        self.community_card.extend(cards)

    def display_community_cards(self) -> None:
        print("Community Cards: ", end=" ")
        for c in self.community_card:
            print(c, end=", ")
        print()

    def betting_round(self) -> None:
        pass

    def change_phase(self) -> None:
        pass

    def determine_winner(self) -> None:
        pass

    def payout(self) -> None:
        pass

    def game_over(self) -> None:
        pass

    @staticmethod
    def create_players(no_of_player: int) -> Player:
        player = Player(id=0, hand=Hand())
        first_player = player

        for i in range(1, no_of_player):
            new_player = Player(id=i, hand=Hand())
            player.next_player = new_player
            player = player.next_player

        player.next_player = first_player
        return first_player


#################################### Initial Poker Game ####################################
first_player = Poker.create_players(2)
poker = Poker(first_player)

# generate chips
while True:
    try:
        chips = int(input("How many chips would you like to play? Enter a number: "))
        print("You entered:", chips)
        if chips <= 0 or chips > 100: raise ValueError
        poker.generate_chips(chips)
        break
    except ValueError:
        print("Please enter a number 1 - 100")

poker.deal_cards()

#################################### Game Start ####################################

# / initial Phase
# / draw community cards relate to phase

# / player start their turn

    ## / print out community cards
    ## / print hand cards
    ## / calulate best hand and print out
    ## betting chips on the table
        ### show the highest bet
        ### show player current bet
        ### select action Call, Riase, Fold, All-in, Check
    
    ## compare betting conditions
        ### if all last bet is 0 and total bet is equal
            #### restart and go back to intial phase
            #### if the last phase the showdown
                ##### determine winner 
                ##### re-start the game
        ### if player fold then another player win
            #### re-start the game
        ### if total bet is equal then keep betting phase going

    ## go to next player

phase_start = True
while phase_start:
    try:
        # inital
        print(f"Phase: {poker.current_phase.name}")
        poker.draw_community_cards(poker.current_phase)  

        # betting
        betting_round = True
        player = poker.first_player
        if player is None: raise ValueError("First player is None!")
        while betting_round:

            poker.display_community_cards()
            if player is None: raise ValueError("Player is None!")
            print(f"Player {player.id} turn!!")

            print("Your Cards: ", end="")
            player.hand.display_hand()

            player.hand.find_best_hand(poker.community_card)
            print("Your Best Rank is", player.hand.stack.name)

            print("Your Best Cards Stack: ", end="")
            player.hand.display_best_cards()

            player = player.next_player

            betting_round = False
        phase_start = False
    except ValueError as error:
        print(error)

#################################### End ####################################

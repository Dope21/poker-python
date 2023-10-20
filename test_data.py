ryf = [
    Card(rank=Rank.ACE, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.KING, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.QUEEN, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.JACK, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.TEN, suit=Suit.HEART, color=Color.RED)
]

straight_flush = [
    Card(rank=Rank.SIX, suit=Suit.DIAMOND, color=Color.BLACK),
    Card(rank=Rank.FIVE, suit=Suit.DIAMOND, color=Color.BLACK),
    Card(rank=Rank.FOUR, suit=Suit.DIAMOND, color=Color.BLACK),
    Card(rank=Rank.THREE, suit=Suit.DIAMOND, color=Color.BLACK),
    Card(rank=Rank.TWO, suit=Suit.DIAMOND, color=Color.BLACK)
]

quads = [
    Card(rank=Rank.KING, suit=Suit.SPADE, color=Color.BLACK),
    Card(rank=Rank.KING, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.KING, suit=Suit.CLUB, color=Color.BLACK),
    Card(rank=Rank.KING, suit=Suit.DIAMOND, color=Color.RED),
    Card(rank=Rank.ACE, suit=Suit.HEART, color=Color.RED)
]

full_house = [
    Card(rank=Rank.KING, suit=Suit.SPADE, color=Color.BLACK),
    Card(rank=Rank.KING, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.KING, suit=Suit.CLUB, color=Color.BLACK),
    Card(rank=Rank.ACE, suit=Suit.DIAMOND, color=Color.RED),
    Card(rank=Rank.ACE, suit=Suit.HEART, color=Color.RED)
]

trips = [
    Card(rank=Rank.QUEEN, suit=Suit.SPADE, color=Color.BLACK),
    Card(rank=Rank.QUEEN, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.QUEEN, suit=Suit.CLUB, color=Color.BLACK),
    Card(rank=Rank.JACK, suit=Suit.DIAMOND, color=Color.RED),
    Card(rank=Rank.ACE, suit=Suit.HEART, color=Color.RED)
]

two_pair = [
    Card(rank=Rank.QUEEN, suit=Suit.SPADE, color=Color.BLACK),
    Card(rank=Rank.QUEEN, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.KING, suit=Suit.CLUB, color=Color.BLACK),
    Card(rank=Rank.KING, suit=Suit.DIAMOND, color=Color.RED),
    Card(rank=Rank.ACE, suit=Suit.HEART, color=Color.RED)
]

one_pair = [
    Card(rank=Rank.QUEEN, suit=Suit.SPADE, color=Color.BLACK),
    Card(rank=Rank.QUEEN, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.KING, suit=Suit.CLUB, color=Color.BLACK),
    Card(rank=Rank.JACK, suit=Suit.DIAMOND, color=Color.RED),
    Card(rank=Rank.ACE, suit=Suit.HEART, color=Color.RED)
]

high_card = [
    Card(rank=Rank.TWO, suit=Suit.SPADE, color=Color.BLACK),
    Card(rank=Rank.KING, suit=Suit.HEART, color=Color.RED),
    Card(rank=Rank.QUEEN, suit=Suit.CLUB, color=Color.BLACK),
    Card(rank=Rank.JACK, suit=Suit.DIAMOND, color=Color.RED),
    Card(rank=Rank.TEN, suit=Suit.HEART, color=Color.RED)
]

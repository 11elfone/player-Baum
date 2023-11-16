from models.bet import Bet
from models.table import Table
from models.card import Card
from models.suit import Suit
from models.rank import Rank


rankv = {Rank._2: 2,
         Rank._3: 3,
         Rank._4: 4,
         Rank._5: 5,
         Rank._6: 6,
         Rank._7: 7,
         Rank._8: 8,
         Rank._9: 9,
         Rank._10: 10,
         Rank.J: 11,
         Rank.Q: 12,
         Rank.K: 13,
         Rank.A: 14}


def restructure(common: list[Card], hand: list[Card]) -> tuple[dict[Rank.name, int], dict[Suit.name, int]]:
    ranks = {}
    suits = {}
    for c in hand:
        if c.rank in ranks.keys():
            ranks[c.rank] += 1
        else:
            ranks[c.rank] = 1

        if c.suit in suits.keys():
            suits[c.suit] += 1
        else:
            suits[c.suit] = 1

    for c in common:
        if c.rank in ranks.keys():
            ranks[c.rank] += 1
        else:
            ranks[c.rank] = 1

        if c.suit in suits.keys():
            suits[c.suit] += 1
        else:
            suits[c.suit] = 1

    return ranks, suits


def find_top_multi(ranks: dict[Rank.name, int]) -> tuple[Rank.name, int]:
    rank: Rank.name = Rank._2
    n = 0
    for r in sorted(ranks.keys()):
        if ranks[r] > n:
            n = ranks[r]
            rank = r
        elif ranks[r] >= n and rankv[r] > rankv[rank]:
            n = ranks[r]
            rank = r
    return rank, n


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)

    hand = table.players[table.activePlayer].cards
    common = table.communityCards

    ranks, suits = restructure(common, hand)
    top_multi, top_multi_rank = find_top_multi(ranks)

    # go all-in
    # bet = Bet(table.players[table.activePlayer].stack)

    # bet min
    bet = Bet(table.minimumRaise)

    return bet

from models.bet import Bet
from models.table import Table
from models.card import Card
from models.suit import Suit
from models.rank import Rank
import traceback


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


def restructure(common: list[Card], hand: list[Card]) -> tuple[dict[Rank, int], dict[Suit, int]]:
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


def find_top_multi(ranks: dict[Rank, int]) -> tuple[Rank, int]:
    rank: Rank = Rank._2
    n = 0
    for r in ranks.keys():
        if ranks[r] > n:
            n = ranks[r]
            rank = r
        elif ranks[r] >= n and rankv[r] > rankv[rank]:
            n = ranks[r]
            rank = r
    return rank, n


def find_highest_flush(cards: list[Card], suits: dict[Suit, int]) -> bool:
    if max(suits.values()) >= 5:
        return True
    else:
        return False


def find_straight(ranks: dict[Rank, int]) -> bool:
    pass


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)

    hand = table.players[table.activePlayer].cards
    common = table.communityCards

    stack = table.players[table.activePlayer].stack
    minraise = table.minimumRaise
    minbet = table.minimumBet

    cards = hand + common

    print('hi')

    try:
        # questionable code goes here
        ranks, suits = restructure(common, hand)
        top_multi, top_multi_rank = find_top_multi(ranks)
        print(f'{top_multi_rank} x {top_multi}')
    except Exception as e:
        print(f'An exception occurred:\n{e}\ntraceback:\n{traceback.print_exc()}')

    print('hi2')

    # go all-in
    # bet = Bet(table.players[table.activePlayer].stack)

    # bet min, never all-in
    if stack-minraise > 0:
        bet = Bet(minraise)
    elif stack-minbet > 0:
        bet = Bet(minbet)
    else:
        bet = Bet(0)

    return bet

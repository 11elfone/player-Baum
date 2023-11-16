from models.bet import Bet
from models.table import Table
from models.card import Card
from models.suit import Suit
from models.rank import Rank
import traceback
import random as rand

# rankv = {Rank._2: 2, Rank._3: 3, Rank._4: 4, Rank._5: 5, Rank._6: 6, Rank._7: 7, Rank._8: 8, Rank._9: 9, Rank._10: 10, Rank.J: 11, Rank.Q: 12, Rank.K: 13, Rank.A: 14}
rankv = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def restructure(cards: list[Card]) -> tuple[dict[str, int], dict[str, int]]:
    ranks = {}
    suits = {}

    for c in cards:
        if type(c) != Card:
            continue

        if c.rank in ranks.keys():
            ranks[c.rank.value] += 1
        else:
            ranks[c.rank.value] = 1

        if c.suit in suits.keys():
            suits[c.suit.value] += 1
        else:
            suits[c.suit.value] = 1

    return ranks, suits


def find_top_multi(ranks: dict[str, int]) -> tuple[str, int]:
    rank: str = ''
    rankvalue = 0
    n = 0
    for r in ranks.keys():
        if ranks[r] > n:
            n = ranks[r]
            rank = r
        elif ranks[r] >= n and rankv[r] > rankvalue:
            n = ranks[r]
            rank = r
            rankvalue = rankv[r]
    return rank, n


def find_highest_flush(cards: list[Card], suits: dict[str, int]) -> bool:
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

    nround = table.round

    cards = hand + common
    print(f'total cards in game: {len(cards)}')

    print('hi')

    try:
        # questionable code goes here
        ranks, suits = restructure(cards)
        print(ranks)
        top_multi_rank, top_multi = find_top_multi(ranks)
        print(f'{top_multi_rank} x {top_multi}')
    except Exception as e:
        print(f'An exception occurred:\n{e}\ntraceback:\n{traceback.print_exc()}')

    # fold on first round
    if table.round == 0:
        return Bet(0)

    # go all-in
    bet_amount = int(max(table.minimumBet, rand.random()*table.players[table.activePlayer].stack))
    bet = Bet(bet_amount)
    print(f"Bet: {bet_amount}, minbet: {table.minimumBet}")
    return bet

    # bet min, never all-in
    if stack-minraise > 0:
        bet = Bet(minraise)
    elif stack-minbet > 0:
        bet = Bet(minbet)
    else:
        bet = Bet(0)

    return bet

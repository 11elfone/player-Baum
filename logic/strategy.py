from models.bet import Bet
from models.table import Table
import traceback
import random as rand
from time import strftime, time

# rankv = {Rank._2: 2, Rank._3: 3, Rank._4: 4, Rank._5: 5, Rank._6: 6, Rank._7: 7, Rank._8: 8, Rank._9: 9, Rank._10: 10, Rank.J: 11, Rank.Q: 12, Rank.K: 13, Rank.A: 14}
value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def restructure(cards: list[dict]) -> tuple[dict[str, int], dict[str, int]]:
    ranks = {}
    suits = {}

    for c in cards:
        if c['rank'] in ranks.keys():
            ranks[c['rank']] += 1
        else:
            ranks[c['rank']] = 1

        if c['suit'] in suits.keys():
            suits[c['suit']] += 1
        else:
            suits[c['suit']] = 1

    return ranks, suits


def find_top_multi(ranks: dict[str, int]) -> tuple[str, int]:
    rank: str = ''
    rankvalue = 0
    n = 0
    for r in ranks.keys():
        if ranks[r] > n:
            n = ranks[r]
            rank = r
        elif ranks[r] == n and rankvalue < value[r]:
            n = ranks[r]
            rank = r
            rankvalue = value[r]
    return rank, n


def find_highest_flush(cards: list[dict], suits: dict[str, int]) -> bool:
    if max(suits.values()) >= 5:
        return True
    else:
        return False


# def find_straight(ranks: dict[Rank, int]) -> bool:
#     pass


def decide(table: Table) -> Bet:
    print((20*'-')+'\ndecision\n'+(20*'-') + strftime('\n[%H:%M:%S]'))
    print(f"Round: {table.round}")

    return Bet(time() % 100 + 2*table.minimumBet)

    hand = []
    common = []
    hand = table.players[table.activePlayer].cards
    common = table.communityCards

    # print(f'size hand: {len(hand)}')
    # print(f'what is this hand: {hand}')
    # print(f'size common: {len(common)}')
    # print(f'what is this common: {common}')

    stack: int = table.players[table.activePlayer].stack
    minraise = table.minimumRaise
    minbet = table.minimumBet

    nround = table.round

    cards = []
    cards = hand + common
    print(f'total cards in game: {len(cards)}')
    print(f'cards: {cards}')

    # questionable code goes here
    ranks, suits = restructure(cards)
    print(ranks)
    top_multi_rank, top_multi = find_top_multi(ranks)
    print(f'{top_multi_rank} x {top_multi}')
    print(f'low cards: {value[top_multi_rank] <= 10}')
    if top_multi < 2 and value[top_multi_rank] <= 9:
        print('folding for low cards')
        return Bet(0)

    if top_multi == 4:
        print('all-in')
        return Bet(stack)

    # fold on first round
    # if table.round == 1:
    #     print(f"--\nfold in first round\n--")
    #     return Bet(0)

    bet_amount = int(max(table.minimumBet + 1, stack / 2, 1))
    if bet_amount > stack:
        bet_amount = stack
    bet = Bet(bet_amount)
    print(f"Bet: {bet_amount}, minbet: {table.minimumBet}")
    return bet

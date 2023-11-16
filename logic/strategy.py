from models.bet import Bet
from models.table import Table
from models.card import Card
from models.suit import Suit


def restructure(common: list[Card], hand: list[Card]) -> tuple[dict[str, int], dict[Suit, int]]:
    ranks = {}
    suits = {}
    for c in hand:
        if str(c.rank) in ranks.keys():
            ranks[str(c.rank)] += 1
        else:
            ranks[str(c.rank)] = 1

        if c.suit in suits.keys():
            suits[c.suit] += 1
        else:
            suits[c.suit] = 1

    for c in common:
        if str(c.rank) in ranks.keys():
            ranks[str(c.rank)] += 1
        else:
            ranks[str(c.rank)] = 1

        if c.suit in suits.keys():
            suits[c.suit] += 1
        else:
            suits[c.suit] = 1

    return ranks, suits


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)

    hand = table.players[table.activePlayer].cards
    common = table.communityCards

    ranks, suits = restructure(common, hand)

    # go all-in
    bet = Bet(table.players[table.activePlayer].stack)

    return bet

from models.bet import Bet
from models.table import Table


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)

    bet = Bet(table.players[table.activePlayer].stack)

    return bet

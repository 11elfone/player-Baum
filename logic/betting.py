def best_amount_to_bet(prob: float, amount_bet: int, cash: int, pot: int):
    """
    :param prob: p of winning this round
    :param amount_bet: the amount we bet in this and previous rounds
    :param cash: our money
    :param pot: money in the pot and bet by all players
    :return: amount to bet
    """
    return (prob - (1-prob)/(pot/amount_bet))*(cash-amount_bet)

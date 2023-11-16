from models.card import Card
from typing import List
from enum import Enum


class PlayerStatusEnum(Enum):
    ACTIVE = 'ACTIVE'
    FOLDED = 'FOLDED'
    OUT = 'OUT'


class Player:
    name: str
    status: PlayerStatusEnum
    stack: int
    bet: int
    cards: List[Card] = []

    def __init__(self, player: dict):
        self.name = player['name']
        self.status = PlayerStatusEnum(player['status'])
        self.stack = player['stack']
        self.bet = player['bet']
        try:
            # for card in player['cards']:
            #     self.cards.append(Card(card))
            self.cards = player['cards']
        except KeyError:
            self.cards = []

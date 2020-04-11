from abc import ABCMeta, abstractmethod

from typing import List

from game.implementations import Game
from game.implementations import Player
from actions.implementations.result import ActionResult

class IAction(metaclass=ABCMeta):
    @abstractmethod
    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult: pass

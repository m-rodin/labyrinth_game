from abc import ABCMeta, abstractmethod

from typing import List

from implementations.game import Game
from implementations.player import Player
from implementations.actions.result import ActionResult

class IAction(metaclass=ABCMeta):
    @abstractmethod
    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult: pass

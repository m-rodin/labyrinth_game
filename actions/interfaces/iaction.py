from abc import ABCMeta, abstractmethod

from typing import List

from game.interfaces.iplayer import IPlayer

from game.implementations import Game
from actions.implementations.result import ActionResult

class IAction(metaclass=ABCMeta):
    @abstractmethod
    def do(self, params: List[str], game: Game, player: IPlayer = None) -> ActionResult: pass

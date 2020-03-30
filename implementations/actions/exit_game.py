from typing import List, Tuple, Optional

from interfaces.actions import IAction

from implementations.game import Game
from implementations.player import Player
from implementations.actions.result import ActionResult

class ExitGameAction(IAction):
    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult:
        return ActionResult.exit()
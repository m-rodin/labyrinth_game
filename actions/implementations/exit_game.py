from typing import List, Tuple, Optional

from actions.interfaces.iaction import IAction

from game.implementations import Game
from game.implementations import Player
from actions.implementations.result import ActionResult

class ExitGameAction(IAction):
    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult:
        return ActionResult.exit()
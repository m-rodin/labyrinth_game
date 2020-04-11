from typing import List, Tuple, Optional

from actions.interfaces.iaction import IAction

from game.implementations import Game
from game.implementations import Player
from actions.implementations.result import ActionResult

from actions.exceptions import InvalidAction

class SkipStepAction(IAction):
    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult:
        if not game.is_started:
            raise InvalidAction("game didn't start yet")

        return ActionResult.success("step skipped")
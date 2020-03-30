from typing import List, Tuple, Optional

from interfaces.actions import IAction

from implementations.game import Game
from implementations.player import Player
from implementations.actions.result import ActionResult

from exceptions import InvalidAction

class SkipStepAction(IAction):
    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult:
        if not game.is_started:
            raise InvalidAction("game didn't start yet")

        return ActionResult.success("step skipped")
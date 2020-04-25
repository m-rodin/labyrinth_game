from typing import List, Tuple, Optional

from actions.interfaces.iaction import IAction
from game.interfaces.iplayer import IPlayer

from game.implementations import Game
from game.implementations.labyrinth.objects import River
from actions.implementations.result import ActionResult

from actions.exceptions import InvalidAction

class SkipStepAction(IAction):
    def do(self, params: List[str], game: Game, player: IPlayer = None) -> ActionResult:
        if not game.is_started:
            raise InvalidAction("game didn't start yet")

        cell = game.labyrinth.getCell(player.x, player.y)
        object = game.labyrinth.getObject(cell)

        if object and isinstance(object, River):
            result = object.activate(player, game)
            return ActionResult.success("step executed, river (" + str(result) + ")")

        return ActionResult.success("step skipped")
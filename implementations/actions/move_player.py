from typing import List, Tuple, Optional

from interfaces.actions import IAction

from implementations.game import Game
from implementations.player import Player
from implementations.actions.result import ActionResult

from implementations.labyrinth.objects import Treasure, Wormhole
from implementations.labyrinth.cell import DIRECTION_BOTTOM, DIRECTION_LEFT, DIRECTION_TOP, DIRECTION_RIGHT

from exceptions import InvalidActionParams, InvalidAction


class MovePlayerAction(IAction):
    def __init__(self):
        self.directionsMap = {
            'up': DIRECTION_TOP,
            'down': DIRECTION_BOTTOM,
            'left': DIRECTION_LEFT,
            'right': DIRECTION_RIGHT
        }

    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult:
        if not game.is_started:
            raise InvalidAction("game didn't start yet")
        if len(params) < 1:
            raise InvalidActionParams("step direction should be given")

        param = params[0]
        if not param in self.directionsMap:
            raise InvalidActionParams("step direction should be one of [up, down, left, right]")

        direction = self.directionsMap[param]

        cell = game.labyrinth.getCell(player.x, player.y)
        result = cell.go(player, direction)

        if result.is_success and not result.is_finish:
            result = self._checkObjects(game, player)

        return result

    def _checkObjects(self, game: Game, player: Player) -> ActionResult:
        cell = game.labyrinth.getCell(player.x, player.y)
        object = game.labyrinth.getObject(cell)

        if object:
            object.activate(player, game)

            if isinstance(object, Treasure):
                return ActionResult.success("step executed, treasure")
            if isinstance(object, Wormhole):
                return ActionResult.success("step executed, wormhole")

        return ActionResult.success("step executed")

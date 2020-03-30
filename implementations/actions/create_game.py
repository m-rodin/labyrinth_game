from typing import List

from interfaces.actions import IAction

from implementations.game import Game
from implementations.player import Player
from implementations.actions.result import ActionResult

from exceptions import InvalidActionParams

class CreateGameAction(IAction):
    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult:
        if len(params) < 1:
            raise InvalidActionParams("labyrinth size should be given")
        
        size = int(params[0])

        if (size < 4) or (size > 10):
            raise InvalidActionParams("labyrinth size should be beetween 4 and 10")

        game.start(size=size, players_count=1)

        return ActionResult.success("game created, let's start")
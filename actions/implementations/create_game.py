from typing import List

from actions.interfaces.iaction import IAction

from game.implementations import Game
from game.implementations import Player
from actions.implementations.result import ActionResult

from actions.exceptions import InvalidActionParams

class CreateGameAction(IAction):
    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult:
        if len(params) < 1:
            raise InvalidActionParams("labyrinth size should be given")
        
        size = int(params[0])

        if (size < 4) or (size > 10):
            raise InvalidActionParams("labyrinth size should be beetween 4 and 10")

        game.start(size=size, players_count=1)

        return ActionResult.success("game created, let's start")
from typing import List, Tuple, Optional
from os import path

from interfaces.actions import IAction

from implementations.game import Game
from implementations.player import Player

from implementations.actions.result import ActionResult
from implementations.game import Game

from exceptions import InvalidActionParams

class LoadGameAction(IAction):
    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult:
        if len(params) < 1:
            raise InvalidActionParams("filename should be given")

        filename = params[0]

        if (not path.exists(filename)) or (not path.isfile(filename)):
            raise InvalidActionParams("file must be exist")

        try:
            game.load(filename)
        except Exception:
            raise InvalidActionParams("file mast be in the correct format")

        return ActionResult.success("game loaded, let's continue")
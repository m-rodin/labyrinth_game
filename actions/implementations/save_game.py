from typing import List, Tuple, Optional
from os import path

from actions.interfaces.iaction import IAction

from game.implementations import Game
from game.implementations import Player
from actions.implementations.result import ActionResult

from actions.exceptions import InvalidActionParams, InvalidAction

class SaveGameAction(IAction):
    def do(self, params: List[str], game: Game, player: Player = None) -> ActionResult:
        if not game.is_started:
            raise InvalidAction("game didn't start yet")

        if len(params) < 1:
            raise InvalidActionParams("filename should be given")

        filename = params[0]

        try:
            game.save(filename)
        except Exception:
            raise Exception("unexpected error while saving")

        return ActionResult.success("game saved")
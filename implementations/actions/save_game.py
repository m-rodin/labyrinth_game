from typing import List, Tuple, Optional
from os import path

from interfaces.actions import IAction

from implementations.game import Game
from implementations.player import Player
from implementations.actions.result import ActionResult

from exceptions import InvalidActionParams, InvalidAction

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
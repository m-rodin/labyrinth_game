from typing import List, Tuple, Optional
from os import path

from actions.interfaces.iaction import IAction
from game.interfaces.iplayer import IPlayer

from game.implementations import Game
from actions.implementations.result import ActionResult

from actions.exceptions import InvalidActionParams

class LoadGameAction(IAction):
    def do(self, params: List[str], game: Game, player: IPlayer = None) -> ActionResult:
        if len(params) < 1:
            raise InvalidActionParams("filename should be given")

        filename = params[0]

        if (not path.exists(filename)) or (not path.isfile(filename)):
            raise InvalidActionParams("file must be exist")

        try:
            game.load(filename)
        except Exception:
            raise InvalidActionParams("file mast be in the correct format")

        return ActionResult.success("game loaded, let's continue", step_completed=False)
from typing import List, Tuple, Optional

from actions.interfaces.iaction import IAction
from game.interfaces.iplayer import IPlayer

from game.implementations import Game
from actions.implementations.result import ActionResult

class ExitGameAction(IAction):
    def do(self, params: List[str], game: Game, player: IPlayer = None) -> ActionResult:
        return ActionResult.exit()
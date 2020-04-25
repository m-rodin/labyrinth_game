from typing import List

from actions.interfaces.iaction import IAction
from game.interfaces.iplayer import IPlayer

from game.implementations import Game
from game.implementations.labyrinth.factory import LabyrinthFactory
from game.implementations.players.factory import PlayersFactory

from actions.implementations.result import ActionResult

from actions.exceptions import InvalidActionParams

class CreateGameAction(IAction):
    def do(self, params: List[str], game: Game, player: IPlayer = None) -> ActionResult:
        if len(params) < 1:
            raise InvalidActionParams("labyrinth size should be given")
        
        size = int(params[0])

        if (size < 4) or (size > 10):
            raise InvalidActionParams("labyrinth size should be beetween 4 and 10")

        labyrinth_factory = LabyrinthFactory(size=size)
        players_factory = PlayersFactory(
            players_count=1,
            bears_count=1,
            labyrinth_size=size
        )

        game.start(labyrinth_factory, players_factory)

        return ActionResult.success("game created, let's start")
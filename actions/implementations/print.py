from typing import List, Tuple, Optional

from actions.interfaces.iaction import IAction
from game.interfaces.iplayer import IPlayer

from game.implementations import Game
from actions.implementations.result import ActionResult

from actions.exceptions import InvalidAction

from game.implementations.labyrinth.cell import DIRECTION_TOP, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_BOTTOM

class PrintAction(IAction):
    def do(self, params: List[str], game: Game, player: IPlayer = None) -> ActionResult:
        if not game.is_started:
            raise InvalidAction("game didn't start yet")

        players_cells = {}
        for player in game.players:
            if player.x not in players_cells:
                players_cells[player.x] = {}
            if player.y not in players_cells[player.x]:
                players_cells[player.x][player.y] = player.getName(short=True)

        s = "\n"
        for row in game.labyrinth.cells:
            for cell in row:
                s += '*  ' if cell.canGo(DIRECTION_TOP) else '*--'
            s += "*\n"
            for cell in row:
                s += ' ' if cell.canGo(DIRECTION_LEFT) else '|'

                if cell.x in players_cells and cell.y in players_cells[cell.x]:
                    s += players_cells[cell.x][cell.y]
                else:
                    obj = game.labyrinth.getObject(cell)
                    s += obj.id if obj else "  "

            s += " \n" if cell.canGo(DIRECTION_RIGHT) else "|\n"
        
        for cell in game.labyrinth.cells[-1]:
            s += '*  ' if cell.canGo(DIRECTION_BOTTOM) else '*--'
        s += "*\n"

        return ActionResult.success(s)
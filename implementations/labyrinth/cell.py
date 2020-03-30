from typing import Tuple
from implementations.player import Player
from implementations.actions.result import ActionResult

SIDE_TYPE_PASS = 0
SIDE_TYPE_MONOLITH = 1
SIDE_TYPE_WALL = 2
SIDE_TYPE_EXIT = 3

DIRECTION_LEFT = "left"
DIRECTION_TOP = "top"
DIRECTION_RIGHT = "right"
DIRECTION_BOTTOM = "bottom"

class Cell:
    def __init__(self, x: int, y: int, size: Tuple[int, int]):
        self.x = x
        self.y = y

        self.directions = {
            DIRECTION_LEFT: SIDE_TYPE_MONOLITH if x == 0 else SIDE_TYPE_WALL,
            DIRECTION_TOP: SIDE_TYPE_MONOLITH if y == 0 else SIDE_TYPE_WALL,
            DIRECTION_RIGHT: SIDE_TYPE_MONOLITH if x + 1 == size[0] else SIDE_TYPE_WALL,
            DIRECTION_BOTTOM: SIDE_TYPE_MONOLITH if y + 1 == size[1] else SIDE_TYPE_WALL
        }

    def openDirection(self, direction: str):
        self.directions[direction] = SIDE_TYPE_PASS

    def setAsExit(self) -> bool:
        for i in self.directions:
            if self.directions[i] == SIDE_TYPE_MONOLITH:
                self.directions[i] = SIDE_TYPE_EXIT
                return True
        return False

    def canGo(self, direction: str) -> bool:
        return self.directions[direction] in [SIDE_TYPE_PASS, SIDE_TYPE_EXIT]

    def go(self, player: Player, direction: str) -> ActionResult:
        if self.directions[direction] == SIDE_TYPE_WALL:
            return ActionResult.fail("step impossible, wall")
        if self.directions[direction] == SIDE_TYPE_MONOLITH:
            return ActionResult.fail("step impossible, monolith")

        if (self.directions[direction] == SIDE_TYPE_EXIT):
            if player.canFinish():
                return ActionResult.finish()
            return ActionResult.fail("exit impossible, treasure not found")

        if direction == DIRECTION_LEFT:
            player.x -= 1
        elif direction == DIRECTION_RIGHT:
            player.x += 1
        elif direction == DIRECTION_TOP:
            player.y -= 1
        elif direction == DIRECTION_BOTTOM:
            player.y += 1

        return ActionResult.success("step executed")

    def dump(self) -> dict:
        return {
            'x': self.x,
            'y': self.y,
            'directions': self.directions
        }

    @staticmethod
    def load(data):
        cell = Cell(data['x'], data['y'], (0, 0))
        cell.directions = data['directions']
        return cell

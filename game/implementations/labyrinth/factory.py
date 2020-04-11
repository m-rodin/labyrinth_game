from random import shuffle, randrange

from game.implementations.labyrinth.cell import Cell
from game.implementations.labyrinth.objects import Treasure, WormholeFactory
from game.implementations.labyrinth.labyrinth import Labyrinth

from game.implementations.labyrinth.cell import DIRECTION_LEFT, DIRECTION_TOP, DIRECTION_RIGHT, DIRECTION_BOTTOM

class LabyrinthFactory:
    def __init__(self, size: int = 4):
        self.w = size
        self.h = size
        self.size = (size, size)

        self.wormholes_count = 5
        self.exits_count = 1
        self.treasure_count = 1

    def create(self) -> Labyrinth:
        cells = self._generateCells()
        labyrinth = Labyrinth(cells)

        for i in range(self.treasure_count):
            cell = self._getRandomCell(cells, labyrinth)
            object = Treasure("G" + str(i))
            object.placeTo(cell)

            labyrinth.addObject(object)

        wormholes = WormholeFactory.getRing(self.wormholes_count)
        for i in range(self.wormholes_count):
            cell = self._getRandomCell(cells, labyrinth)
            wormholes[i].placeTo(cell)

            labyrinth.addObject(wormholes[i])

        for i in range(self.exits_count):
            cell = self._getRandomCell(cells, labyrinth, is_border=True)
            cell.setAsExit()

        return labyrinth

    def _getRandomCell(self, cells: list, labyrinth: Labyrinth, is_border=False) -> Cell:
        while True:
            point = [randrange(self.w), randrange(self.h)]
            if is_border:
                axis = randrange(2)
                point[axis] = [0, (self.w - 1, self.h - 1)[axis]][randrange(2)]
            cell = cells[point[1]][point[0]]
            obj = labyrinth.getObject(cell)

            if not obj:
                return cell

    def _generateCells(self) -> list:
        vis = [[1] * (self.w + 2)] + [[1] + [0] * self.w + [1] for _ in range(self.h)] + [[1] * (self.w + 2)]
        cells = [[Cell(i, j, (self.w, self.h)) for i in range(self.w)] for j in range(self.h)]

        def walk(x, y):
            vis[y + 1][x + 1] = 1
    
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)

            for (xx, yy) in d:
                if vis[yy + 1][xx + 1]:
                    continue
                if xx == x:
                    cells[y][x].openDirection(DIRECTION_BOTTOM if yy == y + 1 else DIRECTION_TOP)
                    cells[yy][xx].openDirection(DIRECTION_TOP if yy == y + 1 else DIRECTION_BOTTOM)
                if yy == y:
                    cells[y][x].openDirection(DIRECTION_RIGHT if xx == x + 1 else DIRECTION_LEFT)
                    cells[yy][xx].openDirection(DIRECTION_LEFT if xx == x + 1 else DIRECTION_RIGHT)
                walk(xx, yy)
        
        walk(randrange(self.w), randrange(self.h))

        return cells
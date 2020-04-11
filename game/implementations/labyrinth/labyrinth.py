from typing import Optional

from game.interfaces.icellobject import ICellObject

from game.implementations import Player
from game.implementations.labyrinth.cell import DIRECTION_TOP, DIRECTION_LEFT, DIRECTION_RIGHT, DIRECTION_BOTTOM
from game.implementations.labyrinth.cell import Cell
from game.implementations.labyrinth import objects

class Labyrinth:
    def __init__(self, cells: list):
        self.cells = cells
        self.objects = {}

    def addObject(self, object: ICellObject):
        self.objects[object.id] = object

    def getObject(self, cell: Cell) -> Optional[ICellObject]:
        for obj in self.objects.values():
            if cell == obj.cell:
                return obj
        return None

    def getObjectById(self, id: str) -> Optional[ICellObject]:
        return self.objects[id] if id in self.objects else None

    def getCell(self, x: int, y: int):
        return self.cells[y][x]

    def dump(self) -> dict:
        return {
            'cells': [[cell.dump() for cell in row] for row in self.cells],
            'objects': {id: object.dump() for id, object in self.objects.items()},
        }

    @staticmethod
    def load(data):
        cells = [[Cell.load(cell) for cell in row] for row in data['cells']]

        labyrinth = Labyrinth(cells)
        for _, object_data in data['objects'].items():
            object = objects.__dict__[object_data['class']].load(object_data, cells)
            labyrinth.addObject(object)

        return labyrinth

from abc import ABCMeta, abstractmethod
from typing import List

from game.interfaces.icellobject import ICellObject
from game.implementations.labyrinth.cell import Cell

class BaseCellObject(ICellObject):
    def __init__(self, id: str):
        self.id = id
        self.cell = None

    def placeTo(self, cell: Cell):
        self.cell = cell

    def dump(self) -> dict:
        return {
            'class': type(self).__name__,
            'id': self.id,
            'cell': [self.cell.x, self.cell.y]
        }

    @classmethod
    def load(cls, data: dict, cells: list):
        tr = cls(data['id'])
        tr.cell = cells[data['cell'][1]][data['cell'][0]]
        return tr


class Treasure(BaseCellObject):
    def activate(self, player, game):
        player.addObject(self)


class Wormhole(BaseCellObject):
    def __init__(self, id: str):
        super().__init__(id)
        self.toId = None

    def activate(self, player, game):
        to = game.labyrinth.getObjectById(self.toId)

        player.x = to.cell.x
        player.y = to.cell.y

    def dump(self) -> dict:
        data = super().dump()
        data['toId'] = self.toId
        return data

    @classmethod
    def load(cls, data, cells):
        obj = super().load(data, cells)
        obj.toId = data['toId']
        return obj


class WormholeFactory:
    @staticmethod
    def getRing(count: int) -> List[Wormhole]:
        objects = []
        for i in range(count):
            objects.append(Wormhole("W" + str(i)))
        
        for i in range(count):
            objects[i].toId = objects[(i + 1) % count].id

        return objects
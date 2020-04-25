from abc import ABCMeta, abstractmethod
from typing import List
import random

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


class River(BaseCellObject):
    def __init__(self, id: str):
        super().__init__(id)
        self.toId = None

    def activate(self, player, game):
        way_len = random.randint(0, 2)

        end = self
        for _ in range(way_len):
            if end.toId:
                end = game.labyrinth.getObjectById(end.toId)

        player.x = end.cell.x
        player.y = end.cell.y

        return way_len

    def dump(self) -> dict:
        data = super().dump()
        data['toId'] = self.toId
        return data

    @classmethod
    def load(cls, data, cells):
        obj = super().load(data, cells)
        obj.toId = data['toId']
        return obj


class RiverFactory:
    @staticmethod
    def getDirect(count: int) -> List[River]:
        objects = []
        for i in range(count):
            objects.append(River("R" + str(i)))
        
        for i in range(count - 1):
            objects[i].toId = objects[i+1].id

        return objects

    @staticmethod
    def getWay(lenght: int, cell: Cell, cells: List) -> List[Cell]:
        variants = [[] for _ in range(4)]

        for i in range(lenght):
            if cell.y - i >= 0:
               variants[0].append(cells[cell.y - i][cell.x])
            if cell.x - i >= 0:
               variants[1].append(cells[cell.y][cell.x - i])
            if cell.y + i < len(cells):
               variants[2].append(cells[cell.y + i][cell.x])
            if cell.x + i < len(cells[cell.y]):
               variants[3].append(cells[cell.y][cell.x + i])

        variants = list(filter(lambda var: len(var) == lenght, variants))

        return random.choice(variants)

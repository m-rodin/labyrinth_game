from inputs.iinput import IInput
from game.interfaces.icellobject import ICellObject
from game.interfaces.iplayer import IPlayer

import random

class Bear(IPlayer):
    def __init__(self, x: int, y: int, index: int = 0):
        self.x = x
        self.y = y
        self.index = index

    def addObject(self, object: ICellObject): pass

    def canFinish(self) -> bool:
        return False

    def isAlive(self) -> bool:
        return True

    def interact(self, anotherPlayer: IPlayer, game):
        anotherPlayer.spendLife(1)

        cell = game.labyrinth.getCell(anotherPlayer.x, anotherPlayer.y)
        directions = cell.getPossibleDirections()
        direction = random.choice(directions)

        cell.go(anotherPlayer, direction)

    def interactBack(self, anotherPlayer: IPlayer, game):
        self.interact(anotherPlayer, game)

    def spendLife(self, count: int): pass
        
    def getName(self, short = False) -> str:
        name = "B" if short else "Bear"
        return name + str(self.index)

    def getNextAction(self, input: IInput):
        action, direction = "go", [random.choice(["up", "down", "left", "right"])]

        print(input.prefix + action + " " + direction[0])
        return action, direction

    def dump(self) -> dict:
        return {
            'x': self.x,
            'y': self.y,
            'index': self.index
        }

    @staticmethod
    def load(data):
        return Bear(data['x'], data['y'], data['index'])

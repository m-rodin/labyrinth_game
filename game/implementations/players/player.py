from inputs.iinput import IInput
from game.interfaces.icellobject import ICellObject
from game.interfaces.iplayer import IPlayer

class Player(IPlayer):
    def __init__(self, x: int, y: int, lives: int = 2, index: int = 0):
        self.x = x
        self.y = y
        self.lives = lives
        self.index = 0

        self.objects = []

    def addObject(self, object: ICellObject):
        self.objects.append(object)

    def canFinish(self) -> bool:
        return len(self.objects) > 0

    def isAlive(self) -> bool:
        return self.lives > 0

    def interact(self, anotherPlayer: IPlayer, game): pass

    def interactBack(self, anotherPlayer: IPlayer, game): pass

    def spendLife(self, count: int):
        self.lives -= 1

    def getName(self, short = False) -> str:
        name = "P" if short else "Player"
        return name + str(self.index)

    def getNextAction(self, input: IInput):
        return input.get()

    def dump(self) -> dict:
        return {
            'x': self.x,
            'y': self.y,
            'lives': self.lives,
            'index': self.index,
            'objects': [obj.id for obj in self.objects]
        }

    @staticmethod
    def load(data, objects: dict):
        player = Player(data['x'], data['y'], data['lives'], data['index'])

        for objectId in data['objects']:
            object = objects[objectId]
            player.addObject(object)
            
        return player

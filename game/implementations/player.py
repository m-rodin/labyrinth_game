from game.interfaces.icellobject import ICellObject

class Player:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

        self.objects = []

    def addObject(self, object: ICellObject):
        self.objects.append(object)

    def canFinish(self) -> bool:
        return len(self.objects) > 0

    def dump(self) -> dict:
        return {
            'x': self.x,
            'y': self.y,
            'objects': [obj.id for obj in self.objects]
        }

    @staticmethod
    def load(data, objects: dict):
        player = Player(data['x'], data['y'])

        for objectId in data['objects']:
            object = objects[objectId]
            player.addObject(object)
            
        return player

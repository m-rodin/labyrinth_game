
import json
from random import randrange

from implementations.labyrinth.factory import LabyrinthFactory
from implementations.labyrinth.labyrinth import Labyrinth
from implementations.player import Player

class Game:
    def __init__(self):
        self.labyrinth = None
        self.players = []
        self.active_index = None
        self.is_started = False

    def nextPlayer(self):
        if not self.is_started:
            return None
        self.active_index = (self.active_index + 1) % len(self.players)        
        return self.players[self.active_index]

    def start(self, size: int, players_count: int = 1):
        factory = LabyrinthFactory(size=size)

        players = []
        for _ in range(players_count):
            player = Player(randrange(size), randrange(size))
            players.append(player)

        self.labyrinth = factory.create()
        self.players = players
        self.active_index = 0
        self.is_started = True

    def load(self, filename: str):
        with open(filename, 'r') as file:
            data = json.load(file)

        labyrinth = Labyrinth.load(data['labyrinth'])
        players = [Player.load(player, labyrinth.objects) for player in data['players']]

        self.labyrinth = labyrinth
        self.players = players
        self.is_started = data['is_started']
        self.active_index = data['active_index']

    def save(self, filename: str):
        data = {
            'labyrinth': self.labyrinth.dump(),
            'players': [player.dump() for player in self.players],
            'is_started': self.is_started,
            'active_index': self.active_index
        }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

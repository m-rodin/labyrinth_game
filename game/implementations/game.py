
import json
from random import randrange
from typing import List

from game.implementations.labyrinth.factory import LabyrinthFactory
from game.implementations.players.factory import PlayersFactory
from game.implementations.players.player import Player

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

    def drop(self, player):
        index = self.players.index(player)
        self.players.remove(player)

        if index < self.active_index:
            self.active_index -= 1

    def hasAcitivePlayers(self):
        for player in self.players:
            if isinstance(player, Player):
                return True
        return False

    def start(self, labyrinth_factory: LabyrinthFactory, players_factory: PlayersFactory):
        self.labyrinth = labyrinth_factory.create()
        self.players = players_factory.create()
        self.active_index = -1
        self.is_started = True

    def load(self, filename: str):
        with open(filename, 'r') as file:
            data = json.load(file)

        self.labyrinth = LabyrinthFactory.load(data['labyrinth'])
        self.players = PlayersFactory.load(data['players'], self.labyrinth.objects)
        self.is_started = data['is_started']
        self.active_index = data['active_index']

    def save(self, filename: str):
        data = {
            'labyrinth': LabyrinthFactory.dump(self.labyrinth),
            'players': PlayersFactory.dump(self.players),
            'is_started': self.is_started,
            'active_index': self.active_index
        }

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

from random import shuffle, randrange
from typing import List

from game.interfaces.iplayer import IPlayer

from game.implementations.players.player import Player
from game.implementations.players.bear import Bear

class PlayersFactory:
    def __init__(self, players_count: int, bears_count: int, labyrinth_size: int):
        self.players_count = players_count
        self.bears_count = bears_count
        self.labyrinth_size = labyrinth_size

    def create(self) -> List[IPlayer]:
        players = []

        for i in range(self.players_count):
            player = Player(randrange(self.labyrinth_size), randrange(self.labyrinth_size), index=i)
            players.append(player)

        for i in range(self.bears_count):
            bear = Bear(randrange(self.labyrinth_size), randrange(self.labyrinth_size), index=i)
            players.append(bear)

        return players

    @staticmethod
    def load(data, objects):
        players = []
        for playerData in data:
            if playerData['class'] == "Player":
                players.append(Player.load(playerData, objects))
            if playerData['class'] == "Bear":
                players.append(Bear.load(playerData))
        return players

    @staticmethod
    def dump(players: List[IPlayer]):
        data = []
        for player in players:
            playerData = player.dump()
            playerData['class'] = type(player).__name__
            
            data.append(playerData)
        return data

from abc import ABCMeta, abstractmethod
from game.interfaces.icellobject import ICellObject
from inputs.iinput import IInput

class IPlayer(metaclass=ABCMeta):

    @abstractmethod
    def addObject(self, object: ICellObject): pass

    @abstractmethod
    def canFinish(self) -> bool: pass

    @abstractmethod
    def isAlive(self) -> bool: pass

    @abstractmethod
    def interact(self, anotherPlayer, game): pass

    @abstractmethod
    def interactBack(self, anotherPlayer, game): pass

    @abstractmethod
    def spendLife(self, count: int): pass

    @abstractmethod
    def getName(self, short = False) -> str: pass

    @abstractmethod
    def getNextAction(self, input: IInput): pass
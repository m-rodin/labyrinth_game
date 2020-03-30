from abc import ABCMeta, abstractmethod

class ICellObject(metaclass=ABCMeta):

    @abstractmethod
    def activate(self, player, game): pass

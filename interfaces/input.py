from typing import Tuple, List
from abc import ABCMeta, abstractmethod

class IInput(metaclass=ABCMeta):

    @abstractmethod
    def get(self) -> Tuple[str, List[str]]: pass

from typing import Tuple, List

from inputs.iinput import IInput

from game.implementations import Game

from actions.exceptions import InvalidAction
from actions.interfaces.iaction import IAction

class CommandLineInput(IInput):

    def __init__(self, game: Game, commands: List[str]):
        self.game = game
        self.available_commands = commands

    def get(self) -> Tuple[str, List[str]]:
        user_input = input(self._get_prefix())
        return self._parse(user_input)

    def _get_prefix(self) -> str:
        if not self.game.is_started:
            return "Input: "
        return "Player{}: ".format(self.game.active_index + 1)

    def _parse(self, command: str) -> Tuple[str, List[str]]:
        clear_input = command.replace("  ", " ").lower()
        input_parts = clear_input.split(" ")
        input_parts = list(filter(lambda x: x.strip() != "", input_parts))

        if (not input_parts) or (input_parts[0] == ""):
            raise InvalidAction("unknown command")

        if input_parts[0] not in self.available_commands:
            raise InvalidAction("unknown command")

        return input_parts[0], input_parts[1:]

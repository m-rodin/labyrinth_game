from typing import Tuple, List

from inputs.iinput import IInput
from actions.exceptions import InvalidAction

class CommandLineInput(IInput):

    def __init__(self, commands: List[str]):
        self.available_commands = commands
        self.prefix = "Input: "

    def get(self) -> Tuple[str, List[str]]:
        user_input = input(self.prefix)
        return self._parse(user_input)

    def _parse(self, command: str) -> Tuple[str, List[str]]:
        clear_input = command.replace("  ", " ").lower()
        input_parts = clear_input.split(" ")
        input_parts = list(filter(lambda x: x.strip() != "", input_parts))

        if (not input_parts) or (input_parts[0] == ""):
            raise InvalidAction("unknown command")

        if input_parts[0] not in self.available_commands:
            raise InvalidAction("unknown command")

        return input_parts[0], input_parts[1:]


from implementations.actions import CreateGameAction, ExitGameAction, LoadGameAction, PrintAction
from implementations.actions import  SaveGameAction, MovePlayerAction, SkipStepAction
from implementations.game import Game
from implementations.cli_input import CommandLineInput

if __name__ == '__main__':
    actions = {
        'start': CreateGameAction(),
        'quit': ExitGameAction(),
        'load': LoadGameAction(),
        'save': SaveGameAction(),
        'go': MovePlayerAction(),
        'skip': SkipStepAction(),
        'print': PrintAction()
    }

    game = Game()
    input = CommandLineInput(game, commands=actions.keys())

    while True:
        try:
            action_alias, args = input.get()

            player = game.nextPlayer()
            result = actions[action_alias].do(args, game, player)
            
            if result.message:
                print(result.message)
            if result.is_finish:
                break
        except Exception as ex:
            print("error:", ex)

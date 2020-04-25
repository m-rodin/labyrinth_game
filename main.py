from actions.implementations import CreateGameAction, ExitGameAction, LoadGameAction, PrintAction
from actions.implementations import  SaveGameAction, MovePlayerAction, SkipStepAction

from game.implementations import Game
from inputs.cli_input import CommandLineInput

if __name__ == '__main__':
    init_actions = {
        'start': CreateGameAction(),
        'quit': ExitGameAction(),
        'load': LoadGameAction(),
    }

    in_game_actions = {
        'quit': ExitGameAction(),
        'load': LoadGameAction(),
        'save': SaveGameAction(),
        'go': MovePlayerAction(),
        'skip': SkipStepAction(),
        'print': PrintAction()
    }

    actions = {**init_actions, **in_game_actions}

    game = Game()
    init_input = CommandLineInput(commands=init_actions.keys())
    player_input = CommandLineInput(commands=in_game_actions.keys())

    prefix = ""
    current_player = None

    while True:
        try:
            if not game.is_started:
                action_alias, args = init_input.get()
            else:
                prefix = current_player.getName() + ": "
                player_input.prefix = prefix
                
                action_alias, args = current_player.getNextAction(player_input)

            result = actions[action_alias].do(args, game, current_player)
            
            if result.message:
                print(prefix + result.message + "\n")
            if result.is_finish:
                break

            for p in game.players:
                if not p.isAlive():
                    print("Game: " + p.getName() + " RIP.\n")
                    game.drop(p)

            if not game.hasAcitivePlayers():
                print("The End \n")
                break

            if result.step_completed:
                current_player = game.nextPlayer()

        except Exception as ex:
            print(prefix + "error,", ex, "\n")

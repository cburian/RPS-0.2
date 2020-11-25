"""
Rock, Paper, Scissors v1.0

Plays a game of Rock, Paper, Scissors (RPS)
The only initial input is a file with the rules

Is able to play multiple types of RPS:
    - RPS-3 (Rock, Paper, Scissors)
    - RPS-5 (Rock, Paper, Scissors, Lizard, Spock)
    - RPS-7

Objectives:
    - make functions do 1 thing
    - document every function with docstrings
    - use exception handling in player inputs
    -

TODO:
    1: enter username
    2: be able to play vs another player
    3: choose game
    4: unlock games
    5: add unicode lock character
    6: keep score
    7: add statistics
    8: keep track of rounds / game / matches
    9: record games / matches
    10: add rules for other RPS games (9, 11, 15, 25, 101)
    11: make it MVC
    12: implement classes for players

"""
import random


def get_available_games() -> list:
    """Returns a list of files (game rules) in 'Rules' directory

    Returns:
        game_files (list(str)): list of strings with name of
                    files in the 'Rules' directory
                    ex: ['RPS-3.txt', 'RPS-5.txt', 'RPS-7.txt', ... ]

    """

    import os

    game_files = os.listdir('Rules/')
    return sorted(game_files)


def print_available_games(game_files: list):
    """Prints the lists of available games

    Args:
         game_files (list(str)): list of strings with name of
                    files in the 'Rules' directory
                    ex: ['RPS-3.txt', 'RPS-5.txt', 'RPS-7.txt', ... ]

    """

    print()
    print('Available games:')
    for index, game in enumerate(game_files):
        print(f'({index + 1}) {game[:-4]}')


def choose_game(game_files: list) -> str:
    """Ask user to choose a game from the list of files with game rules.
    Returns file name for chosen game.

    Args:
        game_files (list(str)): list of strings with name of
                    files in the 'Rules' directory
                    ex: ['RPS-3.txt', 'RPS-5.txt', 'RPS-7.txt', ... ]

    Returns:
        chosen_game (str): string with the name of the file
                    ex: 'RPS-3.txt'

    """

    while True:
        try:
            choice = int(input(f'Choose a game (1 to {len(game_files)}): '))
            assert choice in [x for x in range(1, len(game_files) + 1)]

        except (AssertionError, ValueError):
            print('Please choose on of the options above!')

        else:

            chosen_game = game_files[choice - 1]
            return chosen_game


def extract_rules(game_file_name: str) -> str:
    """Function to extract game rules from txt file.

    Args:
        game_file_name (str): string with the name of the file
                    ex: 'RPS-3.txt'

    Returns:
        rules (str): - string with game rules
                    Ex.: 'Rock breaks scissors, \nscissors cuts paper,
                    \npaper covers rock'

    """

    game_file_name = 'Rules/' + game_file_name
    with open(game_file_name) as f:
        data = f.readlines()
    rules = ''.join(data)

    return rules


def print_rules(rules: str):
    """Prints the rules of the games

    Args:
         rules (str): - string with game rules
                    Ex.: 'Rock breaks scissors, \nscissors cuts paper,
                    \npaper covers rock'

    """

    print()
    print('--- Game Rules: ---')
    print(rules)


def get_components_dict(rules: str) -> tuple:
    """Creates a dictionary from the game rules string

    Takes in rules (str) and extracts a dictionary with
        keys   = tuple(winner(str), looser(str))
        values = rule ex: "Rock breaks scissors"
                ex: {('rock', 'paper') : 'Rock breaks scissors'}

    Args:
        rules (str): - rules of the game
                ex: 'Rock breaks scissors, \n
                    scissors cuts paper, \n
                    paper covers rock'

    Return:
        components (list): - all the components of the game
                ex: ['rock', 'paper', 'scissors')]

        win_dic (dict): - wining dictionary - with the following form:
                {(winner, looser) : rule}
                ex: {('rock', 'paper') : 'Rock breaks scissors'}

    """
    components = set()
    win_dic = {}

    rules_list = rules.split(', \n')
    for rule in rules_list:
        strong_component = rule.split(' ')[0].lower()
        weak_component = rule.split(' ')[-1].lower()

        if strong_component not in components:
            components.add(strong_component)

        if (strong_component, weak_component) not in win_dic.keys():
            win_dic[(strong_component, weak_component)] = rule

    return list(components), win_dic


def print_options(components: list):
    """ Prints the options to choose from.

    Args:
        components (list): - game options (components)
                    ex: ['rock', 'paper', etc.]

    """
    print()
    print('Available options: ')
    for index, k in enumerate(components):
        print(f'({index + 1}) {k}')


def computer_choice(options: list) -> str:
    """Randomly chooses one component from the list

    Args:
         options (list): - list of game options
                    ex: ['rock', 'paper', etc.]

    Returns:
        npc_choice (str): - npc choice
                    ex: 'rock'

    """

    npc_choice = random.choice(options)
    return npc_choice


def playable_choice(options: list) -> str:
    """Randomly chooses one component from the list

    Args:
         options (list): - list of game options
                    ex: ['rock', 'paper', etc.]

    Returns:
        human_choice (str): - playable character choice
                    ex: 'rock'

    """

    while True:
        try:
            choice = int(input(f'\nYour choice: '))
            assert choice in [x for x in range(1, len(options) + 1)]

        except (AssertionError, ValueError):
            print('Please choose on of the options above!')

        else:

            human_choice = options[choice - 1]
            return human_choice


def determine_result(h_choice: str, npc_choice: str,
                     win_dic: dict) -> tuple:
    """Determines the winner of a RPS round

    Args:
        h_choice (str): - human answer
                ex: 'rock'

        npc_choice (str): - npc answer
                ex: 'scissors'

        win_dic (dict): - winning dictionary - with the following form:
                {(winner, looser) : rule}
                ex: {('rock', 'paper') : 'Rock breaks scissors'}

    Returns:
        winner (str / None): - the winning choice
                             - can be: - str: 'rock' - rock won
                                       - None:       - draw

        winning_rule (str / None): - the rule explaining the win
                                   - can be: - str: 'Rock breaks scissors'
                                             - None: draw

    """
    if h_choice != npc_choice:

        if (h_choice, npc_choice) in win_dic.keys():
            winner = h_choice
            winning_rule = win_dic[(h_choice, npc_choice)]
        else:
            winner = npc_choice
            winning_rule = win_dic[(npc_choice, h_choice)]
        return winner, winning_rule

    return None, None


def prt_msg(message: str, border: str = '-'):
    """Applies border to message - for important messages

    todo: make this into a decorator
    """
    print(border * len(message))
    print(message)
    print(border * len(message))


def print_outcome(winner: str, winning_rule: str,
                  player_1: str, player_2: str):
    """Prints the outcome of the round

    Args:
        winner (str / None): - the winning choice
                             - can be: - str: 'rock' - rock won
                                       - None:       - draw

        winning_rule (str / None): - the rule explaining the win
                                   - can be: - str: 'Rock breaks scissors'
                                             - None: draw

        player_1 (str): - player choice
                    ex: 'rock'

        player_2 (str): - player choice
                    ex: 'rock'

    """

    if not winner:
        prt_msg('Draw!', '=')
    else:
        if player_1 == winner:
            msg = f'You win! {winning_rule}'
        elif player_2 == winner:
            msg = f'You lose! {winning_rule}'
        prt_msg(msg, '=')


def play_round(rules: str):
    comp, win_d = get_components_dict(rules)

    print_options(comp)

    human = playable_choice(comp)
    pc = computer_choice(comp)

    winner, winning_rule = determine_result(human, pc, win_d)
    print_outcome(winner, winning_rule, human, pc)


def play_game():
    # 1 - Print available games:
    available_games = get_available_games()
    print_available_games(available_games)
    game_file_name = choose_game(available_games)

    # 2 - Print game rules:
    rules = extract_rules(game_file_name)
    print_rules(rules)

    # 3 - Play round(s):

    play_round(rules)

    while True:
        try:
            another_round = input('\nPlay another round? Y/N: ').lower()
            assert another_round in ['y', 'n']

            if another_round == 'n':
                break

        except AssertionError:
            print('Please chose YES or NO (Y/N)!')

        else:
            play_round(rules)


if __name__ == '__main__':
    play_game()

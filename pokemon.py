                  #
import random     # import random module
import requests   # install the requests library using pip command line: pip install requests, then import requests
import time       # Project Extended - import time module to use the time.sleep() function within the game


def random_pokemon():
    # *REQUIRED* Generate a random number between 1 and 151 to use as the Pokemon ID number
    # Used a range of 1 - 200 to give the player a bigger selection of random Pokemon that could be selected
    pokemon_number = random.randint(1, 200)
    # *REQUIRED* Using the Poke API get a Pokemon based on its ID number
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    # *REQUIRED* Create a dictionary that contains the returned Pokemon's name, id, height and weight
    # Project Extended - Use extra stats from the PokeAPI:
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defense': pokemon['stats'][2]['base_stat'],
        'speed': pokemon['stats'][5]['base_stat'],
            }


def get_player_pokemon(chosen_pokemon):
    # This function is used within the following code - line 131. player_pokemon = get_player_pokemon(player_choice)
    # this is needed to access the player_choice Pokemon stats
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(chosen_pokemon)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defense': pokemon['stats'][2]['base_stat'],
        'speed': pokemon['stats'][5]['base_stat'],
    }


def start_game():
    # Project Extended - Included some styling and '♡' emojis:
    # using ANSI(American National Standards Institute) escape codes directly to change the color of text
    # example → print("\33[97m\33[105m WORD HERE \33[0m ") - [97m - text colour, [105m - background colour, \33[0m - end
    print("")
    print("♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡")
    print("♡                                    ♡")
    print("♡  \33[97m\33[105mCODE FIRST GIRLS: PYTHON & APPS \33[0m  ♡")
    print("♡                                    ♡")
    print("♡            GROUP TWO:              ♡")
    print("♡       ♡ MELISSA & IRENE ♡          ♡")
    print("♡                                    ♡")
    print("♡             PROJECT:               ♡")
    print("♡        POKEMON TOP TRUMPS          ♡")
    print("♡                                    ♡")
    print("♡       ♡  USING pokeAPI  ♡          ♡")
    print("♡                                    ♡")
    print("♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ ♡ \n")  # \n - for the new line
    print(" \33[97m\33[105m ♡ WELCOME TO OUR TOP TRUMPS GAME ♡ \33[0m\n")
    print("       \33[97m\33[105m ♡♡♡  HOW TO PLAY  ♡♡♡ \33[0m \n          ")
    print("1. You will play against an opponent(computer)")
    print("2. Select your Pokemon")
    print("3. Select your stat")
    print("4. A random pokemon and stat will be selected for your opponent(computer)")
    print("5. The stats are compared")
    print("6. The stat with the highest value wins the game")
    print("7. You will be able to play multiple rounds of the game")
    print("8. The scores will be added up at the end of each game \n")
    # Using the time.sleep() function to add a delay of 2 seconds
    time.sleep(2)

    print("       \33[97m\33[105m ♡♡♡  START GAME  ♡♡♡ \33[0m \n          ")


start_game()


def run():

    # *REQUIRED* Get a random Pokemon for the player, the opponent Pokemon is selected later in the game
    # Project Extended - Get multiple random Pokemon and let the player decide which one that they want to use

    # Project Extended - counter which will increment, to get total score of the game and also the score of multiple rounds played
    win = 0
    lose = 0
    draw = 0

    # *REQUIRED* Get a random Pokemon for the player, the opponent Pokemon is selected later in the game
    # Project Extended - Get multiple random Pokemon and let the player decide which one that they want to use
    # below code makes sure that two different Pokemon are generated, if pokemon_one and pokemon_two are the same then
    # a new pokemon will be generated for pokemon_two

    while True:
        pokemon_one = random_pokemon()
        pokemon_two = random_pokemon()

        if pokemon_one == pokemon_two:
            pokemon_two = random_pokemon()

        print("\33[35m     ♡♡♡ CHOOSE YOUR POKEMON ♡♡♡ \33[0m\n           ")

        print('You can choose from: \n\n\33[35m ♡ {} ♡\33[0m or \33[35m♡ {} ♡ \33[0m\n'.format(pokemon_one['name'].title(), pokemon_two['name'].title()))
        # .title() makes the first character of string capital
        print('Which pokemon do you want to choose?')
        player_choice = input('Enter your Pokemon here → ').lower()
        # .lower() makes the input lowercase
        print('')
        time.sleep(1)

        # If the name is not correct the player is asked to input it again
        # if the wrong name is entered twice it stops the program - added PLEASE ENTER YOUR CHOICE CORRECTLY to try and avoid this
        # need to work of a solution to the above problem
        if player_choice != pokemon_one['name'] and player_choice != pokemon_two['name']:
            print('Invalid input: Try Again!\n')
            print('\33[97m\33[105m ♡♡ PLEASE ENTER YOUR CHOICE CORRECTLY! ♡♡ \33[0m\n')
            player_choice = input('Enter your Pokemon here → ').lower()
            print('\n')
        elif player_choice == pokemon_one['name'] or pokemon_two['name']:
            print('\33[35m You chose: ♡ {} ♡ \33[0m \n\n'.format(player_choice).title())
            time.sleep(1)

        # *REQUIRED* Ask the user which stat they want to use (id, height or weight)
        player_pokemon = get_player_pokemon(player_choice)

        print("      \33[97m\33[105m ♡♡♡ LOADING STATS ♡♡♡ \33[0m \n\n         ")
        print('\33[35m♡♡♡ YOUR STATS ♡♡♡\n')

        print('   name: {} \n     id: {}\n height: {}\n weight: {}'.format(player_pokemon['name'].title(), player_pokemon['id'], player_pokemon['height'], player_pokemon['weight']))
        print(' attack: {}\ndefense: {}\n  speed: {}\33[0m\n'.format(player_pokemon['attack'], player_pokemon['defense'], player_pokemon['speed']))

        print('Which stat do you want to use? - id, height, weight, attack, defense, speed\n')
        # if the wrong name is entered twice it stops the program - added PLEASE ENTER YOUR CHOICE CORRECTLY to try and avoid this
        # need to work of a solution to the above problem
        print('\33[97m\33[105m ♡♡ PLEASE ENTER YOUR CHOICE CORRECTLY! ♡♡ \33[0m\n')
        stat_choice = input('Enter your stat here → ').lower()
        print('')
        time.sleep(1)

        # *REQUIRED* Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
        # PROJECT EXTENDED - Allow the opponent (computer) to choose the stat with the highest value that they would like to use
        opponent_pokemon = random_pokemon()
        # a list stores the stats for the random pokemon chosen for the opponent
        opponent_choice = [opponent_pokemon['id'], opponent_pokemon['height'], opponent_pokemon['weight'], opponent_pokemon['attack'], opponent_pokemon['defense'], opponent_pokemon['speed']]

        # max()returns the item with the highest value (from opponent_choice)
        if opponent_pokemon['id'] == max(opponent_choice):
            opponent_stat_choice = 'id'
        elif opponent_pokemon['height'] == max(opponent_choice):
            opponent_stat_choice = 'height'
        elif opponent_pokemon['weight'] == max(opponent_choice):
            opponent_stat_choice = 'weight'
        elif opponent_pokemon['attack'] == max(opponent_choice):
            opponent_stat_choice = 'attack'
        elif opponent_pokemon['defense'] == max(opponent_choice):
            opponent_stat_choice = 'defense'
        elif opponent_pokemon['speed'] == max(opponent_choice):
            opponent_stat_choice = 'speed'

        opponent_stat = opponent_pokemon[opponent_stat_choice]
        player_stat = player_pokemon[stat_choice]

        # print the chosen pokemon and stats of both the player and the opponent
        print('You chose:\n\n\33[35m♡ Pokemon: {} ♡\n♡ Stat: {} ♡\33[0m\n'.format(player_pokemon['name'].title(), stat_choice))
        print('Your opponent has chosen:\n\n\33[35m♡ Pokemon: {} ♡\n♡ Stat: {} ♡\33[0m\n\n'.format(opponent_pokemon['name'].title(), opponent_stat_choice))
        time.sleep(1)
        print("     \33[97m\33[105m ♡♡♡ LOADING RESULTS ♡♡♡ \33[0m\n\n")
        time.sleep(2)

        # if, elif, else statement to determine the winner of the round and the counter for the score to be added to the correct variable
        if player_stat > opponent_stat:
            win += 1  # Adds 1 to win score at the end of the round
            print("\33[35m  ♡♡♡ CONGRATULATIONS: YOU WON ♡♡♡ \33[0m\n")
            print('\33[35m      ♡ Pokemon: \33[0m {} ♡\n'.format(player_pokemon['name'].title()))
            print('\33[35m      ♡ Stat: \33[0m {} - {} ♡\n'.format(stat_choice, player_stat))
            print("\33[35m  ♡♡♡ CONGRATULATIONS: YOU WON ♡♡♡ \33[0m\n\n")
        elif player_stat < opponent_stat:
            lose += 1  # Adds 1 to lose score at the end of the round
            print("   ⌦ ⌦ ⌦   OPPONENT WINS   ⌫ ⌫ ⌫  ️️ \n")
            print('\33[35m      ♡ Pokemon: \33[0m {} ♡\n'.format(opponent_pokemon['name'].title()))
            print('\33[35m      ♡ Stat: \33[0m {} - {} ♡\n'.format(opponent_stat_choice, opponent_stat))
            print("   ⌦ ⌦ ⌦   OPPONENT WINS   ⌫ ⌫ ⌫  ️️ \n\n")
        else:
            draw += 1  # Adds 1 to draw score at the end of the round
            print("          ♡ IT'S A DRAW ♡ \n\n")
            print('          ♥︎ {}, {}: {} ♥︎')
            print('          ♥︎ {}, {}: {} ♥︎ \n\n')

        # Project extended - allow the player to play multiple rounds
        # Prints the scores after each game and will also show the total scores of multiple games
        print("\33[35m      ♡♡♡♡♡♡♡♡ ♡ ♡ ♡ ♡♡♡♡♡♡♡           ")
        print("      ♡♡\33[0m   PLAYER SCORE   \33[35m♡♡           ")
        print("      ♡♡♡♡♡♡♡♡ ♡ ♡ ♡ ♡♡♡♡♡♡♡  \33[0m\n       ")
        print("  \33[97m\33[105m Win: {} \33[0m  \33[35m Draw: {} \33[0m  \33[47m\33[30m Lose: {} \33[0m\n\n".format(win, draw, lose))

        from datetime import datetime  # Project Extended - import the datetime module to use for recording the game scores in a txt file

        # Project extended - Record scores for the player and stores them in a file
        with open('pokemon.txt', 'r') as pokemon_score:
            pokemon_score.read()
            now = datetime.now()
            score_dt = now.strftime("%d/%m/%Y %H:%M:%S")
            score = ("PLAYER SCORE - {}: \n\n\tWIN: {}  DRAW: {}  LOSE: {}\n".format(score_dt, win, draw, lose))

        with open('pokemon.txt', 'a+') as pokemon_score:
            pokemon_score.write(score + '\n')

        # Project extended - allow the player to play multiple rounds
        play_again = input("Would you like to play again? \nEnter yes or no → ")
        print('\n')

        if play_again == 'yes':
            print("       \33[97m\33[105m  ♡♡♡  NEW GAME  ♡♡♡  \33[0m \n          ")
            time.sleep(1)
            continue   # Continue to the start of the While-loop (line 95), allows the player to play another game
        elif play_again != 'yes':
            print("        ♡♡♡ GAME OVER ♡♡♡ ")
            print("        ♡♡♡ GAME OVER ♡♡♡ ")
            print("        ♡♡♡ GAME OVER ♡♡♡ \n\n\n")
            break  # exit out of the loop


run()

import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z']

def start():
    players = set_players()

    categories = set_categories()

    input('Press <Enter> to start the game')

    while True:
        pick()
        input('Press <Enter> to continue')
        assign_points(players, categories)
        inp = input('Do you wish to continue? (y/n): ')
        if inp == 'n' or inp == 'N':
            break

    print_results(players)


def set_players():
    players = {}
    name = input('Player name (empty to finish): ')

    while name != '':
        players[name] = 0
        name = input('Player name (empty to finish): ')

    return players


def set_categories():
    cats = []
    cat = input('Category (empty to finish): ')

    while cat != '':
        cats.append(cat)
        cat = input('Category (empty to finish): ')

    return cats


def pick():
    if len(letters) > 0:
        i = random.randint(0, len(letters) - 1)
        print('The chosen letter is: ' + letters[i])
        letters.pop(i)


def assign_points(players, categories):
    for i in categories:
        print('Category: ' + i + '\n')
        print('How many points per player?')
        for k, v in players.items():
            inp = input(k + ': ')
            n = 0
            try:
                n = int(inp)
            except:
                pass
            players[k] = v + n
        print()


def print_results(players):
    print('\nThe results are:')
    max = -1
    player = ''
    for i in range(len(players)):
        for k, v in players.items():
            if(v > max):
                max = v
                player = k
        print(str(i + 1) + '- ' + player + ' ' +
              str(players.pop(player)) + 'pts')
        max = -1


start()

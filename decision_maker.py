"""
    Game Descision Tree (for 2 Players)
    Goal:       Decide a weekend/evening activity
    Process:    - each player choose a category
                - play tic tac toe to decide the category
                - each player choose an activity for the chosen category
                - play rock paper scissors to decide the activity
                - have fun doing your fairly decided weekend/evening activity
"""

# add time delay [time.sleep(seconds)]
# class for players-categories-activities - inherit to gaming classes
# add exceptions
# complete tic tac toe

import random
import time
from easygui import passwordbox

dict_cat_act = {"Totally lazy": ["Couchpotato", "Wellness", "Cinema"],
                "Slightly active": ["Meet friends", "Restaurant", "Bar"],
                "Going crazy": ["Barhopping", "Club", "Clubhopping"]}


class Player:
    """
        A class representing a player
    """

    def __init__(self, name):
        self.name = name
        self.category = ""
        self.activity = ""

    def choose_category(self):
        category = input("Choose your preferred category: ")
        self.category = [*dict_cat_act][int(category)-1]

    def choose_activity(self, chosen_category):
        activity = input("Choose your preferred activity: ")
        self.activity = dict_cat_act[chosen_category][int(activity)-1]


class RPS:
    """
        Game rock, paper, scissors!
    """

    def __init__(self, list_of_players):
        self.list_of_players = list_of_players
        self.options = {"R": "Rock", "P": "Paper", "S": "Scissors"}
        self.message = {"tie": "\nYawn it's a tie! Let\'s play again!",
                        "decision": "\nYay {}, you won! Sorry {}, maybe next time..."}

    def decide_winner(self, rps_choices):

        for i in self.list_of_players:
            print("\n{}, you selected: {}".format(i, rps_choices[i]))

        i = self.list_of_players[0]
        j = self.list_of_players[1]

        if rps_choices[i] == rps_choices[j]:
            print(self.message["tie"])
            return 0
        elif (rps_choices[i] == self.options["R"] and rps_choices[j] == self.options["S"])\
                or (rps_choices[i] == self.options["P"] and rps_choices[j] == self.options["R"])\
                or (rps_choices[i] == self.options["S"] and rps_choices[j] == self.options["P"]):
            print(self.message["decision"].format(i, j))
            return i
        else:
            print(self.message["decision"].format(j, i))
            return j

    def play_rps(self):
        rps_choices = {}
        for i in self.list_of_players:
            players_rps_choice = passwordbox("{}, please enter Rock (R), Paper (P) or Scissors (S): ".format(i))
            players_rps_choice = self.options[players_rps_choice.upper()]
            rps_choices[i] = players_rps_choice
        winner = self.decide_winner(rps_choices)
        return winner


class TicTacToe:
    """
        Game Tic Tac Toe
    """

    def __init__(self, list_of_players):
        self.list_of_players = list_of_players
        self.letters = ['', '']
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def draw_board(self):
        print(' 1 | 2 | 3')
        print('   |   |')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('   |   |')
        print('-----------')
        print(' 4 | 5 | 6')
        print('   |   |')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('   |   |')
        print('-----------')
        print(' 7 | 8 | 9')
        print('   |   |')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
        print('   |   |')

    def choose_letters(self):
        self.letters[0] = input("\n{}, please choose a letter: X or O ".format(self.list_of_players[0])).upper()
        # check if input was valid
        while self.letters[0] not in ['X', 'O']:
            self.letters[0] = input("\nPlease try again. Choose a letter: X or O ".format(self.list_of_players[0])).upper()

        # ordering the list of letters
        if self.letters[0] == 'X':
            self.letters[1] = 'O'
        else:
            self.letters[1] = 'X'

    def make_move(self, move, letter):
        # check if input was valid
        while (move not in range(1,10)) or (self.board[move-1] != ' '):
            move = int(input("Please choose an empty field with a number between 1 and 9! "))

        # change board and draw updated version
        self.board[move-1] = letter
        self.draw_board()

    def check_winner(self):
        for l in self.letters:
            i = self.letters.index(l)
            if ((self.board[0] == l and self.board[1] == l and self.board[2] == l)
                or (self.board[3] == l and self.board[4] == l and self.board[5] == l)
                or (self.board[6] == l and self.board[7] == l and self.board[8] == l)
                or (self.board[0] == l and self.board[3] == l and self.board[6] == l)
                or (self.board[1] == l and self.board[4] == l and self.board[7] == l)
                or (self.board[2] == l and self.board[5] == l and self.board[8] == l)
                or (self.board[0] == l and self.board[4] == l and self.board[8] == l)
                or (self.board[2] == l and self.board[4] == l and self.board[6] == l)):
                winner = self.list_of_players[i]
                print("winner is {}".format(winner))
                return winner
            else:
                return 0

    def play_tictactoe(self):
        # show the board and first player select a letter
        self.draw_board()
        self.choose_letters()

        # start playing
        move = input("What is your first move? Choose 1 - 9. ")
        self.make_move(int(move), self.letters[0])
        move = input("Now, it's your turn, {}. Choose a position. ".format(self.list_of_players[1]))
        self.make_move(int(move), self.letters[1])
        for i in range(7):
            j = i % 2
            move = input("Next {}: ".format(self.list_of_players[j]))
            self.make_move(int(move), self.letters[j])

            # check if someone won
            winner = self.check_winner()
            if winner != 0:
                print("Yeah, {} you won!".format(winner))
                break
        return winner


class TossCoin:
    """
        Tossing a coin
    """

    def __init__(self, players):
        self.players = players

    def toss_coin(self):
        starter_dict = {0: ['heads', self.players[0]], 1: ['tails', self.players[1]]}

        # toss a coin
        toss = random.randint(0, 1)

        # select the starter
        starter = starter_dict[toss]
        print("\nOk, the coin shows {}, so {} will start. Let's play Tic Tac Toe.\n"
              .format(starter[0], starter[1]))

        # change order of players
        if not self.players[0] == starter[1]:
            self.players.reverse()

        return self.players


# function to decide the activity (rock paper scissors)
def decide_activity(players_activities):
    act_list = list(players_activities.values())
    list_of_players = list(players_activities.keys())
    if act_list[0] == act_list[1]:
        chosen_activity = act_list[0]
        print("\nYou\'ve chosen the same activity: {}".format(chosen_activity))
    else:
        print("\nYou\'ve chosen different activities: {} and {} "
              "\nLet\'s play Rock, Paper or Scissors to decide.\n".format(act_list[0], act_list[1]))
        winner = RPS(list_of_players).play_rps()
        if winner == 0:
            winner = RPS(list_of_players).play_rps()
        chosen_activity = players_activities[winner]
        print("\nSo, the chosen activity is: {} \nHave fun!!".format(chosen_activity))
    return chosen_activity


# function to decide the category (tic tac toe)
def decide_category(players_categories):
    cat_list = list(players_categories.values())
    players = list(players_categories.keys())

    # check if chosen categories are the same
    if cat_list[0] == cat_list[1]:
        chosen_category = cat_list[0]
        print("\nYou've chosen the same category: {}".format(chosen_category))
    else:
        print("\nYou've chosen different categories: {} and {}.".format(cat_list[0], cat_list[1]))
        time.sleep(0.5)
        print("\nLet's play Tic Tac Toe to decide."
              "\nBut first, we toss a coin to decide who should start. "
              "\nIf the coin shows heads, {} starts. If it lands tails up, then {} is first."
              .format(players[0], players[1]))
        time.sleep(0.5)
        print("...")
        time.sleep(1)

        # toss a coin to decide who should start playing tic tac toe
        players_ordered = TossCoin(players).toss_coin()
        time.sleep(2)

        # playing tic tac toe to decide the category
        winner = TicTacToe(players_ordered).play_tictactoe()
        chosen_category = players_categories[winner]
    return chosen_category


# function to get and store the activity choice
def choose_activities(players, chosen_category):
    players_activities={}
    for i in players:
        print("\n{}, which activity would you prefer? (1) {}, (2) {} or (3) {}"
              .format(i.name, dict_cat_act[chosen_category][0], dict_cat_act[chosen_category][1],
                      dict_cat_act[chosen_category][2]))
        i.choose_activity(chosen_category)
        players_activities[i.name] = i.activity
    return players_activities


# function to get and store the category choice
def choose_categories(players):
    players_categories={}
    for i in players:
        print("\n{}, in which mood are you today? (1) {}, (2) {} or (3) {}"
              .format(i.name, [*dict_cat_act][0], [*dict_cat_act][1], [*dict_cat_act][2]))
        i.choose_category()
        players_categories[i.name] = i.category
    return players_categories


# function to set the players
def set_players():
    player1 = input("Name of Player 1: ")
    player1 = Player(player1)
    player2 = input("Name of Player 2: ")
    player2 = Player(player2)
    return [player1, player2]


if __name__ == '__main__':
    # insert the names of the players
    players = set_players()

    # each player choose a category
    players_categories = choose_categories(players)

    # play tic tac toe to decide the category
    category = decide_category(players_categories)

    # each player choose an activity out of the chosen category
    players_activities = choose_activities(players, category)

    # play rock-paper-scissors to decide finally the activity
    activity = decide_activity(players_activities)

# ------------------------------------------------------------
# Name: Krish Gandhi
# ID: 1621641
# CMPUT 274, Fall 2020
#
# Weekly Exercise #6: Object-Oriented Minimax
#
# Description: An implementation of Minimax AI Algorithm in
#              Tic Tac Toe, using Python.
#              This software is available under GPL license.
#              Author: Clederson Cruz
#              Year: 2017
#              License: GNU GENERAL PUBLIC LICENSE (GPL)
# ------------------------------------------------------------
from math import inf as infinity
from random import choice
from random import seed as randomseed       # Paul Lu
import platform
import time
from os import system


class Board:
    """ Board class is used to hold a tic-tac-toe board object data.
        This inlcudes the updated tic-tac-toe board after each human
        mark (X or O) and computer mark (X or O).

        Functions:
            __init__(self)
            __str__(self)
            __repr__(self)
            player_choice(self)
            get_player_choice(self, player)
            set_player_choice(self, player, mark)
            goes_first(self)
            get_player_val(self, player)
            get_board(self)
            set_board(self, update_board)
            render(self)
            set_move(self, x, y, player)
            valid_move(self, x, y)
            ai_turn(self)
            human_turn(self)
            play_game(self)
    """

    def __init__(self):
        """ Automatically initializes attributes for each Board object
            that is instantiated.

            Arguments:
                None

            Return:
                None
        """
        self.type = str(self.__class__)
        self.inst = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.h_choice = ''  # X or O
        self.c_choice = ''  # X or O
        self.first = ''  # if human is the first
        return

    def __str__(self):
        """ Returns the informal string representation of a Board instance.

            Arguments:
                None

            Return:
                <class '__main__.Board'>
        """
        return(self.type)

    def __repr__(self):
        """ Returns the official string representation of a Board instance.

            Arguments:
                None

            Return:
                (<id> <class '__main__.Board'>), where id is some number
        """
        s = "<%d> %s" % (id(self), self.type)
        return(s)

    def player_choice(self):
        """ Prompts the human to choose X or O to represent their mark on
            the tic-tac-toe board. The computer is represented by the mark
            not choosen by the human.

            Arguments:
                None

            Return:
                None
        """
        # Human chooses X or O to play
        while self.get_player_choice("HUMAN") not in ['O', 'X']:
            try:
                print('')
                mark = input('Choose X or O\nChosen: ').upper()
                self.set_player_choice("HUMAN", mark)

            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

        # Setting computer's choice
        if self.get_player_choice("HUMAN") == 'X':
            self.set_player_choice("COMP", 'O')
        else:
            self.set_player_choice("COMP", 'X')
        return

    def get_player_choice(self, player):
        """ Returns the player's choice (mark, X or O).

            Arguments:
                player: the current player

            Return:
                (self.c_choice if the player is computer, otherwise
                self.h_choice if the player is human)
        """
        if player == "COMP":
            return(self.c_choice)
        elif player == "HUMAN":
            return(self.h_choice)

    def set_player_choice(self, player, mark):
        """ Set the player's choice (mark, X or O).

            Arguments:
                player: the current player
                mark: X or O that represents the player

            Return:
                None (self.c_choice is the mark of the computer,
                self.h_choice is the mark of the human)
        """
        if player == "COMP":
            self.c_choice = mark
        elif player == "HUMAN":
            self.h_choice = mark

    def goes_first(self):
        """ Prompts the human to answer if they would like to go first or not.

            Arguments:
                None

            Return:
                None (self.first = Y if the human wants to go first, otherwise
                self.first = N and the computer goes first)
        """
        # Human may starts first
        clean()
        while self.first != 'Y' and self.first != 'N':
            try:
                self.first = input('First to start?[y/n]: ').upper()
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')
        return

    def get_player_val(self, player):
        """ Returns the value assoicated with the player (computer or
            human).

            Arguments:
                player: the current player

            Return:
                (1 if the player is computer, otherwise -1 if the
                player is human)
        """
        if player == "COMP":
            return(1)
        elif player == "HUMAN":
            return(-1)

    def get_board(self):
        """ Returns the updated tic-tac-toe board (self.inst).

            Arguments:
                None

            Return:
                self.inst
        """
        return(self.inst)

    def set_board(self, update_board):
        """ Updates the tic-tac-toe board (self.inst).

            Arguments:
                update_board: the changed board after a player's turn

            Return:
                None
        """
        self.inst = update_board
        return

    def render(self):
        """
        Print the board on console
        """

        chars = {
            -1: self.get_player_choice("HUMAN"),
            +1: self.get_player_choice("COMP"),
            0: ' '
        }
        str_line = '---------------'

        print('\n' + str_line)
        for row in self.get_board():
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + str_line)

    def set_move(self, x, y, player):
        """
        Set the move on board, if the coordinates are valid
        :param x: X coordinate
        :param y: Y coordinate
        :param player: the current player
        """
        if self.valid_move(x, y):
            update_board = self.get_board()
            update_board[x][y] = player
            self.set_board(update_board)
            return True
        else:
            return False

    def valid_move(self, x, y):
        """
        A move is valid if the chosen cell is empty
        :param x: X coordinate
        :param y: Y coordinate
        :return: True if the self.get_board()[x][y] is empty
        """
        if [x, y] in State().empty_cells(self.get_board()):
            return True
        else:
            return False

    def ai_turn(self):
        """
        It calls the minimax function if the depth < 9,
        else it choices a random coordinate.
        :return:
        """
        depth = len(State().empty_cells(self.get_board()))
        if depth == 0 or State().game_over(self.get_board()):
            return

        clean()
        print(f'Computer turn [{self.get_player_choice("COMP")}]')
        self.render()

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = State().minimax(self.get_board(), depth,
                                   self.get_player_val("COMP"))
            x, y = move[0], move[1]

        self.set_move(x, y, self.get_player_val("COMP"))
        # Paul Lu.  Go full speed.
        # time.sleep(1)

    def human_turn(self):
        """
        The Human plays choosing a valid move.
        :return:
        """
        depth = len(State().empty_cells(self.get_board()))
        if depth == 0 or State().game_over(self.get_board()):
            return

        # Dictionary of valid moves
        move = -1
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        clean()
        print(f'Human turn [{self.get_player_choice("HUMAN")}]')
        self.render()

        while move < 1 or move > 9:
            try:
                move = int(input('Use numpad (1..9): '))
                coord = moves[move]
                can_move = self.set_move(coord[0], coord[1],
                                         self.get_player_val("HUMAN"))

                if not can_move:
                    print('Bad move')
                    move = -1
            except (EOFError, KeyboardInterrupt):
                print('Bye')
                exit()
            except (KeyError, ValueError):
                print('Bad choice')

    def play_game(self):
        """ Plays tic-tac-toe by alternating between the human and computer
            turn until one succeeds in placing three of their marks either
            in a row horizontally, vertically or diagonally, or if the board
            is filled and there has been no winner.

            Arguments:
                None

            Return:
                None (prints "YOU WIN!" if the human wins, or "YOU LOSE"
                if the computer wins, or "DRAW" if no one wins)
        """
        # Main loop of this game
        while len(State().empty_cells(self.get_board())) > 0 and\
           not State().game_over(self.get_board()):
            if self.first == 'N':
                self.ai_turn()
                self.first = ''

            self.human_turn()
            self.ai_turn()

        # Game over message
        if State().wins(self.get_board(), self.get_player_val("HUMAN")):
            clean()
            print(f'Human turn [{self.get_player_choice("HUMAN")}]')
            self.render()
            print('YOU WIN!')
        elif State().wins(self.get_board(), self.get_player_val("COMP")):
            clean()
            print(f'Computer turn [{self.get_player_choice("COMP")}]')
            self.render()
            print('YOU LOSE!')
        else:
            clean()
            self.render()
            print('DRAW!')
        return


class State(Board):
    """ State class is used to check the current state of the tic-tac-toe
        board object. This includes finding the best move for the computer,
        and checking if a win condition is met.

        Functions:
            __init__(self)
            __str__(self)
            __repr__(self)
            get_p_val(Board, player)
            empty_cells(self, current_state)
            evaluate(self, current_state)
            wins(self, current_state, player)
            game_over(self, current_state)
            minimax(self, current_state, depth, player)
    """

    def __init__(self):
        """ Automatically initializes attributes for each State object
            that is instantiated.

            Arguments:
                None

            Return:
                None
        """
        self.type = str(self.__class__)
        return

    def __str__(self):
        """ Returns the informal string representation of a State instance.

            Arguments:
                None

            Return:
                <class '__main__.State'>
        """
        return(self.type)

    def __repr__(self):
        """ Returns the official string representation of a State instance.

            Arguments:
                None

            Return:
                (<id> <class '__main__.State'>), where id is some number
        """
        s = "<%d> %s" % (id(self), self.type)
        return(s)

    # classmethod decorator
    def get_p_val(Board, player):
        """ Returns the value assoicated with the player (computer or
            human) using a classmethod decorator approach. Thus, self
            is not referenced and a Board instance is not instantiated
            when a call to this function is made.

            Arguments:
                player: the current player

            Return:
                (1 if the player is computer, otherwise -1 if the
                player is human)
        """
        return Board.get_player_val(player)

    def empty_cells(self, current_state):
        """
        Each empty cell will be added into cells' list
        :param current_state: the state of the current tic-tac-toe board
        :return: a list of empty cells
        """
        cells = []

        for x, row in enumerate(current_state):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def evaluate(self, current_state):
        """
        Function to heuristic evaluation of state.
        :param current_state: the state of the current tic-tac-toe board
        :return: +1 if the computer wins; -1 if the human wins; 0 draw
        """
        if self.wins(current_state, State().get_p_val("COMP")):
            score = +1
        elif self.wins(current_state, State().get_p_val("HUMAN")):
            score = -1
        else:
            score = 0

        return score

    def wins(self, current_state, player):
        """
        This function tests if a specific player wins. Possibilities:
        * Three rows    [X X X] or [O O O]
        * Three cols    [X X X] or [O O O]
        * Two diagonals [X X X] or [O O O]
        :param current_state: the state of the current tic-tac-toe board
        :param player: a human or a computer
        :return: True if the player wins
        """
        win_state = [
            [current_state[0][0], current_state[0][1], current_state[0][2]],
            [current_state[1][0], current_state[1][1], current_state[1][2]],
            [current_state[2][0], current_state[2][1], current_state[2][2]],
            [current_state[0][0], current_state[1][0], current_state[2][0]],
            [current_state[0][1], current_state[1][1], current_state[2][1]],
            [current_state[0][2], current_state[1][2], current_state[2][2]],
            [current_state[0][0], current_state[1][1], current_state[2][2]],
            [current_state[2][0], current_state[1][1], current_state[0][2]],
        ]
        if [player, player, player] in win_state:
            return True
        else:
            return False

    def game_over(self, current_state):
        """
        This function test if the human or computer wins
        :param current_state: the state of the current tic-tac-toe board
        :return: True if the human or computer wins
        """
        return self.wins(current_state, State().get_p_val("HUMAN")) or\
            self.wins(current_state, State().get_p_val("COMP"))

    def minimax(self, current_state, depth, player):
        """
        AI function that choice the best move
        :param current_state: current state of the tic-tac-toe board
        :param depth: node index in the tree (0 <= depth <= 9),
        but never nine in this case (see ai_turn() function in Board class)
        :param player: a human or a computer
        :return: a list with [the best row, best col, best score]
        """
        if player == State().get_p_val("COMP"):
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.game_over(current_state):
            score = self.evaluate(current_state)
            return [-1, -1, score]

        for cell in self.empty_cells(current_state):
            x, y = cell[0], cell[1]
            current_state[x][y] = player
            score = self.minimax(current_state, depth - 1, -player)
            current_state[x][y] = 0
            score[0], score[1] = x, y

            if player == State().get_p_val("COMP"):
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best


def clean():
    """
    Clears the console
    """
    # Paul Lu.  Do not clear screen to keep output human readable.
    print()
    return

    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def main():
    """ Main function that instantiates one Board object and calls Board
        functions to play tic-tac-toe between the human and the computer.

        Arguments:
            None

        Return:
            None
    """
    # Paul Lu.  Set the seed to get deterministic behaviour for each run.
    #       Makes it easier for testing and tracing for understanding.
    randomseed(274 + 2020)

    clean()

    game1 = Board()
    game1.player_choice()
    game1.goes_first()
    game1.play_game()

    exit()


if __name__ == '__main__':
    main()

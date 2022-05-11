#!/usr/bin/env python3
import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

moves = ['rock', 'paper', 'scissors']


class Player:
    wins = 0
    player_move = ""
    opponent_move = ""

    def move(self):
        return 'rock'

    def learn(self, player_move, opponent_move):
        self.player_move = player_move
        self.opponent_move = opponent_move


class RandomPlayer(Player):  # wild player
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        the_player_input = input("PLEASE CHOOSE: paper, rock OR scissors: ")
        if the_player_input in moves:
            return the_player_input
        else:
            print("INVALID CHOICE! PLEASE CHOOSE AGAIN")
            time.sleep(1)
            self.move()


class ReflectPlayer(Player):
    def move(self):  # basic AI
        if self.opponent_move in moves:
            return self.opponent_move
        else:
            return random.choice(moves)


class CyclePlayer(Player):
    def move(self):  # basic win strategy
        if self.player_move == "rock":
            return "paper"
        elif self.player_move == "paper":
            return "scissors"
        elif self.player_move == "scissors":
            return "rock"
        else:  # wild card
            return random.choice(moves)


def beats(one, two):  # how a move beats the other
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, player1, player2):  # players are initialized
        self.player1 = player1
        self.player2 = player2

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.player1.learn(move1, move2)  # remember opponent's move
        self.player2.learn(move2, move1)
        if beats(move1, move2):  # determines the winner of the round
            self.player1.wins += 1
            time.sleep(1)
            print(f"PLAYER 1 BEATS THE OPPONENT: {self.player1.wins}"
                  f" to {self.player2.wins}")
        elif beats(move2, move1):
            self.player2.wins += 1
            time.sleep(1)
            print(f"PLAYER 2 BEATS THE OPPONENT: {self.player2.wins}"
                  f" to {self.player1.wins}")
        else:
            time.sleep(1)
            print(f"The SAME MOVES! CURRENT POINTS: {self.player1.wins}"
                  f" to {self.player2.wins}")

    def play_game(self):
        print("WELCOME TO THE ROCK PAPER SCISSORS GAME!\n")
        time.sleep(1)
        while True:
            try:
                user_choice = int(input("HOW MANY ROUNDS OF GAME?: "))
            except ValueError:
                print("INVALID! WHOLE NUMBERS PLEASE!")
                continue
            else:
                break
        for round in range(user_choice):
            print(f"ROUND {round+1}:")
            self.play_round()

        print("THE GAME IS OVER!")
        time.sleep(1)
        if self.player1.wins > self.player2.wins:  # the winner of the game
            print(f"PLAYER 1 WINS! WITH THE POINTS {self.player1.wins}"
                  f" to {self.player2.wins}")
        elif self.player1.wins < self.player2.wins:
            print(f"PLAYER 2 WINS! WITH THE POINTS {self.player2.wins}"
                  f" to {self.player1.wins}")
        else:
            print(f"IT's A DRAW. Both PLAYERS "
                  f"HAVE {self.player1.wins} POINTS")
        time.sleep(1)
        # Ask if would like to play again
        playagain = input("WOULD YOU LIKE TO PLAY AGAIN: yes/no \n")
        if playagain == "yes":
            game = Game(HumanPlayer(), ReflectPlayer())
            game.play_game()
        else:
            print("THANK YOU. GOOD BYE!")

if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()

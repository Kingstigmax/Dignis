import random
import sys

class RPS:

    def __init__(self):
        print('Welcome to RPS!')

        self.moves = {'rock': '🪨', 'paper': '🧻', 'scissors': '✂️'}
        self.valid_moves = list(self.moves.keys())

    def play_game(self):
        user_move = input('Rock, Paper, Scissors >> ').lower()

        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()

        ai_move = random.choice(self.valid_moves)
        
        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)
    
    def display_moves(self, user_move, ai_move):
        print('------')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[user_move]}')
        print('------')

    def check_moves(self, user_move, ai_move):
        if user_move == ai_move:
            print('It\'s a tie!')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('User wins!')
        elif user_move == 'scissors' and ai_move == 'paper':
            print('User wins!')
        elif user_move == 'paper' and ai_move == 'rock':
            print('User wins!')
        else:
            print('AI wins!')

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()
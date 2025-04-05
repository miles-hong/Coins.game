import random

class CoinGame:
    def __init__(self, total_coins=30):
        self.total_coins = total_coins
        self.current_coins = total_coins
        self.player_turn = None
    
    def print_status(self):
        print(f"\nCoins remaining: {self.current_coins}")
        print("=" * 20)
    
    def player_move(self):
        while True:
            try:
                move = int(input("How many coins do you want to take (1-3)? "))
                if 1 <= move <= 3 and move <= self.current_coins:
                    return move
                else:
                    print("Invalid move. You can take 1, 2, or 3 coins (and cannot take more than remain).")
            except ValueError:
                print("Please enter a number between 1 and 3.")
    
    def computer_move(self):
        # Optimal strategy: leave a multiple of 4 + 1 (1, 5, 9, 13, etc.)
        remainder = self.current_coins % 4
        if remainder == 1:
            # If we're in a losing position, take a random amount (1-3)
            # In perfect play this shouldn't happen if computer goes first
            move = random.randint(1, min(3, self.current_coins))
        else:
            # Take enough coins to leave a losing position for opponent
            move = (remainder - 1) % 4
            if move == 0:  # When remainder is 0, we want to take 3
                move = 3
        
        move = min(move, self.current_coins)  # Don't take more than available
        print(f"Computer takes {move} coins.")
        return move
    
    def play_round(self, move):
        self.current_coins -= move
        self.player_turn = not self.player_turn
    
    def check_winner(self):
        if self.current_coins == 1:
            # The player who took the last coin loses
            return "Computer" if self.player_turn else "Player"
        return None
    
    def play_game(self):
        print("Welcome to the Coin Game!")
        print("Rules: Take 1-3 coins each turn. Whoever takes the last coin loses.")
        
        # Let player choose to go first or second
        while True:
            choice = input("Do you want to go first? (y/n): ").lower()
            if choice in ['y', 'n']:
                self.player_turn = (choice == 'y')
                break
            print("Please enter 'y' or 'n'.")
        
        # Main game loop
        while self.current_coins > 0:
            self.print_status()
            
            if self.player_turn:
                move = self.player_move()
            else:
                move = self.computer_move()
            
            self.play_round(move)
            winner = self.check_winner()
            if winner:
                self.print_status()
                print(f"\nGame over! {winner} wins!")
                return
        
        # Shouldn't reach here
        print("Game ended in a draw (shouldn't happen with these rules).")

# Start the game
if __name__ == "__main__":
    game = CoinGame()
    game.play_game()
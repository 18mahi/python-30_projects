import os
import time
import random
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform coloring
init(autoreset=True)

# Motivational quotes mapped by 'type' of win or gameplay style
MOTIVATIONAL_QUOTES = [
    "Keep going! Great things take time.",
    "Victory is yours! Believe in your power.",
    "Outstanding play! Your focus shines bright.",
    "You're unstoppable! Keep up the great work.",
    "Amazing strategy! The board bows to you.",
    "You've conquered this round; greatness awaits!",
    "A well-played game! Success is the journey.",
    "Your smart moves inspire creativity and strength.",
    "Keep that spirit alive—tomorrow's win is near!",
    "Your dedication is the real trophy today!"
]

def clear_screen():
    # Clear the terminal screen for *nix and Windows
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_symbol(symbol, player_number):
    # Return colored symbol based on player number
    colors = [Fore.CYAN + Style.BRIGHT, Fore.MAGENTA + Style.BRIGHT]
    if player_number in (1,2):
        return colors[player_number-1] + symbol + Style.RESET_ALL
    else:
        return symbol

def print_board(board, player1_symbol, player2_symbol):
    # Print the Tic-Tac-Toe board with colors and styling
    # Board is a list of 9 elements
    # Player symbols are colored distinctly

    # Helper: map symbol to colored symbol if matched to player symbols
    def map_symbol(s):
        if s == player1_symbol:
            return colored_symbol(s, 1)
        elif s == player2_symbol:
            return colored_symbol(s, 2)
        elif s == ' ':
            return ' '
        else:
            return s

    # Column dividers and lines in subtle blue
    divider = Fore.BLUE + Style.BRIGHT + " | " + Style.RESET_ALL
    line = Fore.BLUE + Style.BRIGHT + "───+───+───" + Style.RESET_ALL

    print("\n" + Fore.YELLOW + Style.BRIGHT + "   Tic-Tac-Toe Board\n" + Style.RESET_ALL)
    print(" " + " " * 2 + map_symbol(board[0]) + divider + map_symbol(board[1]) + divider + map_symbol(board[2]))
    print(line)
    print(" " + " " * 2 + map_symbol(board[3]) + divider + map_symbol(board[4]) + divider + map_symbol(board[5]))
    print(line)
    print(" " + " " * 2 + map_symbol(board[6]) + divider + map_symbol(board[7]) + divider + map_symbol(board[8]))
    print()

def is_winner(board, symbol):
    # Define winning triplets
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False

def is_board_full(board):
    return all(space != ' ' for space in board)

def get_move(player_name, symbol, board):
    while True:
        print(Fore.GREEN + Style.BRIGHT + f"{player_name} ({symbol}), it's your turn." + Style.RESET_ALL)
        move = input(Fore.CYAN + f"Enter your move (1-9): " + Style.RESET_ALL)
        if move.isdigit():
            pos = int(move)
            if 1 <= pos <= 9:
                if board[pos-1] == ' ':
                    return pos-1
                else:
                    print(Fore.RED + "That spot is already taken. Try again!" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid position. Please choose 1 through 9." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid input. Please enter a number from 1 to 9." + Style.RESET_ALL)

def get_player_symbol(player_num, taken_symbols):
    while True:
        symbol = input(Fore.YELLOW + Style.BRIGHT + f"Player {player_num}, choose your symbol (single character, e.g. X, O, @, #): " + Style.RESET_ALL).strip()
        if len(symbol) != 1:
            print(Fore.RED + "Please enter exactly one character." + Style.RESET_ALL)
        elif symbol == ' ':
            print(Fore.RED + "Symbol cannot be a space." + Style.RESET_ALL)
        elif symbol in taken_symbols:
            print(Fore.RED + "Symbol already taken. Choose a different symbol." + Style.RESET_ALL)
        else:
            return symbol

def motivational_quote(move_count):
    # For simplicity, pick a quote randomly but factor in move count (speed of win) for variation
    if move_count <= 5:
        # Quick win, energetic quotes
        quotes = [
            Fore.MAGENTA + Style.BRIGHT + "⚡ Lightning-fast! You're a Tic-Tac-Toe champion!" + Style.RESET_ALL,
            Fore.CYAN + "⚡ Swift and clever! Your moves hit like lightning!" + Style.RESET_ALL,
            Fore.MAGENTA + "⚡ Wow! A speedy victory — unstoppable force!" + Style.RESET_ALL,
            Fore.CYAN + "⚡ Dominating the board in record time!" + Style.RESET_ALL,
        ]
        return random.choice(quotes)
    elif move_count <=7:
        # Medium speed win
        quotes = [
            Fore.BLUE + "✨ Steady and sure, a fine victory indeed!" + Style.RESET_ALL,
            Fore.MAGENTA + "✨ Your strategic brilliance shines through!" + Style.RESET_ALL,
            Fore.CYAN + "✨ Thoughtful moves brought your success!" + Style.RESET_ALL,
            Fore.BLUE + "✨ Excellent gameplay, keep it up!" + Style.RESET_ALL,
        ]
        return random.choice(quotes)
    else:
        # Longer gameplay win
        quotes = [
            Fore.GREEN + "🌟 Persistence pays off! Well done!" + Style.RESET_ALL,
            Fore.YELLOW + "🌟 Every move counts — you nailed it!" + Style.RESET_ALL,
            Fore.GREEN + "🌟 Great game! Victory favors the patient." + Style.RESET_ALL,
            Fore.YELLOW + "🌟 Your resilience is inspiring — congrats!" + Style.RESET_ALL,
        ]
        return random.choice(quotes)

def print_fun_message(message):
    # Print a fun message with styling
    print("\n" + Back.BLUE + Fore.WHITE + Style.BRIGHT + ">>> " + message + " <<<" + Style.RESET_ALL + "\n")

def play_game():
    clear_screen()
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to the Aesthetic Tic-Tac-Toe CLI Game!" + Style.RESET_ALL)
    print("Each player can choose their own symbol (any single character except space).")
    print("Positions on the board are numbered 1 to 9 as below:\n")

    sample_board = [str(i) for i in range(1,10)]
    print_board(sample_board, '', '')

    player1_symbol = get_player_symbol(1, taken_symbols=[])
    player2_symbol = get_player_symbol(2, taken_symbols=[player1_symbol])

    player1_name = Fore.CYAN + Style.BRIGHT + "Player 1" + Style.RESET_ALL
    player2_name = Fore.MAGENTA + Style.BRIGHT + "Player 2" + Style.RESET_ALL
    board = [' '] * 9
    current_player = 1
    move_count = 0

    def loading_animation(text="Processing"):
        for _ in range(3):
            print(text + ".", end='\r', flush=True)
            time.sleep(0.4)
            print(text + "..", end='\r', flush=True)
            time.sleep(0.4)
            print(text + "...", end='\r', flush=True)
            time.sleep(0.4)
        print(" " * (len(text)+3), end='\r')

    while True:
        clear_screen()
        print_board(board, player1_symbol, player2_symbol)
        if current_player == 1:
            pos = get_move(player1_name, colored_symbol(player1_symbol, 1), board)
            board[pos] = player1_symbol
            move_count += 1
            loading_animation()
            if is_winner(board, player1_symbol):
                clear_screen()
                print_board(board, player1_symbol, player2_symbol)
                print_fun_message(f"Congratulations {player1_name} ({colored_symbol(player1_symbol, 1)})! You won!")
                print_fun_message(motivational_quote(move_count))
                break
            current_player = 2
        else:
            pos = get_move(player2_name, colored_symbol(player2_symbol, 2), board)
            board[pos] = player2_symbol
            move_count += 1
            loading_animation()
            if is_winner(board, player2_symbol):
                clear_screen()
                print_board(board, player1_symbol, player2_symbol)
                print_fun_message(f"Congratulations {player2_name} ({colored_symbol(player2_symbol, 2)})! You won!")
                print_fun_message(motivational_quote(move_count))
                break
            current_player = 1

        if is_board_full(board):
            clear_screen()
            print_board(board, player1_symbol, player2_symbol)
            print_fun_message("It's a Tie! Well played both players!")
            break

    # Ask if player wants to play again
    while True:
        again = input(Fore.YELLOW + Style.BRIGHT + "Would you like to play again? (y/n): " + Style.RESET_ALL).strip().lower()
        if again == 'y':
            play_game()
            break
        elif again == 'n':
            print(Fore.GREEN + "\nThanks for playing! Keep having fun!\n" + Style.RESET_ALL)
            time.sleep(1)
            break
        else:
            print(Fore.RED + "Please enter 'y' or 'n'." + Style.RESET_ALL)

if __name__ == "__main__":
    play_game()



# For minmax after each move the algorith should evaluate the result of the move for both maximizing player (X) and minimizing Player (O)
# End Conditions 
    #-> win for X: +1
    #-> win for O: -1
    #-> Draw: 0

# Constants for the players
COMPUTER = "X"
PLAYER = "O"
EMPTY = " "


#-->  _______              __      __              __     __                                __                               
#--> |       \            |  \    |  \            |  \   |  \                              |  \                              
#--> | $$$$$$$\  ______  _| $$_   | $$____        | $$   | $$  ______    ______    _______  \$$  ______   _______    _______ 
#--> | $$__/ $$ /      \|   $$ \  | $$    \       | $$   | $$ /      \  /      \  /       \|  \ /      \ |       \  /       \
#--> | $$    $$|  $$$$$$\\$$$$$$  | $$$$$$$\       \$$\ /  $$|  $$$$$$\|  $$$$$$\|  $$$$$$$| $$|  $$$$$$\| $$$$$$$\|  $$$$$$$
#--> | $$$$$$$\| $$  | $$ | $$ __ | $$  | $$        \$$\  $$ | $$    $$| $$   \$$ \$$    \ | $$| $$  | $$| $$  | $$ \$$    \ 
#--> | $$__/ $$| $$__/ $$ | $$|  \| $$  | $$         \$$ $$  | $$$$$$$$| $$       _\$$$$$$\| $$| $$__/ $$| $$  | $$ _\$$$$$$\
#--> | $$    $$ \$$    $$  \$$  $$| $$  | $$          \$$$    \$$     \| $$      |       $$| $$ \$$    $$| $$  | $$|       $$
#-->  \$$$$$$$   \$$$$$$    \$$$$  \$$   \$$           \$      \$$$$$$$ \$$       \$$$$$$$  \$$  \$$$$$$  \$$   \$$ \$$$$$$$ 


board = [EMPTY] * 9 # 9 because there are nine squares
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def display_board(board):
    # Show each row
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print(f"---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"---------")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

def check_winner(board, print_state): 

    # Check for win scenarios
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != EMPTY:
            winner = board[combo[0]]  # Either PLAYER or COMPUTER won
            if print_state: 
                display_board(board)  # Show the final state of the board
                if winner == PLAYER:
                    print("Congratulations You Won!!! 🎉")
                else:
                    print("Sorry The Computer Won!!! 🎉")
            return True  # Return True to indicate the game is over
    
    # Check if it's a draw (all spots are filled and no winner)
    if EMPTY not in board:
            if print_state:
                display_board(board)
                print("It's a draw!")
            return True  # Return True to indicate the game is over
    
    # The game is still ongoing, no winner and not a draw
    return 

def display_winner(winner):
    if winner == PLAYER:
        display_board(board)
        return print("Congratulations You Won!!! 🎉")
    else: 
        display_board(board)
        return print("Sorry The Computer Won!!! 🎉")



def check_player_input():
    while True: 
        try: 
            player_input = int(input("Enter your move (0-8): "))
            if 0 <= player_input <= 8:
                print("<-------------------->")
                if board[player_input] == EMPTY:
                    return player_input  # Return the valid input
                else:
                    print("That spot is already taken. Try a different move.")
            else:
                print("Invalid Input: Please enter a number between 0 and 8.")
        except ValueError:
            print("Invalid Input. Please enter a valid integer.")


def check_game_mode():
    while True: 
        try: 
            player_input = int(input("Which game mode do you want to play?\n    1) Minimax\n    2) Alpha-Beta Pruning\n"))
            if 1 <= player_input <= 2:
                print("\n****************")
                return player_input
            else:
                print("Invalid Input‼️‼️‼️: Please enter either 1 or 2")
        except ValueError:
            print("Invalid Input. Please enter a valid integer.")



#-->   ______     __                                __                            __ 
#-->  /      \   |  \                              |  \                          |  \
#--> |  $$$$$$\ _| $$_     ______   _______    ____| $$  ______    ______    ____| $$
#--> | $$___\$$|   $$ \   |      \ |       \  /      $$ |      \  /      \  /      $$
#-->  \$$    \  \$$$$$$    \$$$$$$\| $$$$$$$\|  $$$$$$$  \$$$$$$\|  $$$$$$\|  $$$$$$$
#-->  _\$$$$$$\  | $$ __  /      $$| $$  | $$| $$  | $$ /      $$| $$   \$$| $$  | $$
#--> |  \__| $$  | $$|  \|  $$$$$$$| $$  | $$| $$__| $$|  $$$$$$$| $$      | $$__| $$
#-->  \$$    $$   \$$  $$ \$$    $$| $$  | $$ \$$    $$ \$$    $$| $$       \$$    $$
#-->   \$$$$$$     \$$$$   \$$$$$$$ \$$   \$$  \$$$$$$$  \$$$$$$$ \$$        \$$$$$$$                                                                    
#-->  __       __  __            __                                                  
#--> |  \     /  \|  \          |  \                                                 
#--> | $$\   /  $$ \$$ _______   \$$ ______ ____    ______   __    __                
#--> | $$$\ /  $$$|  \|       \ |  \|      \    \  |      \ |  \  /  \               
#--> | $$$$\  $$$$| $$| $$$$$$$\| $$| $$$$$$\$$$$\  \$$$$$$\ \$$\/  $$               
#--> | $$\$$ $$ $$| $$| $$  | $$| $$| $$ | $$ | $$ /      $$  >$$  $$                
#--> | $$ \$$$| $$| $$| $$  | $$| $$| $$ | $$ | $$|  $$$$$$$ /  $$$$\                
#--> | $$  \$ | $$| $$| $$  | $$| $$| $$ | $$ | $$ \$$    $$|  $$ \$$\               
#-->  \$$      \$$ \$$ \$$   \$$ \$$ \$$  \$$  \$$  \$$$$$$$ \$$   \$$               
                                                                                
def minimax(board, depth, is_maximizing, nodes_expanded):
    # PART 1: Check for a winner or draw
    winner = check_winner(board, False)
    if winner == COMPUTER:
        print(f"Computer wins at depth {depth}")
        return 1, nodes_expanded  # Computer wins, return score of 1
    elif winner == PLAYER:
        print(f"Player wins at depth {depth}")
        return -1, nodes_expanded  # Player wins, return score of -1
    elif winner == "Draw":
        print(f"Draw at depth {depth}")
        return 0, nodes_expanded  # It's a draw, return score of 0

    # PART 2: Maximizing or Minimizing
    if is_maximizing: 
        best_score = float('-inf')  # Initialize to negative infinity for maximizing
        for i in range(9):
            if board[i] == EMPTY:
                # Maximizing (Computer's turn)
                board[i] = COMPUTER
                print(f"Maximizing: Trying move {i} at depth {depth}")
                score, nodes_expanded_after_move = minimax(board, depth + 1, False, nodes_expanded + 1)
                board[i] = EMPTY
                best_score = max(score, best_score)
                nodes_expanded = nodes_expanded_after_move  # Update nodes expanded
        return best_score, nodes_expanded
    else:
        best_score = float("inf")  # Initialize to positive infinity for minimizing
        for i in range(9):
            if board[i] == EMPTY:
                # Minimizing (Player's turn)
                board[i] = PLAYER
                print(f"Minimizing: Trying move {i} at depth {depth}")
                score, nodes_expanded_after_move = minimax(board, depth + 1, False, nodes_expanded + 1)
                board[i] = EMPTY
                best_score = min(score, best_score)
                nodes_expanded = nodes_expanded_after_move  # Update nodes expanded
        return best_score, nodes_expanded

def find_the_best_computer_move(board):
    best_score = float("-inf")  # Initialize to negative infinity
    best_move = None            # Initialize best move as None
    total_nodes_expanded = 0

    # 1. First, check if AI can win immediately
    for combo in winning_combinations:
        move = find_winning_move(board, COMPUTER, combo)
        if move is not None:
            print(f"AI can win by moving to {move}")
            return move  # AI should win immediately if possible

    # 2. Block the Player if they are about to win
    for combo in winning_combinations:
        move = find_winning_move(board, PLAYER, combo)
        if move is not None:
            print(f"Blocking player from winning by moving to {move}")
            return move  # Block player from winning

    # 3. Regular Minimax to find the best move
    for i in range(9):
        if board[i] == EMPTY:  # Only consider empty spots
            board[i] = COMPUTER  # Try the move
            score, nodes_expanded_after_move = minimax(board, 0, False, 0)
            board[i] = EMPTY  # Undo the move
            total_nodes_expanded += nodes_expanded_after_move

            # Update the best score and move if the current move is better
            if score > best_score:
                best_score = score
                best_move = i
            print(f"Evaluating move {i}: Score {score}, Best Score {best_score}")

    print(f"Total Nodes Expanded: {total_nodes_expanded}")
    print(f"Best Move Found: {best_move}, Best Score: {best_score}")

    if best_move is None:
        print("Error: AI could not find a valid move.")
        raise ValueError("AI could not find a valid move.")

    return best_move



def play_game():
    while True: 
        #-> step 1 ( show board, and get User Input)
        display_board(board)
        player_move: int = check_player_input()
        board[player_move] = PLAYER

        #-> Step 2: Did Player Win? 
        # Step 2: Check if the player won or if it's a draw
        if check_winner(board, True):
            break
        
        #-> Step 3: determine Computer's move & check if the computer won
        ai_move = find_the_best_computer_move(board)
        board[ai_move] = COMPUTER

        if check_winner(board, True):
            break

#play_game()



#-->   ______   __            __                                     
#-->  /      \ |  \          |  \                                    
#--> |  $$$$$$\| $$  ______  | $$____    ______                      
#--> | $$__| $$| $$ /      \ | $$    \  |      \                     
#--> | $$    $$| $$|  $$$$$$\| $$$$$$$\  \$$$$$$\                    
#--> | $$$$$$$$| $$| $$  | $$| $$  | $$ /      $$                    
#--> | $$  | $$| $$| $$__/ $$| $$  | $$|  $$$$$$$                    
#--> | $$  | $$| $$| $$    $$| $$  | $$ \$$    $$                    
#-->  \$$   \$$ \$$| $$$$$$$  \$$   \$$  \$$$$$$$                    
#-->               | $$                                              
#-->               | $$                                              
#-->                \$$                                              
#-->  _______              __                                        
#--> |       \            |  \                                       
#--> | $$$$$$$\  ______  _| $$_     ______                           
#--> | $$__/ $$ /      \|   $$ \   |      \                          
#--> | $$    $$|  $$$$$$\\$$$$$$    \$$$$$$\                         
#--> | $$$$$$$\| $$    $$ | $$ __  /      $$                         
#--> | $$__/ $$| $$$$$$$$ | $$|  \|  $$$$$$$                         
#--> | $$    $$ \$$     \  \$$  $$ \$$    $$                         
#-->  \$$$$$$$   \$$$$$$$   \$$$$   \$$$$$$$                                                                                 
#-->  _______                                 __                     
#--> |       \                               |  \                    
#--> | $$$$$$$\  ______   __    __  _______   \$$ _______    ______  
#--> | $$__/ $$ /      \ |  \  |  \|       \ |  \|       \  /      \ 
#--> | $$    $$|  $$$$$$\| $$  | $$| $$$$$$$\| $$| $$$$$$$\|  $$$$$$\
#--> | $$$$$$$ | $$   \$$| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$
#--> | $$      | $$      | $$__/ $$| $$  | $$| $$| $$  | $$| $$__| $$
#--> | $$      | $$       \$$    $$| $$  | $$| $$| $$  | $$ \$$    $$
#-->  \$$       \$$        \$$$$$$  \$$   \$$ \$$ \$$   \$$ _\$$$$$$$
#-->                                                       |  \__| $$
#-->                                                        \$$    $$
#-->                                                         \$$$$$$ 
def minimax_AB(board, depth, alpha, beta, is_maximizing, nodes_expanded):
    # PART 1: Check for a winner
    winner = check_winner(board, False)
    if winner == PLAYER:
        return -1, nodes_expanded
    elif winner == COMPUTER:
        return 1, nodes_expanded
    elif winner == "Draw":
        return 0, nodes_expanded
    
    # PART 2: Maximizing or Minimizing
    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = COMPUTER
                # Recurse to find the minimizing turn (player's turn next)
                score, nodes_expanded = minimax_AB(board, depth + 1, alpha, beta, False, nodes_expanded + 1)
                board[i] = EMPTY
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)

                # Prune: If beta <= alpha, no need to explore further
                if beta <= alpha:
                    break  # Beta cutoff
        return best_score, nodes_expanded
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER
                # Recurse to find the maximizing turn (computer's turn next)
                score, nodes_expanded = minimax_AB(board, depth + 1, alpha, beta, True, nodes_expanded + 1)
                board[i] = EMPTY
                best_score = min(score, best_score)
                beta = min(beta, best_score)

                # Prune: If beta <= alpha, no need to explore further
                if beta <= alpha:
                    break  # Alpha cutoff
        return best_score, nodes_expanded



def find_the_best_computer_move_AB(curr_board):
    best_score = float("-inf")
    best_move = None
    nodes_expanded = 0
    alpha = float("-inf")
    beta = float("inf")

    
    # 1. First priority: Check if the Computer can win immediately
    for combo in winning_combinations:
        move = find_winning_move(curr_board, COMPUTER, combo)
        if move is not None:
            print(f"AI can win by moving to {move}")
            return move  # AI should win immediately if possible
        
    # Then, check if Player can win immediately
    for combo in winning_combinations:
        move = find_winning_move(curr_board, PLAYER, combo)
        if move is not None:
            print(f"Block player from winning {move}")
            return move  # Block player from winning
    
    # No immediate win or block, so evaluate each move with minimax
    for i in range(9):
        if curr_board[i] == EMPTY:
            curr_board[i] = COMPUTER
            score, nodes_expanded = minimax_AB(curr_board, 0, alpha, beta, True, nodes_expanded)
            curr_board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    print(f"Nodes expanded with Alpha-Beta Pruning: {nodes_expanded}")
    return best_move



def find_winning_move(board, player, combo):
    # Check if the player is one move away from completing a combo
    if board[combo[0]] == board[combo[1]] == player and board[combo[2]] == EMPTY:
        return combo[2]
    if board[combo[1]] == board[combo[2]] == player and board[combo[0]] == EMPTY:
        return combo[0]
    if board[combo[0]] == board[combo[2]] == player and board[combo[1]] == EMPTY:
        return combo[1]
    return None

def play_game_AB():
    while True: 
        #-> step 1 ( show board, and get User Input)
        display_board(board)
        player_move: int = check_player_input()
        board[player_move] = PLAYER
        
        #-> Step 2: Did Player Win? 
        if check_winner(board, True):
            break
        
        #-> Step 3: determine Computer's move & check if the computer won
        ai_move = find_the_best_computer_move_AB(board)
        board[ai_move] = COMPUTER

        if check_winner(board, True):
            break

def start_game():
    selected_game_mode = check_game_mode()
    if selected_game_mode == 1:
        play_game()
    else: 
        play_game_AB()

start_game()
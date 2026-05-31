# it is used to print pattern for playing this game 
def print_pattern():
    num = 1
    pattern = []
    
    for i in range(13):
    
        line = ""
    
        if i in [0, 4, 8, 12]:
            for j in range(25):
                if j in [0, 8, 16, 24]:
                    line += "+"
                else:
                    line += "-"
    
        else:
            for j in range(25):
    
                if j in [0, 8, 16, 24]:
                    line += "|"
    
                else:
                    if i in [2, 6, 10] and j in [4, 12, 20]:
                        line += str(num)
                        num += 1
                    else:
                        line += " "
    
        pattern.append(line)
        if i == 12:
            return pattern

# update pattern as per user and computer choice
def update_board(position, symbol, pattern):
    position_map = {
        1: (2, 4),
        2: (2, 12),
        3: (2, 20),
        4: (6, 4),
        5: (6, 12),
        6: (6, 20),
        7: (10, 4),
        8: (10, 12),
        9: (10, 20)
    }

    row, col = position_map[position]

    temp = list(pattern[row])
    temp[col] = symbol
    pattern[row] = ''.join(temp)

    return pattern

# checks who is winner
def check_winner(moves):
    moves = set(moves)

    for combo in winning_combinations:
        if combo.issubset(moves):
            return True

    return False

# this function checks board has any empty position 
def board_full(user_moves, comp_moves):
    return len(user_moves) + len(comp_moves) == 9


# main script start from here
user_moves = []
comp_moves = []

# when these combination is matched then game ends with winner name
winning_combinations = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {1, 4, 7},
    {2, 5, 8},
    {3, 6, 9},
    {1, 5, 9},
    {3, 5, 7}
]

pattern = print_pattern()

while True:

    user_input = int(input("Enter position (1-9): "))

    if user_input in user_moves or user_input in comp_moves:
        print("Position already occupied.")
        continue

    user_moves.append(user_input)
    pattern = update_board(user_input, "X", pattern)

    for line in pattern:
        print(line)

    if check_winner(user_moves):
        print("You win!")
        break

    if board_full(user_moves, comp_moves):
        print("Match Draw!")
        break

    while True:
        comp_input = rnd.randint(1, 9)

        if comp_input not in user_moves and comp_input not in comp_moves:
            break

    comp_moves.append(comp_input)
    pattern = update_board(comp_input, "O", pattern)

    print(f"Computer chose {comp_input}")

    for line in pattern:
        print(line)

    if check_winner(comp_moves):
        print("Computer wins!")
        break

    if board_full(user_moves, comp_moves):
        print("Match Draw!")
        break

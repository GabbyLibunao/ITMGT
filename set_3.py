def relationship_status(from_member, to_member, social_graph):
    case_one = to_member in social_graph[from_member]["following"]
    case_two = from_member in social_graph[to_member]["following"]
    if case_one and case_two:
        return("friends")
    elif case_one:
        return("follower")
    elif case_two:
        return("followed by")
    else:
        return("no relationship")
    
def tic_tac_toe(board):
    y = 0
    board_size = len(board)

    for i in range(board_size):
        y = 0
        for x in range(board_size - 1):
            if board[i][x] == board[i][x + 1] and board[i][x] != "":
                y += 1
            else:
                break
        if y == board_size - 1:
            return board[i][0]

    for i in range(board_size):
        y = 0
        for x in range(board_size - 1):
            if board[x][i] == board[x + 1][i] and board[x][i] != "":
                y += 1
            else:
                break
        if y == board_size - 1:
            return board[0][i]

    y = 0
    for i in range(board_size - 1):
        if board[i][i] == board[i + 1][i + 1] and board[i][i] != "":
            y += 1
        else:
            break
    if y == board_size - 1:
        return board[0][0]

    y = 0
    for i in range(board_size - 1):
        if board[i][board_size - 1 - i] == board[i + 1][board_size - 2 - i] and board[i][board_size - 1 - i] != "":
            y += 1
        else:
            break
    if y == board_size - 1:
        return board[0][board_size - 1]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    total_time = 0
    stop = first_stop

    while stop != second_stop:
        for leg in route_map:
            if leg[0] == stop:
                total_time += route_map[leg]['travel_time_mins']
                stop = leg[1]
                break

    return total_time
    
    
    
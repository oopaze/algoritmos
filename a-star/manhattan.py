from math import ceil


def get_right_pos(lenght, num):
    x = lenght if num % lenght == 0 else num % lenght
    
    if num / lenght <= 1:
        y = 1
    elif (num / lenght) % num == 0:
        y = (num / lenght) - 1
    else:
        y = ceil(num / lenght)

    return (x - 1, y - 1)

def get_manhattan_distance(board):
    board_length = len(board)
    distance = 0

    for y, line in enumerate(board):
        for x, item in enumerate(line):
            if item is not None:
                right_x, right_y = get_right_pos(board_length, item)
                distance += abs(right_x - x) + abs(right_y - y)
            
    return distance


if __name__ == "__main__":
    mock_board = [[8, 1, 3], [4, None, 2], [7, 6, 5]]
    manhattan_distance = get_manhattan_distance(mock_board)

    assert manhattan_distance == 10
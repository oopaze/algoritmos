from typing import List

def get_hamilton_distance(board: List[List[int]]):
    one_dimension_board = []
    tiles_in_wrong_position = 0

    for line in board:
        one_dimension_board.extend(line)

    for idx, value in enumerate(one_dimension_board):
        if (idx + 1) != value and value is not None:
            tiles_in_wrong_position += 1
    
    return tiles_in_wrong_position


if __name__ == "__main__":
    mock_board = [[8, 1, 3], [4, None, 2], [7, 6, 5]]
    hamilton_distance = get_hamilton_distance(mock_board)

    assert hamilton_distance == 5

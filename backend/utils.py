combinations_wins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 4, 8],
    [2, 4, 6],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8]
]


def clean_positions(board):
    return [(index + 1) for index in range(0, 9) if board[index] == -1]


def get_segments(board):
    segments = []
    for combination in combinations_wins:
        segment = [board[c] for c in combination]
        segments.append(segment)
    return segments


def a_winner(board):
    # find if exist any winner
    for segment in get_segments(board):
        if all_equals(segment):
            return True
    return False


def all_equals(segment):
    r = list(filter(lambda x: x != -1, segment))
    if len(r) < 3:
        return False
    return segment[0] == segment[1] and segment[1] == segment[2]

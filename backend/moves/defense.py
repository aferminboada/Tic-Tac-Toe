from backend.utils import (
    get_segments,
    combinations_wins,
)
borders = {
      0: [0, 3, 5],
      2: [0, 4, 7],
      6: [4, 5, 2],
      8: [2, 3, 7]
}
mediums = {
      1: [0, 6],
      3: [1, 5],
      5: [1, 7],
      7: [2, 6]
}

middle = {
    4: [1, 3, 4, 6]
}


def move(board, who_aim):
    # search if I can win in one move
    win, value = can_win(board, who_aim)
    if win:
        return value
    return defense_move(board, who_aim)


def can_win(board, who_iam):
    positions = get_positions()
    segments = get_segments(board)
    for pos in positions:
        segment = segments[pos]
        if i_can_win(segment, who_iam):
            return True, combinations_wins[pos][segment.index(-1)]
    return False, None


def defense_move(board, who_iam):
    # if one cell will represent a loss is necessary play this cell
    # if two or more cell represent loss is necessary choose the best cell to play
    cell_loss = get_cell_loss(board, who_iam)
    if len(cell_loss) == 1:
        return cell_loss[0][0]
    # if cell_loss[0][0] == 0:
    #     # search a great place to play
    #     return search_great_move(board, who_iam)
    return decided_loss(cell_loss)


def search_great_move(board, who_iam):
    raise NotImplementedError()


def decided_loss(cell_loss):
    # undefined logic
    # for a while choice the first option
    return cell_loss[0][0]


def get_cell_loss(board, who_iam):
    attack_coefficient = []
    for index in range(9):
        if board[index] == -1:
            # is a empty cell
            coefficient = get_attack_coefficient(board, index, who_iam)
            attack_coefficient.append((index, coefficient))

    # sort the most dangerous cells
    attack_coefficient.sort(key=lambda x: x[1], reverse=True)
    # find only the most dangerous cells
    return list(
        filter(lambda x: x[1] == attack_coefficient[0][1], attack_coefficient)
    )


def get_attack_coefficient(board, key, who_iam):
    coefficient = 0
    segments = get_segments(board)
    if key in borders:
        positions = borders.get(key)
    elif key in mediums:
        positions = mediums.get(key)
    else:
        positions = middle.get(key)

    for pos in positions:
        coefficient += is_under_attack(segments[pos], who_iam)
    return coefficient


def get_positions():
    _positions = set()
    for _, border in borders.items():
        for segment in border:
            _positions.add(segment)

    for _, medium in mediums.items():
        for segment in medium:
            _positions.add(segment)

    return list(_positions)


def is_under_attack(segment, who_iam):
    opponent = 0
    for cell in segment:
        opponent += cell != who_iam and cell != -1

    return opponent == 2


def i_can_win(segment, who_iam):
    i = 0
    for cell in segment:
        i += cell == who_iam
    return i == 2 and (-1 in segment)

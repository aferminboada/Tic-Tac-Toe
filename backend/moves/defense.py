
def defense_move(board):
    # if one cell will represent a loss is necessary play this cell
    # if two or more cell represent loss is necessary choose the best cell to play
    cell_loss = get_cell_loss(board)
    if len(cell_loss) == 1:
        return cell_loss[0]

    return decided_loss(cell_loss)


def decided_loss(cell_loss):
    # undefined logic
    raise NotImplementedError()


def get_cell_loss(board):
    # get if any cell will represent lost the game
    raise NotImplementedError()

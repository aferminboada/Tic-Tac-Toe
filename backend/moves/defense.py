from .move_utils import borders, mediums, middle


def get_attack_coefficient(segments, positions, who_iam):
    coefficient = 0
    for pos in positions:
        coefficient += is_under_attack(segments[pos], who_iam)
    return coefficient


def get_positions(key):
    if key in borders:
        return borders.get(key)
    if key in mediums:
        return mediums.get(key)
    
    return middle.get(key)


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


def i_will_win(segment, who_iam):
    enemy = list(filter(lambda x: x != who_iam and x != -1, segment))
    if len(enemy) > 0:
        return False
    clear = list(filter(lambda x: x == -1, segment))
    return len(clear) > 1

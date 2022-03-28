position = tuple[int, int]


def position_create(row: int, col: int) -> position:
    if not (type(row) is int and row >= 0) or not (type(col) is int and col >= 0):
        raise ValueError('position_create: invalid arguments')
    return row, col


# Tests if position is valid
def position_is(pos) -> bool:
    if type(pos) is tuple and len(pos) == 2 and type(pos[0]) is int and type(pos[1]) is int:
        return True
    else:
        return False


# Returns
def position_row(pos) -> int:
    if position_is(pos):
        return pos[0]
    else:
        raise ValueError("position_row: invalid arguments")


def position_col(pos) -> int:
    if position_is(pos):
        return pos[1]
    else:
        raise ValueError("position_col: invalid arguments")


def position_equal(pos1, pos2) -> bool:
    if position_is(pos1) and position_is(pos2):
        if pos1 == pos2:
            return True
        else:
            return False
    else:
        raise ValueError("position_equal: invalid arguments")


def position_str(pos) -> str:
    if position_is(pos):
        return "(" + str(pos[0]) + ", " + str(pos[1]) + ")"
    else:
        raise ValueError("position_str: invalid arguments")

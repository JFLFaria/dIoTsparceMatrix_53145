# (int, int)
def position_create(row, col):
    if isinstance(row, int) and isinstance(col, int) and row > 0 and col > 0:
        return row, col
    else:
        raise ValueError("position_create: invalid arguments")


# (position)
def position_is(pos):
    return False


# (position)
def position_row(pos):
    return False


def position_col(pos):
    return False


def position_equal(pos, pos2):
    return False


def position_str(pos):
    return False

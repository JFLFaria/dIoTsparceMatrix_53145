from position import *

dok = {}


# (float)
def spmatrix_create(zero: float = 0.0):
    if not (type(zero) is float):
        raise ValueError('position_create: invalid arguments')
    return zero, dok


# (spmatrix)
def spmatrix_is(mat):
    if type(mat) is tuple and type(mat[0]) is float and type[1] is dict:
        return True
    else:
        return False


# (spmatrix)
def spmatrix_zero_get(mat):
    if spmatrix_is(mat):
        return mat[0]
    else:
        raise ValueError("spmatrix_zero_get: invalid arguments")


# (spmatrix, float)
def spmatrix_zero_set(mat, zero):
    if spmatrix_is(mat) and type(zero) is float:
        mat[0] = zero
        for key in mat[1].keys():
            if mat[1][key] == zero:
                del mat[1][key]
    else:
        raise ValueError("spmatrix_zero_set: invalid arguments")


# (spmatrix, position)
def spmatrix_value_get(mat, pos):
    if spmatrix_is(mat) and type(pos) is tuple:
        return mat[1][pos]
    else:
        raise ValueError("spmatrix_value_get: invalid arguments")


# (spmatrix, position, float)
def spmatrix_value_set(mat, pos, val):
    return False  # TODO: Continue


# (spmatrix)
def spmatrix_copy(mat):
    return False


# (spmatrix)
def spmatrix_dim(mat):
    return False


# (spmatrix)
def spmatrix_sparsity(mat):
    return False


# (spmatrix)
def spmatrix_str(mat):
    return False


# (spmatrix)
def spmatrix_row(mat):
    return False


# (spmatrix)
def spmatrix_col(mat):
    return False


# (spmatrix)
def spmatrix_diagonal(mat):
    return False

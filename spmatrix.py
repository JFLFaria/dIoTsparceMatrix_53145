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
    return False


# (spmatrix, float)
def spmatrix_zero_set(mat, zero):
    return False


# (spmatrix, float)
def spmatrix_value_get(mat, pos):
    return False


# (spmatrix, position, float)
def spmatrix_value_set(mat, pos, val):
    return False


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

from position import *


# dok = {}


# (float)
def spmatrix_create(zero: float = 0.0):
    if not (type(zero) is float):
        raise ValueError('position_create: invalid arguments')
    return zero, {}


# (spmatrix)
def spmatrix_is(mat):
    if type(mat) is tuple and type(mat[0]) is float and type(mat[1]) is dict:
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
    if spmatrix_is(mat) and type(pos) is tuple and type(val) is float:
        mat[1][pos] = val
    else:
        raise ValueError("spmatrix_value_set: invalid arguments")


# (spmatrix)
def spmatrix_copy(mat):
    if spmatrix_is(mat):
        new_mat = ()
        # TODO: Copy the elements now
        return new_mat
    else:
        raise ValueError("spmatrix_copy: invalid arguments")


# (spmatrix)
def spmatrix_dim(mat):
    if spmatrix_is(mat):
        if mat[1]:
            max_row = max(mat[1].keys(), key=lambda item: item[0])[0]
            max_col = max(mat[1].keys(), key=lambda item: item[1])[1]
            min_row = min(mat[1].keys(), key=lambda item: item[0])[0]
            min_col = min(mat[1].keys(), key=lambda item: item[1])[1]
            return position_create(min_row, min_col), position_create(max_row, max_col)
        else:
            return ()
    else:
        raise ValueError("spmatrix_dim: invalid arguments")


# (spmatrix)
def spmatrix_sparsity(mat):
    if spmatrix_is(mat):
        dimension = spmatrix_dim(mat)
        if dimension:
            return len(mat[1]) / (dimension[0] * dimension[1])
        else:
            return 0.0
    else:
        raise ValueError("spmatrix_sparsity: invalid arguments")


# (spmatrix)
def spmatrix_str(mat):
    if spmatrix_is(mat):
        mat[1]  # TODO: Tirar duvida (ordenar as posições?)
    else:
        raise ValueError("spmatrix_str: invalid arguments")


# (spmatrix)
def spmatrix_row(mat):
    if spmatrix_is(mat):
        mat[1]  # TODO: Tirar duvida
    else:
        raise ValueError("spmatrix_row: invalid arguments")


# (spmatrix)
def spmatrix_col(mat):
    if spmatrix_is(mat):
        mat[1]  # TODO: Tirar duvida
    else:
        raise ValueError("spmatrix_col: invalid arguments")


# (spmatrix)
def spmatrix_diagonal(mat):
    if spmatrix_is(mat):
        mat[1]  # TODO: Tirar duvida
    else:
        raise ValueError("spmatrix_diagonal: invalid arguments")

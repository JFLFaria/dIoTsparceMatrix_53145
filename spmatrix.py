from position import *
from copy import deepcopy


# dok = {}


# (float)
def spmatrix_create(zero: float = 0.0):
    if not (type(zero) is float or type(zero) is int):
        raise ValueError('position_create: invalid arguments')
    return [float(zero), {}]


# (spmatrix)
def spmatrix_is(mat):
    if type(mat) is list and type(mat[0]) is float and type(mat[1]) is dict:
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
    if spmatrix_is(mat) and (type(zero) is float or type(zero) is int):
        mat[0] = float(zero)
        for key in mat[1].copy():
            if mat[1][key] == float(zero):
                del mat[1][key]
    else:
        raise ValueError("spmatrix_zero_set: invalid arguments")


# (spmatrix, position)
def spmatrix_value_get(mat, pos):
    if spmatrix_is(mat) and type(pos) is tuple:
        return mat[1].get(pos, 0.0)
    else:
        raise ValueError("spmatrix_value_get: invalid arguments")


# (spmatrix, position, float)
def spmatrix_value_set(mat, pos, val):
    if spmatrix_is(mat) and type(pos) is tuple and (type(val) is float or type(val) is int):
        mat[1][pos] = float(val)
    else:
        raise ValueError("spmatrix_value_set: invalid arguments")


# (spmatrix)
def spmatrix_copy(mat):
    if spmatrix_is(mat):
        new_mat = deepcopy(mat)
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

            n_col = position_col(dimension[1]) - position_col(dimension[0]) + 1
            n_row = position_row(dimension[1]) - position_row(dimension[0]) + 1
            n_elements = n_col * n_row

            n_zero = n_elements - len(mat[1])

            return n_zero / n_elements
        else:
            return 1.0
    else:
        raise ValueError("spmatrix_sparsity: invalid arguments")


# (spmatrix)
def spmatrix_str(mat, format):
    response = ""
    if spmatrix_is(mat):
        dimension = spmatrix_dim(mat)
        if dimension:
            row_l = position_row(dimension[0])
            col_l = position_col(dimension[0])
            row_h = position_row(dimension[1])
            col_h = position_col(dimension[1])

            for row in range(row_l, row_h + 1):
                for col in range(col_l, col_h + 1):
                    response += format.format(spmatrix_value_get(mat, position_create(row,
                                                                                      col)))
        return response
    else:
        raise ValueError("spmatrix_str: invalid arguments")


# (spmatrix)
def spmatrix_row(mat, row):
    if spmatrix_is(mat):
        new_mat = spmatrix_create(spmatrix_zero_get(mat))
        dimension = spmatrix_dim(mat)
        if dimension:
            col_l = position_col(dimension[0])
            col_h = position_col(dimension[1])

            for col in range(col_l, col_h + 1):
                pos = position_create(row, col)
                if spmatrix_value_get(mat, pos) != spmatrix_zero_get(mat):
                    spmatrix_value_set(new_mat, pos, spmatrix_value_get(mat, pos))

        return new_mat
    else:
        raise ValueError("spmatrix_row: invalid arguments")


# (spmatrix)
def spmatrix_col(mat, col):
    if spmatrix_is(mat):
        new_mat = spmatrix_create(spmatrix_zero_get(mat))
        dimension = spmatrix_dim(mat)
        if dimension:
            row_l = position_row(dimension[0])
            row_h = position_row(dimension[1])

            for row in range(row_l, row_h + 1):
                pos = position_create(row, col)
                if spmatrix_value_get(mat, pos) != spmatrix_zero_get(mat):
                    spmatrix_value_set(new_mat, pos, spmatrix_value_get(mat, pos))

        return new_mat
    else:
        raise ValueError("spmatrix_col: invalid arguments")


# (spmatrix)
def spmatrix_diagonal(mat):
    if spmatrix_is(mat):
        new_mat = spmatrix_create(spmatrix_zero_get(mat))
        dimension = spmatrix_dim(mat)
        if dimension:
            row_l = position_row(dimension[0])
            row_h = position_row(dimension[1])
            col_l = position_col(dimension[0])
            col_h = position_col(dimension[1])

            if (row_h - row_l) - (col_h - col_l) != 0:
                raise ValueError("spmatrix_diagonal: matrix not square")

            for row, col in zip(range(row_l, row_h + 1), range(col_l, col_h + 1)):
                pos = position_create(row, col)
                if spmatrix_value_get(mat, pos) != spmatrix_zero_get(mat):
                    spmatrix_value_set(new_mat, pos, spmatrix_value_get(mat, pos))

        return new_mat
    else:
        raise ValueError("spmatrix_diagonal: invalid arguments")

import numpy as np


def calculate(list):
    assert len(list) == 9, "The list's length is not 9."

    array = np.reshape(list, (3, 3))
    statistics = dict()
    statistics["max"] = get_max(array)


    return statistics


def get_max(array):
    maxs = list()

    maxs.append(array.max(axis=0)) # y axis
    maxs.append(array.max(axis=1)) # x axis
    maxs.append(array.max()) # flattened

    return  maxs


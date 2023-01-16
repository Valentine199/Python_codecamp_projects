import numpy as np





def calculate(list):
    assert len(list) == 9, "The list's length is not 9."

    array = np.reshape(list, (3, 3))
    statistics = dict()
    statistics["mean"] = get_mean(array)
    statistics["max"] = get_max(array)
    statistics["min"] = get_min(array)
    statistics["sum"] = get_sum(array)


    return statistics


def get_mean(array):
    means = list()

    means.append(array.mean(axis=0))  # Y axis
    means.append(array.mean(axis=1))  # X axis
    means.append(array.mean())  # Flattened

    return means

def get_max(array):
    maxs = list()

    maxs.append(array.max(axis=0)) # y axis
    maxs.append(array.max(axis=1)) # x axis
    maxs.append(array.max()) # flattened

    return  maxs

def get_min(array):
    mins = list()

    mins.append(array.min(axis=0))  # y axis
    mins.append(array.min(axis=1))  # x axis
    mins.append(array.min())  # flattened

    return mins

def get_sum(array):
    sums = list()

    sums.append(array.sum(axis=0))  # y axis
    sums.append(array.sum(axis=1))  # x axis
    sums.append(array.sum())  # flattened

    return sums


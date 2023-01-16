import numpy as np


def calculate(num_list):
    if len(num_list) < 9:
        raise ValueError("List must contain nine numbers")


    array = np.reshape(num_list, (3, 3))
    statistics = dict()

    statistics["mean"] = get_mean(array)
    statistics["variance"] = get_variance(array)
    statistics["standard deviation"] = get_standard_deviation(array)
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


def get_variance(array):
    variances = list()

    variances.append(array.var(axis=0))  # Y axis
    variances.append(array.var(axis=1))  # X axis
    variances.append(array.var())  # Flattened

    return variances


def get_standard_deviation(array):
    stds = list()

    stds.append(array.std(axis=0))  # Y axis
    stds.append(array.std(axis=1))  # X axis
    stds.append(array.std())  # Flattened

    return stds


def get_max(array):
    maxs = list()

    maxs.append(array.max(axis=0))  # y axis
    maxs.append(array.max(axis=1))  # x axis
    maxs.append(array.max())  # flattened

    return maxs


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

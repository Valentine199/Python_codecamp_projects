import numpy as np


def calculate(list):
    assert len(list) == 9, "The list's length is not 9."

    array = np.reshape(list, (3, 3))

    return array

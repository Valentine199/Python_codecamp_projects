# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from typing import Tuple


# I know only the previous step of the enemy

def pattern_seeking(opponent_history: list[str]) -> Tuple[bool, int]:
    # find pattern
    idx = -1
    is_pattern = False
    combined_plays = "".join(opponent_history)
    if len(combined_plays) > 3:
        sample = combined_plays[-3:]

        if combined_plays.count(sample) >= 2:
            is_pattern = True
            idx = combined_plays.index(sample) + len(sample)



    return is_pattern, idx

def avarage_output(opponent_history: list[str]) -> str:
    weight_dict = {
        "R": 1,
        "S": 1,
        "P": 1
    }

    for play in opponent_history:
        if play in weight_dict:
            weight_dict[play] += 1

    n = len(opponent_history)
    idx = 0
    max_chance = 0.0
    for i, weight in enumerate(weight_dict.values()):
        weight_chance = (weight / n)
        if weight_chance > max_chance:
            max_chance = weight_chance
            idx = i

    return list(weight_dict.keys())[idx]

def is_player_affecting(opponent_history: list[str]) -> bool:
    if "R" in opponent_history[-3:] and "S" in opponent_history[-3:] and "P" in opponent_history[-3:]:
        # Player affects outcome

        return True
    return False


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)  # keeps on growing (python thing)

    counter_dict = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    is_pattern, idx = pattern_seeking(opponent_history)

    is_affected = is_player_affecting(opponent_history)

    if not is_pattern:
        probable_enemy_play = avarage_output(opponent_history)

    if is_pattern:
        most_probable_enemy_play = opponent_history[idx]

        # if is_affected:
        #most_probable_enemy_play = counter_dict[most_probable_enemy_play] # I simulate the opponent's counter

    else:
        most_probable_enemy_play = probable_enemy_play

    guess = counter_dict[most_probable_enemy_play]

    # if len(opponent_history) > 2:
    #     guess = opponent_history[-2]

    return guess

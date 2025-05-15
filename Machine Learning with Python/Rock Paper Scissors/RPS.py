# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from typing import Tuple

track = {}
# I know only the previous step of the enemy
# default strat
def pattern_seeking(opponent_history: list[str]) -> Tuple[bool, str]:
    global track
    n = 3
    combined_plays = "".join(opponent_history)
    if len(combined_plays) > n:
        input = combined_plays[-n:]
        lookback = combined_plays[-(n+1):]

        if lookback in track:
            track[lookback] += 1
        else:
            track[lookback] = 1

        possible = [input + "R", input + "P", input + "S"]

        for i in possible:
            if not i in track:
                track[i] = 0

        enemy_str = max(possible, key=lambda inp: track[inp])
        enemy_move = enemy_str[-1]

        return True, enemy_move

    return False, ''

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)  # keeps on growing (python thing)

    counter_dict = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    is_pattern, enemy_play = pattern_seeking(opponent_history)



    if not is_pattern:
        probable_enemy_play = 'R'

    if is_pattern:
        most_probable_enemy_play = enemy_play
    else:
        most_probable_enemy_play = probable_enemy_play

    guess = counter_dict[most_probable_enemy_play]

    # if len(opponent_history) > 2:
    #     guess = opponent_history[-2]

    return guess

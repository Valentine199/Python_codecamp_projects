import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **balls):
        self.contents = Hat.unpack_balls(balls)

    @staticmethod
    def unpack_balls(balls):
        contents = list()
        for key in balls:
            for i in range(balls[key]):
                contents.append(key)

        return contents

    def draw(self, num_draws):
        drawn = list()
        copy_content = copy.copy(self.contents)
        if num_draws <= len(copy_content):
            # doesn't seem so random
            for i in range(num_draws):
                j = random.randrange(0, len(copy_content))
                drawn.append(self.contents[j])
                del copy_content[j]

            return drawn
        else:
            return self.contents

# hat, dictionary, int, int


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for i in range(num_experiments):
        good = True
        returned_balls = turn2dictionary(hat.draw(num_balls_drawn))
        for key in expected_balls:
            if key not in returned_balls or expected_balls[key] > returned_balls[key]:
                good = False
        if good:
            num_success += 1

    return num_success/num_experiments


def turn2dictionary(list2turn):
    made_dictionary = dict()
    for part in list2turn:
        made_dictionary[part] = made_dictionary.get(part, 0) + 1

    return made_dictionary

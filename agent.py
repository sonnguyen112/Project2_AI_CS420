import random


class Agent():
    def __init__(self):
        self.__is_win = False
        self.__pos = self.__set_init_pos()
        self.__hint_list = []

    def __set_init_pos(self, map):
        # Add code
        x = random.randint(0, map.size()-1)
        y = random.randint(0, map.size()-1)
        while (map[y][x][-1] == '0' or map[x][y][-1] == 'M' or map[y][x][-1] == 'P'):
            x = random.randint(0, map.size()-1)
            y = random.randint(0, map.size()-1)
        return (x, y)

    def get_pos(self):
        return self.__pos

    def check_hint(hint):
        # Add code
        return True

    def is_win(self):  # Use to check whether agent win
        return self.__is_win

    def action(self, hint):
        # Add code to agent choose action
        return ["The agent moves 2 steps to the north and SMALL SCAN", "The agent moves 4 steps to the north and SMALL SCAN"]

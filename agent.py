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

    def is_win(self):  # Use to check whether agent win
        return self.__is_win

    def check_hint(hint):
        # Add code
        return True

    def determine_treasure_location(self, hint, map):
        pass

    def move_small_scan(self, hint):
        pass

    def only_move(self, hint):
        pass

    def stay_large_scan(self, hint, map):
        y = self.get_pos()[0]
        x = self.get_pos()[1]

        for x_ in range(x-2, x+3):
            for y_ in range(y-2, y+3):
                if (0 <= x_ < len(map) and 0 <= y_ < len(map)):
                    if map[x_][y_][-1] == 'P':
                        self.__is_win = True

    def Teleport(self, hint, map):
        pass

    def cal_distance():
        pass

    def action(self, hint, map):
        tempt_treasure_location = self.determine_treasure_location(
            self, hint, map)
        current_row, current_col = self.get_pos()
        treasure_row, treasure_col = tempt_treasure_location
        # Add code to agent choose action
        if
        return ["The agent moves 2 steps to the north and SMALL SCAN", "The agent moves 4 steps to the north and SMALL SCAN"]

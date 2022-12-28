import random
import map_of_game
import math


class Agent():
    def __init__(self, map):
        self.__is_win = False
        self.__pos = self.__set_init_pos(map)
        self.__hint_list_true = []
        self.is_first_turn = True
        self.__virtual_treasure = (0, 0)
        self.is_know_pirate_pos = False
        self.__pirate_pos = (0, 0)

    def __set_init_pos(self, map):
        # Add code
        x = random.randint(0, len(map)-1)
        y = random.randint(0, len(map)-1)
        while (map[y][x][-1] == '0' or map[x][y][-1] == 'M' or map[y][x][-1] == 'P'):
            x = random.randint(0, len(map)-1)
            y = random.randint(0, len(map)-1)
        return (y, x)

    def get_pos(self):
        return self.__pos

    def is_win(self):  # Use to check whether agent win
        return self.__is_win

    def check_hint(hint, game_map):
        # Add code
        return True

    def determine_treasure_location_init(self, hint, game_map):
        if hint["id"] == 1:
            obtain_list = []
            for i in range(len(game_map)-1):
                for j in range(len(game_map)-1):
                    if (game_map[i][j] not in hint['val'] and game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P'):
                        obtain_list.append((i, j))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)

        if hint["id"] == 2:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 3:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 4:
            obtain_list = []
            for i in range(len(game_map)-1):
                for j in range(len(game_map)-1):
                    if (game_map[i][j] not in hint['val'] and game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P'):
                        obtain_list.append((i, j))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 5:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 6:
            obtain_list = []
            for i in range(len(game_map)-1):
                for j in range(len(game_map)-1):
                    if (game_map[i][j] not in hint['val'] and game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P'):
                        obtain_list.append((i, j))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 7:
            obtain_list = []
            for i in range(len(game_map)-1):
                for j in range(len(game_map)-1):
                    if (game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P'):
                        obtain_list.append((i, j))
            self.__hint_list_true.append()
            return self.__pos
        if hint["id"] == 8:
            if "row" not in hint["val"] or "col" not in hint["val"]:
                if "row" in hint["val"]:
                    valid_list = []
                    for i in range(1, len(game_map) - 2):
                        if game_map[hint["val"]["row"]][i] != 0 and game_map[hint["val"]["row"]][i][-1] != "M" and game_map[hint["val"]["row"]][i][-1] != "P":
                            valid_list.append((hint["val"]["row"], i))
                    self.__hint_list_true.append(valid_list)
                    return random.choice(valid_list)
                else:
                    valid_list = []
                    for i in range(1, len(game_map) - 2):
                        if game_map[i][hint["val"]["col"]] != 0 and game_map[i][hint["val"]["col"]][-1] != "M" and game_map[i][hint["val"]["col"]][-1] != "P":
                            valid_list.append((i, hint["val"]["col"]))
                    self.__hint_list_true.append(valid_list)
                    return random.choice(valid_list)
            else:
                self.__hint_list_true.append(
                    [(hint["val"]["row"], hint["val"]["col"])])
                return (hint["val"]["row"], hint["val"]["col"])
        if hint["id"] == 9:
            obtain_list = []
            if "row" not in hint["val"] or "col" not in hint["val"]:
                if "row" in hint["val"]:
                    for i in range(len(game_map)-1):
                        for j in range(len(game_map)-1):
                            if (game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P' and i != hint["val"]["row"]):
                                obtain_list.append((i, j))
                elif "col" in hint["val"]:
                    for i in range(len(game_map)-1):
                        for j in range(len(game_map)-1):
                            if (game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P' and j != hint["val"]["col"]):
                                obtain_list.append((i, j))
            else:
                for i in range(len(game_map)-1):
                    for j in range(len(game_map)-1):
                        if (game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P' and i != hint["val"]["row"] and j != hint["val"]["col"]):
                            obtain_list.append((i, j))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 10:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 11:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 12:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 13:
            obtain_list = []
            for i in range(len(game_map)-1):
                for j in range(len(game_map)-1):
                    if (game_map[i][j] not in hint['val'] and game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P'):
                        obtain_list.append((i, j))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 14:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)
        if hint["id"] == 15:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            self.__hint_list_true.append(obtain_list)
            return random.choice(obtain_list)

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

    def is_change_virtual_treasure(self, current_obtain_list):
        if self.__virtual_treasure not in current_obtain_list:
            return True
        return False

    def determine_treasure_location_normal(self, hint, game_map, num_action_rest):
        if hint["id"] == 1:
            obtain_list = []
            for i in range(len(game_map)-1):
                for j in range(len(game_map)-1):
                    if (game_map[i][j] not in hint['val'] and game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P'):
                        obtain_list.append((i, j))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 2:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 3:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 4:
            obtain_list = []
            for i in range(len(game_map)-1):
                for j in range(len(game_map)-1):
                    if (game_map[i][j] not in hint['val'] and game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P'):
                        obtain_list.append((i, j))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 5:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 6:
            obtain_list = []
            for i in range(len(game_map)-1):
                for j in range(len(game_map)-1):
                    if (game_map[i][j] not in hint['val'] and game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P'):
                        obtain_list.append((i, j))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 7:
            obtain_list = self.__hint_list_true.copy()
            if hint['val'] == 'agent':
                for i in obtain_list:
                    if math.sqrt((i[0]-self.__pos[0])**2 + (i[1]-self.__pos[1])**2) > math.sqrt(((i[0]-self.__pirate_pos[0])**2 + (i[1]-self.__pirate_pos[1])**2)):
                        obtain_list.remove(i)
            else:
                for i in obtain_list:
                    if math.sqrt((i[0]-self.__pos[0])**2 + (i[1]-self.__pos[1])**2) < math.sqrt(((i[0]-self.__pirate_pos[0])**2 + (i[1]-self.__pirate_pos[1])**2)):
                        obtain_list.remove(i)
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 8:
            if "row" not in hint["val"] or "col" not in hint["val"]:
                if "row" in hint["val"]:
                    valid_list = []
                    for i in range(1, len(game_map) - 2):
                        if game_map[hint["val"]["row"]][i] != 0 and game_map[hint["val"]["row"]][i][-1] != "M" and game_map[hint["val"]["row"]][i][-1] != "P":
                            valid_list.append((hint["val"]["row"], i))
                    if self.is_change_virtual_treasure(valid_list) == True:
                        if self.check_hint(hint, game_map):
                            num_action_rest = num_action_rest-1
                            self.__hint_list_true.append(valid_list)
                            self.__hint_list_true = set.intersection(
                                *map_of_game(set, self.__hint_list_true))
                            self.__virtual_treasure = random.choice(
                                self.__hint_list_true)
                    return self.__virtual_treasure
                else:
                    valid_list = []
                    for i in range(1, len(game_map) - 2):
                        if game_map[i][hint["val"]["col"]] != 0 and game_map[i][hint["val"]["col"]][-1] != "M" and game_map[i][hint["val"]["col"]][-1] != "P":
                            valid_list.append((i, hint["val"]["col"]))
                    if self.is_change_virtual_treasure(valid_list) == True:
                        if self.check_hint(hint, game_map):
                            num_action_rest = num_action_rest-1
                            self.__hint_list_true.append(valid_list)
                            self.__hint_list_true = set.intersection(
                                *map_of_game(set, self.__hint_list_true))
                            self.__virtual_treasure = random.choice(
                                self.__hint_list_true)
                    return self.__virtual_treasure
            else:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = [
                        (hint["val"]["row"], hint["val"]["col"])]
                    self.__virtual_treasure = (
                        hint["val"]["row"], hint["val"]["col"])
                return self.__virtual_treasure
        if hint["id"] == 9:
            obtain_list = []
            if "row" not in hint["val"] or "col" not in hint["val"]:
                if "row" in hint["val"]:
                    for i in range(len(game_map)-1):
                        for j in range(len(game_map)-1):
                            if (game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P' and i != hint["val"]["row"]):
                                obtain_list.append((i, j))
                elif "col" in hint["val"]:
                    for i in range(len(game_map)-1):
                        for j in range(len(game_map)-1):
                            if (game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P' and j != hint["val"]["col"]):
                                obtain_list.append((i, j))
            else:
                for i in range(len(game_map)-1):
                    for j in range(len(game_map)-1):
                        if (game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P' and i != hint["val"]["row"] and j != hint["val"]["col"]):
                            obtain_list.append((i, j))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 10:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 11:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 12:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 13:
            obtain_list = []
            for i in range(len(game_map)-1):
                for j in range(len(game_map)-1):
                    if (game_map[i][j] not in hint['val'] and game_map[i][j][-1] != '0' and game_map[i][j][-1] != 'M' and game_map[i][j][-1] != 'P'):
                        obtain_list.append((i, j))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 14:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 15:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.check_hint(hint, game_map):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true.append(obtain_list)
                    self.__hint_list_true = set.intersection(
                        *map_of_game(set, self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
            return self.__virtual_treasure

    def teleport(self, hint, map):
        pass

    def cal_distance():
        pass

    def receive_hint(self, hint, map, num_action_rest):
        if self.is_first_turn:
            self.__virtual_treasure = self.determine_treasure_location_init(
                hint, map)
            self.is_first_turn = False
        else:
            self.determine_treasure_location_normal(hint, map, num_action_rest)

    def A_start_find_way(self, map):
        pass

    def action(self, hint, map):
        num_action_rest = 2
        self.receive_hint(self, hint, map, num_action_rest)
        self.A_start_find_way(map)

        # Add code to agent choose action
        return ["The agent moves 2 steps to the north and SMALL SCAN", "The agent moves 4 steps to the north and SMALL SCAN"]


# map_generator = map.MapGenerateTool()
# map = map_generator.generate_map(16, 4).get_map()
# agent = Agent(map)
# print(agent.get_pos())
# print(map[agent.get_pos()[0]][agent.get_pos()[1]])

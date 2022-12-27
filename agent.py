import random
import map_of_game
import math
import numpy as np
import heapq
import operator

class Agent():
    def __init__(self, map):
        self.__is_win = False
        self.__pos = self.__set_init_pos(map)
        self.__hint_list_true = []
        self.is_first_turn = True
        self.__virtual_treasure = self.__set_init_pos(map)
        self.is_know_pirate_pos = False
        self.__pirate_pos = (0, 0)

    def __set_init_pos(self, map):
        # Add code
        x = random.randint(0, len(map)-1)
        y = random.randint(0, len(map)-1)
        while (map[y][x][-1] == '0' or map[y][x][-1] == 'M' or map[y][x][-1] == 'P'):
            x = random.randint(0, len(map)-1)
            y = random.randint(0, len(map)-1)
        return (y, x)

    def get_pos(self):
        return self.__pos

    def get_virtual_treasure(self):
        return self.__virtual_treasure

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


    def only_move(self, hint):
        pass

    def small_scan(self,map):
        y = self.get_pos()[0]
        x = self.get_pos()[1]

        for x_ in range(x-1, x+2):
            for y_ in range(y-2, y+3):
                if (0 <= x_ < len(map) and 0 <= y_ < len(map)):
                    if map[x_][y_][-1] == 'P':
                        self.__is_win = True

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

    def heuristic(self, a, b):
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    def A_start_find_way(self, game_map,direction):
        map_tempt = np.array(game_map)
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        close_set = set()
        came_from = {}
        gscore = {self.__pos: 0}
        fscore = {self.__pos: self.heuristic(
            self.__pos, self.__virtual_treasure)}
        oheap = []
        heapq.heappush(oheap, (fscore[self.__pos], self.__pos))
        while oheap:
            current = heapq.heappop(oheap)[1]
            if current == self.__virtual_treasure:
                data = []
                while current in came_from:
                    data.append(current)
                    direction.append(tuple(map(lambda i, j: i - j, came_from[current], current)))
                    current = came_from[current]
                return data
            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + \
                    self.heuristic(current, neighbor)
                if 0 <= neighbor[0] < map_tempt.shape[0]:
                    if 0 <= neighbor[1] < map_tempt.shape[1]:
                        if map_tempt[neighbor[0]][neighbor[1]][-1] == '0' or map_tempt[neighbor[0]][neighbor[1]][-1] == 'M':
                            continue
                    else:
                        continue
                else:
                    continue
                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue
                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + \
                        self.heuristic(neighbor, self.__virtual_treasure)
                    heapq.heappush(oheap, (fscore[neighbor], neighbor))
            
        return False


    def action(self, hint, map):
        num_action_rest = 2
        self.receive_hint(self, hint, map, num_action_rest)
        if self.__pos == self.__virtual_treasure:
                self.stay_large_scan   
                num_action_rest = 1 
        direction = []
        way_to_treasure = self.A_start_find_way(map,direction)
        if way_to_treasure != False :
            for i in range(len(direction)):
                sum_of_direction = 1
                if direction[i] == direction[i+1]:
                    sum_of_direction += 1
                else:
                    if num_action_rest > 0 :
                        if self.__pos == self.__virtual_treasure:
                                self.stay_large_scan   
                                num_action_rest = num_action_rest-1
                        else: 
                            if sum_of_direction<=2:
                                self.__pos=way_to_treasure[sum_of_direction]
                                self.small_scan(map)
                                num_action_rest=num_action_rest-1
                            else :
                                self.__pos=way_to_treasure[sum_of_direction]
                                num_action_rest=num_action_rest-1
                     
        # for j in way_to_treasure:
        #     for i in direction:
        #         if [sum(tup) for tup in zip(i, self.__pos)] == j

        # Add code to agent choose action
        # return ["The agent moves 2 steps to the north and SMALL SCAN", "The agent moves 4 steps to the north and SMALL SCAN"]


map_generator = map_of_game.MapGenerateTool()
map_of_game = map_generator.generate_map(16, 4)
agent = Agent(map_of_game.get_map())
direction = []
print(agent.A_start_find_way(map_of_game.get_map(),direction))
print(direction)
my_dict = {i:direction.count(i) for i in direction}
print(my_dict)
print(agent.get_pos())
print(agent.get_virtual_treasure())
print(map_of_game)


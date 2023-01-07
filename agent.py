import random
import map_of_game
import math
import numpy as np
import heapq
from pirate import Pirate

random.seed(3)
class Agent():
    def __init__(self, init_pos, map, turn_pirate_reveal, turn_pirate_free,num_region):
        self.__is_win = False
        self.__pos = init_pos
        self.__hint_list_true = []
        self.is_first_turn = True
        self.__virtual_treasure = init_pos
        self.is_know_pirate_pos = False
        self.__pirate_pos = None
        self.turn_pirate_free_agent_know = turn_pirate_free
        self.__hint_list_init = []
        self.__scan = []
        self.turn_teleport = 1
        self.first_turn_check_hint =[]
        for i in range(len(map)):
            for j in range(len(map)):
                    self.__hint_list_init.append((i, j))
        self.action_list = []
        self.__pirate = Pirate(map, turn_pirate_reveal,
                               turn_pirate_free, self.__pos,num_region)

    def __set_init_pos(self, map):
        # Add code
        x = random.randint(0, len(map)-1)
        y = random.randint(0, len(map)-1)
        while (map[x][y][-1] == '0' or map[x][y][-1] == 'M' or map[x][y][-1] == 'P'):
            x = random.randint(0, len(map)-1)
            y = random.randint(0, len(map)-1)
        return (x, y)

    def get_pos(self):
        return self.__pos

    def get_virtual_treasure(self):
        return self.__virtual_treasure

    def is_win(self):  # Use to check whether agent win
        return self.__is_win

    def set_pirate_pos(self, pos):
        self.__pirate_pos = pos

    def intersection(self, lst1, lst2):
        tup1 = map(tuple, lst1)
        tup2 = map(tuple, lst2)
        return list(map(list, set(tup1).intersection(tup2)))

    def determine_treasure_location_init(self, hint, game_map):
        if hint["id"] == 1:
            obtain_list = []
            for i in range(len(game_map)):
                for j in range(len(game_map)):
                    if ((i, j) in hint["val"] and game_map[i][j][-1] != '0' ):
                        obtain_list.append((i, j))
            self.first_turn_check_hint += obtain_list
            self.__hint_list_true = (list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
            
            return random.choice(self.__hint_list_true)

        if hint["id"] == 2:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if obtain_list == []:
                self.__hint_list_true = (list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
                return random.choice(self.__hint_list_true)
            self.__hint_list_true += (obtain_list)
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
            return random.choice(obtain_list)
        if hint["id"] == 3:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if obtain_list == []:
                self.__hint_list_true = (list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
                return random.choice(self.__hint_list_true)
            self.__hint_list_true += (obtain_list)
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
            return random.choice(obtain_list)
        if hint["id"] == 4:
            obtain_list = []
            for i in range(len(game_map)):
                for j in range(len(game_map)):
                    if ((i, j) in hint["val"] and game_map[i][j][-1] != '0' ):
                        obtain_list.append((i, j))
            self.__hint_list_true = (
                list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
            self.first_turn_check_hint = obtain_list
            return random.choice(self.__hint_list_true)
        if hint["id"] == 5:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if obtain_list == []:
                self.__hint_list_true = (list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
                return random.choice(self.__hint_list_true)
            self.__hint_list_true += (obtain_list)
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
            return random.choice(obtain_list)
        if hint["id"] == 6:
            obtain_list = []
            for i in range(len(game_map)):
                for j in range(len(game_map)):
                    if ((i, j) in hint["val"] and game_map[i][j][-1] != '0' ):
                        obtain_list.append((i, j))
            self.__hint_list_true = (
                list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
            self.first_turn_check_hint = obtain_list
            return random.choice(self.__hint_list_true)
        if hint["id"] == 7:
            obtain_list = self.__hint_list_init.copy()

            for i in obtain_list:
                if math.sqrt((i[0]-self.__pos[0])**2 + (i[1]-self.__pos[1])**2) > math.sqrt(((i[0]-self.__pirate_pos[0])**2 + (i[1]-self.__pirate_pos[1])**2)):
                    obtain_list.remove(i)

        
            self.__hint_list_true += (obtain_list)
            self.__virtual_treasure = random.choice(
                self.__hint_list_true)
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
                  
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 8:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if obtain_list == []:
                self.__hint_list_true = (list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
                return random.choice(self.__hint_list_true)
            self.__hint_list_true += (obtain_list)
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
            return random.choice(obtain_list)
        if hint["id"] == 9:
            obtain_list = []
            for i in range(len(game_map)):
                for j in range(len(game_map)):
                    if ((i, j) in hint["val"] and game_map[i][j][-1] != '0' ):
                        obtain_list.append((i, j))
            self.__hint_list_true = (
                list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
            self.first_turn_check_hint = obtain_list
            return random.choice(self.__hint_list_true)
        if hint["id"] == 10:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if obtain_list == []:
                self.__hint_list_true = (
                list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
                return random.choice(self.__hint_list_true)
            self.__hint_list_true += (obtain_list)
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
            return random.choice(obtain_list)
        if hint["id"] == 11:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][0] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if obtain_list == []:
                self.__hint_list_true = (list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
                return random.choice(self.__hint_list_true)
            self.__hint_list_true += (obtain_list)
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
            return random.choice(obtain_list)
        if hint["id"] == 12:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if obtain_list == []:
                self.__hint_list_true = (list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
                return random.choice(self.__hint_list_true)
            self.__hint_list_true += (obtain_list)
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
            return random.choice(obtain_list)
        if hint["id"] == 13:
            obtain_list = []
            for i in range(len(game_map)):
                for j in range(len(game_map)):
                    if ((i, j) in hint["val"] and game_map[i][j][-1] != '0' ):
                        obtain_list.append((i, j))
            self.__hint_list_true = (
                list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
            self.first_turn_check_hint = obtain_list
            return random.choice(self.__hint_list_true)
        if hint["id"] == 14:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))

            if obtain_list == []:
                self.__hint_list_true = (list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
                return random.choice(self.__hint_list_true)
            self.__hint_list_true += (obtain_list)
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
            return random.choice(obtain_list)
        if hint["id"] == 15:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))

            if obtain_list == []:
                self.__hint_list_true = (list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
                return random.choice(self.__hint_list_true)

          

            self.__hint_list_true = obtain_list
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
            print("obtain_list")
            print(obtain_list)
            print("__hint_list_true")
            print(self.__hint_list_true)
            print("first_turn_check_hint")
            print(self.first_turn_check_hint)
            return random.choice(obtain_list)
        if hint["id"] == 16:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))

            if obtain_list == []:
                self.__hint_list_true = (list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_init)))
                return random.choice(self.__hint_list_true)
            self.__hint_list_true = obtain_list
            self.first_turn_check_hint +=  list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0', self.__hint_list_init))
            return random.choice(obtain_list)

    def only_move(self, hint):
        pass

    def small_scan(self, game_map):
        y = self.get_pos()[1]
        x = self.get_pos()[0]
        obtain_list = []
        for x_ in range(x-1, x+2):
            for y_ in range(y-1, y+2):
                if (0 <= x_ < len(game_map) and 0 <= y_ < len(game_map)):
                    if game_map[x_][y_][-1] == 'T':
                        self.__is_win = True
                    if game_map[x_][y_][-1] != '0':
                        obtain_list.append((x_, y_))
                    
        if self.__is_win != True:
            self.__hint_list_true = list(filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' , self.__hint_list_true))
        self.__scan.append(obtain_list)

    def stay_large_scan(self, hint, map):
        y = self.get_pos()[1]
        x = self.get_pos()[0]
        obtain_list = []
        for x_ in range(x-2, x+3):
            for y_ in range(y-2, y+3):
                if (0 <= x_ < len(map) and 0 <= y_ < len(map)):
                    if map[x_][y_][-1] == 'T':
                        self.__is_win = True
                    if map[x_][y_][-1] != '0':
                        obtain_list.append((x_, y_))
        if self.__is_win != True:
            self.__hint_list_true = list(filter(lambda x: x not in obtain_list and map[x[0]][x[1]][-1] != '0' , self.__hint_list_true))
        self.__scan.append(obtain_list)

    def is_change_virtual_treasure(self, current_obtain_list):
        if self.__virtual_treasure not in current_obtain_list:
            return True
        return False

    def determine_treasure_location_normal(self, hint, game_map, num_action_rest,action_infor):
        if hint["id"] == 1:
            obtain_list = []
            for i in range(len(game_map)):
                for j in range(len(game_map)):
                    if ((i, j) in hint["val"] and game_map[i][j][-1] != '0' ):
                        obtain_list.append((i, j))
            if self.is_change_virtual_treasure(obtain_list) == False:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })

            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 2:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 3:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', hint['val']))

            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 4:
            obtain_list = []
            for i in range(len(game_map)):
                for j in range(len(game_map)):
                    if ((i, j) in hint["val"] and game_map[i][j][-1] != '0' ):
                        obtain_list.append((i, j))
            if self.is_change_virtual_treasure(obtain_list) == False:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 5:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' , hint['val']))
            print("obtain_list")
            print(obtain_list)
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    print("hintlisttrue 5")
                    print(self.__hint_list_true)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 6:
            obtain_list = []
            for i in range(len(game_map)):
                for j in range(len(game_map)):
                    if ((i, j) in hint["val"] and game_map[i][j][-1] != '0' ):
                        obtain_list.append((i, j))
            if self.is_change_virtual_treasure(obtain_list) == False:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]][x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 7:
            obtain_list = self.__hint_list_true.copy()
            if self.__pirate(hint) == True:
                for i in obtain_list:
                    if (math.sqrt((i[0]-self.__pos[0])**2 + (i[1]-self.__pos[1])**2) > math.sqrt(((i[0]-self.__pirate_pos[0])**2 + (i[1]-self.__pirate_pos[1])**2))) :
                        obtain_list.remove(i)
            else:
                for i in obtain_list:
                    if math.sqrt((i[0]-self.__pos[0])**2 + (i[1]-self.__pos[1])**2) < math.sqrt(((i[0]-self.__pirate_pos[0])**2 + (i[1]-self.__pirate_pos[1])**2)) :
                        obtain_list.remove(i)
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' , self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 8:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' , hint['val']))
            print("obtain_list")
            print(obtain_list)
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    print("hintlisttrue 8")
                    print(self.__hint_list_true)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure": list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 9:
            obtain_list = []
            for i in range(len(game_map)):
                for j in range(len(game_map)):
                    if ((i, j) in hint["val"] and game_map[i][j][-1] != '0' ):
                        obtain_list.append((i, j))
            if self.is_change_virtual_treasure(obtain_list) == False:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 10:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' , hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure": obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 11:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0', hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list           
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 12:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' , hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure": obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 13:
            obtain_list = []
            for i in range(len(game_map)):
                for j in range(len(game_map)):
                    if ((i, j) in hint["val"] and game_map[i][j][-1] != '0' ):
                        obtain_list.append((i, j))
            if self.is_change_virtual_treasure(obtain_list) == False:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure": obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 14:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' , hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 15:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' , hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list           
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure
        if hint["id"] == 16:
            obtain_list = list(filter(lambda x: game_map[x[0]][x[1]][-1] != '0' , hint['val']))
            if self.is_change_virtual_treasure(obtain_list) == True:
                if self.__pirate.check_hint(hint):
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = self.intersection(
                        self.__hint_list_true, obtain_list)
                    self.__virtual_treasure = random.choice(
                        self.__hint_list_true)
                    self.first_turn_check_hint = list(filter(lambda x: x not in obtain_list, self.__hint_list_true))
                    action_infor.append({
                            "list_tiles_not_include_treasure":  list(filter(lambda x: x not in obtain_list, self.__hint_list_true)),
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is True",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": True,
                            "is_win": self.is_win()
                        })
                else:
                    num_action_rest = num_action_rest-1
                    self.__hint_list_true = list(
                        filter(lambda x: x not in obtain_list and game_map[x[0]][x[1]][-1] != '0' and game_map[x[0]]
                               [x[1]][-1] != 'M' and game_map[x[0]][x[1]][-1] != 'P', self.__hint_list_true))
                    self.first_turn_check_hint = obtain_list
                    action_infor.append({
                            "list_tiles_not_include_treasure":  obtain_list,
                            "description": f"The agent verify hint {hint['id']}, {hint['id']} is False",
                            "pos": self.__pos,
                            "which_hint_checked": hint["id"],
                            "is_hint_checked_true": False,
                            "is_win": self.is_win()
                        })
            if self.__virtual_treasure not in self.__hint_list_true:
                self.__virtual_treasure = random.choice(
                    self.__hint_list_true)
            return self.__virtual_treasure

    def teleport(self, x, y):
        self.__pos = (x, y)

    def receive_hint(self, hint, map, num_action_rest,action_infor):
        if self.is_first_turn:
            self.__virtual_treasure = self.determine_treasure_location_init(
                hint, map)
            print(self.__hint_list_true)
        else:
            self.determine_treasure_location_normal(hint, map, num_action_rest,action_infor)

    def heuristic(self, a, b):
        # print("Bug",a, b)
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    def A_start_find_way(self, game_map, direction):
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
                    direction.append(
                        tuple(map(lambda i, j: j - i, came_from[current], current)))
                    current = came_from[current]
                return data[::-1]
            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + \
                    self.heuristic(current, neighbor)
                if 0 <= neighbor[0] < map_tempt.shape[0]:
                    if 0 <= neighbor[1] < map_tempt.shape[1]:
                        if map_tempt[neighbor[0]][neighbor[1]][-1] == '0' or map_tempt[neighbor[0]][neighbor[1]][-1] == 'M'  or map_tempt[neighbor[0]][neighbor[1]][-1] == 'P':
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

    def get_count(self, num_list):
        count = 1
        listA = []
        for i in range(1, len(num_list)):
            if num_list[i] == num_list[i-1]:
                count = count + 1
            else:
                listA.append(count)
                count = 1
            if i == len(num_list)-1:
                listA.append(count)
        return listA

 # count down agent turn
    def action(self, hint, map):
            if self.turn_pirate_free_agent_know == 0 and self.turn_teleport > 0:
                if self.heuristic(self.__pirate_pos, self.__virtual_treasure) < self.heuristic(self.__pos, self.__virtual_treasure):
                    self.teleport(
                        self.__virtual_treasure[0], self.__virtual_treasure[1])
                    self.turn_teleport = self.turn_teleport-1
            num_action_rest = 2
            steps = 0
            dir_of_agent = []
            action_infor = []
            while num_action_rest > 0:

                self.receive_hint(hint, map, num_action_rest,action_infor)
                direction = []
        
                way_to_treasure = self.A_start_find_way(map, direction)
                direction = direction[::-1]
                remain = 0
                remain2 = 0
                steps = 0
                
            
                print("way to treasure")
                print(way_to_treasure)
                print(self.__pos)
                print(self.__virtual_treasure)
                print("direction")
                print(direction)
                if way_to_treasure != False:
                    summary_list_dir = self.get_count(direction)
                    for i in summary_list_dir:
                        if direction[remain2] == (1, 0):
                            dir_of_agent.append("south")
                        if direction[remain2] == (-1, 0):
                            dir_of_agent.append("north")
                        if direction[remain2] == (0, 1):
                            dir_of_agent.append("east")
                        if direction[remain2] == (0, -1):
                            dir_of_agent.append("west")
                        remain2 = remain2 + i 
                        if num_action_rest > 0:
                            if self.__pos == self.__virtual_treasure:
                                self.stay_large_scan
                                action_infor.append({
                                    "list_tiles_not_include_treasure":  self.__scan.pop(),
                                    "description": "The agent perform a LARGE SCAN",
                                    "pos": self.__pos,
                                    "which_hint_checked": None,
                                    "is_hint_checked_true": None,
                                    "is_win": self.is_win()
                                })
                                num_action_rest = num_action_rest-1
                            else:
                                if i <= 2:
                                    steps = i
                                    # print(remain + sum_of_direction)
                                    self.__pos = way_to_treasure[remain + i-1]
                                    remain = remain+i
                                    print("pos")
                                    print(self.__pos)
                                    self.small_scan(map)
                                    print("scan")
                                    print(self.__scan)
                                    action_infor.append({
                                    "list_tiles_not_include_treasure":  self.__scan.pop(),
                                    "description":  f"The agent moves {steps} steps to the {dir_of_agent[0]} and SMALL SCAN",
                                    "pos": self.__pos,
                                    "which_hint_checked": None,
                                    "is_hint_checked_true": None,
                                    "is_win": self.is_win()
                                    })
                                    dir_of_agent.pop(0)
                                    num_action_rest = num_action_rest-1
                                elif i <= 3:
                                    steps = i
                                  
                                    self.__pos = way_to_treasure[remain + i-1]
                                    remain = remain+i
                                    action_infor.append({
                                    "list_tiles_not_include_treasure":  [],
                                    "description": f"The agent moves {steps} steps to the {dir_of_agent[0]}",
                                    "pos": self.__pos,
                                    "which_hint_checked": None,
                                    "is_hint_checked_true": None,
                                    "is_win": self.is_win()
                                })
                                    dir_of_agent.pop(0)
                                    num_action_rest = num_action_rest-1
                                else:
                                  
                                    self.__pos = way_to_treasure[remain + 4-1]
                                    remain = remain+4
                                    action_infor.append({
                                    "list_tiles_not_include_treasure":  [],
                                    "description": f"The agent moves 4 steps to the {dir_of_agent[0]}",
                                    "pos": self.__pos,
                                    "which_hint_checked": None,
                                    "is_hint_checked_true": None,
                                    "is_win": self.is_win()
                                })
                                    dir_of_agent.pop(0)
                                    num_action_rest = num_action_rest-1
                    if num_action_rest > 0:
                        self.stay_large_scan
                        action_infor.append({
                                "list_tiles_not_include_treasure":  self.__scan.pop,
                                "description": "The agent perform a LARGE SCAN",
                                "pos": self.__pos,
                                "which_hint_checked": None,
                                "is_hint_checked_true": None,
                                "is_win": self.is_win()
                            })
                        num_action_rest = num_action_rest-1
                else:
                    if num_action_rest > 0:
                        self.stay_large_scan
                        action_infor.append({
                            "list_tiles_not_include_treasure":  self.__scan.pop(),
                            "description": "The agent perform a LARGE SCAN",
                            "pos": self.__pos,
                            "which_hint_checked": None,
                            "is_hint_checked_true": None,
                            "is_win": self.is_win()
                        })
                        num_action_rest = num_action_rest-1
            action_1 = action_infor.pop(0)
            action_2 = action_infor.pop(0)
            self.action_list.clear()
    
            if self.is_first_turn:
                print(
                    {
                        "action_1": 
                            action_1
                        ,
                        "action_2": 
                            action_2
                        ,
                        "first_check_hint" : self.first_turn_check_hint
                    } 
                )
                self.is_first_turn = False
                return{
                    "action_1": 
                        action_1
                    ,
                    "action_2": 
                        action_2
                    ,
                    "first_check_hint" : self.first_turn_check_hint
                }
                
            
            return {
                "action_1": 
                    action_1
                ,
                "action_2": 
                    action_2
                ,
            }


if __name__ == "__main__":
    pass
    # map_generator = map_of_game.MapGenerateTool()
    # map_of_game = map_generator.generate_map(16, 4)
    # agent = Agent(map_of_game.get_map(),2,3)
    # direction = []
    # print(agent.A_start_find_way(map_of_game.get_map(),direction))
    # print(direction[::-1] )
    # my_dict = {i:direction.count(i) for i in direction}
    # print(my_dict)
    # print(agent.get_pos())
    # print(agent.get_virtual_treasure())
    # print(map_of_game)

import random
from utils import astar

class Pirate():
    def __init__(self, game_map, turn_reveal, turn_free, agent_pos):
        self.__agent_pos = agent_pos
        self.__is_win = False
        self.__size = len(game_map)
        self.__map = game_map
        self.__turn_reveal = turn_reveal
        self.__turn_free = turn_free
        self.__treasure = (3, 4)
        self.__treasureRegion = 2
        self.__regions = 7
        self.__hint_dict = {
            # 1: self.hint_1(),
            # 2: self.hint_2(),
            3: self.hint_3(),
            # 4: self.hint_4(),
            5: self.hint_5(),
            # 6: self.hint_6(),
            # 7: self.hint_7(),
            8: self.hint_8(),
            # 9: self.hint_9(),
            # 10: self.hint_10(),
            # 11: self.hint_11(),
            # 12: self.hint_12(),
            # 13: self.hint_13(),
            # 14: self.hint_14(),
            # 15: self.hint_15(),
            # 16: self.hint_16(),

            # Add code
        }
        self.__pos = self.__set_init_pos()
        self.__path_to_treasure = astar(self.__map, self.__pos, self.__treasure)
        self.__index_path = 0
        self.__turn = 1

    
    def check_hint(self,hint):
        if hint["id"] == 8:
            if "col" not in hint["val"]:
                if self.__treasure[0] == hint["val"]["row"]:
                    return True
                else : 
                    return False
            if "row" not in hint["val"]:
                if self.__treasure[1] == hint["val"]["col"]:
                    return True
                else: 
                    return False
        elif hint["id"] == 9:
            if "col" not in hint["val"]:
                if self.__treasure[0] == hint["val"]["row"]:
                    return False
                else : 
                    return True
            if "row" not in hint["val"]:
                if self.__treasure[1] == hint["val"]["col"]:
                    return False
                else: 
                    return True
        elif hint["id"] == 6:
            return True
        else:
            if self.__treasure in hint["val"]:
                return True
            else:
                return False
        return False


    def set_agent_pos(self, agent_pos):
        self.__agent_pos = agent_pos

    def __set_init_pos(self):
        # Add code
        pos = (random.randint(1, self.__size - 2), random.randint(1, self.__size - 2))
        while self.__map[pos[0]][pos[1]][-1] == "M" or self.__map[pos[0]][pos[1]][-1] == "P" or self.__map[pos[0]][pos[1]][0] == "M":  
            pos = (random.randint(1, self.__size - 2), random.randint(1, self.__size - 2))
        return pos

    def get_pos(self):
        return self.__pos

    def get_turn_reveal(self):
        return self.__turn_reveal

    def get_turn_free(self):
        return self.__turn_free

    def is_win(self):  # Use to check whether pirate is win
        return self.__is_win

    def give_hint(self, turn):
        # Add code
        if len(list(self.__hint_dict.items())) == 0:
            return None
        key, val = random.choice(list(self.__hint_dict.items()))
        if turn == 1:
            while self.check_hint(val) == False:
                key, val = random.choice(list(self.__hint_dict.items()))
        del self.__hint_dict[key]
        return val

    def action(self, turn):
        # Add code for pirate do action
        if turn < self.__turn_reveal:
            return None
        elif turn < self.__turn_free:
            return self.__pos
        else:
            self.__index_path += 2
            self.__pos = self.__path_to_treasure[self.__index_path]
            return self.__pos

    def hint_1(self):
        list_tile = []
        n = random.randint(0, self.__size)
        m = random.randint(0, self.__size)
        size = random.randint(1, 12)
        while ((n, m) not in list_tile and len(list_tile) < size and (n, m) != self.__treasure):
            list_tile.append((n, m))
            n = random.randint(0, self.__size)
            m = random.randint(0, self.__size)
        a = ','.join(str(e) for e in list_tile)
        return {
            "id": 1,
            "val": list_tile,
            "description": "A list of random tiles that doesn't contain the treasure:" + a
        }

    def hint_3(self):
        n = random.randint(2, 5)
        list_re = []
        list_re.append(self.__treasureRegion)
        tiles = []
        m = random.randint(1, self.__regions)
        while (len(list_re) < n and m not in list_re):
            list_re.append(m)
            m = random.randint(0, self.__regions)
        for re in list_re:
            for x in range(self.__size):
                for y in range(self.__size):
                    if str(re) in self.__map[x][y]:
                        tiles.append((x, y))
        a = ','.join(str(e) for e in tiles)
        return {
            "id": 3,
            "val": tiles,
            "description": "Regions that 1 of them has the treasure:" + a
        }

    def hint_4(self):
        n = random.randint(1, 3)
        list_re = []
        tiles = []
        m = random.randint(1, self.__regions)
        while (len(list_re) < n and m not in list_re and m != self.__treasureRegion):
            list_re.append(m)
            m = random.randint(0, self.__regions)
        for re in list_re:
            for x in range(self.__size):
                for y in range(self.__size):
                    if str(re) in self.__map[x][y]:
                        tiles.append((x, y))
        a = ','.join(str(e) for e in tiles)
        return {
            "id": 4,
            "val": tiles,
            "description": "Regions that do not contain the treasure:" + a
        }

    def hint_5(self):
        n1 = random.randint(0, (self.__size -1) // 4) 
        n2 = random.randint(0, (self.__size -1) // 4) 
        m1 = random.randint((self.__size*3 -1) // 4, (self.__size-1)) 
        m2 = random.randint((self.__size*3 -1) // 4, self.__size-1) 
        tiles = []
        for x in range(n1, m1+1):
            for y in range(n2, m2+1):
                tiles.append((x, y))
        a = str((n1, n2, m1, m2))
        return {
            "id": 5,
            "val": tiles,
            "description": "A large rectangle area that has the treasure:" + a
        }

    def hint_6(self):
        n1 = random.randint(self.__size // 4, self.__size // 2) - 1
        n2 = random.randint(self.__size // 4, self.__size // 2) - 1
        m1 = random.randint(self.__size // 2, self.__size*3 // 4) - 1
        m2 = random.randint(self.__size // 2, self.__size*3 // 4) - 1
        tiles = []
        for x in range(n1, m1+1):
            for y in range(n2, m2+1):
                tiles.append((x, y))
        a = str((n1, n2, m1, m2))
        return {
            "id": 6,
            "val": tiles,
            "description": "A small rectangle area that doesn't has the treasure:" + a
        }

    def hint_7(self):

        return {
            "id": 7,
            "val": [],
            "description": "The agent receives the first hint: “Region number 2 does not has treasure:"
        }

    def hint_8(self):
        # Add code
        a = random.randint(0, 2)
        n = random.randint(0, self.__size)
        m = random.randint(0, self.__size)
        if (a == 0):
            return {
                "id": 8,
                "val": {
                    "col": n,
                    "row": m
                },
                "description": "A column and a row that contain the treasure:" + str((m,n))
            }
        if (a == 1):
            return {
                "id": 8,
                "val": {
                    "col": n,
                },
                "description": "A column that contain the treasure:" + str(n)
            }
        if (a == 2):
            return {
                "id": 8,
                "val": {
                    "row": m
                },
                "description": "A row that contain the treasure:" + str(m)
            }

    def hint_9(self):
        a = random.randint(0, 2)
        n = random.randint(0, self.__size)
        m = random.randint(0, self.__size)
        if (a == 0):
            return {
                "id": 9,
                "val": {
                    "col": n,
                    "row": m
                },
                "description": "A column and a row that do not contain the treasure:" + str((m,n))
            }
        if (a == 1):
            return {
                "id": 9,
                "val": {
                    "col": n,
                },
                "description": "A column that do not contain the treasure:" + str(n)
            }
        if (a == 2):
            return {
                "id": 9,
                "val": {
                    "row": m
                },
                "description": "A row that do not contain the treasure:" + str(m)
            }

    def hint_10(self):
        n = random.randint(0, self.__regions)
        m = random.randint(0, self.__regions)
        while (m == n):
            m = random.randint(0, self.__regions)
        return {
            "id": 10,
            "val": [m, n],
            "description": "Two 2 regions that the treasure is somewhere in their boundary is: "
        }

    def hint_11(self):
        # Add code
        return {
            "id": 11,
            "val": [],
            "description": "The agent receives the first hint: “Region number 2 does not has treasure"
        }

    def hint_12(self):
        # Add code
        return {
            "id": 12,
            "val": [],
            "description": "The agent receives the first hint: “Region number 2 does not has treasure"
        }

    def hint_13(self):
        a = random.randint(0, 3)
        tiles = []
        if (a == 0):
            for x in range(0, self.__size//2):
                for y in range(0, self.__size//2):
                    tiles.append((x, y))
        if (a == 1):
            for x in range(0, self.__size//2):
                for y in range(self.__size//2, self.__size):
                    tiles.append((x, y))
        if (a == 2):
            for x in range(self.__size//2, self.__size):
                for y in range(0, self.__size//2):
                    tiles.append((x, y))
        if (a == 3):
            for x in range(self.__size//2, self.__size):
                for y in range(self.__size//2, self.__size):
                    tiles.append((x, y))
        return {
            "id": 13,
            "val": tiles,
            "description": "A half of the map without treasure."
        }

    def hint_14(self):
        pass

    def hint_15(self):
        n1 = random.randint(0, (self.__size - 1) // 4)
        n2 = random.randint(0, (self.__size - 1) // 4)
        m1 = random.randint((self.__size*3 - 1) // 4, self.__size-1)
        m2 = random.randint((self.__size*3 - 1) // 4, self.__size-1)
        x1 = random.randint((self.__size - 1) // 4, (self.__size - 1) // 2)
        x2 = random.randint((self.__size - 1) // 4, (self.__size - 1) // 2)
        y1 = random.randint((self.__size - 1) // 2, (self.__size*3 - 1) // 4)
        y2 = random.randint((self.__size - 1) // 2, (self.__size*3 - 1) // 4)
        tiles = []
        for x in range(n1, m1+1):
            for y in range(n2, m2+1):
                tiles.append((x, y))
        for x in range(x1, y1+1):
            for y in range(x2, y2+1):
                tiles.remove((x, y))
        return {
            "id": 15,
            "val": tiles,
            "description": "The treasure is somewhere in the gap between 2 squares:" + str((n1, n2, m1, m2)) + " and " + str((x1, x2, y1, y2))
        }

    def hint_16(self):
        tiles = []
        for x in range(self.__size):
            for y in range(self.__size):
                if 'M' in self.__map[x][y]:
                    tiles.append((x, y))
        return {
            "id": 16,
            "val": tiles,
            "description": "The treasure is in a region that has mountain."
        }

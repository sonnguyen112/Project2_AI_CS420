import random
from utils import astar

class Pirate():
    def __init__(self, game_map, turn_reveal, turn_free, agent_pos,region_num):
        self.__agent_pos = agent_pos
        self.__is_win = False
        self.__size = len(game_map)
        self.__map = game_map
        self.__turn_reveal = turn_reveal
        self.__turn_free = turn_free
        self.__treasure = None
        self.__treasureRegion = 2
        self.__regions = region_num
        self.__hint_dict = {
            # 1: self.hint_1(),
            # # 2: self.hint_2(),
            # 3: self.hint_3(),
            4: self.hint_4(),
            # 5: self.hint_5(),
            # 6: self.hint_6(),
            # 7: self.hint_7(),
            # 8: self.hint_8(),
            # 9: self.hint_9(),
            #10: self.hint_10(),
            # 11: self.hint_11(),
            # 12: self.hint_12(),
            # 13: self.hint_13(),
            # # 14: self.hint_14(),
            # 15: self.hint_15(),
            # 16: self.hint_16(),

            # Add code
        }
        self.__pos = self.__set_init_pos()
        self.__path_to_treasure = None
        self.__index_path = 0
        self.__turn = 1

    def cal_path(self):
        self.__path_to_treasure = astar(self.__map, self.__pos, self.__treasure)

    def set_treasure(self,tresure_pos):
        self.__treasure=tresure_pos

    def check_boundary(self, re1,re2):
        tiles = []
        for x in range(1,self.__size -1):
            for y in range(1,self.__size-1):
                if ( str(re1) in self.__map[x][y]):
                    if( str(re2) in self.__map[x-1][y] or str(re2) in self.__map[x+1][y] or str(re2) in self.__map[x][y-1] or str(re2) in self.__map[x][y+1]):
                        tiles.append((x,y))
                elif(str(re2) in self.__map[x][y]):
                    if( str(re1) in self.__map[x-1][y] or str(re1) in self.__map[x+1][y] or str(re1) in self.__map[x][y-1] or str(re1) in self.__map[x][y+1]):
                        tiles.append((x,y))
        for y in range(1,self.__size-1):
            x = 0
            if ( str(re1) in self.__map[x][y]):
                if(str(re2) in self.__map[x+1][y] or str(re2) in self.__map[x][y-1] or str(re2) in self.__map[x][y+1]):
                        tiles.append((x,y))
            elif(str(re2) in self.__map[x][y]):
                if(str(re1) in self.__map[x+1][y] or str(re1) in self.__map[x][y-1] or str(re1) in self.__map[x][y+1]):
                        tiles.append((x,y))

            x = self.__size -1
            if ( str(re1) in self.__map[x][y]):
                if(str(re2) in self.__map[x-1][y] or str(re2) in self.__map[x][y-1] or str(re2) in self.__map[x][y+1]):
                        tiles.append((x,y))
            elif(str(re2) in self.__map[x][y]):
                if(str(re1) in self.__map[x-1][y] or str(re1) in self.__map[x][y-1] or str(re1) in self.__map[x][y+1]):
                        tiles.append((x,y))
        
        for x in range(1,self.__size-1 -1):
            y = 0
            if ( str(re1) in self.__map[x][y]):
                if(str(re2) in self.__map[x+1][y] or str(re2) in self.__map[x-1][y] or str(re2) in self.__map[x][y+1]):
                        tiles.append((x,y))
            elif(str(re2) in self.__map[x][y]):
                if(str(re1) in self.__map[x+1][y] or str(re1) in self.__map[x-1][y] or str(re1) in self.__map[x][y+1]):
                        tiles.append((x,y))
            y = self.__size -1
            if ( str(re1) in self.__map[x][y]):
                if(str(re2) in self.__map[x+1][y] or str(re2) in self.__map[x-1][y] or str(re2) in self.__map[x][y-1]):
                        tiles.append((x,y))
            elif(str(re2) in self.__map[x][y]):
                if(str(re1) in self.__map[x+1][y] or str(re1) in self.__map[x-1][y] or str(re1) in self.__map[x][y-1]):
                        tiles.append((x,y))
        x = 0
        y = 0
        if(str(re1) in self.__map[x][y]):
            if(str(re2) in self.__map[x+1][y] or str(re2) in self.__map[x][y+1]):
                tiles.append((x,y))
        elif(str(re2) in self.__map[x][y]):
            if(str(re1) in self.__map[x+1][y] or str(re1) in self.__map[x][y+1]):
                tiles.append((x,y))
        x = 0 
        y = self.__size - 1
        if(str(re1) in self.__map[x][y]):
            if(str(re2) in self.__map[x+1][y] or str(re2) in self.__map[x][y-1]):
                tiles.append((x,y))
        elif(str(re2) in self.__map[x][y]):
            if(str(re1) in self.__map[x+1][y] or str(re1) in self.__map[x][y-1]):
                tiles.append((x,y))
        x = self.__size - 1 
        y = self.__size - 1
        if(str(re1) in self.__map[x][y]):
            if(str(re2) in self.__map[x-1][y] or str(re2) in self.__map[x][y-1]):
                tiles.append((x,y))
        elif(str(re2) in self.__map[x][y]):
            if(str(re1) in self.__map[x-1][y] or str(re1) in self.__map[x][y-1]):
                tiles.append((x,y))
        x = self.__size - 1 
        y = 0
        if(str(re1) in self.__map[x][y]):
            if(str(re2) in self.__map[x-1][y] or str(re2) in self.__map[x][y+1]):
                tiles.append((x,y))
        elif(str(re2) in self.__map[x][y]):
            if(str(re1) in self.__map[x-1][y] or str(re1) in self.__map[x][y+1]):
                tiles.append((x,y))
        return tiles

    def check_hint(self,hint):
        if hint["id"] == 7:
            a = (self.__treasure[0] - self.__pos[0] )*(self.__treasure[0] - self.__pos[0]) + (self.__treasure[1] - self.__pos[1] )*(self.__treasure[1] + self.__pos[1])
            b = (self.__treasure[0] - self.__agent_pos[0] )*(self.__treasure[0] - self.__agent_pos[0]) + (self.__treasure[1] - self.__agent_pos[1] )*(self.__treasure[1] - self.__agent_pos[1]) 
            if ( a > b):
                if (hint["val"] == 0):
                    return False
                else:
                    return True
            else:
                if (hint["val"] == 0):
                    return True
                else:
                    return False
        elif ( hint["id"] in [1,2,4,6,9,13]):
            if self.__treasure  not in hint["val"]:
                return True
            else:
                return False
        else:
            if self.__treasure in hint["val"]:
                return True
            else:
                return False



    def set_agent_pos(self, agent_pos):
        self.__agent_pos = agent_pos

    def __set_init_pos(self):
        # Add code
        prisons = []
        for i in range(len(self.__map)):
            for j in range(len(self.__map)):
                if self.__map[i][j][-1] == "P":
                    prisons.append((i, j))
        return random.choice(prisons)

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
        # if turn == 1:
        #     while self.check_hint(val) == False:
        #         key, val = random.choice(list(self.__hint_dict.items()))
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
    
    def hint_2(self):
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
            "description": "A list of random tiles that contain the treasure:" + a
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
        n1 = random.randint((self.__size -1) // 4, (self.__size -1) // 2) 
        n2 = random.randint((self.__size -1) // 4, (self.__size -1) // 2) 
        m1 = random.randint((self.__size -1) // 2, (self.__size -1)*3 // 4) 
        m2 = random.randint((self.__size -1) // 2, (self.__size -1)*3 // 4) 
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
        a = random.randint(0,1)
        b = ""
        if ( a == 0):
            b = "Pirate"
        else:
            b = "You"
        return {
            "id": 7,
            "val": a,
            "description":  b +" are the nearest person to the treasure."
        }

    def hint_8(self):
        # Add code
        a = random.randint(0, 2)
        n = random.randint(0, self.__size)
        m = random.randint(0, self.__size)
        titles = []
        if (a == 0):
            titles = []
            for i in range(self.__size):
                titles.append((m,i))
                titles.append((i,n))            
            return {
                "id": 8,
                "val": titles,
                "description": "A column and a row that contain the treasure:" + str((m,n))
            }
        if (a == 1):
            for i in range(self.__size):
                titles.append((i,n))
            return {
                "id": 8,
                "val":titles,
                "description": "A column that contain the treasure:" + str(n)
            }
        if (a == 2):
            for i in range(self.__size):
                titles.append((m,i))
            return {
                "id": 8,
                "val":titles,
                "description": "A row that contain the treasure:" + str(m)
            }

    def hint_9(self):
        a = random.randint(0, 2)
        n = random.randint(0, self.__size-1)
        m = random.randint(0, self.__size-1)
        titles = []
        if (a == 0):
            
            for i in range(self.__size):
                titles.append(((m,i)))
                titles.append(((i,n)))         
            return {
                "id": 8,
                "val": titles,
                "description": "A column and a row that do not contain the treasure:" + str((m,n))
            }
        if (a == 1):
            for i in range(self.__size):
                titles.append((i,n)) 
            return {
                "id": 8,
                "val":titles,
                "description": "A column that do not contain the treasure:" + str(n)
            }
        if (a == 2):
            for i in range(self.__size):
                titles.append((m,i))
            return {
                "id": 8,
                "val":titles,
                "description": "A row that do not contain the treasure:" + str(m)
            }

    def hint_10(self):
        n = random.randint(1, self.__regions-1)
        m = random.randint(1, self.__regions-1)
        while (m == n):
            m = random.randint(1, self.__regions-1)
        tiles = self.check_boundary(m,n)
        #tiles += self.check_boundary(n,m)
        return {
            "id": 10,
            "val": tiles,
            "description": "Two 2 regions that the treasure is somewhere in their boundary" + str((m,n))

        }

    def hint_11(self):
        tiles = []
        for x in range(1, self.__regions-1):
            for y in range(x +1,self.__regions):
                tiles += self.check_boundary(x,y)
                # tiles += self.check_boundary(y,x)
        # tiles = list(dict.fromkeys(tiles))
        return {
            "id": 11,
            "val": tiles,
            "description": "The treasure is somewhere in a boundary of 2 regions"
        }

    def hint_12(self):
        tile = []
        tile_0 = []
        for x in range(1, self.__regions):
            tile += self.check_boundary(x,0)
        for i in tile:
            if self.__map[i[0]][i[1]] == "0":
                tile_0.append(i)
        return {
            "id": 12,
            "val": tile_0,
            "description": "The treasure is somewhere in an area bounded by 1 tiles from sea"
        }

    def hint_13(self):
        a = random.randint(0, 3)
        tiles = []
        if (a == 0):
            for x in range(0, self.__size):
                for y in range(0, self.__size//2):
                    tiles.append((x, y))
        if (a == 1):
            for x in range(0, self.__size):
                for y in range(self.__size//2, self.__size):
                    tiles.append((x, y))
        if (a == 2):
            for x in range(self.__size//2, self.__size):
                for y in range(0, self.__size):
                    tiles.append((x, y))
        if (a == 3):
            for x in range(0, self.__size//2):
                for y in range(0, self.__size):
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
        re_have_M = []
        for x in range(self.__size):
            for y in range(self.__size):
                if 'M' in self.__map[x][y]:
                    re_have_M.append (self.__map[x][y][0])
        tiles= []
        for x in range(self.__size):
            for y in range(self.__size):
                if self.__map[x][y][0] in re_have_M:
                    tiles.append (self.__map[x][y])
        return {
            "id": 16,
            "val": tiles,
            "description": "The treasure is in a region that has mountain."
        }

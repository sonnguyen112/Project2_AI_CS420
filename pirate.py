import random

class Pirate():
    def __init__(self, turn_reveal, turn_free):
        self.__is_win = False
        self.pos = self.__set_init_pos()
        self.__turn_reveal = turn_reveal
        self.__turn_free = turn_free
        self.__treasure = (3,3)
        self.__treasureRegion = 2
        self.__regions = 7
        self.__size = 16
        self.__map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '1M', '1M', '1M', '1', '1', '1', '0', '0', '4', '4', '4', '4', '4', '4', '0'], ['0', '1M', '1M', '1M', '1M', '1', '1', '5', '4', '4', '4', '4', '4', '4', '4', '0'], ['0', '1M', '1M', '1M', '1', '1', '1', '5', '5', '4', '4', '4', '4', '4', '4', '0'], ['0', '1M', '1M', '1', '1', '1', '1', '5', '5', '5', '4', '4', '4', '4', '4', '0'], ['0', '2', '1M', '2', '1', '1', '5', '5', '5', '5', '4', '4', '4', '0', '0', '0'], ['0', '2', '2', '2', '2', '1', '5', '5', '5M', '5', '5', '4', '6', '0', '0', '0'], ['0', '2', '2', '2', '2', '2', '2', '5M', '5M', '5M', '5', '6', '6', '6P', '6', '0'], ['0', '2', '2', '2', '2', '2', '2', '5M', '5M', '5M', '5', '6', '6', '6', '6', '0'], ['0', '2', '2P', '2', '2', '2', '5', '5M', '5M', '5M', '6', '6', '6', '6', '6', '0'], ['0', '2', '2', '2', '0', '2', '5', '3', '0', '6', '6', '6', '6', '6', '6', '0'], ['0', '2', '2', '3', '3', '3', '3', '3', '3', '0', '6', '6', '6', '6', '6', '0'], ['0', '3', '3', '3', '3', '3', '3', '3', '3', '0', '0', '6', '6', '6', '6', '0'], ['0', '3', '3', '3P', '3', '3', '3', '3', '3', '3', '0', '0', '0', '0', '0', '0'], ['0', '3', '3', '3', '3', '3', '3', '3', '3', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]
        self.__hint_dict = {
            1: self.hint_1(),
            2: self.hint_2(),
            3: self.hint_3(),
            4: self.hint_4(),
            5: self.hint_5(),
            6: self.hint_6(),
            7: self.hint_7(),
            8: self.hint_8(),
            9: self.hint_9(),
            10: self.hint_10(),
            11: self.hint_11(),
            12: self.hint_12(),
            13: self.hint_13(),
            14: self.hint_14(),
            15: self.hint_15(),

            # Add code
        }

    def __set_init_pos(self):
        # Add code
        return (0,0)

    def get_turn_reveal(self):
        return self.__turn_reveal
    
    def get_turn_free(self):
        return self.__turn_free

    def is_win(self): # Use to check whether pirate is win
        return self.__is_win

    def give_hint(self, turn):
        # Add code
        return self.__hint_dict[1] 

    def action(self, turn):
        # Add code for pirate do action 
        return "The pirate moves 2 steps to the north and SMALL SCAN"

    def hint_1(self):
        list_tile = []
        n = random.randint(0, self.__size)
        m = random.randint(0, self.__size)
        size = random.randint(1,12)
        while ( (n,m) not in list_tile and len(list_tile) < size and (n,m) != self.__treasure):
            list_tile.append((n,m))
            n = random.randint(0, self.__size)
            m = random.randint(0, self.__size)
        return {
            "id": 1,
            "val" : list_tile,
            "description" : "A list of random tiles that doesn't contain the treasure:"
        }
    def hint_2(self):
        n = random.randint(2,5)
        list_re = []
        list_re.append(self.__treasureRegion)
        tiles = []
        m = random.randint(1,self.__regions)
        while( len(list_re) < n and m not in list_re):
            list_re.append(m)
            m = random.randint(0, self.__regions)
        for re in list_re:
            for x in range(self.__size):
                for y in range(self.__size):
                    if str(re) in map[x][y]:
                        tiles.append((x,y))
        return {
            "id": 2,
            "val" : tiles,
            "description" : "Regions that 1 of them has the treasure:"
        }
    def hint_3(self):
        n = random.randint(1,3)
        list_re = []
        tiles = []
        m = random.randint(1,self.__regions)
        while( len(list_re) < n and m not in list_re and m != self.__treasureRegion):
            list_re.append(m)
            m = random.randint(0, self.__regions)
        for re in list_re:
            for x in range(self.__size):
                for y in range(self.__size):
                    if str(re) in map[x][y]:
                        tiles.append((x,y))
        return {
            "id": 3,
            "val" : tiles,
            "description" : "Regions that do not contain the treasure:"
        }
    def hint_4(self):
        n1 = random.randint(0, self._size // 4) -1
        n2 = random.randint(0, self._size // 4) -1 
        m1 = random.randint(self.__size*3 // 4, self.__size) -1
        m2 = random.randint(self.__size*3 // 4, self.__size) -1
        tiles = []
        for x in range(n1,m1+1):
            for y in range(n2,m2+1):
                tiles.append((x,y))
        return {
            "id": 4,
            "val" : tiles,
            "description" : "A large rectangle area that has the treasure:"
        }
    def hint_5(self):
        n1 = random.randint(self._size // 4,self._size // 2) -1
        n2 = random.randint(self._size // 4,self._size // 2) -1 
        m1 = random.randint(self._size // 2,self.__size*3 // 4) -1
        m2 = random.randint(self._size // 2,self.__size*3 // 4) -1
        tiles = []
        for x in range(n1,m1+1):
            for y in range(n2,m2+1):
                tiles.append((x,y))
        return {
            "id": 5,
            "val" : tiles,
            "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
        }
    def hint_6(self):

        return {
            "id": 6,
            "val" : [],
            "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
        }
    def hint_7(self):
        # Add code
        a = random.randint(0,3)
        n = random.randint(0,self.__size)
        m = random.randint(0,self.__size)
        if ( a == 0):
            return {
                "id": 7,
                "val" : {
                    "col": n,
                    "row" : m
                },
                "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
            }
        if ( a == 1):
            return {
                "id": 7,
                "val" : {
                    "col": n,
                },
                "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
            }
        if ( a == 2):
            return {
                "id": 7,
                "val" : {
                    "row" : m
                },
                "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
            }
    def hint_8(self):
        a = random.randint(0,3)
        n = random.randint(0,self.__size)
        m = random.randint(0,self.__size)
        if ( a == 0):
            return {
                "id": 7,
                "val" : {
                    "col": n,
                    "row" : m
                },
                "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
            }
        if ( a == 1):
            return {
                "id": 7,
                "val" : {
                    "col": n,
                },
                "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
            }
        if ( a == 2):
            return {
                "id": 7,
                "val" : {
                    "row" : m
                },
                "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
            }
    def hint_9(self):
        n = random.randint(0, self.__regions)
        m = random.randint(0, self.__regions)
        while(m == n):
            m = random.randint(0, self.__regions)
        return {
            "id": 9,
            "val" : [m,n],
            "description" : "Two 2 regions that the treasure is somewhere in their boundary is: " 
        }
    def hint_10(self):
        # Add code
        return {
            "id": 10,
            "val" : [],
            "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
        }
    def hint_11(self):
        # Add code
        return {
            "id": 11,
            "val" : [],
            "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
        }
    def hint_12(self):
        # Add code
        return {
            "id": 12,
            "val" : [],
            "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
        }
    def hint_13(self):
        n = random.randint(0,1)
        # 0 is center, 1 is prison
        m = random.randint(1,8)
        # 1- 8 is W, E, N, S, SE, SW, NE, NW
        return {
            "id": 13,
            "val" : [n,m],
            "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
        }
    def hint_14(self):
        n1 = random.randint(0, self._size // 4) -1
        n2 = random.randint(0, self._size // 4) -1 
        m1 = random.randint(self.__size*3 // 4, self.__size) -1
        m2 = random.randint(self.__size*3 // 4, self.__size) -1
        x1 = random.randint(self.__size // 4, self.__size // 2) -1
        x2 = random.randint(self.__size // 4, self.__size // 2) -1
        y1 = random.randint(self.__size // 2, self.__size*3 // 2) -1 
        y2 = random.randint(self.__size // 2, self.__size*3 // 2) -1
        tiles1 = []
        tiles2 = []
        for x in range(n1,m1+1):
            for y in range(n2,m2+1):
                tiles1.append((x,y))
        for x in range(n1,m1+1):
            for y in range(n2,m2+1):
                tiles2.append((x,y))
        return {
            "id": 14,
            "val" : [(n1,n2,m1,m2), (x1,x2,y1,y2)],
            "description" : "The treasure is somewhere in the gap between 2 squares:"
        }
    def hint_15(self):
        return {
            "id": 15,
            "val" : [],
            "description" : "The treasure is in a region that has mountain."
        }

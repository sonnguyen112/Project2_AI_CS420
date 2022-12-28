import random


class Pirate():
    def __init__(self, turn_reveal, turn_free):
        self.__is_win = False
        self.pos = self.__set_init_pos()
        self.__turn_reveal = turn_reveal
        self.__turn_free = turn_free

        self.__regions = 5
        self.__size = 10
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
        return (0, 0)

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
        return self.__hint_dict[1]

    def action(self, turn):
        # Add code for pirate do action
        return "The pirate moves 2 steps to the north and SMALL SCAN"

    def hint_1(self):
        list_tile = []
        n = random.randint(0, self.__size)
        m = random.randint(0, self.__size)
        size = random.randint(1,12)
        while ( (n,m) not in list_tile and len(list_tile) < size):
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
        m = random.randint(1,self.__regions)
        while( len(list_re) < n and m not in list_re):
            list_re.append(m)
            m = random.randint(0, self.__regions)
        return {
            "id": 2,
            "val" : list_re,
            "description" : "Regions that 1 of them has the treasure:"
        }
    def hint_3(self):
        n = random.randint(1,3)
        list_re = []
        m = random.randint(1,self.__regions)
        while( len(list_re) < n and m not in list_re):
            list_re.append(m)
            m = random.randint(0, self.__regions)
        return {
            "id": 3,
            "val" : list_re,
            "description" : "Regions that do not contain the treasure:"
        }
    def hint_4(self):
        n1 = random.randint(0, self._size // 4) -1
        n2 = random.randint(0, self._size // 4) -1 
        m1 = random.randint(self.__size*3 // 4, self.__size) -1
        m2 = random.randint(self.__size*3 // 4, self.__size) -1
        return {
            "id": 4,
            "val" : [(n1,n2,m1,m2)],
            "description" : "A large rectangle area that has the treasure:"
        }
    def hint_5(self):
        # Add code
        return {
            "id": 5,
            "val" : [],
            "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
        }
    def hint_6(self):
        # Add code
        return {
            "id": 6,
            "val" : [],
            "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
        }
    def hint_7(self):
        # Add code
        return {
            "id": 7,
            "val" : [],
            "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
        }
    def hint_8(self):
        # Add code
        return {
            "id": 8,
            "val" : [],
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

    def hint_2(self):
        pass

    def hint_3(self):
        pass
import random

class Pirate():
    def __init__(self, turn_reveal, turn_free):
        self.__is_win = False
        self.pos = self.__set_init_pos()
        self.__turn_reveal = turn_reveal
        self.__turn_free = turn_free
        self.__hint_dict = {
            1: self.hint_1(),
            2: self.hint_2(),
            3: self.hint_3(),
            # Add code
        }

    def __set_init_pos(self):
        # Add code
        return (0,0)
        
    def get_pos(self):
        return self.__pos

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
        # Add code
        return {
            "id": 1,
            "val" : [],
            "description" : "The agent receives the first hint: “Region number 2 does not has treasure"
        }

    def hint_2(self):
        pass

    def hint_3(self):
        pass
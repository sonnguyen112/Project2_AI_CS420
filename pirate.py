import random

class Pirate():
    def __init__(self):
        self.__is_win = False
        self.pos = self.__set_init_pos()
        self.__turn_reveal = random.randint(2, 4)
        self.__turn_free = self.__set_turn_free()
        self.__hint_dict = {
            1: self.hint_1(),
            2: self.hint_2(),
            3: self.hint_3(),
            # Add code
        }

    def __set_init_pos(self):
        # Add code
        return (0,0)

    def __set_turn_free(self):
        # Add code
        return 5

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
        pass

    def hint_1(self):
        pass

    def hint_2(self):
        pass

    def hint_3(self):
        pass
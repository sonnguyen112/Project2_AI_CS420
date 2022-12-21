class Agent():
    def __init__(self):
        self.__is_win = False
        self.__pos = self.__set_init_pos()
        self.__hint_list = []

    def __set_init_pos(self):
        # Add code
        return (0,0)

    def get_pos(self):
        return self.__pos

    def check_hint(hint):
        # Add code 
        return True

    def is_win(self): # Use to check whether agent win
        return self.__is_win

    def action(self, hint):
        # Add code to agent choose action
        return ["The agent moves 2 steps to the north and SMALL SCAN", "The agent moves 4 steps to the north and SMALL SCAN"]
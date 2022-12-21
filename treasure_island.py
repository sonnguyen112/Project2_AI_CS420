from map import Map
from agent import Agent
from pirate import Pirate

class TreasureIslandGame():
    def __init__(self, map, agent, pirate) -> None:
        self.__map = map
        self.__agent = agent
        self.__pirate = pirate
        self.__turn = 1

    def play(self):
        while self.__agent.is_win() == False and self.__pirate.is_win() == False:
            print("Turn",self.__turn)
            hint = self.__pirate.give_hint(self.__turn)
            agent_actions = self.__agent.action(hint)
            pirate_action = self.__pirate.action(self.__turn)
            self.__turn += 1
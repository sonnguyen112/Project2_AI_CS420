from agent import Agent
from pirate import Pirate
import random
from utils import astar
import pickle
random.seed(3)

class TreasureIslandGame():
    def __init__(self, map_file) -> None:
        self.__size, self.__turn_reveal, self.__turn_free, self.__num_region, self.__treasure_pos, self.__game_map = self.__load_map(
            map_file)
        agent_pos_init = (random.randint(1, self.__size-2),
                          random.randint(1, self.__size-2))
        while self.__game_map[agent_pos_init[0]][agent_pos_init[1]][-1] == "M" or self.__game_map[agent_pos_init[0]][agent_pos_init[1]][-1] == "P" or self.__game_map[agent_pos_init[0]][agent_pos_init[1]][0] == "0":
            agent_pos_init = (random.randint(1, self.__size-2),
                          random.randint(1, self.__size-2))
        while astar(self.__game_map, agent_pos_init, self.__treasure_pos) == False:
            agent_pos_init = (random.randint(1, self.__size-2),
                              random.randint(1, self.__size-2))
        self.__agent = Agent(agent_pos_init, self.__game_map,
                             self.__turn_reveal, self.__turn_free,self.__num_region)
        self.__pirate = Pirate(
            self.__game_map, self.__turn_reveal, self.__turn_free, self.__agent.get_pos(),self.__num_region)
        self.__pirate.set_treasure(self.__treasure_pos)
        self.__pirate.cal_path()
        self.__turn = 1

    def __load_map(self, map_file):
        with open(map_file, "r") as file:
            size = int(file.readline().split()[0])
            turn_reveal = int(file.readline())
            turn_free = int(file.readline())
            num_region = int(file.readline())
            temp = file.readline().split()
            treasure_pos = (int(temp[0]), int(temp[1]))
            game_map = []
            for i in range(size):
                game_map.append(file.readline().replace("\n", "").split("; "))

        return size, turn_reveal, turn_free, num_region, treasure_pos, game_map

    def __save_log(self, file_name, log):
        with open(file_name, 'wb') as handle:
            pickle.dump(log, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def play(self):
        try:
            logs = {
                "map": self.__game_map,
                "num_of_region": self.__num_region,
                "agent_pos_init": self.__agent.get_pos(),
                "treasure_pos": self.__treasure_pos,
                "turn_pirate_reveal": self.__turn_reveal,
                "turn_pirate_free": self.__turn_free,
                "who_win": None,
                "machine_turn": [],
            }
            prev_agent_pos = self.__agent.get_pos()
            while self.__agent.is_win() == False and self.__pirate.is_win() == False:
                print("Turn", self.__turn)
                hint = self.__pirate.give_hint(self.__turn)
                print("HINT", hint)
                agent_actions = self.__agent.action(hint, self.__game_map)
                print("agent_action")
                print(agent_actions)
                self.__pirate.set_agent_pos(self.__agent.get_pos())
                print("AGENT ACTION", agent_actions)
                pirate_pos = self.__pirate.action(self.__turn)
                print("PIRATE ACTION", pirate_pos)
                self.__agent.set_pirate_pos(pirate_pos)
                machine_turn = agent_actions

            
                machine_turn["hint"] = {
                    "list_tiles": hint["val"],
                    "description": hint["description"],
                    "pos": prev_agent_pos
                },

                prev_agent_pos = agent_actions["action_2"]["pos"]
                
                machine_turn["pirate_pos"] = pirate_pos
                logs["machine_turn"].append(machine_turn)
                self.__turn += 1
            self.__save_log("logs/log_1.pickle", logs)
        except Exception as e:
            self.__save_log("logs/log_1.pickle", logs)


if __name__ == "__main__":
    game = TreasureIslandGame("map/map_16x16.txt")
    game.play()

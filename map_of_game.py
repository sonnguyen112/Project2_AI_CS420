import random
from utils import astar

class Map():
    def __init__(self, map):
        self.__map = map

    def __repr__(self):
        output = ""
        for row in self.__map:
            output += " ".join(map(str, row)) + "\n"

        return output

    def get_map(self):
        map_str = [list(map(str, self.__map[i])) for i in range(len(self.__map))]
        return map_str


class MapGenerateTool():
    def generate_map(self, size, num_of_region):
        map = [[0 for _ in range(size)] for _ in range(size)]
        
        for region in range(1, num_of_region):
            tiles = []
            for _ in range(((size - 2)**2 // (num_of_region - 1)) - random.randint(0, (size*5)//16)):
                tiles.append(region)

            temp_arr = [(-1,0), (1,0), (0, -1), (0, 1)]

            queue = []

            init_fill = (1, 1)
            while map[init_fill[0]][init_fill[1]] != 0:
                init_fill = (random.randint(1, size - 2), random.randint(1, size-2)) 
            queue.append(init_fill)

            index_tile = 0
            len_tile = len(tiles)
            while len(queue) != 0 and index_tile < len_tile:
                temp = queue.pop(random.randint(0, len(queue) - 1))

                for i in temp_arr:
                    # print((temp[0]+i[0], temp[1]+i[1]))
                    if map[temp[0]+i[0]][temp[1]+i[1]] == 0 and temp[0]+i[0] > 0 and temp[0]+i[0] < size - 1 and temp[1]+i[1] > 0 and temp[1]+i[1] < size - 1:
                        queue.append((temp[0]+i[0], temp[1]+i[1]))
                        map[temp[0]+i[0]][temp[1]+i[1]] = tiles[index_tile]
                        index_tile += 1
                        if index_tile == len_tile:
                            break

        mountain_long = ["M" for _ in range(size)]
        mountains = []

        num_mountain = (size*3) // 16
        remain_mountain = mountain_long
        remain_num_mountain = num_mountain
        for _ in range(num_mountain):
            cut = random.randint(1, len(remain_mountain) - remain_num_mountain - 1)
            mountains.append(remain_mountain[:cut])
            remain_num_mountain -= 1


        for mountain in mountains:
            temp_arr = [(-1,0), (1,0), (0, -1), (0, 1)]

            queue = []

            init_fill = (1, 1)
            while "M" in str(map[init_fill[0]][init_fill[1]]):
                init_fill = (random.randint(1, size - 2), random.randint(1, size-2)) 
            queue.append(init_fill)

            index_mountain = 0
            len_mountain = len(mountain)

            while len(queue) != 0 and index_mountain < len_mountain:
                temp = queue.pop(random.randint(0, len(queue) - 1))

                for i in temp_arr:
                    if "M" not in str(map[temp[0]+i[0]][temp[1]+i[1]]) and temp[0]+i[0] > 0 and temp[0]+i[0] < size - 1 and temp[1]+i[1] > 0 and temp[1]+i[1] < size - 1 and map[temp[0]+i[0]][temp[1]+i[1]] != 0:
                        queue.append((temp[0]+i[0], temp[1]+i[1]))
                        if "M" not in str(map[temp[0]+i[0]][temp[1]+i[1]]):
                            map[temp[0]+i[0]][temp[1]+i[1]] = str(map[temp[0]+i[0]][temp[1]+i[1]]) + "M"
                        index_mountain += 1
                        if index_mountain == len_mountain:
                            break
        
        num_prison = (size*3)//16
        for _ in range(num_prison):
            pos = (random.randint(1, size-2), random.randint(1, size-2))
            while map[pos[0]][pos[1]] == 0 or "M" in str(map[pos[0]][pos[1]]):
                pos = (random.randint(1, size-2), random.randint(1, size-2))
            
            if "P" not in str(map[pos[0]][pos[1]]):
                map[pos[0]][pos[1]] = str(map[pos[0]][pos[1]]) + "P"

        map = Map(map)
        return map

    def export_file(self, size, file_name, turn_reveal = 2, turn_free = 5, num_region = 7):
        map = self.generate_map(size, num_region).get_map()
        treasure_pos = (random.randint(1, size-2), random.randint(1, size-2))
        while map[treasure_pos[0]][treasure_pos[1]][-1] == "M" or  map[treasure_pos[0]][treasure_pos[1]][-1] == "P" or  map[treasure_pos[0]][treasure_pos[1]][0] == "0":
            treasure_pos = (random.randint(1, size-2), random.randint(1, size-2))
        with open(file_name, "w") as file:
            file.write(f"{size} {size}\n")
            file.write(f"{turn_reveal}\n")
            file.write(f"{turn_free}\n")
            file.write(f"{num_region}\n")
            file.write(f"{treasure_pos[0]} {treasure_pos[1]}\n")
            for row in map:
                file.write(f"{'; '.join(row)}\n")


if __name__== "__main__":
    map_generator = MapGenerateTool()
    # map_sample = map_generator.generate_map(16, 4)
    # actual_map = map_sample.get_map()
    # print(map_sample)
    # print(map_sample)

    map_generator.export_file(16, "map/map_16x16.txt", turn_reveal=7)
    map_generator.export_file(32, "map/map_32x32.txt", turn_reveal=10)
    map_generator.export_file(64, "map/map_64x64.txt", turn_reveal=13)
    map_generator.export_file(70, "map/map_70x70.txt", turn_reveal=16)
    map_generator.export_file(74, "map/map_74x74.txt", turn_reveal=20)
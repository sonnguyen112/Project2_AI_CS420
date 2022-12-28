import random

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
                        map[temp[0]+i[0]][temp[1]+i[1]] = str(map[temp[0]+i[0]][temp[1]+i[1]]) + "M"
                        index_mountain += 1
                        if index_mountain == len_mountain:
                            break
        
        num_prison = (size*3)//16
        for _ in range(num_prison):
            pos = (random.randint(1, size-2), random.randint(1, size-2))
            while map[pos[0]][pos[1]] == 0 or "M" in str(map[pos[0]][pos[1]]):
                pos = (random.randint(1, size-2), random.randint(1, size-2))
            
            map[pos[0]][pos[1]] = str(map[pos[0]][pos[1]]) + "P"

        map = Map(map)
        return map

# map_generate = MapGenerateTool()
# print(map_generate.generate_map(16, 7))
# print(map_generate.generate_map(16, 7).get_map())

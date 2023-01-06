from tkinter import *
import pickle
import random
import tkinter.scrolledtext as scrolledtext


class VisualizationTool():
    def __init__(self, log_file) -> None:
        with open(log_file, 'rb') as handle:
            self.__log = pickle.load(handle)
        self.__root = Tk()
        self.__root.attributes('-fullscreen', True)
        self.__root.configure(bg="black")
        self.__map_frame = Frame(self.__root, width=800, height=800)
        self.__right_frame = Frame(self.__root, width=800, height=800)
        self.__note_frame = Frame(
            self.__right_frame, width=800, height=200, bg="red")
        self.__log_frame = Frame(
            self.__right_frame, width=800, height=600, bg="yellow")
        self.__log_text = scrolledtext.ScrolledText(
            self.__log_frame, undo=True)
        self.__log_text['font'] = ('consolas', '12')
        self.__num_region = self.__log["num_of_region"]
        self.__map = self.__log["map"]
        self.__agent_pos = self.__log["agent_pos_init"]
        self.__agent_pos_init = self.__log["agent_pos_init"]
        self.__pirate_pos = None
        self.__treasure_pos = self.__log["treasure_pos"]
        if self.__num_region > 10:
            self.__color_list = ["blue"] + ["#"+''.join([random.choice(
                '0123456789ABCDEF') for j in range(6)])for i in range(self.__num_region - 1)]
            while len(self.__color_list) != len(set(self.__color_list)):
                self.__color_list = ["blue"] + ["#"+''.join([random.choice(
                    '0123456789ABCDEF') for j in range(6)])for i in range(self.__num_region - 1)]
        else:
            self.__color_list = ["blue", "#f5d442", "#a7f542", "#42f5cb",
                                 "#646373", "#9245bf", "#3af20c", "#e8469f", "#e00744", "#8f727a"]
        self.__list_tiles_not_include_treasure = []
        self.__list_tiles_include_treasure = []
        self.__all_labels = []
        self.__list_drawn_tile = []
        self.action_visual_list = []
        for index, action_visual in enumerate(self.__log["machine_turn"]):
            self.action_visual_list.append({
                "type" : "hint",
                "list_tile": action_visual["hint"][0]["list_tiles"],
                "description": action_visual["hint"][0]["description"],
                "pos": action_visual["hint"][0]["pos"],
                "pirate_pos" : action_visual["pirate_pos"]
            })
            if index == 0:
                self.action_visual_list.append({
                    "type": "first_check_hint",
                    "list_not_include": action_visual["first_check_hint"],
                    "pos": self.__agent_pos,
                    "pirate_pos" : None,
                    "description": None
                })
            self.action_visual_list.append({
                "type": "action_1",
                "list_not_include": action_visual["action_1"]["list_tiles_not_include_treasure"],
                "pos": action_visual["action_1"]["pos"],
                "description": action_visual["action_1"]["description"],
                "pirate_pos" : action_visual["pirate_pos"]
            })
            self.action_visual_list.append({
                "type": "action_2",
                "list_not_include": action_visual["action_2"]["list_tiles_not_include_treasure"],
                "pos": action_visual["action_2"]["pos"],
                "description": action_visual["action_1"]["description"],
                "pirate_pos" : action_visual["pirate_pos"]
            })
        self.__actual_turn = 1
        self.__draw_red_list = []



    def __close_win(self, e):
        self.__root.destroy()

    def __click_left(self, e):
        if self.__turn > 0:
            self.__turn -= 1
            self.__update_game()

    def __click_right(self, e):
        if self.__turn < len(self.action_visual_list):
            self.__turn += 1
            self.__update_game()

    def __update_game(self):
        self.__actual_turn = 1

        for tile in self.__list_drawn_tile:
            # if tile["text"] != None:
            #     tile["canvas"].delete(tile["text"])
            tile["canvas"].configure(highlightbackground="white", highlightthickness=1)
            tile["canvas"].configure(bg=self.__color_list[int(self.__map[tile["pos"][0]][tile["pos"][1]][0])])
        self.__list_drawn_tile = []

        prev_pos_agent = (self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]])
        prev_pos_pirate = None
        # prev_red_border_list = self.__list_tiles_include_treasure

        self.__log_text.configure(state="normal")
        self.__log_text.delete('1.0', END)
        self.__log_text.insert(INSERT,
                               f"""\
Game start
Agent appears at [{self.__agent_pos_init[0]},{self.__agent_pos_init[1]}]
The pirate’s prison is going to reveal the at the beginning of {self.__log["turn_pirate_reveal"]}rd turn
The pirate is free at the beginning of the {self.__log["turn_pirate_free"]}th turn
""")    
        # if self.__turn == 0:
        #     text = self.__all_labels[self.__agent_pos_init[0]][self.__agent_pos_init[1]]["canvas"].create_text(int(self.__all_labels[self.__agent_pos_init[0]][self.__agent_pos_init[1]]["canvas"]["width"]) // 2, int(
        #                     self.__all_labels[self.__agent_pos_init[0]][self.__agent_pos_init[1]]["canvas"]["height"]) // 2, text="A", fill="black", font=('Helvetica 15 bold'))
        #     self.__all_labels[self.__agent_pos_init[0]][self.__agent_pos_init[1]]["text"] = text
        #     prev_pos_agent = (self.__all_labels[self.__agent_pos_init[0]][self.__agent_pos_init[1]])
        #     self.__list_drawn_tile.append(self.__all_labels[self.__agent_pos_init[0]][self.__agent_pos_init[1]])

        for turn in range(self.__turn):
            for tile in self.__list_drawn_tile:
                tile["canvas"].configure(highlightbackground="white", highlightthickness=1)
            self.__list_drawn_tile = []
            # if self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["text"] != None:
            #     self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["canvas"].delete(self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["text"])
            # for tile in self.__list_tiles_include_treasure:
            #     self.__all_labels[tile[0]][tile[1]]["canvas"].configure(highlightbackground="white", highlightthickness=1)
            # for tile in self.__list_tiles_not_include_treasure:
            #     if self.__all_labels[tile[0]][tile[1]]["text"] != None:
            #         self.__all_labels[tile[0]][tile[1]]["canvas"].delete(self.__all_labels[tile[0]][tile[1]]["text"])
            #     self.__all_labels[tile[0]][tile[1]]["canvas"].configure(bg=self.__color_list[int(
            #                 self.__map[tile[0]][tile[1]][0])])
            # for tile in prev_red_border_list:
            #     self.__all_labels[tile[0]][tile[1]]["canvas"].configure(highlightbackground="white", highlightthickness=1)
            prev_pos_agent["canvas"].delete(prev_pos_agent["text"])
            if self.__pirate_pos != None:
                prev_pos_pirate["canvas"].delete(prev_pos_pirate["text"])
            machine_log = self.action_visual_list[turn]
            print("MACHINE LOG")
            print(machine_log)
            if machine_log["type"] == "hint":
                self.__agent_pos = machine_log["pos"]


                for tile in machine_log["list_tile"]:
                    self.__all_labels[tile[0]][tile[1]]["canvas"].configure(highlightbackground="red", highlightthickness=1)
                    self.__list_drawn_tile.append(self.__all_labels[tile[0]][tile[1]])
                    self.__draw_red_list.append(self.__all_labels[tile[0]][tile[1]])
                        

                text = self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["canvas"].create_text(int(self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["canvas"]["width"]) // 2, int(
                            self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["canvas"]["height"]) // 2, text="A", fill="black", font=('Helvetica 15 bold'))
                self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["text"] = text
                prev_pos_agent = (self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]])
                self.__list_drawn_tile.append(self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]])   
            else:
                self.__agent_pos = machine_log["pos"]
                self.__list_tiles_not_include_treasure = machine_log["list_not_include"]
                
            # self.__list_tiles_include_treasure = machine_log["list_tiles_include_treasure"]
            # prev_red_border_list = self.__list_tiles_include_treasure
            

                for tile in self.__list_tiles_not_include_treasure:
                    # if self.__all_labels[tile[0]][tile[1]]["text"] != None:
                        # self.__all_labels[tile[0]][tile[1]]["canvas"].delete(self.__all_labels[tile[0]][tile[1]]["text"])
                    self.__all_labels[tile[0]][tile[1]]["canvas"].configure(bg="#f5eded")
                    self.__list_drawn_tile.append(self.__all_labels[tile[0]][tile[1]])

                text = self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["canvas"].create_text(int(self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["canvas"]["width"]) // 2, int(
                            self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["canvas"]["height"]) // 2, text="A", fill="black", font=('Helvetica 15 bold'))
                self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]]["text"] = text
                prev_pos_agent = (self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]])
                self.__list_drawn_tile.append(self.__all_labels[self.__agent_pos[0]][self.__agent_pos[1]])

                self.__pirate_pos = machine_log["pirate_pos"]
                if self.__pirate_pos != None:
                    text = self.__all_labels[self.__pirate_pos[0]][self.__pirate_pos[1]]["canvas"].create_text(int(self.__all_labels[self.__pirate_pos[0]][self.__pirate_pos[1]]["canvas"]["width"]) // 2, int(
                            self.__all_labels[self.__pirate_pos[0]][self.__pirate_pos[1]]["canvas"]["height"]) // 2, text="Pi", fill="black", font=('Helvetica 15 bold'))
                    self.__all_labels[self.__pirate_pos[0]][self.__pirate_pos[1]]["text"] = text
                    prev_pos_pirate = (self.__all_labels[self.__pirate_pos[0]][self.__pirate_pos[1]])
                    self.__list_drawn_tile.append(self.__all_labels[self.__pirate_pos[0]][self.__pirate_pos[1]])

            # for tile in self.__list_tiles_include_treasure:
            #     self.__all_labels[tile[0]][tile[1]]["canvas"].configure(highlightbackground="red", highlightthickness=1)
            #     self.__list_drawn_tile.append(self.__all_labels[tile[0]][tile[1]])

#             human_log = self.__log["human_turn"][turn]
            if machine_log["type"] == "hint":
                self.__log_text.insert(INSERT, f"""\
START TURN {self.__actual_turn}
""")        
            if machine_log["pirate_pos"] != None:
                self.__log_text.insert(INSERT, f"""\
The pirate is at the ({machine_log["pirate_pos"][0]}, {machine_log["pirate_pos"][1]}) prison
""")        
            if machine_log["type"] == "hint":
                self.__log_text.insert(INSERT, f"""\
HINT {self.__actual_turn}: {machine_log["description"]}
ADD HINT{self.__actual_turn} TO HINT LIST
""")
            if turn + 1 == 2:
                self.__log_text.insert(INSERT, f"""\
HINT1: is_verified = TRUE, is_truth = TRUE
""")        
            if machine_log["type"] != "hint" and machine_log["description"] != None:
                self.__log_text.insert(INSERT, f"""\
{machine_log["description"]}
""")        
            if machine_log["type"] == "action_2":
                self.__log_text.insert(INSERT, f"""\
END TURN {self.__actual_turn}
""")      
                self.__actual_turn += 1
        self.__log_text.configure(state="disable")
        self.__log_text.see(END)

    def __render_map(self):
        for i in range(len(self.__map)+1):
            if i == 0:
                for j in range(len(self.__map)+1):
                    label = Canvas(
                        self.__map_frame, bg="gray",
                        width=int(self.__map_frame["width"])//(len(self.__map) + 1) - 2,
                        height=int(self.__map_frame["height"])//(len(self.__map) + 1) - 2, highlightthickness=1, highlightbackground="white")
                    if j != 0:
                        label.create_text(int(label["width"]) // 2, int(label["height"]) // 2,
                                      text=str(j-1), fill="black", font=('Helvetica 15 bold'))
                    label.grid(row=i, column=j)
            
            else:
                label = Canvas(
                    self.__map_frame, bg="gray",
                        width=int(self.__map_frame["width"])//(len(self.__map) + 1) - 2,
                        height=int(self.__map_frame["height"])//(len(self.__map) + 1) - 2, highlightthickness=1, highlightbackground="white")
                label.create_text(int(label["width"]) // 2, int(label["height"]) // 2,
                                      text=str(i-1), fill="black", font=('Helvetica 15 bold'))
                label.grid(row=i, column=0)

        for index_row in range((len(self.__map))):
            row_label = []
            for index_col in range((len(self.__map))):
                label = Canvas(
                    self.__map_frame, bg=self.__color_list[int(
                        self.__map[index_row][index_col][0])],
                    width=int(self.__map_frame["width"])//(len(self.__map) + 1) - 2,
                    height=int(self.__map_frame["height"])//(len(self.__map) + 1) - 2, highlightthickness=1, highlightbackground="white")
                text = None
                if self.__map[index_row][index_col][-1] == "M" or self.__map[index_row][index_col][-1] == "P":
                    text = label.create_text(int(label["width"]) // 2, int(label["height"]) // 2,
                                      text=self.__map[index_row][index_col][-1], fill="white", font=('Helvetica 15 bold'))
                if index_row == self.__agent_pos[0] and index_col == self.__agent_pos[1]:
                    text = label.create_text(int(label["width"]) // 2, int(
                        label["height"]) // 2, text="A", fill="white", font=('Helvetica 15 bold'))
                if self.__pirate_pos != None:
                    if index_row == self.__pirate_pos[0] and index_col == self.__pirate_pos[1]:
                        text = label.create_text(int(label["width"]) // 2, int(
                            label["height"]) // 2, text="Pi", fill="white", font=('Helvetica 15 bold'))
                if index_row == self.__treasure_pos[0] and index_col == self.__treasure_pos[1]:
                    text = label.create_text(int(label["width"]) // 2, int(
                        label["height"]) // 2, text="T", fill="yellow", font=('Helvetica 15 bold'))

                label.grid(row=index_row + 1, column=index_col + 1)
                row_label.append({
                    "canvas": label,
                    "text" : text,
                    "pos": (index_row, index_col)
                })
            self.__all_labels.append(row_label)

    def visualize(self):
        self.__turn = 0
        self.__map_frame.grid(row=0, column=0)
        self.__right_frame.grid(row=0, column=1)
        self.__log_frame.grid(row=0, column=0)
        self.__note_frame.grid(row=1, column=0, sticky="news")
        self.__render_map()

        i = 0
        j = 0
        num_row = self.__num_region//5 + 1
        for index in range(self.__num_region):
            note = Canvas(self.__note_frame, width=(self.__note_frame["width"] // self.__num_region) - 20, height=(
                self.__note_frame["height"] // num_row)-20, bg=self.__color_list[index])
            note.create_text(int(note["width"]) // 2, int(note["height"]) //
                             2, text=str(index), fill="white", font=('Helvetica 15 bold'))
            note.grid(row=i, column=j, padx=(0, 20), pady=(0, 20))
            if j == 4:
                i += 1
                j = 0
            else:
                j += 1

        self.__log_text.pack(expand=True, fill='both')
        
        self.__log_text.insert(INSERT,
                               f"""\
Game start
Agent appears at [{self.__agent_pos[0]},{self.__agent_pos[1]}]
The pirate’s prison is going to reveal the at the beginning of {self.__log["turn_pirate_reveal"]}rd turn
The pirate is free at the beginning of the {self.__log["turn_pirate_free"]}th turn
""")
        self.__log_text.configure(state="disable")

        self.__root.bind('<Escape>', lambda e: self.__close_win(e))
        self.__root.bind('<Left>', self.__click_left)
        self.__root.bind('<Right>', self.__click_right)
        self.__root.mainloop()


visualize_tool = VisualizationTool("logs/log_1.pickle")
visualize_tool.visualize()

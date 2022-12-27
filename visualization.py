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
        self.__log_text = scrolledtext.ScrolledText(self.__log_frame, undo=True)
        self.__log_text['font'] = ('consolas', '12')
        self.__num_region = self.__log["num_of_region"]
        self.__map = self.__log["map"]
        self.__agent_pos = self.__log["agent_pos_init"]
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

    def __close_win(self, e):
        self.__root.destroy()

    def __click_left(self, e):
        if self.__turn > 1:
            self.__turn -= 1
            print(self.__turn)

    def __click_right(self, e):
        if self.__turn < len(self.__log["machine_turn"]):
            self.__turn += 1
            print(self.__turn)

    def visualize(self):
        self.__turn = 1
        self.__map_frame.grid(row=0, column=0)
        self.__right_frame.grid(row=0, column=1)
        self.__log_frame.grid(row=0, column=0)
        self.__note_frame.grid(row=1, column=0, sticky="news")
        all_labels = []
        for index_row in range(len(self.__map)):
            row_labels = []
            for index_col in range(len(self.__map)):
                label = Canvas(
                    self.__map_frame, bg=self.__color_list[int(
                        self.__map[index_row][index_col][0])],
                    width=int(self.__map_frame["width"])//len(self.__map),
                    height=int(self.__map_frame["height"])//len(self.__map), highlightthickness=1, highlightbackground="white")
                if self.__map[index_row][index_col][-1] == "M" or self.__map[index_row][index_col][-1] == "P":
                    label.create_text(int(label["width"]) // 2, int(label["height"]) // 2,
                                      text=self.__map[index_row][index_col][-1], fill="white", font=('Helvetica 15 bold'))
                if index_row == self.__agent_pos[0] and index_col == self.__agent_pos[1]:
                    label.create_text(int(label["width"]) // 2, int(
                        label["height"]) // 2, text="A", fill="white", font=('Helvetica 15 bold'))
                if index_row == self.__treasure_pos[0] and index_col == self.__treasure_pos[1]:
                    label.create_text(int(label["width"]) // 2, int(
                        label["height"]) // 2, text="T", fill="yellow", font=('Helvetica 15 bold'))
                label.grid(row=index_row, column=index_col)
                row_labels.append(label)
            all_labels.append(row_labels)

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
        self.__root.bind('<Left>', lambda e: self.__click_left(e))
        self.__root.bind('<Right>', lambda e: self.__click_right(e))
        self.__root.mainloop()


visualize_tool = VisualizationTool("log.pickle")
visualize_tool.visualize()

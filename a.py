import tkinter
import tkinter.scrolledtext as scrolledtext

main_window = tkinter.Tk()

txt = scrolledtext.ScrolledText(main_window, undo=True)
txt['font'] = ('consolas', '12')
txt.pack(expand=True, fill='both')

main_window.mainloop()
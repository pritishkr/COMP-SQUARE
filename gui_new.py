from curses import panel
import tkinter as tk
from tkinter import BOTH, HORIZONTAL, VERTICAL, Label, filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.ttk import PanedWindow
from turtle import bgcolor, right

root = tk.Tk()


# Gui-window-size
root.title('SOLVE DIFFERENTIAL EQUATIONS!')
root.minsize(650,500)

# ------------- Menu Bar --------------

# ------------ Open File-Box on open
def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


# Creating Menubar
menubar = tk.Menu(root)

# Adding File Menu and commands
file = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = lambda:select_file())
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Pre-Processor Menu and commands
pre_processor = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Pre-Processor', menu = pre_processor)


# Adding Solver Menu
solver = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Solver', menu = solver)

# Adding Post-Processor Menu
postprocessor = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Post-Processor', menu = postprocessor)


# ------------- Menu Bar Ends--------------





# display Menu
root.config(menu = menubar)

root.mainloop()
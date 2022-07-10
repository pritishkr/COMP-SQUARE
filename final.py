from cProfile import label
from cgitb import text
from multiprocessing import dummy
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from turtle import fd


# creating tkinter window
root = Tk()

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
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Pre-Processor Menu and commands
pre_processor = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Pre-Processor', menu = pre_processor)


# Adding Solver Menu
solver = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Solver', menu = solver)

# Adding Post-Processor Menu
postprocessor = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Post-Processor', menu = postprocessor)

# ------------ menu bar ends -------------------

# ------------ Panels --------------------------

# panedwindow object
pw = PanedWindow()
pw.pack(fill=BOTH, expand=1)

hor_pw = PanedWindow(pw,orient=VERTICAL)
right_pw = PanedWindow(pw,orient=VERTICAL)
pw.add(hor_pw)
pw.add(right_pw)

# ------------ Right paned window commands --------

# ------------ first button NO OF BLOCKS -----------
Nblocks_text = Label(right_pw, text="Enter the No. of blocks: -")
Nblocks_entry = Entry(right_pw)
Nblocks_entry.insert(0,"1")
NI_text = Label(right_pw,text="Enter the value of NI: -")
NI_entry = Entry(right_pw)
NI_entry.insert(0,"192")
NJ_text = Label(right_pw,text="Enter the value of NJ: -")
NJ_entry = Entry(right_pw)
NJ_entry.insert(0,"192")
NK_text = Label(right_pw, text="Enter the value of NK: -")
NK_entry = Entry(right_pw)
NK_entry.insert(0,"192")
NMAX_text = Label(right_pw,text="Enter the value of NMAX: -")
NMAX_entry = Entry(right_pw)
NMAX_entry.insert(0,"192")
Nblocks_save = Button(right_pw,text="SAVE")


# ----------- Commands to Panels ---------------
def Nblocks_cmd():
    right_pw.add(Nblocks_text)
    right_pw.add(Nblocks_entry)
    right_pw.add(NI_text)
    right_pw.add(NI_entry)
    right_pw.add(NJ_text)
    right_pw.add(NJ_entry)
    right_pw.add(NK_text)
    right_pw.add(NK_entry)
    right_pw.add(NMAX_text)
    right_pw.add(NMAX_entry)
    right_pw.add(Nblocks_save)



# Button widget
Nblocks = Button(hor_pw, text ="No. of Blocks", command=Nblocks_cmd)
Scheme = Button(hor_pw, text ="Scheme")
Order = Button(hor_pw, text="Button")
Boundary_order = Button(hor_pw, text="Boundary Order")
filter_order = Button(hor_pw, text="Filter Order")
self_periodicity = Button(hor_pw, text="Self Periodicity")
animation = Button(hor_pw,text="Animation")
dummy_btn = Button(hor_pw)

# This will add button widget to the panedwindow
hor_pw.add(Nblocks)
hor_pw.add(Scheme)
hor_pw.add(Order)
hor_pw.add(Boundary_order)
hor_pw.add(filter_order)
hor_pw.add(self_periodicity)
hor_pw.add(animation)
hor_pw.add(dummy_btn)



# --------- Panels-End --------------------------

# display Menu
root.config(menu = menubar)
pw.configure(sashrelief = RAISED)
mainloop()

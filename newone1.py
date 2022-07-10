from cProfile import label
from cgitb import text
from multiprocessing import dummy
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from turtle import fd


# creating tkinter window
window = Tk()

# Gui-window-size
window.title('SOLVE DIFFERENTIAL EQUATIONS!')
window.minsize(1300,700)

# creating a main frame
main_frame = Frame(window)
main_frame.pack(fill=BOTH, expand=1)

# creating a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

# Adding a scroll bar to the canvas
my_scrollbar = Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

# configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create another frame inside the canvas
root = Frame(my_canvas)

# Add the new frame to window in the canvas
my_canvas.create_window((0,0),window=root, anchor="nw")


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
file.add_command(label ='Open...', command = select_file)
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

# set default button command
def setdefault():
    import Set_Default_Input

# ---- Zeroth line --------
Button(root, text = "Load From Previous").grid(row=0,column=3)
Button(root, text = "Set Default", command=setdefault).grid(row=0,column=4)

# first-line
Label(root, text="Nblocks: -").grid(row=2, column=0)
Label(root, text = "NImax: -").grid(row = 2, column = 2)
Label(root, text = "NJmax: -").grid(row = 2, column = 4)
Label(root, text = "NKmax: -").grid(row = 2, column = 6)
Label(root, text = "NMAX: -").grid(row = 2, column = 8)

# first-line
nblocks = IntVar(root)
nblocks = Entry(root,width=10)
nblocks.grid(row=2, column=1)

NImax = IntVar(root)
NImax = Entry(root, width=10)
NImax.grid(row = 2, column = 3)

NJmax = IntVar(root)
NJmax = Entry(root, width=10)
NJmax.grid(row = 2, column = 5)

NKmax = IntVar(root)
NKmax =Entry(root, width=10)
NKmax.grid(row = 2, column = 7)

maxindex = IntVar(root)
maxindex =Entry(root, width=10)
maxindex.grid(row = 2, column = 9)


# maxindex = IntVar(root,"100")
# maxindex = max(NImax,NJmax,NKmax)

# ------ second line ---------
Restart = IntVar(root,"10")
Radiobutton(root,text="FRESH",variable=Restart, value=1).grid(row=3,column=3)
Radiobutton(root,text="RESTART",variable=Restart,value=0).grid(row=3,column=4)

# -------Third line --------
Steady = IntVar(root,"10")
Radiobutton(root,text="STEADY",variable=Steady, value=1).grid(row=4,column=3)
Radiobutton(root,text="UNSTEADY",variable=Steady,value=0).grid(row=4,column=4)


# -------fourth line --------
Grid2D = IntVar(root,"10")
Radiobutton(root,text="2-DIMENSIONAL",variable=Grid2D, value=1).grid(row=5,column=3)
Radiobutton(root,text="3-DIMENSIONAL",variable=Grid2D,value=0).grid(row=5,column=4)

# --------- fifth line --------
viscosity = IntVar(root,"10")
Radiobutton(root,text="VISCOUS",variable=viscosity,value=1).grid(row=6,column=3)
Radiobutton(root,text="INVISCID",variable=viscosity,value=0).grid(row=6,column=4)

# --------- sixth line --------
compressibility = IntVar(root,"10")
Radiobutton(root,text="COMPRESSIBLE",variable=compressibility,value=1).grid(row=7,column=3)
Radiobutton(root,text="INCOMPRESSIBLE",variable=compressibility,value=0).grid(row=7,column=4)

# --------- seventh line --------
method = IntVar(root,"10")
Radiobutton(root,text="LES",variable=method,value=1).grid(row=8,column=3)
Radiobutton(root,text="K-OMEGA",variable=method,value=0).grid(row=8,column=4)

Wale = BooleanVar(root)
Checkbutton(root,text="WALE",variable=Wale).grid(row=8,column=5)

# Third-line entry values
Label(root, text="Pstag: -").grid(row=9, column=0)
Label(root, text = "Tstag: -").grid(row = 9, column = 2)
Label(root, text = "Pexit: -").grid(row = 9, column = 4)
Label(root, text = "Twall: -").grid(row = 9, column = 6)
Label(root, text = "L_Char: -").grid(row = 9, column = 8)
Label(root, text = "alpha_aoa: -").grid(row = 10, column = 2)
Label(root, text = "Mach_in: -").grid(row = 10, column = 4)
Label(root, text = "Re: -").grid(row = 10, column = 6)
Label(root, text = "Lref: -").grid(row = 10, column = 8)
Label(root, text = "phi_bw: -").grid(row = 11, column = 2)

# Third-line
P0 = DoubleVar(root)
P0 = Entry(root, width=10)
P0.grid(row=9, column=1)

T0 = DoubleVar(root)
T0 = Entry(root, width= 10)
T0.grid(row = 9, column = 3)

Pexit = DoubleVar(root)
Pexit = Entry(root, width= 10)
Pexit.grid(row = 9, column = 5)

Twall = DoubleVar(root)
Twall = Entry(root, width= 10)
Twall.grid(row = 9, column = 7)

Lchar = DoubleVar(root)
Lchar = Entry(root, width= 10)
Lchar.grid(row = 9, column = 9)

AoA = DoubleVar(root)
AoA = Entry(root, width= 10)
AoA.grid(row = 10, column = 3)

Mach = DoubleVar(root)
Mach = Entry(root, width= 10)
Mach.grid(row = 10, column = 5)

Re = DoubleVar(root)
Re = Entry(root, width= 10)
Re.grid(row = 10, column = 7)

Lref = DoubleVar(root)
Lref = Entry(root, width= 10)
Lref.grid(row = 10, column = 9)

phi_bw = DoubleVar(root)
phi_bw = Entry(root, width= 10)
phi_bw.grid(row = 11, column = 3)


# --------- ninth line --------
Interior_order = IntVar(root,"10")
Label(root, text = "INTERIOR ORDER: -").grid(row = 12, column = 1)
Radiobutton(root,text="E2",variable=Interior_order,value=1).grid(row=12,column=2)
Radiobutton(root,text="E4",variable=Interior_order,value=2).grid(row=12,column=3)
Radiobutton(root,text="C4",variable=Interior_order,value=3).grid(row=12,column=4)
Radiobutton(root,text="C6",variable=Interior_order,value=4).grid(row=12,column=5)

# --------- tenth line --------
boundary1 = IntVar(root,"10")
Label(root, text = "BOUNDARY 1: -").grid(row = 13, column = 1)
Radiobutton(root,text="2",variable=boundary1,value=2).grid(row=13,column=2)
Radiobutton(root,text="4",variable=boundary1,value=4).grid(row=13,column=3)

# --------- eleventh line --------
boundary2 = IntVar(root,"10")
Label(root, text = "BOUNDARY 2: -").grid(row = 14, column = 1)
Radiobutton(root,text="2",variable=boundary2,value=2).grid(row=14,column=2)
Radiobutton(root,text="4",variable=boundary2,value=4).grid(row=14,column=3)

# --------- twelfth line --------
orderk = IntVar(root,"10")
Label(root, text = "ORDER IN K: -").grid(row = 15, column = 1)
Radiobutton(root,text="E2",variable=orderk,value=1).grid(row=15,column=2)
Radiobutton(root,text="E4",variable=orderk,value=2).grid(row=15,column=3)
Radiobutton(root,text="C4",variable=orderk,value=3).grid(row=15,column=4)
Radiobutton(root,text="C6",variable=orderk,value=4).grid(row=15,column=5)

# --------- thirteenth line --------
boundaryk1 = IntVar(root,"10")
Label(root, text = "BOUNDARY K1: -").grid(row = 16, column = 1)
Radiobutton(root,text="2",variable=boundaryk1,value=2).grid(row=16,column=2)
Radiobutton(root,text="4",variable=boundaryk1,value=4).grid(row=16,column=3)

# --------- fourteenth line --------
boundaryk2 = IntVar(root,"10")
Label(root, text = "BOUNDARY K2: -").grid(row = 17, column = 1)
Radiobutton(root,text="2",variable=boundaryk2,value=2).grid(row=17,column=2)
Radiobutton(root,text="4",variable=boundaryk2,value=4).grid(row=17,column=3)

# Seventh-line
Label(root, text="alpha_f: -").grid(row=18, column=0)
alphaf = DoubleVar(root)
alphaf = Entry(root, width=10)
alphaf.grid(row=18, column=1)



# -------- fifteenth line -------
Label(root, text = "F Order i: -").grid(row = 19, column = 0)
# drop menu
drop_menu=StringVar()
drop_menu.set("Select")
#options
forderi = IntVar(root)
forderi = OptionMenu(root,drop_menu,"2","4","6","8","10")
forderi.grid(row=19,column=1)
Label(root, text = "F Order j: -").grid(row = 19, column = 2)
forderj = IntVar(root)
forderj = OptionMenu(root,drop_menu,"2","4","6","8","10")
forderj.grid(row=19,column=3)
Label(root, text = "F Order K: -").grid(row = 19, column = 4)
forderk = IntVar(root)
forderk = OptionMenu(root,drop_menu,"2","4","6","8","10")
forderk.grid(row=19,column=5)

# --------- sixteenth line --------
timeint = IntVar(root,"10")
Label(root, text = "Time Integration: -").grid(row = 20, column = 0)
Radiobutton(root,text="RK4",variable=timeint,value=1).grid(row=20,column=1)
Radiobutton(root,text="DTS",variable=timeint,value=2).grid(row=20,column=2)

# seventeenth-line
Label(root, text="CFL: -").grid(row=21, column=0)
Label(root, text = "niter: -").grid(row = 21, column = 2)
Label(root, text = "subiter: -").grid(row = 21, column = 4)
Label(root, text = "dt: -").grid(row = 21, column = 6)

# seventeenth-line
CFL = DoubleVar(root)
CFL = Entry(root,width=10)
CFL.grid(row=21, column=1)

niter = IntVar(root)
niter = Entry(root, width=10)
niter.grid(row = 21, column = 3)

subiter = IntVar(root)
subiter = Entry(root, width=10)
subiter.grid(row = 21, column = 5)

dt = DoubleVar(root)
dt =Entry(root, width=10)
dt.grid(row = 21, column = 7)


# --------- eighteenth line --------
NSCBC = IntVar(root,"10")
Label(root, text = "NSBC: -").grid(row = 22, column = 0)
Radiobutton(root,text="ON",variable=NSCBC,value=1).grid(row=22,column=1)
Radiobutton(root,text="OFF",variable=NSCBC,value=0).grid(row=22,column=2)

# nineteenth-line
Label(root, text="CBC Order: -").grid(row=23, column=0)
# nineteenth-line
CBC_order = IntVar(root)
Radiobutton(root,text="2",variable=CBC_order,value=2).grid(row=23,column=1)
Radiobutton(root,text="4",variable=CBC_order,value=4).grid(row=23,column=2)


# --------- twentieth line --------
Sponge = IntVar(root,"10")
Label(root, text = "SPONGE: -").grid(row = 24, column = 0)
Radiobutton(root,text="ON",variable=Sponge,value=1).grid(row=24,column=1)
Radiobutton(root,text="OFF",variable=Sponge,value=0).grid(row=24,column=2)

# line 11 entry values
Label(root, text="Sponge a: -").grid(row=25, column=0)
Label(root, text = "Sponge n: -").grid(row = 25, column = 2)
Label(root, text = "Sponge X1: -").grid(row = 25, column = 4)
Label(root, text = "Sponge Xh: -").grid(row = 25, column = 6)
Label(root, text = "Sponge Y1: -").grid(row = 25, column = 8)
Label(root, text = "Sponge Yh: -").grid(row = 26, column = 2)
Label(root, text = "Sponge Z1: -").grid(row = 26, column = 4)
Label(root, text = "Sponge Zh: -").grid(row = 26, column = 6)
Label(root, text = "Sponge radl: -").grid(row = 26, column = 8)
Label(root, text = "Sponge radh: -").grid(row = 27, column = 2)

# line 11
Sponge_a = DoubleVar(root)
Sponge_a = Entry(root, width=10)
Sponge_a.grid(row=25, column=1)

Sponge_n = DoubleVar(root)
Sponge_n = Entry(root, width= 10)
Sponge_n.grid(row = 25, column = 3)

Sponge_X1 = DoubleVar(root)
Sponge_X1 = Entry(root, width= 10)
Sponge_X1.grid(row = 25, column = 5)

Sponge_Xh = DoubleVar(root)
Sponge_Xh = Entry(root, width= 10)
Sponge_Xh.grid(row = 25, column = 7)

Sponge_Y1 = DoubleVar(root)
Sponge_Y1 = Entry(root, width= 10)
Sponge_Y1.grid(row = 25, column = 9)

Sponge_Yh = DoubleVar(root)
Sponge_Yh = Entry(root, width= 10)
Sponge_Yh.grid(row = 26, column = 3)

Sponge_Z1 = DoubleVar(root)
Sponge_Z1 = Entry(root, width= 10)
Sponge_Z1.grid(row = 26, column = 5)

Sponge_Zh = DoubleVar(root)
Sponge_Zh = Entry(root, width= 10)
Sponge_Zh.grid(row = 26, column = 7)

Sponge_radl = DoubleVar(root)
Sponge_radl = Entry(root, width= 10)
Sponge_radl.grid(row = 26, column = 9)

Sponge_radh = DoubleVar(root)
Sponge_radh = Entry(root, width= 10)
Sponge_radh.grid(row = 27, column = 3)



# 21st line
Animate = IntVar(root,"10")
Label(root, text = "ANIMATE: -").grid(row = 29, column = 0)
Radiobutton(root,text="ON",variable=Animate,value=1).grid(row=29,column=1)
Radiobutton(root,text="OFF",variable=Animate,value=0).grid(row=29,column=2)

# line 12 entry values
Label(root, text="ANIM-FILENAME: -").grid(row=30, column=0)
Label(root, text = "ANIM-FREQUENCY: -").grid(row = 30, column = 2)
Label(root, text = "BACK-FREQUENCY: -").grid(row = 30, column = 4)

# line 13
Anim_filename = IntVar(root)
Anim_filename = Entry(root, width=10)
Anim_filename.grid(row=30, column=1)

Anim_frequency = IntVar(root)
Anim_frequency = Entry(root, width= 10)
Anim_frequency.grid(row = 30, column = 3)

Back_frequency = IntVar(root)
Back_frequency = Entry(root, width= 10)
Back_frequency.grid(row = 30, column = 5)


# line 14
Average = IntVar(root,"10")
Label(root, text = "AVERAGE: -").grid(row = 31, column = 0)
Radiobutton(root,text="ON",variable=Average,value=1).grid(row=31,column=1)
Radiobutton(root,text="OFF",variable=Average,value=0).grid(row=31,column=2)
# line 14 contd
Average_restart = IntVar(root,"10")
Label(root, text = "AVERAGE RESTART: -").grid(row = 32, column = 0)
Radiobutton(root,text="ON",variable=Average_restart,value=1).grid(row=32,column=1)
Radiobutton(root,text="OFF",variable=Average_restart,value=0).grid(row=32,column=2)

# Line 15
Label(root, text = "PERIODICITY: -").grid(row = 33, column = 0)
SelfI = BooleanVar(root,"0")
SelfJ = BooleanVar(root,"0")
SelfK = BooleanVar(root,"0")
Checkbutton(root,text="I",variable=SelfI).grid(row=33,column=1)
Checkbutton(root,text="j",variable=SelfJ).grid(row=33,column=2)
Checkbutton(root,text="K",variable=SelfK).grid(row=33,column=3)

# Line 16
bulkturb = IntVar(root,"10")
Label(root, text = "BULK TURBULENCE: -").grid(row = 34, column = 0)
Radiobutton(root,text="ON",variable=bulkturb,value=1).grid(row=34,column=1)
Radiobutton(root,text="OFF",variable=bulkturb,value=0).grid(row=34,column=2)

# Line 17
channel_flow = IntVar(root,"10")
Label(root, text = "CHANNEL CASE: -").grid(row = 35, column = 0)
Radiobutton(root,text="ON",variable=channel_flow,value=1).grid(row=35,column=1)
Radiobutton(root,text="OFF",variable=channel_flow,value=0).grid(row=35,column=2)

# Line 18
channel_restart = IntVar(root,"10")
Label(root, text = "CHANNEL RESTART: -").grid(row = 36, column = 0)
Radiobutton(root,text="ON",variable=channel_restart,value=1).grid(row=36,column=1)
Radiobutton(root,text="OFF",variable=channel_restart,value=0).grid(row=36,column=2)

# Line 19
taylor_case = IntVar(root,"10")
Label(root, text = "TAYLOR CASE: -").grid(row = 37, column = 0)
Radiobutton(root,text="ON",variable=taylor_case,value=1).grid(row=37,column=1)
Radiobutton(root,text="OFF",variable=taylor_case,value=0).grid(row=37,column=2)

# Line 20
Rsv = IntVar(root,"10")
Label(root, text = "RSV CASE: -").grid(row = 38, column = 0)
Radiobutton(root,text="ON",variable=Rsv,value=1).grid(row=38,column=1)
Radiobutton(root,text="OFF",variable=Rsv,value=0).grid(row=38,column=2)

# Line 19
IBM = IntVar(root,"10")
Label(root, text = "IBM: -").grid(row = 39, column = 0)
Radiobutton(root,text="ON",variable=IBM,value=1).grid(row=39,column=1)
Radiobutton(root,text="OFF",variable=IBM,value=0).grid(row=39,column=2)

# line 19 entry values
Label(root, text="MUL: -").grid(row=40, column=0)
Label(root, text = "MOVING OBJ: -").grid(row = 40, column = 2)
Label(root, text = "DEL X: -").grid(row = 40, column = 4)

# line 19
mu1 = IntVar(root)
mu1 = Entry(root, width=10)
mu1.grid(row=40, column=1)

moving_obj = IntVar(root)
moving_obj = Entry(root, width= 10)
moving_obj.grid(row = 40, column = 3)

del_x = IntVar(root)
del_x = Entry(root, width= 10)
del_x.grid(row = 40, column = 5)


# line 20 entry values
Label(root, text="NODES: -").grid(row=41, column=0)
Label(root, text = "ELEMENTS: -").grid(row = 41, column = 2)
Label(root, text = "SPTS1 LIMIT: -").grid(row = 41, column = 4)
Label(root, text = "FLUID POINTS: -").grid(row = 41, column = 6)

# line 20
nodes = IntVar(root)
nodes = Entry(root, width=10)
nodes.grid(row=41, column=1)

elements = IntVar(root)
elements = Entry(root, width= 10)
elements.grid(row = 41, column = 3)

SPTS1_limit = IntVar(root)
SPTS1_limit = Entry(root, width= 10)
SPTS1_limit.grid(row = 41, column = 5)

fluid_points = IntVar(root)
fluid_points = Entry(root, width= 10)
fluid_points.grid(row = 41, column = 7)


# line 21 entry values
Label(root, text="Y_TOP: -").grid(row=42, column=0)
Label(root, text = "Y_BOT: -").grid(row = 42, column = 2)
Label(root, text = "Y_PER: -").grid(row = 42, column = 4)

# line 21
ytop = DoubleVar(root)
ytop = Entry(root, width=10)
ytop.grid(row=42, column=1)

ybot = DoubleVar(root)
ybot = Entry(root, width= 10)
ybot.grid(row = 42, column = 3)

yper = IntVar(root)
yper = Entry(root, width= 10)
yper.grid(row = 42, column = 5)


# line 22 entry values
Label(root, text="IB_U: -").grid(row=43, column=0)
Label(root, text = "IB_V: -").grid(row = 43, column = 2)
Label(root, text = "IB_W: -").grid(row = 43, column = 4)
Label(root, text = "IB_T: -").grid(row = 43, column = 6)

# line 22
IB_U = DoubleVar(root)
IB_U = Entry(root, width=10)
IB_U.grid(row=43, column=1)

IB_V = DoubleVar(root)
IB_V = Entry(root, width= 10)
IB_V.grid(row = 43, column = 3)

IB_W = DoubleVar(root)
IB_W = Entry(root, width= 10)
IB_W.grid(row = 43, column = 5)

IB_T = DoubleVar(root)
IB_T = Entry(root, width= 10)
IB_T.grid(row = 43, column = 7)


# Line 23
Skew_symmetric = IntVar(root,"10")
Label(root, text = "SKEW SYMMETRIC: -").grid(row = 44, column = 0)
Radiobutton(root,text="ON",variable=Skew_symmetric,value=1).grid(row=44,column=1)
Radiobutton(root,text="OFF",variable=Skew_symmetric,value=0).grid(row=44,column=2)

# line 23 entry values
Label(root, text="EXP FILTER: -").grid(row=45, column=0)
Label(root, text = "SIG FILTER: -").grid(row = 45, column = 2)

# line 23
exp_filter = IntVar(root)
exp_filter = Entry(root, width=10)
exp_filter.grid(row=45, column=1)

sig_filter = IntVar(root)
sig_filter = Entry(root, width= 10)
sig_filter.grid(row = 45, column = 3)


# Line 24
probe = IntVar(root,"10")
Label(root, text = "PROBE: -").grid(row = 46, column = 0)
Radiobutton(root,text="ON",variable=probe,value=1).grid(row=46,column=1)
Radiobutton(root,text="OFF",variable=probe,value=0).grid(row=46,column=2)

# line 25 entry values
Label(root, text="Probe points: -").grid(row=47, column=0)

# line 25
probe_pts = IntVar(root)
probe_pts = Entry(root, width=10)
probe_pts.grid(row=47, column=1)


# Line 24
inflow_turb = IntVar(root,"10")
Label(root, text = "INFLOW TURBULENCE: -").grid(row = 48, column = 0)
Radiobutton(root,text="ON",variable=inflow_turb,value=1).grid(row=48,column=1)
Radiobutton(root,text="OFF",variable=inflow_turb,value=0).grid(row=48,column=2)

# line 25 entry values
Label(root, text="NUM EDDIES: -").grid(row=49, column=0)

# line 25
Num_eddies = IntVar(root)
Num_eddies = Entry(root, width=10)
Num_eddies.grid(row=49, column=1)


# Line 25
Eddy_func = IntVar(root,"10")
Label(root, text = "EDDY FUNCTION: -").grid(row = 50, column = 0)
Radiobutton(root,text="TENT",variable=Eddy_func,value=1).grid(row=50,column=1)
Radiobutton(root,text="STEP",variable=Eddy_func,value=0).grid(row=50,column=2)

# line 25 entry values
Label(root, text="Sigma: -").grid(row=51, column=0)
Label(root, text = "BoxLx: -").grid(row = 51, column = 2)
Label(root, text = "BoxLy: -").grid(row = 51, column = 4)
Label(root, text = "BoxLz: -").grid(row = 51, column = 6)
Label(root, text = "Turb Intensity: -").grid(row = 51, column = 8)

# line 25
sigma = DoubleVar(root)
sigma = Entry(root, width=10)
sigma.grid(row=51, column=1)

BoxLx = DoubleVar(root)
BoxLx = Entry(root, width= 10)
BoxLx.grid(row = 51, column = 3)

BoxLy = DoubleVar(root)
BoxLy = Entry(root, width= 10)
BoxLy.grid(row = 51, column = 5)

BoxLz = DoubleVar(root)
BoxLz = Entry(root, width= 10)
BoxLz.grid(row = 51, column = 7)

Turb_Intensity = DoubleVar(root)
Turb_Intensity = Entry(root, width= 10)
Turb_Intensity.grid(row = 51, column = 9)


# line 26 entry values
Label(root, text="Dx: -").grid(row=52, column=0)
Label(root, text = "Dy: -").grid(row = 52, column = 2)
Label(root, text = "Dz: -").grid(row = 52, column = 4)

# line 26
Dx = DoubleVar(root)
Dx = Entry(root, width=10)
Dx.grid(row=52, column=1)

Dy = DoubleVar(root)
Dy = Entry(root, width= 10)
Dy.grid(row = 52, column = 3)

Dz = DoubleVar(root)
Dz = Entry(root, width= 10)
Dz.grid(row = 52, column = 5)






# run button commands
def geninputfile():
    import Write_input.py



# run button
Button(root, text = "GENERATE INPUT FILE", command=geninputfile).grid(row=54,column=3)








# display Menu
window.config(menu = menubar)
mainloop()
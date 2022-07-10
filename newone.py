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

# ---- Zeroth line --------
Button(root, text = "Load From Previous").grid(row=0,column=3)
Button(root, text = "Set Default").grid(row=0,column=4)

# first-line
Label(root, text="Nblocks: -").grid(row=2, column=0)
Label(root, text = "NImax: -").grid(row = 2, column = 2)
Label(root, text = "NJmax: -").grid(row = 2, column = 4)
Label(root, text = "NKmax: -").grid(row = 2, column = 6)
# Label(root, text = "NMAX: -").grid(row = 0, column = 8)

# first-line
nblocks = Entry(root,width=10)
nblocks.grid(row=2, column=1)
nblocks.insert(0,"1")

NImax = Entry(root, width=10)
NImax.grid(row = 2, column = 3)
NImax.insert(0,"100")

NJmax = Entry(root, width=10)
NJmax.grid(row = 2, column = 5)
NJmax.insert(0,"100")

NKmax =Entry(root, width=10)
NKmax.grid(row = 2, column = 7)
NKmax.insert(0,"100")

# maxindex = StringVar(root,"100")
# maxindex = max(NImax,NJmax,NKmax)

# ------ second line ---------
Restart = StringVar(root,"0")
Radiobutton(root,text="FRESH",variable=Restart, value=1).grid(row=3,column=3)
Radiobutton(root,text="RESTART",variable=Restart,value=0).grid(row=3,column=4)

# -------Third line --------
Steady = StringVar(root,"0")
Radiobutton(root,text="STEADY",variable=Steady, value=1).grid(row=4,column=3)
Radiobutton(root,text="UNSTEADY",variable=Steady,value=0).grid(row=4,column=4)


# -------fourth line --------
Grid2D = StringVar(root,"1")
Radiobutton(root,text="2-DIMENSIONAL",variable=Grid2D, value=1).grid(row=5,column=3)
Radiobutton(root,text="3-DIMENSIONAL",variable=Grid2D,value=0).grid(row=5,column=4)

# --------- fifth line --------
viscosity = StringVar(root,"1")
Radiobutton(root,text="VISCOUS",variable=viscosity,value=1).grid(row=6,column=3)
Radiobutton(root,text="INVISCID",variable=viscosity,value=0).grid(row=6,column=4)

# --------- sixth line --------
compressibility = StringVar(root,"1")
Radiobutton(root,text="COMPRESSIBLE",variable=compressibility,value=1).grid(row=7,column=3)
Radiobutton(root,text="INCOMPRESSIBLE",variable=compressibility,value=0).grid(row=7,column=4)

# --------- seventh line --------
method = StringVar(root,"1")
Radiobutton(root,text="LES",variable=method,value=1).grid(row=8,column=3)
Radiobutton(root,text="K-OMEGA",variable=method,value=0).grid(row=8,column=4)
Radiobutton(root,text="WALE",variable=method,value=0).grid(row=8,column=5)

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
P0 = Entry(root, width=10)
P0.grid(row=9, column=1)
P0.insert(0,"101325.0")

T0 = Entry(root, width= 10)
T0.grid(row = 9, column = 3)
T0.insert(0,"294.4")

Pexit = Entry(root, width= 10)
Pexit.grid(row = 9, column = 5)
Pexit.insert(0,"101325.0")

Twall = Entry(root, width= 10)
Twall.grid(row = 9, column = 7)
Twall.insert(0,"294.4")

Lchar = Entry(root, width= 10)
Lchar.grid(row = 9, column = 9)
Lchar.insert(0,"5.0")

AoA = Entry(root, width= 10)
AoA.grid(row = 10, column = 3)
AoA.insert(0,"0.0")

Mach = Entry(root, width= 10)
Mach.grid(row = 10, column = 5)
Mach.insert(0,"0.1")

Re = Entry(root, width= 10)
Re.grid(row = 10, column = 7)
Re.insert(0,"1600")

Lref = Entry(root, width= 10)
Lref.grid(row = 10, column = 9)
Lref.insert(0,"0.001524")

phi_bw = Entry(root, width= 10)
phi_bw.grid(row = 11, column = 3)
phi_bw.insert(0,"0.0")

# --------- ninth line --------
Interior_order = StringVar(root,"2")
Label(root, text = "INTERIOR ORDER: -").grid(row = 12, column = 1)
Radiobutton(root,text="E2",variable=Interior_order,value=1).grid(row=12,column=2)
Radiobutton(root,text="E4",variable=Interior_order,value=2).grid(row=12,column=3)
Radiobutton(root,text="C4",variable=Interior_order,value=3).grid(row=12,column=4)
Radiobutton(root,text="C6",variable=Interior_order,value=4).grid(row=12,column=5)

# --------- tenth line --------
boundary1 = StringVar(root,"2")
Label(root, text = "BOUNDARY 1: -").grid(row = 13, column = 1)
Radiobutton(root,text="2",variable=boundary1,value=2).grid(row=13,column=2)
Radiobutton(root,text="4",variable=boundary1,value=4).grid(row=13,column=3)

# --------- eleventh line --------
boundary2 = StringVar(root,"2")
Label(root, text = "BOUNDARY 2: -").grid(row = 14, column = 1)
Radiobutton(root,text="2",variable=boundary2,value=2).grid(row=14,column=2)
Radiobutton(root,text="4",variable=boundary2,value=4).grid(row=14,column=3)

# --------- twelfth line --------
orderk = StringVar(root,"1")
Label(root, text = "ORDER IN K: -").grid(row = 15, column = 1)
Radiobutton(root,text="E2",variable=orderk,value=1).grid(row=15,column=2)
Radiobutton(root,text="E4",variable=orderk,value=2).grid(row=15,column=3)
Radiobutton(root,text="C4",variable=orderk,value=3).grid(row=15,column=4)
Radiobutton(root,text="C6",variable=orderk,value=4).grid(row=15,column=5)

# --------- thirteenth line --------
boundaryk1 = StringVar(root,"2")
Label(root, text = "BOUNDARY K1: -").grid(row = 16, column = 1)
Radiobutton(root,text="2",variable=boundaryk1,value=2).grid(row=16,column=2)
Radiobutton(root,text="4",variable=boundaryk1,value=4).grid(row=16,column=3)

# --------- fourteenth line --------
boundaryk2 = StringVar(root,"2")
Label(root, text = "BOUNDARY K2: -").grid(row = 17, column = 1)
Radiobutton(root,text="2",variable=boundaryk2,value=2).grid(row=17,column=2)
Radiobutton(root,text="4",variable=boundaryk2,value=4).grid(row=17,column=3)

# Seventh-line
Label(root, text="alpha_f: -").grid(row=18, column=0)
alphaf = Entry(root, width=10)
alphaf.grid(row=18, column=1)
alphaf.insert(0,"0.495")


# -------- fifteenth line -------
Label(root, text = "F Order i: -").grid(row = 19, column = 0)
# drop menu
drop_menu=StringVar()
drop_menu.set("Select")
#options
forderi = OptionMenu(root,drop_menu,"2","4","6","8","10")
forderi.grid(row=19,column=1)
Label(root, text = "F Order j: -").grid(row = 19, column = 2)
forderj = OptionMenu(root,drop_menu,"2","4","6","8","10")
forderj.grid(row=19,column=3)
Label(root, text = "F Order K: -").grid(row = 19, column = 4)
forderk = OptionMenu(root,drop_menu,"2","4","6","8","10")
forderk.grid(row=19,column=5)

# --------- sixteenth line --------
timeint = StringVar(root,"1")
Label(root, text = "Time Integration: -").grid(row = 20, column = 0)
Radiobutton(root,text="RK4",variable=timeint,value=1).grid(row=20,column=1)
Radiobutton(root,text="DTS",variable=timeint,value=2).grid(row=20,column=2)

# seventeenth-line
Label(root, text="CFL: -").grid(row=21, column=0)
Label(root, text = "niter: -").grid(row = 21, column = 2)
Label(root, text = "subiter: -").grid(row = 21, column = 4)
Label(root, text = "dt: -").grid(row = 21, column = 6)

# seventeenth-line
CFL = Entry(root,width=10)
CFL.grid(row=21, column=1)
CFL.insert(0,"1.0")

niter = Entry(root, width=10)
niter.grid(row = 21, column = 3)
niter.insert(0,"10000")

subiter = Entry(root, width=10)
subiter.grid(row = 21, column = 5)
subiter.insert(0,"10")

dt =Entry(root, width=10)
dt.grid(row = 21, column = 7)
dt.insert(0,"1e-3")

# --------- eighteenth line --------
NSCBC = StringVar(root,"0")
Label(root, text = "NSBC: -").grid(row = 22, column = 0)
Radiobutton(root,text="ON",variable=NSCBC,value=1).grid(row=22,column=1)
Radiobutton(root,text="OFF",variable=NSCBC,value=0).grid(row=22,column=2)

# nineteenth-line
Label(root, text="CBC Order: -").grid(row=23, column=0)
# nineteenth-line
CBC_order = Entry(root,width=10)
CBC_order.grid(row=23, column=1)
CBC_order.insert(0,"2")

# --------- twentieth line --------
Sponge = StringVar(root,"0")
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
Sponge_a = Entry(root, width=10)
Sponge_a.grid(row=25, column=1)
Sponge_a.insert(0,"0")

Sponge_n = Entry(root, width= 10)
Sponge_n.grid(row = 25, column = 3)
Sponge_n.insert(0,"0")

Sponge_X1 = Entry(root, width= 10)
Sponge_X1.grid(row = 25, column = 5)
Sponge_X1.insert(0,"0")

Sponge_Xh = Entry(root, width= 10)
Sponge_Xh.grid(row = 25, column = 7)
Sponge_Xh.insert(0,"0")

Sponge_Y1 = Entry(root, width= 10)
Sponge_Y1.grid(row = 25, column = 9)
Sponge_Y1.insert(0,"0")

Sponge_Yh = Entry(root, width= 10)
Sponge_Yh.grid(row = 26, column = 3)
Sponge_Yh.insert(0,"0")

Sponge_Z1 = Entry(root, width= 10)
Sponge_Z1.grid(row = 26, column = 5)
Sponge_Z1.insert(0,"0")

Sponge_Zh = Entry(root, width= 10)
Sponge_Zh.grid(row = 26, column = 7)
Sponge_Zh.insert(0,"0")

Sponge_radl = Entry(root, width= 10)
Sponge_radl.grid(row = 26, column = 9)
Sponge_radl.insert(0,"0")

Sponge_radh = Entry(root, width= 10)
Sponge_radh.grid(row = 27, column = 3)
Sponge_radh.insert(0,"0")

# line 12 entry values
Label(root, text="VISC: -").grid(row=28, column=0)
Label(root, text = "EDAC: -").grid(row = 28, column = 2)
Label(root, text = "ERM: -").grid(row = 28, column = 4)

# line 12
Visc = Entry(root, width=10)
Visc.grid(row=28, column=1)
Visc.insert(0,"1")

EDAC = Entry(root, width= 10)
EDAC.grid(row = 28, column = 3)
EDAC.insert(0,"0")

ERM = Entry(root, width= 10)
ERM.grid(row = 28, column = 5)
ERM.insert(0,"1")

# 21st line
Animate = StringVar(root,"0")
Label(root, text = "ANIMATE: -").grid(row = 29, column = 0)
Radiobutton(root,text="ON",variable=Animate,value=1).grid(row=29,column=1)
Radiobutton(root,text="OFF",variable=Animate,value=0).grid(row=29,column=2)

# line 12 entry values
Label(root, text="ANIM-FILENAME: -").grid(row=30, column=0)
Label(root, text = "ANIM-FREQUENCY: -").grid(row = 30, column = 2)
Label(root, text = "BACK-FREQUENCY: -").grid(row = 30, column = 4)

# line 13
Anim_filename = Entry(root, width=10)
Anim_filename.grid(row=30, column=1)
Anim_filename.insert(0,"1")

Anim_frequency = Entry(root, width= 10)
Anim_frequency.grid(row = 30, column = 3)
Anim_frequency.insert(0,"10000")

Back_frequency = Entry(root, width= 10)
Back_frequency.grid(row = 30, column = 5)
Back_frequency.insert(0,"10000")

# line 14
Average = StringVar(root,"0")
Label(root, text = "AVERAGE: -").grid(row = 31, column = 0)
Radiobutton(root,text="ON",variable=Average,value=1).grid(row=31,column=1)
Radiobutton(root,text="OFF",variable=Average,value=0).grid(row=31,column=2)
# line 14 contd
Average_restart = StringVar(root,"0")
Label(root, text = "AVERAGE RESTART: -").grid(row = 32, column = 0)
Radiobutton(root,text="ON",variable=Average_restart,value=1).grid(row=32,column=1)
Radiobutton(root,text="OFF",variable=Average_restart,value=0).grid(row=32,column=2)

# Line 15
Label(root, text = "PERIODICITY: -").grid(row = 33, column = 0)
SelfI = StringVar(root,"0")
SelfJ = StringVar(root,"0")
SelfK = StringVar(root,"0")
Checkbutton(root,text="I",variable=SelfI).grid(row=33,column=1)
Checkbutton(root,text="j",variable=SelfJ).grid(row=33,column=2)
Checkbutton(root,text="K",variable=SelfK).grid(row=33,column=3)

# Line 16
bulkturb = StringVar(root,"0")
Label(root, text = "BULK TURBULENCE: -").grid(row = 34, column = 0)
Radiobutton(root,text="ON",variable=bulkturb,value=1).grid(row=34,column=1)
Radiobutton(root,text="OFF",variable=bulkturb,value=0).grid(row=34,column=2)

# Line 17
channel_flow = StringVar(root,"0")
Label(root, text = "CHANNEL CASE: -").grid(row = 35, column = 0)
Radiobutton(root,text="ON",variable=channel_flow,value=1).grid(row=35,column=1)
Radiobutton(root,text="OFF",variable=channel_flow,value=0).grid(row=35,column=2)

# Line 18
channel_restart = StringVar(root,"0")
Label(root, text = "CHANNEL RESTART: -").grid(row = 36, column = 0)
Radiobutton(root,text="ON",variable=channel_restart,value=1).grid(row=36,column=1)
Radiobutton(root,text="OFF",variable=channel_restart,value=0).grid(row=36,column=2)

# Line 19
taylor_case = StringVar(root,"0")
Label(root, text = "TAYLOR CASE: -").grid(row = 37, column = 0)
Radiobutton(root,text="ON",variable=taylor_case,value=1).grid(row=37,column=1)
Radiobutton(root,text="OFF",variable=taylor_case,value=0).grid(row=37,column=2)

# Line 20
Rsv = StringVar(root,"0")
Label(root, text = "RSV CASE: -").grid(row = 38, column = 0)
Radiobutton(root,text="ON",variable=Rsv,value=1).grid(row=38,column=1)
Radiobutton(root,text="OFF",variable=Rsv,value=0).grid(row=38,column=2)

# Line 19
IBM = StringVar(root,"0")
Label(root, text = "IBM: -").grid(row = 39, column = 0)
Radiobutton(root,text="ON",variable=IBM,value=1).grid(row=39,column=1)
Radiobutton(root,text="OFF",variable=IBM,value=0).grid(row=39,column=2)

# line 19 entry values
Label(root, text="MUL: -").grid(row=40, column=0)
Label(root, text = "MOVING OBJ: -").grid(row = 40, column = 2)
Label(root, text = "DEL X: -").grid(row = 40, column = 4)

# line 19
mu1 = Entry(root, width=10)
mu1.grid(row=40, column=1)
mu1.insert(0,"0")

moving_obj = Entry(root, width= 10)
moving_obj.grid(row = 40, column = 3)
moving_obj.insert(0,"0")

del_x = Entry(root, width= 10)
del_x.grid(row = 40, column = 5)
del_x.insert(0,"0")

# line 20 entry values
Label(root, text="NODES: -").grid(row=41, column=0)
Label(root, text = "ELEMENTS: -").grid(row = 41, column = 2)
Label(root, text = "SPTS1 LIMIT: -").grid(row = 41, column = 4)
Label(root, text = "FLUID POINTS: -").grid(row = 41, column = 6)

# line 20
nodes = Entry(root, width=10)
nodes.grid(row=41, column=1)
nodes.insert(0,"0")

elements = Entry(root, width= 10)
elements.grid(row = 41, column = 3)
elements.insert(0,"0")

SPTS1_limit = Entry(root, width= 10)
SPTS1_limit.grid(row = 41, column = 5)
SPTS1_limit.insert(0,"0")

fluid_points = Entry(root, width= 10)
fluid_points.grid(row = 41, column = 7)
fluid_points.insert(0,"0")

# line 21 entry values
Label(root, text="Y_TOP: -").grid(row=42, column=0)
Label(root, text = "Y_BOT: -").grid(row = 42, column = 2)
Label(root, text = "Y_PER: -").grid(row = 42, column = 4)

# line 21
ytop = Entry(root, width=10)
ytop.grid(row=42, column=1)
ytop.insert(0,"0")

ybot = Entry(root, width= 10)
ybot.grid(row = 42, column = 3)
ybot.insert(0,"0")

yper = Entry(root, width= 10)
yper.grid(row = 42, column = 5)
yper.insert(0,"0")

# line 22 entry values
Label(root, text="IB_U: -").grid(row=43, column=0)
Label(root, text = "IB_V: -").grid(row = 43, column = 2)
Label(root, text = "IB_W: -").grid(row = 43, column = 4)
Label(root, text = "IB_T: -").grid(row = 43, column = 6)

# line 22
IB_U = Entry(root, width=10)
IB_U.grid(row=43, column=1)
IB_U.insert(0,"0")

IB_V = Entry(root, width= 10)
IB_V.grid(row = 43, column = 3)
IB_V.insert(0,"0")

IB_W = Entry(root, width= 10)
IB_W.grid(row = 43, column = 5)
IB_W.insert(0,"0")

IB_T = Entry(root, width= 10)
IB_T.grid(row = 43, column = 7)
IB_T.insert(0,"0")

# Line 23
Skew_symmetric = StringVar(root,"0")
Label(root, text = "SKEW SYMMETRIC: -").grid(row = 44, column = 0)
Radiobutton(root,text="ON",variable=Skew_symmetric,value=1).grid(row=44,column=1)
Radiobutton(root,text="OFF",variable=Skew_symmetric,value=0).grid(row=44,column=2)

# line 23 entry values
Label(root, text="EXP FILTER: -").grid(row=45, column=0)
Label(root, text = "SIG FILTER: -").grid(row = 45, column = 2)

# line 23
exp_filter = Entry(root, width=10)
exp_filter.grid(row=45, column=1)
exp_filter.insert(0,"0")

sig_filter = Entry(root, width= 10)
sig_filter.grid(row = 45, column = 3)
sig_filter.insert(0,"0")

# Line 24
probe = StringVar(root,"0")
Label(root, text = "PROBE: -").grid(row = 46, column = 0)
Radiobutton(root,text="ON",variable=probe,value=1).grid(row=46,column=1)
Radiobutton(root,text="OFF",variable=probe,value=0).grid(row=46,column=2)

# line 25 entry values
Label(root, text="Probe points: -").grid(row=47, column=0)

# line 25
probe_pts = Entry(root, width=10)
probe_pts.grid(row=47, column=1)
probe_pts.insert(0,"0")

# Line 24
inflow_turb = StringVar(root,"0")
Label(root, text = "INFLOW TURBULENCE: -").grid(row = 48, column = 0)
Radiobutton(root,text="ON",variable=inflow_turb,value=1).grid(row=48,column=1)
Radiobutton(root,text="OFF",variable=inflow_turb,value=0).grid(row=48,column=2)

# line 25 entry values
Label(root, text="NUM EDDIES: -").grid(row=49, column=0)

# line 25
Num_eddies = Entry(root, width=10)
Num_eddies.grid(row=49, column=1)
Num_eddies.insert(0,"500")

# Line 25
Eddy_func = StringVar(root,"1")
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
sigma = Entry(root, width=10)
sigma.grid(row=51, column=1)
sigma.insert(0,"0")

BoxLx = Entry(root, width= 10)
BoxLx.grid(row = 51, column = 3)
BoxLx.insert(0,"0")

BoxLy = Entry(root, width= 10)
BoxLy.grid(row = 51, column = 5)
BoxLy.insert(0,"0")

BoxLz = Entry(root, width= 10)
BoxLz.grid(row = 51, column = 7)
BoxLz.insert(0,"0")

Turb_Intensity = Entry(root, width= 10)
Turb_Intensity.grid(row = 51, column = 9)
Turb_Intensity.insert(0,"10")

# line 26 entry values
Label(root, text="Dx: -").grid(row=52, column=0)
Label(root, text = "Dy: -").grid(row = 52, column = 2)
Label(root, text = "Dz: -").grid(row = 52, column = 4)

# line 26
Dx = Entry(root, width=10)
Dx.grid(row=52, column=1)
Dx.insert(0,"0")

Dy = Entry(root, width= 10)
Dy.grid(row = 52, column = 3)
Dy.insert(0,"0")

Dz = Entry(root, width= 10)
Dz.grid(row = 52, column = 5)
Dz.insert(0,"0")

# Line 27
Wale = StringVar(root,"0")
Label(root, text = "Wale: -").grid(row = 53, column = 0)
Radiobutton(root,text="ON",variable=Eddy_func,value=1).grid(row=53,column=1)
Radiobutton(root,text="OFF",variable=Eddy_func,value=0).grid(row=53,column=2)





# run button
Button(root, text = "GENERATE INPUT FILE").grid(row=54,column=3)








# display Menu
window.config(menu = menubar)
mainloop()
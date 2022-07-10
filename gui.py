# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
window.title('Comp-Square')
window.minsize(1300,700)

# creating a canvas
my_canvas = Canvas(window)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

# Adding a scroll bar to the canvas
my_scrollbar = Scrollbar(window,orient=VERTICAL,command=my_canvas.yview)
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
    # Line 1
    nblocks = 1
    NImax = 100
    NJmax = 100
    NKmax = 100
    maxindex = max(NImax,NJmax,NKmax)
    # Line 2
    Restart = 0
    Steady = 0
    Grid2D = 0
    # Line 3
    P0 = 101325.0
    T0 = 294.4
    Pexit = 101325.0
    Pspill = 101325.0
    Twall = 294.4
    Lchar = 5.0
    AoA = 0.0
    Mach = 0.1
    Re = 100000
    Lref = 5.0
    phi_bw = 1.0
    # Line 4
    Interior_order = 2
    # Line 5
    boundary1 = 2
    boundary2 = 2
    # Line 6
    orderk = 2
    boundaryk1 = 2
    boundaryk2 = 2
    # Line 7
    alphaf = 0.495
    # Line 8
    forderi = 10
    forderj = 10
    forderk = 2
    # Line 9
    timeint = 1
    CFL = 1.0
    niter = 10000
    subiter = 10
    dt = 1e-3
    # Line 10
    NSCBC = 0
    CBC_order = 2
    # Line 11
    Sponge = 0
    Sponge_a = 0
    Sponge_n = 0
    Sponge_Xl = 0
    Sponge_Xh = 0
    Sponge_Yl = 0
    Sponge_Yh = 0
    Sponge_Zl = 0
    Sponge_Zh = 0
    Sponge_radl = 0
    Sponge_radh = 0
    # Line 12
    Visc = 1
    EDAC = 0
    ERM =  1
    # Line 13
    Animate = 0
    Anim_filename = 1
    Anim_frequency =  10000
    Back_frequency =  10000
    # Line 14
    Average = 0
    Average_restart = 0
    # Line 15
    SelfI = 0
    SelfJ = 0
    SelfK =  0
    # Line 16
    bulkturb = 0
    # Line 17
    channel_flow = 0
    channel_restart = 0
    # Line 18
    taylor_case = 0
    Rsv = 0
    # Line 19
    IBM = 0
    mu1 = 0
    moving_obj = 0
    del_x = 0
    # Line 20
    nodes = 0
    elements = 0
    SPTS1_limit = 0
    fluid_points = 0
    # Line 21
    ytop = 0
    ybot = 0
    yper = 0
    # Line 22
    IB_U = 0
    IB_V = 0
    IB_W = 0
    IB_T = 0
    # Line 23
    Skew_symmetric = 0
    exp_filter = 0
    sig_filter = 0
    # Line 24
    probe = 0
    probe_pts = 0
    # Line 25
    inflow_turb = 0
    Num_eddies = 500
    Eddy_func = 1
    sigma = 0
    BoxLx = 0
    BoxLy = 0
    BoxLz = 0
    Turb_Intensity = 10
    # Line 26
    Dx = 0
    Dy = 0
    Dz = 0
    # Line 27
    Wale = 0
    
    #deleting previous values
    e_nblocks.delete(0,END)
    e_NImax.delete(0,END)
    e_NJmax.delete(0,END)
    e_NKmax.delete(0,END)
    r_Restart.set(str(Restart))
    r_Steady.set(str(Steady))
    r_Grid2D.set(str(Grid2D))
    r_viscosity.set(str(Visc))
    r_compressibility.set(str(EDAC))
    method.set(str(ERM))
    c_Wale.set(str(Wale))
    e_P0.delete(0, END)
    e_T0.delete(0, END)
    e_Pexit.delete(0, END)
    e_Pspill.delete(0, END)
    e_Twall.delete(0, END)
    e_Lchar.delete(0, END)
    e_AoA.delete(0, END)
    e_Mach.delete(0, END)
    e_Re.delete(0, END)
    e_Lref.delete(0, END)
    e_phi_bw.delete(0, END)
    r_Interior_order.set(str(Interior_order))
    r_boundary1.set(str(boundary1))
    r_boundary2.set(str(boundary2))
    r_orderk.set(str(orderk))
    r_boundaryk1.set(str(boundaryk1))
    r_boundaryk2.set(str(boundaryk2))
    e_alphaf.delete(0, END)
    drop_menui.set(str(forderi))
    drop_menuj.set(str(forderj))
    drop_menuk.set(str(forderk))
    r_timeint.set(str(timeint))
    e_CFL.delete(0, END)
    e_niter.delete(0, END)
    e_subiter.delete(0, END)
    e_dt.delete(0, END)
    r_NSCBC.set(str(NSCBC))
    r_CBC_order.set(str(CBC_order))
    r_Sponge.set(str(Sponge))
    e_Sponge_a.delete(0, END)
    e_Sponge_n.delete(0, END)
    e_Sponge_Xh.delete(0, END)
    e_Sponge_Xl.delete(0, END)
    e_Sponge_Yh.delete(0, END)
    e_Sponge_Yl.delete(0, END)
    e_Sponge_Zh.delete(0, END)
    e_Sponge_Zl.delete(0, END)
    e_Sponge_radh.delete(0, END)
    e_Sponge_radl.delete(0, END)
    r_Animate.set(str(Animate))
    e_Anim_filename.delete(0, END)
    e_Anim_frequency.delete(0, END)
    e_Back_frequency.delete(0, END)
    r_Average.set(str(Average))
    r_Average_restart.set(str(Average_restart))
    b_SelfI.set(str(SelfI))
    b_SelfJ.set(str(SelfJ))
    b_SelfK.set(str(SelfK))
    r_bulkturb.set(str(bulkturb))
    r_channel_flow.set(str(channel_flow))
    r_channel_restart.set(str(channel_restart))
    r_taylor_case.set(str(taylor_case))
    r_Rsv.set(str(Rsv))
    r_IBM.set(str(IBM))
    e_mu1.delete(0, END)
    e_moving_obj.delete(0, END)
    e_del_x.delete(0, END)
    e_nodes.delete(0, END)
    e_elements.delete(0, END)
    e_SPTS1_limit.delete(0, END)
    e_fluid_points.delete(0, END)
    e_ytop.delete(0, END)
    e_ybot.delete(0, END)
    e_yper.delete(0, END)
    e_IB_U.delete(0, END)
    e_IB_V.delete(0, END)
    e_IB_W.delete(0, END)
    e_IB_T.delete(0, END)
    r_Skew_symmetric.set(str(Skew_symmetric))
    e_exp_filter.delete(0, END)
    e_sig_filter.delete(0, END)
    r_probe.set(str(probe))    
    e_probe_pts.delete(0, END)
    r_inflow_turb.set(str(inflow_turb))
    e_Num_eddies.delete(0, END)
    r_Eddy_func.set(str(Eddy_func))
    e_sigma.delete(0, END)
    e_BoxLx.delete(0, END)
    e_BoxLy.delete(0, END)
    e_BoxLz.delete(0, END)
    e_Turb_Intensity.delete(0, END)
    e_Dx.delete(0, END)
    e_Dy.delete(0, END)
    e_Dz.delete(0, END)

    # setting in default
    e_nblocks.insert(0, nblocks)
    e_NImax.insert(0, NImax)
    e_NJmax.insert(0, NJmax)
    e_NKmax.insert(0, NKmax)
    maxindex = max(NImax,NJmax,NKmax)
    r_Restart.set(str(Restart))
    r_Steady.set(str(Steady))
    r_Grid2D.set(str(Grid2D))
    r_viscosity.set(str(Visc))
    r_compressibility.set(str(EDAC))
    method.set(str(ERM))
    c_Wale.set(str(Wale))
    e_P0.insert(0, P0)
    e_T0.insert(0, T0)
    e_Pexit.insert(0, Pexit)
    e_Pspill.insert(0, Pspill)
    e_Twall.insert(0, Twall)
    e_Lchar.insert(0, Lchar)
    e_AoA.insert(0, AoA)
    e_Mach.insert(0, Mach)
    e_Re.insert(0, Re)
    e_Lref.insert(0, Lref)
    e_phi_bw.insert(0, phi_bw)
    r_Interior_order.set(str(Interior_order))
    r_boundary1.set(str(boundary1))
    r_boundary2.set(str(boundary2))
    r_orderk.set(str(orderk))
    r_boundaryk1.set(str(boundaryk1))
    r_boundaryk2.set(str(boundaryk2))
    e_alphaf.insert(0, alphaf)
    drop_menui.set(str(forderi))
    drop_menuj.set(str(forderj))
    drop_menuk.set(str(forderk))
    r_timeint.set(str(timeint))
    e_CFL.insert(0, CFL)
    e_niter.insert(0, niter)
    e_subiter.insert(0, subiter)
    e_dt.insert(0, dt)
    r_NSCBC.set(str(NSCBC))
    r_CBC_order.set(str(CBC_order))
    r_Sponge.set(str(Sponge))
    e_Sponge_a.insert(0, Sponge_a)
    e_Sponge_n.insert(0, Sponge_n)
    e_Sponge_Xh.insert(0, Sponge_Xh)
    e_Sponge_Xl.insert(0, Sponge_Xl)
    e_Sponge_Yh.insert(0, Sponge_Yh)
    e_Sponge_Yl.insert(0, Sponge_Yl)
    e_Sponge_Zh.insert(0, Sponge_Zh)
    e_Sponge_Zl.insert(0, Sponge_Zl)
    e_Sponge_radh.insert(0, Sponge_radh)
    e_Sponge_radl.insert(0, Sponge_radl)
    r_Animate.set(str(Animate))
    e_Anim_filename.insert(0, Anim_filename)
    e_Anim_frequency.insert(0, Anim_frequency)
    e_Back_frequency.insert(0, Back_frequency)
    r_Average.set(str(Average))
    r_Average_restart.set(str(Average_restart))
    b_SelfI.set(str(SelfI))
    b_SelfJ.set(str(SelfJ))
    b_SelfK.set(str(SelfK))
    r_bulkturb.set(str(bulkturb))
    r_channel_flow.set(str(channel_flow))
    r_channel_restart.set(str(channel_restart))
    r_taylor_case.set(str(taylor_case))
    r_Rsv.set(str(Rsv))
    r_IBM.set(str(IBM))
    e_mu1.insert(0, mu1)
    e_moving_obj.insert(0, moving_obj)
    e_del_x.insert(0, del_x)
    e_nodes.insert(0, nodes)
    e_elements.insert(0, elements)
    e_SPTS1_limit.insert(0, SPTS1_limit)
    e_fluid_points.insert(0, fluid_points)
    e_ytop.insert(0, ytop)
    e_ybot.insert(0, ybot)
    e_yper.insert(0, yper)
    e_IB_U.insert(0, IB_U)
    e_IB_V.insert(0, IB_V)
    e_IB_W.insert(0, IB_W)
    e_IB_T.insert(0, IB_T)
    r_Skew_symmetric.set(str(Skew_symmetric))
    e_exp_filter.insert(0, exp_filter)
    e_sig_filter.insert(0, sig_filter)
    r_probe.set(str(probe))    
    e_probe_pts.insert(0, probe_pts)
    r_inflow_turb.set(str(inflow_turb))
    e_Num_eddies.insert(0, Num_eddies)
    r_Eddy_func.set(str(Eddy_func))
    e_sigma.insert(0, sigma)
    e_BoxLx.insert(0, BoxLx)
    e_BoxLy.insert(0, BoxLy)
    e_BoxLz.insert(0, BoxLz)
    e_Turb_Intensity.insert(0, Turb_Intensity)
    e_Dx.insert(0, Dx)
    e_Dy.insert(0, Dy)
    e_Dz.insert(0, Dz)


    

def loadfromprev():
    import pandas
    column_names = [i for i in range(0, 100)]
    df=pandas.read_csv('input.in', header=None, sep="\s|,|\t", names=column_names)
    # Line 1
    nblocks = int(df[0][0])
    NImax = int(df[1][0])
    NJmax = int(df[2][0])
    NKmax = int(df[3][0])
    maxindex = max(NImax,NJmax,NKmax)
    # Line 2 
    Restart = int(df[0][1])
    Steady = int(df[1][1])
    Grid2D = int(df[2][1])
    # Line 3 
    P0 = float(df[0][2])
    T0 = float(df[1][2])
    Pexit = float(df[2][2])
    Pspill = float(df[3][2])
    Twall = float(df[4][2])
    Lchar = float(df[5][2])
    AoA = float(df[6][2])
    Mach = float(df[7][2])
    Re = float(df[8][2])
    Lref = float(df[9][2])
    phi_bw = float(df[10][2])
    # Line 4
    Interior_order = int(df[0][3])
    # Line 5
    boundary1 = int(df[0][4])
    boundary2 = int(df[1][4])
    # Line 6
    orderk = int(df[0][5])
    boundaryk1 = int(df[1][5])
    boundaryk2 = int(df[2][5])
    # Line 7
    alphaf = float(df[0][6])
    # Line 8
    forderi = int(df[0][7])
    forderj = int(df[1][7])
    forderk = int(df[2][7])
    # Line 9
    timeint = int(df[0][8])
    CFL = float(df[1][8])
    niter = int(df[2][8])
    subiter = int(df[3][8])
    dt = float(df[4][8])
    # Line 10
    NSCBC = int(df[0][9])
    CBC_order = int(df[1][9])
    # Line 11
    Sponge = int(df[0][10])
    Sponge_a = float(df[1][10])
    Sponge_n = float(df[2][10])
    Sponge_X1 = float(df[3][10])
    Sponge_Xh = float(df[4][10])
    Sponge_Y1 = float(df[5][10])
    Sponge_Yh = float(df[6][10])
    Sponge_Z1 = float(df[7][10])
    Sponge_Zh = float(df[8][10])
    Sponge_radl = float(df[9][10])
    Sponge_radh = float(df[10][10])
    # Line 12
    Visc = int(df[0][11])
    EDAC = int(df[1][11])
    ERM =  int(df[2][11])
    # Line 13
    Animate = int(df[0][12])
    Anim_filename = int(df[1][12])
    Anim_frequency =  int(df[2][12])
    Back_frequency =  int(df[3][12])
    # Line 14
    Average = int(df[0][13])
    Average_restart = int(df[1][13])
    # Line 15
    SelfI = int(df[0][14])
    SelfJ = int(df[1][14])
    SelfK =  int(df[2][14])
    # Line 16
    bulkturb = int(df[0][15])
    # Line 17
    channel_flow = int(df[0][16])
    channel_restart = int(df[1][16])
    # Line 18
    taylor_case = int(df[0][17])
    Rsv = int(df[1][17])
    # Line 19
    IBM = int(df[0][18])
    mu1 = int(df[1][18])
    moving_obj = int(df[2][18])
    del_x = float(df[3][18])
    # Line 20
    nodes = int(df[0][19])
    elements = int(df[1][19])
    SPTS1_limit = int(df[2][19])
    fluid_points = int(df[3][19])
    # Line 21
    ytop = int(df[0][20])
    ybot = int(df[1][20])
    yper = int(df[2][20])
    # Line 22
    IB_U = float(df[0][21])
    IB_V = float(df[1][21])
    IB_W = float(df[2][21])
    IB_T = float(df[3][21])
    # Line 23
    Skew_symmetric = int(df[0][22])
    exp_filter = int(df[1][22])
    sig_filter = int(df[2][22])
    # Line 24
    probe = int(df[0][23])
    probe_pts = int(df[1][23])
    # Line 25
    inflow_turb = int(df[0][24])
    Num_eddies = int(df[1][24])
    Eddy_func = int(df[2][24])
    sigma = float(df[3][24])
    BoxLx = float(df[4][24])
    BoxLy = float(df[5][24])
    BoxLz = float(df[6][24])
    Turb_Intensity = float(df[7][24])
    # Line 26
    Dx = float(df[0][25])
    Dy = float(df[1][25])
    Dz = float(df[2][25])
    # Line 27
    Wale = int(df[0][26])

    e_nblocks.insert(0, nblocks)
    e_NImax.insert(0, NImax)
    e_NJmax.insert(0, NJmax)
    e_NKmax.insert(0, NKmax)
    maxindex = max(NImax,NJmax,NKmax)
    r_Restart.set(str(Restart))
    r_Steady.set(str(Steady))
    r_Grid2D.set(str(Grid2D))
    r_viscosity.set(str(Visc))
    r_compressibility.set(str(EDAC))
    method.set(str(ERM))
    c_Wale.set(str(Wale))
    e_P0.insert(0, P0)
    e_T0.insert(0, T0)
    e_Pexit.insert(0, Pexit)
    e_Pspill.insert(0, Pspill)
    e_Twall.insert(0, Twall)
    e_Lchar.insert(0, Lchar)
    e_AoA.insert(0, AoA)
    e_Mach.insert(0, Mach)
    e_Re.insert(0, Re)
    e_Lref.insert(0, Lref)
    e_phi_bw.insert(0, phi_bw)
    r_Interior_order.set(str(Interior_order))
    r_boundary1.set(str(boundary1))
    r_boundary2.set(str(boundary2))
    r_orderk.set(str(orderk))
    r_boundaryk1.set(str(boundaryk1))
    r_boundaryk2.set(str(boundaryk2))
    e_alphaf.insert(0, alphaf)
    drop_menui.set(str(forderi))
    drop_menuj.set(str(forderj))
    drop_menuk.set(str(forderk))
    r_timeint.set(str(timeint))
    e_CFL.insert(0, CFL)
    e_niter.insert(0, niter)
    e_subiter.insert(0, subiter)
    e_dt.insert(0, dt)
    r_NSCBC.set(str(NSCBC))
    r_CBC_order.set(str(CBC_order))
    r_Sponge.set(str(Sponge))
    e_Sponge_a.insert(0, Sponge_a)
    e_Sponge_n.insert(0, Sponge_n)
    e_Sponge_Xh.insert(0, Sponge_Xh)
    e_Sponge_Xl.insert(0, Sponge_Xl)
    e_Sponge_Yh.insert(0, Sponge_Yh)
    e_Sponge_Yl.insert(0, Sponge_Yl)
    e_Sponge_Zh.insert(0, Sponge_Zh)
    e_Sponge_Zl.insert(0, Sponge_Zl)
    e_Sponge_radh.insert(0, Sponge_radh)
    e_Sponge_radl.insert(0, Sponge_radl)
    r_Animate.set(str(Animate))
    e_Anim_filename.insert(0, Anim_filename)
    e_Anim_frequency.insert(0, Anim_frequency)
    e_Back_frequency.insert(0, Back_frequency)
    r_Average.set(str(Average))
    r_Average_restart.set(str(Average_restart))
    b_SelfI.set(str(SelfI))
    b_SelfJ.set(str(SelfJ))
    b_SelfK.set(str(SelfK))
    r_bulkturb.set(str(bulkturb))
    r_channel_flow.set(str(channel_flow))
    r_channel_restart.set(str(channel_restart))
    r_taylor_case.set(str(taylor_case))
    r_Rsv.set(str(Rsv))
    r_IBM.set(str(IBM))
    e_mu1.insert(0, mu1)
    e_moving_obj.insert(0, moving_obj)
    e_del_x.insert(0, del_x)
    e_nodes.insert(0, nodes)
    e_elements.insert(0, elements)
    e_SPTS1_limit.insert(0, SPTS1_limit)
    e_fluid_points.insert(0, fluid_points)
    e_ytop.insert(0, ytop)
    e_ybot.insert(0, ybot)
    e_yper.insert(0, yper)
    e_IB_U.insert(0, IB_U)
    e_IB_V.insert(0, IB_V)
    e_IB_W.insert(0, IB_W)
    e_IB_T.insert(0, IB_T)
    r_Skew_symmetric.set(str(Skew_symmetric))
    e_exp_filter.insert(0, exp_filter)
    e_sig_filter.insert(0, sig_filter)
    r_probe.set(str(probe))    
    e_probe_pts.insert(0, probe_pts)
    r_inflow_turb.set(str(inflow_turb))
    e_Num_eddies.insert(0, Num_eddies)
    r_Eddy_func.set(str(Eddy_func))
    e_sigma.insert(0, sigma)
    e_BoxLx.insert(0, BoxLx)
    e_BoxLy.insert(0, BoxLy)
    e_BoxLz.insert(0, BoxLz)
    e_Turb_Intensity.insert(0, Turb_Intensity)
    e_Dx.insert(0, Dx)
    e_Dy.insert(0, Dy)
    e_Dz.insert(0, Dz)

# ---- Zeroth line --------
Button(root, text = "Load From Previous", command=loadfromprev).grid(row=0,column=3)
Button(root, text = "Set Default", command=setdefault).grid(row=0,column=4)

# first-line
Label(root, text="Nblocks: -").grid(row=2, column=0)
Label(root, text = "NImax: -").grid(row = 2, column = 2)
Label(root, text = "NJmax: -").grid(row = 2, column = 4)
Label(root, text = "NKmax: -").grid(row = 2, column = 6)
Label(root, text = "NMAX: -").grid(row = 2, column = 8)

# first-line
e_nblocks = IntVar(root)
e_nblocks = Entry(root,width=10)
e_nblocks.grid(row=2, column=1)

e_NImax = IntVar(root)
e_NImax = Entry(root, width=10)
e_NImax.grid(row = 2, column = 3)

e_NJmax = IntVar(root)
e_NJmax = Entry(root, width=10)
e_NJmax.grid(row = 2, column = 5)

e_NKmax = IntVar(root)
e_NKmax =Entry(root, width=10)
e_NKmax.grid(row = 2, column = 7)

# e_maxindex = IntVar(root)
# e_maxindex =Entry(root, width=10)
# e_maxindex.grid(row = 2, column = 9)


# e_maxindex.insert(0,maxindex)

# ------ second line ---------
r_Restart = IntVar(root,"10")
Radiobutton(root,text="FRESH",variable=r_Restart, value=0).grid(row=3,column=3)
Radiobutton(root,text="RESTART",variable=r_Restart,value=1).grid(row=3,column=4)

Restart = r_Restart.get()

# -------Third line --------
r_Steady = IntVar(root,"10")
Radiobutton(root,text="STEADY",variable=r_Steady, value=1).grid(row=4,column=3)
Radiobutton(root,text="UNSTEADY",variable=r_Steady,value=0).grid(row=4,column=4)

Steady = r_Steady.get()

# -------fourth line --------
r_Grid2D = IntVar(root,"10")
Radiobutton(root,text="2-DIMENSIONAL",variable=r_Grid2D, value=1).grid(row=5,column=3)
Radiobutton(root,text="3-DIMENSIONAL",variable=r_Grid2D,value=0).grid(row=5,column=4)

Grid2D = r_Grid2D.get()

# --------- fifth line --------
r_viscosity = IntVar(root,"10")
Radiobutton(root,text="VISCOUS",variable=r_viscosity,value=1).grid(row=6,column=3)
Radiobutton(root,text="INVISCID",variable=r_viscosity,value=0).grid(row=6,column=4)

Visc = r_viscosity.get()

# --------- sixth line --------
r_compressibility = IntVar(root,"10")
Radiobutton(root,text="COMPRESSIBLE",variable=r_compressibility,value=0).grid(row=7,column=3)
Radiobutton(root,text="INCOMPRESSIBLE",variable=r_compressibility,value=1).grid(row=7,column=4)

EDAC = r_compressibility.get()

# --------- seventh line --------
method = IntVar(root,"10")
Radiobutton(root,text="LES",variable=method,value=1).grid(row=8,column=3)
Radiobutton(root,text="K-OMEGA",variable=method,value=0).grid(row=8,column=4)

ERM = method.get()

c_Wale = BooleanVar(root)
Checkbutton(root,text="WALE",variable=c_Wale).grid(row=8,column=5)

Wale = c_Wale.get()

# Third-line entry values
Label(root, text="Pstag: -").grid(row=9, column=0)
Label(root, text = "Tstag: -").grid(row = 9, column = 2)
Label(root, text = "Pexit: -").grid(row = 9, column = 4)
Label(root, text = "Pspill: -").grid(row = 9, column = 6)
Label(root, text = "Twall: -").grid(row = 9, column = 8)
Label(root, text = "L_Char: -").grid(row = 10, column = 2)
Label(root, text = "alpha_aoa: -").grid(row = 10, column = 4)
Label(root, text = "Mach_in: -").grid(row = 10, column = 6)
Label(root, text = "Re: -").grid(row = 10, column = 8)
Label(root, text = "Lref: -").grid(row = 11, column = 2)
Label(root, text = "phi_bw: -").grid(row = 11, column = 4)

# Third-line
e_P0 = DoubleVar(root)
e_P0 = Entry(root, width=10)
e_P0.grid(row=9, column=1)

P0 = e_P0.get()

e_T0 = DoubleVar(root)
e_T0 = Entry(root, width= 10)
e_T0.grid(row = 9, column = 3)

T0 = e_T0.get()

e_Pexit = DoubleVar(root)
e_Pexit = Entry(root, width= 10)
e_Pexit.grid(row = 9, column = 5)

Pexit = e_Pexit.get()

e_Pspill = DoubleVar(root)
e_Pspill = Entry(root, width= 10)
e_Pspill.grid(row = 9, column = 7)

Pspill = e_Pspill.get()

e_Twall = DoubleVar(root)
e_Twall = Entry(root, width= 10)
e_Twall.grid(row = 9, column = 9)

Twall = e_Twall.get()

e_Lchar = DoubleVar(root)
e_Lchar = Entry(root, width= 10)
e_Lchar.grid(row = 10, column = 3)

Lchar = e_Lchar.get()

e_AoA = DoubleVar(root)
e_AoA = Entry(root, width= 10)
e_AoA.grid(row = 10, column = 5)

AoA = e_AoA.get()

e_Mach = DoubleVar(root)
e_Mach = Entry(root, width= 10)
e_Mach.grid(row = 10, column = 7)

Mach = e_Mach.get()

e_Re = DoubleVar(root)
e_Re = Entry(root, width= 10)
e_Re.grid(row = 10, column = 9)

Re = e_Re.get()

e_Lref = DoubleVar(root)
e_Lref = Entry(root, width= 10)
e_Lref.grid(row = 11, column = 3)

Lref = e_Lref.get()

e_phi_bw = DoubleVar(root)
e_phi_bw = Entry(root, width= 10)
e_phi_bw.grid(row = 11, column = 5)

phi_bw = e_phi_bw.get()

# --------- ninth line --------
r_Interior_order = IntVar(root,"10")
Label(root, text = "INTERIOR ORDER: -").grid(row = 12, column = 1)
Radiobutton(root,text="E2",variable=r_Interior_order,value=1).grid(row=12,column=2)
Radiobutton(root,text="E4",variable=r_Interior_order,value=2).grid(row=12,column=3)
Radiobutton(root,text="C4",variable=r_Interior_order,value=3).grid(row=12,column=4)
Radiobutton(root,text="C6",variable=r_Interior_order,value=4).grid(row=12,column=5)

Interior_order = r_Interior_order.get()

# --------- tenth line --------
r_boundary1 = IntVar(root,"10")
Label(root, text = "BOUNDARY 1: -").grid(row = 13, column = 1)
Radiobutton(root,text="2",variable=r_boundary1,value=2).grid(row=13,column=2)
Radiobutton(root,text="4",variable=r_boundary1,value=4).grid(row=13,column=3)

boundary1 = r_boundary1.get()

# --------- eleventh line --------
r_boundary2 = IntVar(root,"10")
Label(root, text = "BOUNDARY 2: -").grid(row = 14, column = 1)
Radiobutton(root,text="2",variable=r_boundary2,value=2).grid(row=14,column=2)
Radiobutton(root,text="4",variable=r_boundary2,value=4).grid(row=14,column=3)

boundary2 = r_boundary2.get()

# --------- twelfth line --------
r_orderk = IntVar(root,"10")
Label(root, text = "ORDER IN K: -").grid(row = 15, column = 1)
Radiobutton(root,text="E2",variable=r_orderk,value=1).grid(row=15,column=2)
Radiobutton(root,text="E4",variable=r_orderk,value=2).grid(row=15,column=3)
Radiobutton(root,text="C4",variable=r_orderk,value=3).grid(row=15,column=4)
Radiobutton(root,text="C6",variable=r_orderk,value=4).grid(row=15,column=5)

orderk = r_orderk.get()

# --------- thirteenth line --------
r_boundaryk1 = IntVar(root,"10")
Label(root, text = "BOUNDARY K1: -").grid(row = 16, column = 1)
Radiobutton(root,text="2",variable=r_boundaryk1,value=2).grid(row=16,column=2)
Radiobutton(root,text="4",variable=r_boundaryk1,value=4).grid(row=16,column=3)

boundaryk1 = r_boundaryk1.get()

# --------- fourteenth line --------
r_boundaryk2 = IntVar(root,"10")
Label(root, text = "BOUNDARY K2: -").grid(row = 17, column = 1)
Radiobutton(root,text="2",variable=r_boundaryk2,value=2).grid(row=17,column=2)
Radiobutton(root,text="4",variable=r_boundaryk2,value=4).grid(row=17,column=3)

boundaryk2 = r_boundaryk2.get()

# Seventh-line
Label(root, text="alpha_f: -").grid(row=18, column=0)
e_alphaf = DoubleVar(root)
e_alphaf = Entry(root, width=10)
e_alphaf.grid(row=18, column=1)

alphaf = e_alphaf.get()

# -------- fifteenth line -------
Label(root, text = "F Order i: -").grid(row = 19, column = 0)
# drop menu
drop_menui=StringVar()
drop_menui.set("Select")
#options
d_forderi = IntVar(root)
d_forderi = OptionMenu(root,drop_menui,"2","4","6","8","10")
d_forderi.grid(row=19,column=1)

forderi = drop_menui.get()

Label(root, text = "F Order j: -").grid(row = 19, column = 2)
drop_menuj=StringVar()
drop_menuj.set("Select")
d_forderj = IntVar(root)
d_forderj = OptionMenu(root,drop_menuj,"2","4","6","8","10")
d_forderj.grid(row=19,column=3)

forderj = drop_menuj.get()

Label(root, text = "F Order K: -").grid(row = 19, column = 4)
drop_menuk=StringVar()
drop_menuk.set("Select")
d_forderk = IntVar(root)
d_forderk = OptionMenu(root,drop_menuk,"2","4","6","8","10")
d_forderk.grid(row=19,column=5)

forderk = drop_menuk.get()

# --------- sixteenth line --------
r_timeint = IntVar(root,"10")
Label(root, text = "Time Integration: -").grid(row = 20, column = 0)
Radiobutton(root,text="RK4",variable=r_timeint,value=1).grid(row=20,column=1)
Radiobutton(root,text="DTS",variable=r_timeint,value=2).grid(row=20,column=2)

timeint = r_timeint.get()

# seventeenth-line
Label(root, text="CFL: -").grid(row=21, column=0)
Label(root, text = "niter: -").grid(row = 21, column = 2)
Label(root, text = "subiter: -").grid(row = 21, column = 4)
Label(root, text = "dt: -").grid(row = 21, column = 6)

# seventeenth-line
e_CFL = DoubleVar(root)
e_CFL = Entry(root,width=10)
e_CFL.grid(row=21, column=1)

CFL = e_CFL.get()

e_niter = IntVar(root)
e_niter = Entry(root, width=10)
e_niter.grid(row = 21, column = 3)

niter = e_niter.get()

e_subiter = IntVar(root)
e_subiter = Entry(root, width=10)
e_subiter.grid(row = 21, column = 5)

subiter = e_subiter.get()

e_dt = DoubleVar(root)
e_dt =Entry(root, width=10)
e_dt.grid(row = 21, column = 7)

dt = e_dt.get()

# --------- eighteenth line --------
r_NSCBC = IntVar(root,"10")
Label(root, text = "NSBC: -").grid(row = 22, column = 0)
Radiobutton(root,text="ON",variable=r_NSCBC,value=1).grid(row=22,column=1)
Radiobutton(root,text="OFF",variable=r_NSCBC,value=0).grid(row=22,column=2)

NSCBC = r_NSCBC.get()

# nineteenth-line
Label(root, text="CBC Order: -").grid(row=23, column=0)
# nineteenth-line
r_CBC_order = IntVar(root)
Radiobutton(root,text="2",variable=r_CBC_order,value=2).grid(row=23,column=1)
Radiobutton(root,text="4",variable=r_CBC_order,value=4).grid(row=23,column=2)

CBC_order = r_CBC_order.get()

# --------- twentieth line --------
r_Sponge = IntVar(root,"10")
Label(root, text = "SPONGE: -").grid(row = 24, column = 0)
Radiobutton(root,text="ON",variable=r_Sponge,value=1).grid(row=24,column=1)
Radiobutton(root,text="OFF",variable=r_Sponge,value=0).grid(row=24,column=2)

Sponge = r_Sponge.get()

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
e_Sponge_a = DoubleVar(root)
e_Sponge_a = Entry(root, width=10)
e_Sponge_a.grid(row=25, column=1)

Sponge_a = e_Sponge_a.get()

e_Sponge_n = DoubleVar(root)
e_Sponge_n = Entry(root, width= 10)
e_Sponge_n.grid(row = 25, column = 3)

Sponge_n = e_Sponge_n.get()

e_Sponge_Xl = DoubleVar(root)
e_Sponge_Xl = Entry(root, width= 10)
e_Sponge_Xl.grid(row = 25, column = 5)

Sponge_Xl = e_Sponge_Xl.get()

e_Sponge_Xh = DoubleVar(root)
e_Sponge_Xh = Entry(root, width= 10)
e_Sponge_Xh.grid(row = 25, column = 7)

Sponge_Xh = e_Sponge_Xh.get()

e_Sponge_Yl = DoubleVar(root)
e_Sponge_Yl = Entry(root, width= 10)
e_Sponge_Yl.grid(row = 25, column = 9)

Sponge_Yl = e_Sponge_Yl.get()

e_Sponge_Yh = DoubleVar(root)
e_Sponge_Yh = Entry(root, width= 10)
e_Sponge_Yh.grid(row = 26, column = 3)

Sponge_Yh = e_Sponge_Yh.get()

e_Sponge_Zl = DoubleVar(root)
e_Sponge_Zl = Entry(root, width= 10)
e_Sponge_Zl.grid(row = 26, column = 5)

Sponge_Zl = e_Sponge_Zl.get()

e_Sponge_Zh = DoubleVar(root)
e_Sponge_Zh = Entry(root, width= 10)
e_Sponge_Zh.grid(row = 26, column = 7)

Sponge_Zh = e_Sponge_Zh.get()

e_Sponge_radl = DoubleVar(root)
e_Sponge_radl = Entry(root, width= 10)
e_Sponge_radl.grid(row = 26, column = 9)

Sponge_radl = e_Sponge_radl.get()

e_Sponge_radh = DoubleVar(root)
e_Sponge_radh = Entry(root, width= 10)
e_Sponge_radh.grid(row = 27, column = 3)

Sponge_radh = e_Sponge_radh.get()

# 21st line
r_Animate = IntVar(root,"10")
Label(root, text = "ANIMATE: -").grid(row = 29, column = 0)
Radiobutton(root,text="ON",variable=r_Animate,value=1).grid(row=29,column=1)
Radiobutton(root,text="OFF",variable=r_Animate,value=0).grid(row=29,column=2)

Animate = r_Animate.get()

# line 12 entry values
Label(root, text="ANIM-FILENAME: -").grid(row=30, column=0)
Label(root, text = "ANIM-FREQUENCY: -").grid(row = 30, column = 2)
Label(root, text = "BACK-FREQUENCY: -").grid(row = 30, column = 4)

# line 13
e_Anim_filename = IntVar(root)
e_Anim_filename = Entry(root, width=10)
e_Anim_filename.grid(row=30, column=1)

Anim_filename = e_Anim_filename.get()

e_Anim_frequency = IntVar(root)
e_Anim_frequency = Entry(root, width= 10)
e_Anim_frequency.grid(row = 30, column = 3)

Anim_frequency = e_Anim_frequency.get()

e_Back_frequency = IntVar(root)
e_Back_frequency = Entry(root, width= 10)
e_Back_frequency.grid(row = 30, column = 5)

Back_frequency = e_Back_frequency.get()

# line 14
r_Average = IntVar(root,"10")
Label(root, text = "AVERAGE: -").grid(row = 31, column = 0)
Radiobutton(root,text="ON",variable=r_Average,value=1).grid(row=31,column=1)
Radiobutton(root,text="OFF",variable=r_Average,value=0).grid(row=31,column=2)

Average = r_Average.get()

# line 14 contd
r_Average_restart = IntVar(root,"10")
Label(root, text = "AVERAGE RESTART: -").grid(row = 32, column = 0)
Radiobutton(root,text="ON",variable=r_Average_restart,value=1).grid(row=32,column=1)
Radiobutton(root,text="OFF",variable=r_Average_restart,value=0).grid(row=32,column=2)

Average_restart = r_Average_restart.get()

# Line 15
Label(root, text = "PERIODICITY: -").grid(row = 33, column = 0)
b_SelfI = BooleanVar(root,"0")
b_SelfJ = BooleanVar(root,"0")
b_SelfK = BooleanVar(root,"0")
Checkbutton(root,text="I",variable=b_SelfI).grid(row=33,column=1)
Checkbutton(root,text="j",variable=b_SelfJ).grid(row=33,column=2)
Checkbutton(root,text="K",variable=b_SelfK).grid(row=33,column=3)

SelfI = int(b_SelfI.get())
SelfJ = int(b_SelfJ.get())
SelfK = int(b_SelfK.get())

# Line 16
r_bulkturb = IntVar(root,"10")
Label(root, text = "BULK TURBULENCE: -").grid(row = 34, column = 0)
Radiobutton(root,text="ON",variable=r_bulkturb,value=1).grid(row=34,column=1)
Radiobutton(root,text="OFF",variable=r_bulkturb,value=0).grid(row=34,column=2)

bulkturb = r_bulkturb.get()

# Line 17
r_channel_flow = IntVar(root,"10")
Label(root, text = "CHANNEL CASE: -").grid(row = 35, column = 0)
Radiobutton(root,text="ON",variable=r_channel_flow,value=1).grid(row=35,column=1)
Radiobutton(root,text="OFF",variable=r_channel_flow,value=0).grid(row=35,column=2)

channel_flow = r_channel_flow.get()

# Line 18
r_channel_restart = IntVar(root,"10")
Label(root, text = "CHANNEL RESTART: -").grid(row = 36, column = 0)
Radiobutton(root,text="ON",variable=r_channel_restart,value=1).grid(row=36,column=1)
Radiobutton(root,text="OFF",variable=r_channel_restart,value=0).grid(row=36,column=2)

channel_restart = r_channel_restart.get()

# Line 19
r_taylor_case = IntVar(root,"10")
Label(root, text = "TAYLOR CASE: -").grid(row = 37, column = 0)
Radiobutton(root,text="ON",variable=r_taylor_case,value=1).grid(row=37,column=1)
Radiobutton(root,text="OFF",variable=r_taylor_case,value=0).grid(row=37,column=2)

taylor_case = r_taylor_case.get()

# Line 20
r_Rsv = IntVar(root,"10")
Label(root, text = "RSV CASE: -").grid(row = 38, column = 0)
Radiobutton(root,text="ON",variable=r_Rsv,value=1).grid(row=38,column=1)
Radiobutton(root,text="OFF",variable=r_Rsv,value=0).grid(row=38,column=2)

Rsv = r_Rsv.get()

# Line 19
r_IBM = IntVar(root,"10")
Label(root, text = "IBM: -").grid(row = 39, column = 0)
Radiobutton(root,text="ON",variable=r_IBM,value=1).grid(row=39,column=1)
Radiobutton(root,text="OFF",variable=r_IBM,value=0).grid(row=39,column=2)

IBM = r_IBM.get()

# line 19 entry values
Label(root, text="MUL: -").grid(row=40, column=0)
Label(root, text = "MOVING OBJ: -").grid(row = 40, column = 2)
Label(root, text = "DEL X: -").grid(row = 40, column = 4)

# line 19
e_mu1 = IntVar(root)
e_mu1 = Entry(root, width=10)
e_mu1.grid(row=40, column=1)

mu1 = e_mu1.get()

e_moving_obj = IntVar(root)
e_moving_obj = Entry(root, width= 10)
e_moving_obj.grid(row = 40, column = 3)

moving_obj = e_moving_obj.get()

e_del_x = IntVar(root)
e_del_x = Entry(root, width= 10)
e_del_x.grid(row = 40, column = 5)

del_x = e_del_x.get()

# line 20 entry values
Label(root, text="NODES: -").grid(row=41, column=0)
Label(root, text = "ELEMENTS: -").grid(row = 41, column = 2)
Label(root, text = "SPTS1 LIMIT: -").grid(row = 41, column = 4)
Label(root, text = "FLUID POINTS: -").grid(row = 41, column = 6)

# line 20
e_nodes = IntVar(root)
e_nodes = Entry(root, width=10)
e_nodes.grid(row=41, column=1)

nodes = e_nodes.get()

e_elements = IntVar(root)
e_elements = Entry(root, width= 10)
e_elements.grid(row = 41, column = 3)

elements = e_elements.get()

e_SPTS1_limit = IntVar(root)
e_SPTS1_limit = Entry(root, width= 10)
e_SPTS1_limit.grid(row = 41, column = 5)

SPTS1_limit = e_SPTS1_limit.get()

e_fluid_points = IntVar(root)
e_fluid_points = Entry(root, width= 10)
e_fluid_points.grid(row = 41, column = 7)

fluid_points = e_fluid_points.get()

# line 21 entry values
Label(root, text="Y_TOP: -").grid(row=42, column=0)
Label(root, text = "Y_BOT: -").grid(row = 42, column = 2)
Label(root, text = "Y_PER: -").grid(row = 42, column = 4)

# line 21
e_ytop = DoubleVar(root)
e_ytop = Entry(root, width=10)
e_ytop.grid(row=42, column=1)

ytop = e_ytop.get()

e_ybot = DoubleVar(root)
e_ybot = Entry(root, width= 10)
e_ybot.grid(row = 42, column = 3)

ybot = e_ybot.get()

e_yper = IntVar(root)
e_yper = Entry(root, width= 10)
e_yper.grid(row = 42, column = 5)

yper = e_yper.get()

# line 22 entry values
Label(root, text="IB_U: -").grid(row=43, column=0)
Label(root, text = "IB_V: -").grid(row = 43, column = 2)
Label(root, text = "IB_W: -").grid(row = 43, column = 4)
Label(root, text = "IB_T: -").grid(row = 43, column = 6)

# line 22
e_IB_U = DoubleVar(root)
e_IB_U = Entry(root, width=10)
e_IB_U.grid(row=43, column=1)

IB_U = e_IB_U.get()

e_IB_V = DoubleVar(root)
e_IB_V = Entry(root, width= 10)
e_IB_V.grid(row = 43, column = 3)

IB_V = e_IB_V.get()


e_IB_W = DoubleVar(root)
e_IB_W = Entry(root, width= 10)
e_IB_W.grid(row = 43, column = 5)

IB_W = e_IB_W.get()

e_IB_T = DoubleVar(root)
e_IB_T = Entry(root, width= 10)
e_IB_T.grid(row = 43, column = 7)

IB_T = e_IB_T.get()

# Line 23
r_Skew_symmetric = IntVar(root,"10")
Label(root, text = "SKEW SYMMETRIC: -").grid(row = 44, column = 0)
Radiobutton(root,text="ON",variable=r_Skew_symmetric,value=1).grid(row=44,column=1)
Radiobutton(root,text="OFF",variable=r_Skew_symmetric,value=0).grid(row=44,column=2)

Skew_symmetric = r_Skew_symmetric.get()

# line 23 entry values
Label(root, text="EXP FILTER: -").grid(row=45, column=0)
Label(root, text = "SIG FILTER: -").grid(row = 45, column = 2)

# line 23
e_exp_filter = IntVar(root)
e_exp_filter = Entry(root, width=10)
e_exp_filter.grid(row=45, column=1)

exp_filter = e_exp_filter.get()

e_sig_filter = IntVar(root)
e_sig_filter = Entry(root, width= 10)
e_sig_filter.grid(row = 45, column = 3)

sig_filter = e_sig_filter.get()

# Line 24
r_probe = IntVar(root,"10")
Label(root, text = "PROBE: -").grid(row = 46, column = 0)
Radiobutton(root,text="ON",variable=r_probe,value=1).grid(row=46,column=1)
Radiobutton(root,text="OFF",variable=r_probe,value=0).grid(row=46,column=2)

probe = r_probe.get()

# line 25 entry values
Label(root, text="Probe points: -").grid(row=47, column=0)

# line 25
e_probe_pts = IntVar(root)
e_probe_pts = Entry(root, width=10)
e_probe_pts.grid(row=47, column=1)

probe_pts = e_probe_pts.get()

# Line 24
r_inflow_turb = IntVar(root,"10")
Label(root, text = "INFLOW TURBULENCE: -").grid(row = 48, column = 0)
Radiobutton(root,text="ON",variable=r_inflow_turb,value=1).grid(row=48,column=1)
Radiobutton(root,text="OFF",variable=r_inflow_turb,value=0).grid(row=48,column=2)

inflow_turb = r_inflow_turb.get()

# line 25 entry values
Label(root, text="NUM EDDIES: -").grid(row=49, column=0)

# line 25
e_Num_eddies = IntVar(root)
e_Num_eddies = Entry(root, width=10)
e_Num_eddies.grid(row=49, column=1)

Num_eddies = e_Num_eddies.get()

# Line 25
r_Eddy_func = IntVar(root,"10")
Label(root, text = "EDDY FUNCTION: -").grid(row = 50, column = 0)
Radiobutton(root,text="TENT",variable=r_Eddy_func,value=1).grid(row=50,column=1)
Radiobutton(root,text="STEP",variable=r_Eddy_func,value=0).grid(row=50,column=2)

Eddy_func = r_Eddy_func.get()

# line 25 entry values
Label(root, text="Sigma: -").grid(row=51, column=0)
Label(root, text = "BoxLx: -").grid(row = 51, column = 2)
Label(root, text = "BoxLy: -").grid(row = 51, column = 4)
Label(root, text = "BoxLz: -").grid(row = 51, column = 6)
Label(root, text = "Turb Intensity: -").grid(row = 51, column = 8)

# line 25
e_sigma = DoubleVar(root)
e_sigma = Entry(root, width=10)
e_sigma.grid(row=51, column=1)

sigma = e_sigma.get()

e_BoxLx = DoubleVar(root)
e_BoxLx = Entry(root, width= 10)
e_BoxLx.grid(row = 51, column = 3)

BoxLx = e_BoxLx.get()

e_BoxLy = DoubleVar(root)
e_BoxLy = Entry(root, width= 10)
e_BoxLy.grid(row = 51, column = 5)

BoxLy = e_BoxLy.get()

e_BoxLz = DoubleVar(root)
e_BoxLz = Entry(root, width= 10)
e_BoxLz.grid(row = 51, column = 7)

BoxLz = e_BoxLz.get()

e_Turb_Intensity = DoubleVar(root)
e_Turb_Intensity = Entry(root, width= 10)
e_Turb_Intensity.grid(row = 51, column = 9)

Turb_Intensity = e_Turb_Intensity.get()

# line 26 entry values
Label(root, text="Dx: -").grid(row=52, column=0)
Label(root, text = "Dy: -").grid(row = 52, column = 2)
Label(root, text = "Dz: -").grid(row = 52, column = 4)

# line 26
e_Dx = DoubleVar(root)
e_Dx = Entry(root, width=10)
e_Dx.grid(row=52, column=1)

Dx = e_Dx.get()

e_Dy = DoubleVar(root)
e_Dy = Entry(root, width= 10)
e_Dy.grid(row = 52, column = 3)

Dy = e_Dy.get()

e_Dz = DoubleVar(root)
e_Dz = Entry(root, width= 10)
e_Dz.grid(row = 52, column = 5)

Dz = e_Dz.get()


# run button commands
def geninputfile():
    nblocks = e_nblocks.get()
    NImax = e_NImax.get()
    NJmax = e_NJmax.get()
    NKmax = e_NKmax.get()
    maxindex = max(NImax,NJmax,NKmax)
    Restart = r_Restart.get()
    Steady = r_Steady.get()
    Grid2D = r_Grid2D.get()
    Visc = r_viscosity.get()
    EDAC = r_compressibility.get()
    ERM = method.get()
    Wale = int(c_Wale.get())
    P0 = e_P0.get()
    T0 = e_T0.get()
    Pexit = e_Pexit.get()
    Pspill = e_Pspill.get()
    Twall = e_Twall.get()
    Lchar = e_Lchar.get()
    AoA = e_AoA.get()
    Mach = e_Mach.get()
    Re = e_Re.get()
    Lref = e_Lref.get()
    phi_bw = e_phi_bw.get()
    Interior_order = r_Interior_order.get()
    boundary1 = r_boundary1.get()
    boundary2 = r_boundary2.get()
    orderk = r_orderk.get()
    boundaryk1 = r_boundaryk1.get()
    boundaryk2 = r_boundaryk2.get()
    alphaf = e_alphaf.get()
    forderi = drop_menui.get()
    forderj = drop_menuj.get()
    forderk = drop_menuk.get()
    timeint = r_timeint.get()
    CFL = e_CFL.get()
    niter = e_niter.get()
    subiter = e_subiter.get()
    dt = e_dt.get()
    NSCBC = r_NSCBC.get()
    CBC_order = r_CBC_order.get()
    Sponge = r_Sponge.get()
    Sponge_a = e_Sponge_a.get()
    Sponge_n = e_Sponge_n.get()
    Sponge_Xl = e_Sponge_Xl.get()
    Sponge_Xh = e_Sponge_Xh.get()
    Sponge_Yl = e_Sponge_Yl.get()
    Sponge_Yh = e_Sponge_Yh.get()
    Sponge_Zl = e_Sponge_Zl.get()
    Sponge_Zh = e_Sponge_Zh.get()
    Sponge_radl = e_Sponge_radl.get()
    Sponge_radh = e_Sponge_radh.get()
    Animate = r_Animate.get()
    Anim_filename = e_Anim_filename.get()
    Anim_frequency = e_Anim_frequency.get()
    Back_frequency = e_Back_frequency.get()
    Average = r_Average.get()
    Average_restart = r_Average_restart.get()
    SelfI = int(b_SelfI.get())
    SelfJ = int(b_SelfJ.get())
    SelfK = int(b_SelfK.get())
    bulkturb = r_bulkturb.get()
    channel_flow = r_channel_flow.get()
    channel_restart = r_channel_restart.get()
    taylor_case = r_taylor_case.get()
    Rsv = r_Rsv.get()
    IBM = r_IBM.get()
    mu1 = e_mu1.get()
    moving_obj = e_moving_obj.get()
    del_x = e_del_x.get()
    nodes = e_nodes.get()
    elements = e_elements.get()
    SPTS1_limit = e_SPTS1_limit.get()
    fluid_points = e_fluid_points.get()
    ytop = e_ytop.get()
    ybot = e_ybot.get()
    yper = e_yper.get()
    IB_U = e_IB_U.get()
    IB_V = e_IB_V.get()
    IB_W = e_IB_W.get()
    IB_T = e_IB_T.get()
    Skew_symmetric = r_Skew_symmetric.get()
    exp_filter = e_exp_filter.get()
    sig_filter = e_sig_filter.get()
    probe = r_probe.get()
    probe_pts = e_probe_pts.get()
    inflow_turb = r_inflow_turb.get()
    Num_eddies = e_Num_eddies.get()
    Eddy_func = r_Eddy_func.get()
    sigma = e_sigma.get()
    BoxLx = e_BoxLx.get()
    BoxLy = e_BoxLy.get()
    BoxLz = e_BoxLz.get()
    Turb_Intensity = e_Turb_Intensity.get()
    Dx = e_Dx.get()
    Dy = e_Dy.get()
    Dz = e_Dz.get()
    Line1 = str(nblocks)+' '+str(NImax)+' '+str(NJmax)+' '+str(NKmax)+' '+str(maxindex)
    Line2 = str(Restart)+' '+str(Steady)+' '+str(Grid2D)
    Line3 = str(P0)+' '+str(T0)+' '+str(Pexit)+' '+str(Pspill)+' '+str(Twall)+' '+str(Lchar)+' '+str(AoA)+' '+str(Mach)+' '+str(Re)+' '+str(Lref)+' '+str(phi_bw)
    Line4 = str(Interior_order)
    Line5 = str(boundary1)+' '+str(boundary1)
    Line6 = str(orderk)+' '+str(boundaryk1)+' '+str(boundaryk1)
    Line7 = str(alphaf)
    Line8 = str(forderi)+' '+str(forderj)+' '+str(forderk)
    Line9 = str(timeint)+' '+str(CFL)+' '+str(niter)+' '+str(subiter)+' '+str(dt)
    Line10 = str(NSCBC)+' '+str(CBC_order)
    Line11 = str(Sponge)+' '+str(Sponge_a)+' '+str(Sponge_n)+' '+str(Sponge_Xl)+' '+str(Sponge_Xh)+' '+str(Sponge_Yl)+' '+str(Sponge_Yh)+' '+str(Sponge_Zl)+' '+str(Sponge_Zh)+' '+str(Sponge_radl)+' '+str(Sponge_radh)
    Line12 = str(Visc)+' '+str(EDAC)+' '+str(ERM)
    Line13 = str(Animate)+' '+str(Anim_filename)+' '+str(Anim_frequency)+' '+str(Back_frequency)
    Line14 = str(Average)+' '+str(Average_restart)
    Line15 = str(SelfI)+' '+str(SelfJ)+' '+str(SelfK)
    Line16 = str(bulkturb)
    Line17 = str(channel_flow)+' '+str(channel_restart)
    Line18 = str(taylor_case)+' '+str(Rsv)
    Line19 = str(IBM)+' '+str(mu1)+' '+str(moving_obj)+' '+str(del_x)
    Line20 = str(nodes)+' '+str(elements)+' '+str(SPTS1_limit)+' '+str(fluid_points)
    Line21 = str(ytop)+' '+str(ybot)+' '+str(yper)
    Line22 = str(IB_U)+' '+str(IB_V)+' '+str(IB_W)+' '+str(IB_T)
    Line23 = str(Skew_symmetric)+' '+str(exp_filter)+' '+str(sig_filter)
    Line24 = str(probe)+' '+str(probe_pts)
    Line25 = str(inflow_turb)+' '+str(Num_eddies)+' '+str(Eddy_func)+' '+str(sigma)+' '+str(BoxLx)+' '+str(BoxLy)+' '+str(BoxLz)+' '+str(Turb_Intensity)
    Line26 = str(Dx)+' '+str(Dy)+' '+str(Dz)
    Line27 = str(Wale)
    Line = [Line1,Line2,Line3,Line4,Line5,Line6,Line7,Line8,Line9,Line10,Line11,Line12,Line13,Line14,Line15,Line16,Line17,Line18,Line19,Line20,Line21,Line22,Line23,Line24,Line25,Line26,Line27]
    with open('input.in', 'w') as f:
        for line in Line:
            f.write(line+'\n')



# run button
Button(root, text = "GENERATE INPUT FILE", command=geninputfile).grid(row=54,column=3)

# display Menu
window.config(menu = menubar)
mainloop()
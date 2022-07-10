import pandas
column_names = [i for i in range(0, 100)]
df=pandas.read_csv('input.in', header=None, sep="\s|,|\t", names=column_names)
# Line 1
nblocks = int(df[0][0])
NImax = int(df[1][0])
NJmax = int(df[2][0])
NKmax = int(df[3][0])
maxindex = max(NImax,NJmax,NKmax)
# Line 2 Start
Restart = int(df[0][1])
# Buttons - Fresh, Restart
Steady = int(df[1][1])
# Buttons - Steady, Unsteady
Grid2D = int(df[2][1])
# Buttons - 2 2D, 3D
# Line 12
# Buttons - Viscous, Inviscid
# Buttons - Compressible, Incompressible
# Buttons - Method - LES, k-omega
# Line 3 Entry values
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
# Buttons - E2, E4, C4, C6
# Line 5
boundary1 = int(df[0][4])
# Buttons - 2,4
boundary2 = int(df[1][4])
# Buttons - 2,4
# Line 6
orderk = int(df[0][5])
# Buttons - E2, E4, C4, C6
boundaryk1 = int(df[1][5])
# Buttons - 2,4
boundaryk2 = int(df[2][5])
# Buttons - 2,4
# Line 7
alphaf = float(df[0][6])
# Entry value
# Line 8
forderi = int(df[0][7])
forderj = int(df[1][7])
forderk = int(df[2][7])
# Buttons/Drop down - 2, 4, 6, 8, 10
# Line 9
timeint = int(df[0][8])
CFL = float(df[1][8])
niter = int(df[2][8])
subiter = int(df[3][8])
dt = float(df[4][8])
# Buttons - time integration - 1,2
# Entry values - CFL, niter, subiter, dt
# Line 10
NSCBC = int(df[0][9])
# Buttons - NSCBC - on, off
CBC_order = int(df[1][9])
# Entry value
# Line 11
Sponge = int(df[0][10])
# Buttons - Sponge - on, off
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
# Entry value
# Line 12
Visc = int(df[0][11])
EDAC = int(df[1][11])
ERM =  int(df[2][11])
# Line 13
Animate = int(df[0][12])
# Buttons - Animate - on, off
Anim_filename = int(df[1][12])
Anim_frequency =  int(df[2][12])
Back_frequency =  int(df[3][12])
# Entry value
# Line 14
Average = int(df[0][13])
# Buttons - Average - on, off
Average_restart = int(df[1][13])
# Buttons - Restart - on, off

# Line 15
SelfI = int(df[0][14])
SelfJ = int(df[1][14])
SelfK =  int(df[2][14])
# Check boxes - Periodicity - I, J, K
# Line 16
bulkturb = int(df[0][15])
# Buttons - Bulk Turbulence - on, off
# Line 17
# Buttons - Channel case - on, off
channel_flow = int(df[0][16])
# Buttons - Channel restart - on, off
channel_restart = int(df[1][16])
# Line 18
# Buttons - Taylor case - on, off
taylor_case = int(df[0][17])
# Buttons - RSV case - on, off
Rsv = int(df[1][17])
# Line 19
# Buttons - IBM - on, off
IBM = int(df[0][18])
mu1 = int(df[1][18])
moving_obj = int(df[2][18])
del_x = float(df[3][18])
# Entry value
# Line 20
# Entry values
nodes = int(df[0][19])
elements = int(df[1][19])
SPTS1_limit = int(df[2][19])
fluid_points = int(df[3][19])
# Line 21
# Entry values
ytop = int(df[0][20])
ybot = int(df[1][20])
yper = int(df[2][20])
# Line 22
# Entry values
IB_U = float(df[0][21])
IB_V = float(df[1][21])
IB_W = float(df[2][21])
IB_T = float(df[3][21])
# Line 23
Skew_symmetric = int(df[0][22])
# Buttons - Skew-Symmetric on/off
exp_filter = int(df[1][22])
sig_filter = int(df[2][22])
# Entry values
# Line 24
probe = int(df[0][23])
# Buttons - Probe on/off
probe_pts = int(df[1][23])
# Entry value
# Line 25
# Buttons - Inflow Turbulence on/off
inflow_turb = int(df[0][24])
# Entry value - N Eddies
Num_eddies = int(df[1][24])
# Buttons - Function - Tent, Step
Eddy_func = int(df[2][24])
# Entry values
sigma = float(df[3][24])
BoxLx = float(df[4][24])
BoxLy = float(df[5][24])
BoxLz = float(df[6][24])
Turb_Intensity = float(df[7][24])
# Line 26
# Entry values
Dx = float(df[0][25])
Dy = float(df[1][25])
Dz = float(df[2][25])
# Line 27
# Buttons - On/off
Wale = int(df[0][26])
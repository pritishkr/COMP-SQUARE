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
Line11 = str(Sponge)+' '+str(Sponge_a)+' '+str(Sponge_n)+' '+str(Sponge_X1)+' '+str(Sponge_Xh)+' '+str(Sponge_Y1)+' '+str(Sponge_Yh)+' '+str(Sponge_Z1)+' '+str(Sponge_Zh)+' '+str(Sponge_radl)+' '+str(Sponge_radh)
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
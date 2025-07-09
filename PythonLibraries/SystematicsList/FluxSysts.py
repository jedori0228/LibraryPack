from SystInfo import SystInfo
from SystGroupInfo import SystGroupInfo

def GetNuMIBeamline_HornCurr():
    ret = SystGroupInfo(Name='HornCurr', Latex='HornCurr')
    ret.SystInfos.append( SystInfo(Name='numi_HornCurr', Latex='HornCurr', Type='multisigma') )
    return ret
def GetNuMIBeamline_Horn1_x():
    ret = SystGroupInfo(Name='Horn1_x', Latex='Horn1_x')
    ret.SystInfos.append( SystInfo(Name='numi_Horn1_x', Latex='Horn1_x', Type='multisigma') )
    return ret
def GetNuMIBeamline_Horn1_y():
    ret = SystGroupInfo(Name='Horn1_y', Latex='Horn1_y')
    ret.SystInfos.append( SystInfo(Name='numi_Horn1_y', Latex='Horn1_y', Type='multisigma') )
    return ret
def GetNuMIBeamline_Beam_spot():
    ret = SystGroupInfo(Name='Beam_spot', Latex='Beam_spot')
    ret.SystInfos.append( SystInfo(Name='numi_Beam_spot', Latex='Beam_spot', Type='multisigma') )
    return ret
def GetNuMIBeamline_Horn2_x():
    ret = SystGroupInfo(Name='Horn2_x', Latex='Horn2_x')
    ret.SystInfos.append( SystInfo(Name='numi_Horn2_x', Latex='Horn2_x', Type='multisigma') )
    return ret
def GetNuMIBeamline_Horn2_y():
    ret = SystGroupInfo(Name='Horn2_y', Latex='Horn2_y')
    ret.SystInfos.append( SystInfo(Name='numi_Horn2_y', Latex='Horn2_y', Type='multisigma') )
    return ret
def GetNuMIBeamline_Horns_water():
    ret = SystGroupInfo(Name='Horns_water', Latex='Horns_water')
    ret.SystInfos.append( SystInfo(Name='numi_Horns_water', Latex='Horns_water', Type='multisigma') )
    return ret
def GetNuMIBeamline_Beam_shift_x():
    ret = SystGroupInfo(Name='Beam_shift_x', Latex='Beam_shift_x')
    ret.SystInfos.append( SystInfo(Name='numi_Beam_shift_x', Latex='Beam_shift_x', Type='multisigma') )
    return ret
def GetNuMIBeamline_Beam_shift_y():
    ret = SystGroupInfo(Name='Beam_shift_y', Latex='Beam_shift_y')
    ret.SystInfos.append( SystInfo(Name='numi_Beam_shift_y', Latex='Beam_shift_y', Type='multisigma') )
    return ret
def GetNuMIBeamline_Target_z():
    ret = SystGroupInfo(Name='Target_z', Latex='Target_z')
    ret.SystInfos.append( SystInfo(Name='numi_Target_z', Latex='Target_z', Type='multisigma') )
    return ret

def GetNuMIFluxBeamlineSystGroupInfo():

    ret = SystGroupInfo(Name='Beamline', Latex='Flux, Beamline')

    # ret.SystInfos.append( SystInfo(Name='numi_beam_div', Latex=r'beam 54 $\mu$rad divergence', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_beam_power', Latex=r'beam power', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_beam_shift_y', Latex=r'beam shift in y $\pm$1mm', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_beam_shift_x', Latex=r'beam shift in x $\pm$1mm', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_beam_spot', Latex=r'beam spot size $\pm$0.2cm', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_horn1_x', Latex=r'horn1 x position $\pm$0.3cm', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_horn1_y', Latex=r'horn1 y position $\pm$0.3cm', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_horn_current_plus', Latex=r'horn current +2kA', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_water_layer', Latex=r'water layer $\pm$1mm', Type='multisigma') )

    ret.SystInfos.append( SystInfo(Name='numi_HornCurr', Latex=r'HornCurr', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Horn1_x', Latex=r'Horn1_x', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Horn1_y', Latex=r'Horn1_y', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Beam_spot', Latex=r'Beam_spot', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Horn2_x', Latex=r'Horn2_x', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Horn2_y', Latex=r'Horn2_y', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Horns_water', Latex=r'Horns_water', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Beam_shift_x', Latex=r'Beam_shift_x', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Beam_shift_y', Latex=r'Beam_shift_y', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Target_z', Latex=r'Target_z', Type='multisigma') )

    return ret

def GetNuMIFluxHadronProductionPCASystGroupInfo(N):

    ret = SystGroupInfo(Name='FluxHP', Latex='Flux, HP')

    for i in range(0,N):
        ret.SystInfos.append( SystInfo(Name='numi_pc_%d'%(i), Latex='NuMI HP PCA%d'%(i), Type='multisigma') )

    return ret

def GetNuMIFluxStatSystGroupInfo():

    ret = SystGroupInfo(Name='FluxStat', Latex='Flux, stat.')

    ret.SystInfos.append( SystInfo(Name='numi_stat', Latex='NuMI stat.', Type='multisigma') )

    return ret

def GetNuMIFluxG3ChaseSystGroupInfo():

    ret = SystGroupInfo(Name='G3Chase', Latex='G3Chase')

    ret.SystInfos.append( SystInfo(Name='numi_beam_G3Chase', Latex='G3Chase', Type='multisigma' ) )

    return ret

def GetCosmicSliceSystGroupInfo():

  ret = SystGroupInfo(Name='CosmicSlice', Latex='Cosmic slice')

  ret.SystInfos.append( SystInfo(Name='CosmicSlice', Latex=r'40% on cosmic slice', Type='norm', OneSig=0.50, ApplyOn='IsSignal==5') )

  return ret



def GetAllNuMIFluxSystGroupInfo(AddG3Chase=True):

    ret = SystGroupInfo(Name='Flux', Latex='Flux')

    # ret.SystInfos.append( SystInfo(Name='numi_beam_div', Latex=r'beam 54 $\mu$rad divergence', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_beam_power', Latex=r'beam power', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_beam_shift_y', Latex=r'beam shift in y $\pm$1mm', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_beam_shift_x', Latex=r'beam shift in x $\pm$1mm', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_beam_spot', Latex=r'beam spot size $\pm$0.2cm', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_horn1_x', Latex=r'horn1 x position $\pm$0.3cm', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_horn1_y', Latex=r'horn1 y position $\pm$0.3cm', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_horn_current_plus', Latex=r'horn current +2kA', Type='multisigma') )
    # ret.SystInfos.append( SystInfo(Name='numi_water_layer', Latex=r'water layer $\pm$1mm', Type='multisigma') )

    ret.SystInfos.append( SystInfo(Name='numi_HornCurr', Latex=r'HornCurr', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Horn1_x', Latex=r'Horn1_x', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Horn1_y', Latex=r'Horn1_y', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Beam_spot', Latex=r'Beam_spot', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Horn2_x', Latex=r'Horn2_x', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Horn2_y', Latex=r'Horn2_y', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Horns_water', Latex=r'Horns_water', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Beam_shift_x', Latex=r'Beam_shift_x', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Beam_shift_y', Latex=r'Beam_shift_y', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_Target_z', Latex=r'Target_z', Type='multisigma') )

    for i in range(0, 15):
        ret.SystInfos.append( SystInfo(Name='numi_pc_%d'%(i), Latex='NuMI HP PCA%d'%(i), Type='multisigma') )

    ret.SystInfos.append( SystInfo(Name='numi_stat', Latex='NuMI stat.', Type='multisigma') )

    if AddG3Chase:
      ret.SystInfos.append( SystInfo(Name='numi_beam_G3Chase', Latex='G3Chase', Type='multisigma' ) )

    ret.SystInfos.append( SystInfo(Name='CosmicSlice', Latex=r'40% on cosmic slice', Type='norm', OneSig=0.50, ApplyOn='IsSignal==5') )

    return ret


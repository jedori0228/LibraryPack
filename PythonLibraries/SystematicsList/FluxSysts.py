from SystInfo import SystInfo
from SystGroupInfo import SystGroupInfo

def GetNuMIFluxBeamlineSystGroupInfo():

    ret = SystGroupInfo(Name='Beamline', Latex='Flux, Beamline')

    ret.SystInfos.append( SystInfo(Name='numi_beam_div', Latex=r'beam 54 $\mu$rad divergence', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_beam_power', Latex=r'beam power', Type='multisigma') )

    #ret.SystInfos.append( SystInfo(Name='numi_beam_shift_y_minus', Latex=r'beam shift in y -1mm', Type='multisigma') )
    #ret.SystInfos.append( SystInfo(Name='numi_beam_shift_y_plus', Latex=r'beam shift in y +1mm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_beam_shift_y', Latex=r'beam shift in y $\pm$1mm', Type='multisigma') )

    ret.SystInfos.append( SystInfo(Name='numi_beam_shift_x', Latex=r'beam shift in x $\pm$1mm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_beam_spot', Latex=r'beam spot size $\pm$0.2cm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_horn1_x', Latex=r'horn1 x position $\pm$0.3cm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_horn1_y', Latex=r'horn1 y position $\pm$0.3cm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_horn_current_plus', Latex=r'horn current +2kA', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_water_layer', Latex=r'water layer $\pm$1mm', Type='multisigma') )

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

def GetAllNuMIFluxSystGroupInfo(AddG3Chase=True):

    ret = SystGroupInfo(Name='Flux', Latex='Flux')

    ret.SystInfos.append( SystInfo(Name='numi_beam_div', Latex=r'beam 54 $\mu$rad divergence', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_beam_power', Latex=r'beam power', Type='multisigma') )
    #ret.SystInfos.append( SystInfo(Name='numi_beam_shift_y_minus', Latex=r'beam shift in y -1mm', Type='multisigma') )
    #ret.SystInfos.append( SystInfo(Name='numi_beam_shift_y_plus', Latex=r'beam shift in y +1mm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_beam_shift_y', Latex=r'beam shift in y $\pm$1mm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_beam_shift_x', Latex=r'beam shift in x $\pm$1mm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_beam_spot', Latex=r'beam spot size $\pm$0.2cm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_horn1_x', Latex=r'horn1 x position $\pm$0.3cm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_horn1_y', Latex=r'horn1 y position $\pm$0.3cm', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_horn_current_plus', Latex=r'horn current +2kA', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='numi_water_layer', Latex=r'water layer $\pm$1mm', Type='multisigma') )

    for i in range(0, 98):
        ret.SystInfos.append( SystInfo(Name='numi_pc_%d'%(i), Latex='NuMI HP PCA%d'%(i), Type='multisigma') )

    ret.SystInfos.append( SystInfo(Name='numi_stat', Latex='NuMI stat.', Type='multisigma') )

    if AddG3Chase:
      ret.SystInfos.append( SystInfo(Name='numi_beam_G3Chase', Latex='G3Chase', Type='multisigma' ) )

    return ret

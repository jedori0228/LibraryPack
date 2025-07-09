from SystInfo import SystInfo
from SystGroupInfo import SystGroupInfo

def GetNuSystCCQERPAGroupInfo():

    ret = SystGroupInfo(Name='NuSystCCQERPA', Latex='Template CCQE RPA')

    ret.SystInfos.append( SystInfo(Name='CCQERPAReweight', Latex='Template CCQE RPA', Type='morph') )

    return ret

def GetNuSystPCAZExpGroupInfo():

    ret = SystGroupInfo(Name='NuSystPCAZExp', Latex='PCA-ed Z-exp params')

    ret.SystInfos.append( SystInfo(Name='ZExpPCAB1', Latex='PCA-ed z-exp, b1', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='ZExpPCAB2', Latex='PCA-ed z-exp, b2', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='ZExpPCAB3', Latex='PCA-ed z-exp, b3', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='ZExpPCAB4', Latex='PCA-ed z-exp, b4', Type='multisigma') )

    return ret

def GetNuSystLars2p2hGroupInfo():

    ret = SystGroupInfo(Name='Lars2p2h', Latex='Lars\' 2p2h')

    ret.SystInfos.append( SystInfo(Name='Lars2p2h_XSecShape_CCMEC', Latex='2p2h to Valencia', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='Lars2p2h_XSecShape_CCMEC_Empirical', Latex='2p2h to GENIE empirical', Type='morph') )
    # ret.SystInfos.append( SystInfo(Name='Lars2p2h_XSecShape_CCMEC_Martini', Latex='2p2h to Martini', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='Lars2p2h_EnergyDependence_CCMEC', Latex='Lars'' 2p2h, EnergyDependence_CCMEC', Type='morph') )



    ret.SystInfos.append( SystInfo(Name='Lars2p2p_DecayAngMEC_P1Variation_P2CV', Latex='Decay angle MEC, P1', Type='morph') )
    # ret.SystInfos.append( SystInfo(Name='Lars2p2p_DecayAngMEC_P1Variation_P2p1sig', Latex=r'Decay angle MEC, P1 (P2=+1$\sigma$)', Type='morph') )
    # ret.SystInfos.append( SystInfo(Name='Lars2p2p_DecayAngMEC_P1p1sig_P2Variation', Latex=r'Decay angle MEC, P2 (P1=+1$\sigma$)', Type='morph') )

    return ret


def GetNuSystFSIGroupInfo():

    ret = SystGroupInfo(Name='NuSystFSI', Latex='Template FSI')

    ret.SystInfos.append( SystInfo(Name='FSIReweight_hN', Latex='hA-to-hN', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='FSIReweight_INCL', Latex='hA-to-INCL', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='FSIReweight_G4BC', Latex='hA-to-G4BC', Type='morph') )

    return ret

def GetNuSystNuclearGroundStateGroupInfo():

    ret = SystGroupInfo(Name='NuSystNuclearGroundState', Latex='Nuclear ground state')

    ret.SystInfos.append( SystInfo(Name='Emiss_CorrTail_Ar_p', Latex=r'$E_{miss}$, CorrTail, Ar, p', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='Emiss_CorrTail_Ar_n', Latex=r'$E_{miss}$, CorrTail, Ar, n', Type='multisigma') )
    
    ret.SystInfos.append( SystInfo(Name='Emiss_Linear_Ar_p', Latex=r'$E_{miss}$, Linear non-SRC, Ar, p', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='Emiss_Linear_Ar_n', Latex=r'$E_{miss}$, Linear non-SRC, Ar, n', Type='multisigma') )

    ret.SystInfos.append( SystInfo(Name='Emiss_ShiftPeak_Ar_p', Latex=r'$E_{miss}$, peak shift, Ar, p', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='Emiss_ShiftPeak_Ar_n', Latex=r'$E_{miss}$, peak shift, Ar, n', Type='multisigma') )

    return ret
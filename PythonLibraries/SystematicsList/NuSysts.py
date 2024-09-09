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

    #ret.SystInfos.append( SystInfo(Name='Lars2p2h_XSecShape_CCMEC_Empirical', Latex='Lars'' 2p2h, XSecShape_CCMEC_Empirical', Type='morph') )
    #ret.SystInfos.append( SystInfo(Name='Lars2p2h_XSecShape_CCMEC_Martini', Latex='Lars'' 2p2h, XSecShape_CCMEC_Martini', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='Lars2p2h_EnergyDependence_CCMEC', Latex='Lars'' 2p2h, EnergyDependence_CCMEC', Type='morph') )



    ret.SystInfos.append( SystInfo(Name='Lars2p2p_DecayAngMEC_P1Variation_P2CV', Latex='Decay angle MEC, P1', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='Lars2p2p_DecayAngMEC_P1Variation_P2p1sig', Latex=r'Decay angle MEC, P1 (P2=+1$\sigma$)', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='Lars2p2p_DecayAngMEC_P1p1sig_P2Variation', Latex=r'Decay angle MEC, P2 (P1=+1$\sigma$)', Type='morph') )

    return ret



from SystInfo import SystInfo
from SystGroupInfo import SystGroupInfo

def GetGENIETestSystGroupInfo():

    ret = SystGroupInfo(Name='TEST', Latex='TEST')

    ret.SystInfos.append( SystInfo(Name='FSI_pi_VariationResponse', Latex='FSI $\pi$', Type='multisim', NUniv=100) )
    #ret.SystInfos.append( SystInfo(Name='FSI_N_VariationResponse', Latex='FSI N', Type='multisim', NUniv=100) )

    return ret

def GetGENIECCQESystGroupInfo():

    ret = SystGroupInfo(Name='CCQE', Latex='CCQE')

    ret.SystInfos.append( SystInfo(Name='RPA_CCQE', Latex='RPA CCQE', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='CoulombCCQE', Latex='CCQE Coulomb', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='VecFFCCQEshape', Latex='ZExp-to-Dipole', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='ZExpAVariationResponse', Latex='ZExp Coeff.', Type='multisim', NUniv=100) )

    return ret

def GetGENIEMECSystGroupInfo():

    ret = SystGroupInfo(Name='MEC', Latex='MEC')

    ret.SystInfos.append( SystInfo(Name='NormCCMEC', Latex='CCMEC norm.', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NormNCMEC', Latex='NCMEC norm.', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='DecayAngMEC', Latex='MEC angular dist.', Type='morph') )

    return ret

## RES

def GetGENIEResSystGroupInfo():

    ret = SystGroupInfo(Name='Res', Latex='Res')

    ret.SystInfos.append( SystInfo(Name='CCRESVariationResponse', Latex=r'CC Res, $M_{A}$ and $M_{V}$', Type='multisim', NUniv=100) )
    ret.SystInfos.append( SystInfo(Name='NCRESVariationResponse', Latex=r'NC Res, $M_{A}$ and $M_{V}$', Type='multisim', NUniv=100) )
    ret.SystInfos.append( SystInfo(Name='RDecBR1gamma', Latex='X+#gamma BR', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='RDecBR1eta', Latex='X+#eta BR', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='Theta_Delta2Npi', Latex='#Delta#rightarrow#pi N angular dist.', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='ThetaDelta2NRad', Latex='#Delta#rightarrow#gamma N angular dist.', Type='morph') )

    return ret

def GetCC1piTPiSystGroupInfo():

    ret = SystGroupInfo(Name='CC1piTPi', Latex=r'CC$1\pi T_{Pi}$')

    ret.SystInfos.append( SystInfo(Name='CC1piTPi', Latex=r'CC$1\pi T_{Pi}$', Type='multisigma') )

    return ret

## Non-res

def GetGENIENonResSystGroupInfo():

    ret = SystGroupInfo(Name='NonRes', Latex='NonRes')

    ret.SystInfos.append( SystInfo(Name='NonRESBGvpCC1pi', Latex=r'$\nu$ p CC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvpCC2pi', Latex=r'$\nu$ p CC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvpNC1pi', Latex=r'$\nu$ p NC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvpNC2pi', Latex=r'$\nu$ p NC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvnCC1pi', Latex=r'$\nu$ n CC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvnCC2pi', Latex=r'$\nu$ n CC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvnNC1pi', Latex=r'$\nu$ n NC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvnNC2pi', Latex=r'$\nu$ n NC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarpCC1pi', Latex=r'$\bar{\nu}$ p CC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarpCC2pi', Latex=r'$\bar{\nu}$ p CC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarpNC1pi', Latex=r'$\bar{\nu}$ p NC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarpNC2pi', Latex=r'$\bar{\nu}$ p NC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarnCC1pi', Latex=r'$\bar{\nu}$ n CC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarnCC2pi', Latex=r'$\bar{\nu}$ n CC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarnNC1pi', Latex=r'$\bar{\nu}$ n NC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarnNC2pi', Latex=r'$\bar{\nu}$ n NC 2pi', Type='multisigma') )

    return ret

def GetGENIEDISSystGroupInfo():

    ret = SystGroupInfo(Name='DIS', Latex='DIS')

    ret.SystInfos.append( SystInfo(Name='DISBYVariationResponse', Latex='DIS DY params.', Type='multisim', NUniv=100) )

    return ret

def GetGENIECOHSystGroupInfo():

    ret = SystGroupInfo(Name='COH', Latex='COH')

    ret.SystInfos.append( SystInfo(Name='NormCCCOH', Latex='CC COH norm.', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NormNCCOH', Latex='NC COH norm.', Type='multisigma') )

    return ret

def GetGENIEFSISystGroupInfo():

    ret = SystGroupInfo(Name='FSI', Latex='FSI')

    ret.SystInfos.append( SystInfo(Name='FSI_pi_VariationResponse', Latex='FSI $\pi$', Type='multisim', NUniv=100) )
    ret.SystInfos.append( SystInfo(Name='FSI_N_VariationResponse', Latex='FSI N', Type='multisim', NUniv=100) )

    return ret

def GetGENIENCELSystGroupInfo():

    ret = SystGroupInfo(Name='NCEL', Latex='NCEL')

    ret.SystInfos.append( SystInfo(Name='NCELVariationResponse', Latex='NC elastic', Type='multisim', NUniv=100) )

    return ret


def GetAllGENIESystGroupInfo(AddSPP=True):

    ret = SystGroupInfo(Name='xsec', Latex='Cross-section')

    ret.SystInfos.append( SystInfo(Name='RPA_CCQE', Latex='RPA CCQE', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='CoulombCCQE', Latex='CCQE Coulomb', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='VecFFCCQEshape', Latex='ZExp-to-Dipole', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='ZExpAVariationResponse', Latex='ZExp Coeff.', Type='multisim', NUniv=100) )

    ret.SystInfos.append( SystInfo(Name='NormCCMEC', Latex='CCMEC norm.', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NormNCMEC', Latex='NCMEC norm.', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='DecayAngMEC', Latex='MEC angular dist.', Type='morph') )

    ret.SystInfos.append( SystInfo(Name='CCRESVariationResponse', Latex=r'CC Res, $M_{A}$ and $M_{V}$', Type='multisim', NUniv=100) )
    ret.SystInfos.append( SystInfo(Name='NCRESVariationResponse', Latex=r'NC Res, $M_{A}$ and $M_{V}$', Type='multisim', NUniv=100) )
    ret.SystInfos.append( SystInfo(Name='RDecBR1gamma', Latex=r'$X+\gamma$ BR', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='RDecBR1eta', Latex=r'$X+\eta$ BR', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='Theta_Delta2Npi', Latex=r'$\Delta \rightarrow \pi N$ angular dist.', Type='morph') )
    ret.SystInfos.append( SystInfo(Name='ThetaDelta2NRad', Latex=r'$\Delta \rightarrow \gamma N$ angular dist.', Type='morph') )
                         
    ret.SystInfos.append( SystInfo(Name='NonRESBGvpCC1pi', Latex=r'$\nu$ p CC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvpCC2pi', Latex=r'$\nu$ p CC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvpNC1pi', Latex=r'$\nu$ p NC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvpNC2pi', Latex=r'$\nu$ p NC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvnCC1pi', Latex=r'$\nu$ n CC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvnCC2pi', Latex=r'$\nu$ n CC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvnNC1pi', Latex=r'$\nu$ n NC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvnNC2pi', Latex=r'$\nu$ n NC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarpCC1pi', Latex=r'$\bar{\nu}$ p CC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarpCC2pi', Latex=r'$\bar{\nu}$ p CC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarpNC1pi', Latex=r'$\bar{\nu}$ p NC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarpNC2pi', Latex=r'$\bar{\nu}$ p NC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarnCC1pi', Latex=r'$\bar{\nu}$ n CC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarnCC2pi', Latex=r'$\bar{\nu}$ n CC 2pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarnNC1pi', Latex=r'$\bar{\nu}$ n NC 1pi', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NonRESBGvbarnNC2pi', Latex=r'$\bar{\nu}$ n NC 2pi', Type='multisigma') )

    ret.SystInfos.append( SystInfo(Name='DISBYVariationResponse', Latex='DIS DY params.', Type='multisim', NUniv=100) )

    ret.SystInfos.append( SystInfo(Name='NormCCCOH', Latex='CC COH norm.', Type='multisigma') )
    ret.SystInfos.append( SystInfo(Name='NormNCCOH', Latex='NC COH norm.', Type='multisigma') )

    ret.SystInfos.append( SystInfo(Name='FSI_pi_VariationResponse', Latex='FSI $\pi$', Type='multisim', NUniv=100) )
    ret.SystInfos.append( SystInfo(Name='FSI_N_VariationResponse', Latex='FSI N', Type='multisim', NUniv=100) )

    ret.SystInfos.append( SystInfo(Name='NCELVariationResponse', Latex='NC elastic', Type='multisim', NUniv=100) )

    if AddSPP:
      ret.SystInfos.append( SystInfo(Name='CC1piTPi', Latex=r'CC$1\pi T_{Pi}$', Type='multisigma') )


    return ret

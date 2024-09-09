from SystInfo import SystInfo
from SystGroupInfo import SystGroupInfo

'''
  128: reinteractions_piminus_Geant4, type 0, 1000 universes, adjusted parameters:
    fPiMinusAbs
    fPiMinusCex
    fPiMinusDCex
    fPiMinusElast
    fPiMinusPiProd
    fPiMinusReacHigh
    fPiMinusReacLow
  129: reinteractions_piplus_Geant4, type 0, 1000 universes, adjusted parameters:
    fPiPlusAbs
    fPiPlusCex
    fPiPlusDCex
    fPiPlusElast
    fPiPlusPiProd
    fPiPlusReacHigh
    fPiPlusReacLow
  130: reinteractions_proton_Geant4, type 0, 1000 universes, adjusted parameters:
    fProtonElast
    fProtonReac
'''

def GetGEANT4HadronFateSystGroupInfo():

  ret = SystGroupInfo(Name='GEANT4', Latex='GEANT4')

  ret.SystInfos.append( SystInfo(Name='reinteractions_piminus_Geant4', Latex=r'G4 $\pi^{-}$', Type='multisim', NUniv=1000, RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='reinteractions_piplus_Geant4', Latex=r'G4 $\pi^{+}$', Type='multisim', NUniv=1000, RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='reinteractions_proton_Geant4', Latex=r'G4 p', Type='multisim', NUniv=1000, RecoOnly=True) )

  return ret


def GetGEANT4ChargedPionFateSystGroupInfo():

  ret = SystGroupInfo(Name='G4pipm', Latex=r'G4 #pi^{#pm}')

  ret.SystInfos.append( SystInfo(Name='reinteractions_piminus_Geant4', Latex=r'G4 $\pi^{-}$', Type='multisim', NUniv=1000, RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='reinteractions_piplus_Geant4', Latex=r'G4 $\pi^{+}$', Type='multisim', NUniv=1000, RecoOnly=True) )

  return ret


def GetGEANT4ProtonFateSystGroupInfo():

  ret = SystGroupInfo(Name='G4proton', Latex='G4 p')

  ret.SystInfos.append( SystInfo(Name='reinteractions_proton_Geant4', Latex=r'G4 p', Type='multisim', NUniv=1000, RecoOnly=True) )

  return ret

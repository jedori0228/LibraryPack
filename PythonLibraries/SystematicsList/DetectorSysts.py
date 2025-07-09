from SystInfo import SystInfo
from SystGroupInfo import SystGroupInfo

# Calorimetry
def GetCalodEdXShiftSystGroupInfo():
  ret = SystGroupInfo(Name='CalodEdXShift', Latex=r'Calo. $dE/dX$ $\pm 1 \sigma$')
  ret.SystInfos.append( SystInfo(Name='CalodEdXShiftUp', Latex=r'Calo. $dE/dX$ $+1\sigma$', Type='shift', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='CalodEdXShiftDown', Latex=r'Calo. $dE/dX$ $-1\sigma$', Type='shift', RecoOnly=True) )
  return ret
def GetCaloGainShiftSystGroupInfo():
  ret = SystGroupInfo(Name='CaloGainShift', Latex=r'Calo. gain $\pm 1 \sigma$')
  ret.SystInfos.append( SystInfo(Name='CaloGainShiftUp', Latex=r'Calo. gain $+1\sigma$', Type='shift', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='CaloGainShiftDown', Latex=r'Calo. gain $-1\sigma$', Type='shift', RecoOnly=True) )
  return ret
# - Up/Down Separately
def GetCalodEdXShiftUpSystGroupInfo():
  ret = SystGroupInfo(Name='CalodEdXShiftUp', Latex=r'Calo. $dE/dX$ $+1\sigma$')
  ret.SystInfos.append( SystInfo(Name='CalodEdXShiftUp', Latex=r'Calo. $dE/dX$ $+1\sigma$', Type='shift', RecoOnly=True) )
  return ret
def GetCalodEdXShiftDownSystGroupInfo():
  ret = SystGroupInfo(Name='CalodEdXShiftDown', Latex=r'Calo. $dE/dX$ $-1\sigma$')
  ret.SystInfos.append( SystInfo(Name='CalodEdXShiftDown', Latex=r'Calo. $dE/dX$ $-1\sigma$', Type='shift', RecoOnly=True) )
  return ret
def GetCaloGainShiftUpSystGroupInfo():
  ret = SystGroupInfo(Name='CaloGainShiftUp', Latex=r'Calo. gain $+1\sigma$')
  ret.SystInfos.append( SystInfo(Name='CaloGainShiftUp', Latex=r'Calo. gain $+1\sigma$', Type='shift', RecoOnly=True) )
  return ret
def GetCaloGainShiftDownSystGroupInfo():
  ret = SystGroupInfo(Name='CaloGainShiftDown', Latex=r'Calo. gain $-1\sigma$')
  ret.SystInfos.append( SystInfo(Name='CaloGainShiftDown', Latex=r'Calo. gain $-1\sigma$', Type='shift', RecoOnly=True) )
  return ret
# - Reweighting veresion
def GetCaloGainShiftFlatSystGroupInfo():
  ret = SystGroupInfo(Name='NuMIXSecCaloGainSyst', Latex=r'Calo. gain $\pm 1 \sigma$')
  ret.SystInfos.append( SystInfo(Name='NuMIXSecCaloGainSyst', Latex=r'Calo. gain $\pm1\sigma$; 3%', Type='multisigma', RecoOnly=True) )
  return ret

# MC Variation
def GetFrontIndPlaneGainSystGroupInfo():
  ret = SystGroupInfo(Name='NuMIXSecFrontIndPlaneGainSyst', Latex=r'Front ind. plane gain $\pm20$%')
  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneGainSyst', Latex=r'Front ind. plane gain $\pm20$%', Type='multisigma', RecoOnly=True) )
  return ret
def GetFrontIndPlaneNoiseSyst():
  ret = SystGroupInfo(Name='NuMIXSecFrontIndPlaneNoiseSyst', Latex=r'Front ind. plane noise +10%')
  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneNoiseSyst', Latex=r'Front ind. plane noise +10%', Type='multisigma', RecoOnly=True) )
  return ret
def GetFrontIndPlaneSignalShapeSyst():
  ret = SystGroupInfo(Name='NuMIXSecFrontIndPlaneSignalShapeSyst', Latex=r'Front ind. plane signal shape')
  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneSignalShapeSyst', Latex=r'Front ind. plane signal shape', Type='multisigma', RecoOnly=True) )
  return ret
def GetFrontIndPlaneSignalShapeFittedSyst():
  ret = SystGroupInfo(Name='NuMIXSecFrontIndPlaneSignalShapeFittedSyst', Latex=r'Front ind. plane signal shape')
  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneSignalShapeFittedSyst', Latex=r'Front ind. plane signal shape', Type='multisigma', RecoOnly=True) )
  return ret
def GetMiddleIndPlaneTransparencySyst():
  ret = SystGroupInfo(Name='NuMIXSecMiddleIndPlaneTransparencySyst', Latex=r'Middle ind. plane transparency')
  ret.SystInfos.append( SystInfo(Name='NuMIXSecMiddleIndPlaneTransparencySyst', Latex=r'Middle ind. plane transparency', Type='multisigma', RecoOnly=True) )
  return ret



def GetDetSystTest():
  ret = SystGroupInfo(Name='DetectorSyst', Latex='Detector')

  ret.SystInfos.append( SystInfo(Name='CalodEdXShiftUp', Latex=r'Calo. $dE/dX$ $+1\sigma$', Type='shift', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='CalodEdXShiftDown', Latex=r'Calo. $dE/dX$ $-1\sigma$', Type='shift', RecoOnly=True) )

  ret.SystInfos.append( SystInfo(Name='CaloGainShiftUp', Latex=r'Calo. gain $+1\sigma$', Type='shift', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='CaloGainShiftDown', Latex=r'Calo. gain $-1\sigma$', Type='shift', RecoOnly=True) )

  ret.SystInfos.append( SystInfo(Name='NuMIXSecCaloGainSyst', Latex=r'Calo. gain $\pm1\sigma$; 3%%', Type='multisigma', RecoOnly=True) )

  ret.SystInfos.append( SystInfo(Name='NuMIXSecLifetimeSyst', Latex='Electron lifetime', Type='multisigma', RecoOnly=True) )

  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneGainSyst', Latex=r'Front ind. plane gain $\pm20$%%', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneNoiseSyst', Latex=r'Front ind. plane noise +10%%', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneSignalShapeSyst', Latex=r'Front ind. plane signal shape', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecMiddleIndPlaneTransparencySyst', Latex=r'Middle ind. plane transparency', Type='multisigma', RecoOnly=True) )

  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneSignalShapeFittedSyst', Latex=r'Front ind. plane signal shape (fit)', Type='multisigma', RecoOnly=True) )

  return ret

def GetMCVariationSystGroupInfo():
  ret = SystGroupInfo(Name='DetectorSyst', Latex='Detector')

  ret.SystInfos.append( SystInfo(Name='CalodEdXShiftUp', Latex=r'Calo. $dE/dX$ $+1\sigma$', Type='shift', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='CalodEdXShiftDown', Latex=r'Calo. $dE/dX$ $-1\sigma$', Type='shift', RecoOnly=True) )

  ret.SystInfos.append( SystInfo(Name='CaloGainShiftUp', Latex=r'Calo. gain $+1\sigma$', Type='shift', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='CaloGainShiftDown', Latex=r'Calo. gain $-1\sigma$', Type='shift', RecoOnly=True) )

  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneGainSyst', Latex=r'Front ind. plane gain $\pm20$%', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneNoiseSyst', Latex=r'Front ind. plane noise +10$%', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecMiddleIndPlaneTransparencySyst', Latex=r'Middle ind. plane transparency', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneSignalShapeSyst', Latex=r'Front ind. plane signal shape', Type='multisigma', RecoOnly=True) )

  return ret

def GetMCVariationSystTestFinalGroupInfo():
  ret = SystGroupInfo(Name='DetectorSyst', Latex='Detector')

  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneGainSyst', Latex=r'Front ind. plane gain $\pm20$%', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneNoiseSyst', Latex=r'Front ind. plane noise +10$%', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecFrontIndPlaneSignalShapeFittedSyst', Latex=r'Front ind. plane signal shape', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecMiddleIndPlaneTransparencySyst', Latex=r'Middle ind. plane transparency', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecCaloGainSyst', Latex=r'Calo. gain $+1\sigma$; 3%', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecLifetimeSyst', Latex='Electron lifetime', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecTrackSplitSyst', Latex='Track split', Type='multisigma', RecoOnly=True) )
  ret.SystInfos.append( SystInfo(Name='NuMIXSecProtonEffSyst', Latex='Proton efficiency', Type='multisigma', RecoOnly=True) )

  return ret






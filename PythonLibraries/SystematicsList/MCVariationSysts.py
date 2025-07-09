from SystInfo import SystInfo
from SystGroupInfo import SystGroupInfo

def GetCV():

  ret = SystGroupInfo(Name='CV', Latex=r'CV')
  ret.SystInfos.append( SystInfo(Name='CV', Latex=r'CV', Type='shift') )

  return ret

def GetCVRerun():

  ret = SystGroupInfo(Name='CVRerun', Latex=r'CV reran')
  ret.SystInfos.append( SystInfo(Name='CVRerun', Latex=r'CV reran', Type='shift') )

  return ret

def GetGainVariation():
  ret = SystGroupInfo(Name='Gain', Latex=r'Ind. 1 gain $\pm$15%')
  ret.SystInfos.append( SystInfo(Name='GainHi', Latex=r'Ind. 1 gain +15%', Type='shift') )
  ret.SystInfos.append( SystInfo(Name='GainLo', Latex=r'Ind. 1 gain -15%', Type='shift') )

  return ret

def GetGainVVariation():
  ret = SystGroupInfo(Name='GainV', Latex=r'Ind. 1 gain $\pm$20%')
  ret.SystInfos.append( SystInfo(Name='GainVHi', Latex=r'Ind. 1 gain +20%', Type='shift') )
  ret.SystInfos.append( SystInfo(Name='GainVLo', Latex=r'Ind. 1 gain -20%', Type='shift') )

  return ret

def GetInd1TransparancyVariation():
  ret = SystGroupInfo(Name='Ind1Tranparancy', Latex=r'Ind. 2 tranprancy')
  ret.SystInfos.append( SystInfo(Name='Ind1O', Latex=r'Ind. 2 Opaque', Type='shift') )
  ret.SystInfos.append( SystInfo(Name='Ind1T', Latex=r'Ind. 2 Transparant', Type='shift') )

  return ret

def GetOverallNoiseVariation():
  ret = SystGroupInfo(Name='OverallNoise', Latex=r'Noise')
  ret.SystInfos.append( SystInfo(Name='OverallNoise', Latex=r'Noise +10%', Type='shift') )

  return ret

def GetOldLifetimeVariation():
  ret = SystGroupInfo(Name='LifetimeOld', Latex='Electron lifetime')
  ret.SystInfos.append( SystInfo(Name='LifetimeHi', Latex=r'$\tau$=9.2ms (old)', Type='shift') )
  ret.SystInfos.append( SystInfo(Name='LifetimeLo', Latex=r'$\tau$=3.8ms (old)', Type='shift') )

  return ret

def GetLifetimeVariation():
  ret = SystGroupInfo(Name='Lifetime', Latex='Electron lifetime')
  ret.SystInfos.append( SystInfo(Name='LifetimeHi2', Latex=r'$\tau$=9.2ms', Type='shift') )
  ret.SystInfos.append( SystInfo(Name='LifetimeLo2', Latex=r'$\tau$=3.8ms', Type='shift') )

  return ret

def GetInd1SignalShapeVariation():
  ret = SystGroupInfo(Name='Ind1SignalShape', Latex=r'Ind. 1 signal shape')
  ret.SystInfos.append( SystInfo(Name='Untuned', Latex=r'Ind. 1 signal shape', Type='shift') )

  return ret

def GetLightLevelVariation():
  ret = SystGroupInfo(Name='LightLevel', Latex=r'Light level')
  ret.SystInfos.append( SystInfo(Name='LightLevel', Latex=r'Light tune', Type='shift') )

  return ret

def GetSCEFixVariation():
  ret = SystGroupInfo(Name='SCEFix', Latex=r'SCE fix')
  ret.SystInfos.append( SystInfo(Name='SCEFix', Latex=r'SCE fix', Type='shift') )

  return ret

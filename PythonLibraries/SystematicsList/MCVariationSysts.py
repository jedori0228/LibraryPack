from SystInfo import SystInfo
from SystGroupInfo import SystGroupInfo

def GetGainVariation():
  ret = SystGroupInfo(Name='Gain', Latex=r'Gain $\pm$15%')
  ret.SystInfos.append( SystInfo(Name='GainHi', Latex=r'Gain +15%', Type='shift') )
  ret.SystInfos.append( SystInfo(Name='GainLo', Latex=r'Gain -15%', Type='shift') )

  return ret

def GetGainVVariation():
  ret = SystGroupInfo(Name='GainV', Latex=r'Gain $\pm$20%')
  ret.SystInfos.append( SystInfo(Name='GainVHi', Latex=r'Gain +20%', Type='shift') )
  ret.SystInfos.append( SystInfo(Name='GainVLo', Latex=r'Gain -20%', Type='shift') )

  return ret

def GetInd1TransparancyVariation():
  ret = SystGroupInfo(Name='Ind1Tranparancy', Latex=r'Ind. 1 tranprancy')
  ret.SystInfos.append( SystInfo(Name='Ind1O', Latex=r'Ind. 1 Opaque', Type='shift') )
  ret.SystInfos.append( SystInfo(Name='Ind1T', Latex=r'Ind. 1 Transparant', Type='shift') )

  return ret

def GetOverallNoiseVariation():
  ret = SystGroupInfo(Name='OverallNoise', Latex=r'Noise')
  ret.SystInfos.append( SystInfo(Name='OverallNoise', Latex=r'Noise +10%', Type='shift') )

  return ret
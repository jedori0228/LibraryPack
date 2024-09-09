from SystInfo import SystInfo
from SystGroupInfo import SystGroupInfo

def GetMCStatSystGroupInfo():

    ret = SystGroupInfo(Name='MCStat', Latex='Stat. (MC)')

    ret.SystInfos.append( SystInfo(Name='MCStat', Latex='Stat. (MC)', Type='MCStat') )

    return ret

def GetOffbeamStatSystGroupInfo():

    ret = SystGroupInfo(Name='OffbeamStat', Latex='Stat. (Offbeam)')

    ret.SystInfos.append( SystInfo(Name='OffbeamStat', Latex='Stat. (Offbeam)', Type='OffbeamStat') )

    return ret

def GetAllStatSystGroupInfo():

    ret = SystGroupInfo(Name='Stat', Latex='Stat.')

    ret.SystInfos.append( SystInfo(Name='MCStat', Latex='Stat. (MC)', Type='MCStat') )
    ret.SystInfos.append( SystInfo(Name='OffbeamStat', Latex='Stat. (Offbeam)', Type='OffbeamStat') )

    return ret

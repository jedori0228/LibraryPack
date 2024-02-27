def GetICARUSNuMIPOT(run, beam, prodname):

  ## beam: 0 (Off), 1 (On)
  if beam!=0 and beam!=1:
    raise ValueError("[GetICARUSNuMIPOT] beam must be 0 (Off) or 1 (On), but ", beam,"  is given")

  if beam==0:
    return 0.

  if run=="Run1":

    if prodname=="Reprod":
      return 51770019.83189027E12

    elif prodname=="ReprodD":
      return 52428876.437749E12

    elif prodname=="DP2023G_reprodD":
      return 52428876.437749E12
    elif prodname=="DP2023G_reprodD_Random15Percent":
      return 7307090.76762222E12

    elif prodname=="DMCP2023F_F":
      #return 50555533.354061E12
      return 5.165487279415409e+19 ## BRUCE
    elif prodname=="DMCP2023F_F_Random15Percent":
      #return 6824749.08755274E12
      return 6.983230011348827e+18 ## BRUCE

    else:
      raise ValueError("[GetICARUSNuMIPOT] Wrong prodname %s for run %s"%(prodname, run))

  elif run=="Run2":

    if prodname=="ReprodD":
      return 243522448.605790E12

    elif prodname=="DP2023G_reprodD":
      return 203542547.998370E12
    elif prodname=="DP2023G_reprodD_Random15Percent":
      return 26665149.8459446E12

    elif prodname=="DMCP2023F_F":
      return 203869890.211324E12
    elif prodname=="DMCP2023F_F_Random15Percent":
      #return 29182931.4684785E12 ### ARG commented out at 2024 Feb. 12th, we were using this number for technote plot
      return 2.9300301931345543e+19 ## BRUCE

    else:
      raise ValueError("[GetICARUSNuMIPOT] Wrong prodname %s for run %s"%(prodname, run))

  elif run=="Run12":

    return 5.165487279415409e+19+203869890.211324E12


def GetICARUSNuMILivetime(run, beam, prodname):

  ## beam: 0 (Off), 1 (On)
  if beam!=0 and beam!=1:
    raise ValueError("[GetICARUSNuMILivetime] beam must be 0 (Off) or 1 (On), but ", beam,"  is given")

  if run=="Run1":

    if prodname=="Reprod":
      if beam==0:
        return 5757556.51
      else:
        return 9776414.853179745

    elif prodname=="ReprodD":
      if beam==0:
        return 5118894.120000
      else:
        return 10101806.048333

    elif prodname=="DP2023G_reprodD":
      if beam==0:
        return 5118894.120000
      else:
        return 10101806.048333
    elif prodname=="DP2023G_reprodD_Random15Percent":
      if beam==0:
        raise ValueError("[GetICARUSNuMILivetime] Random15Percent on OffBeam is wrong")
      else:
        return 1425382.86833333

    elif prodname=="DMCP2023F_F":
      if beam==0:
        return 8492620.855000
      else:
        #return 9811811.313333
        return 10755359.373333331 ## BRUCE
    elif prodname=="DMCP2023F_F_Random15Percent":
      if beam==0:
        raise ValueError("[GetICARUSNuMILivetime] Random15Percent on OffBeam is wrong")
      else:
        #return 1317743.465
        return 1453270.9883333335 ## BRUCE

    else:
      raise ValueError("[GetICARUSNuMILivetime] Wrong prodname %s for run %s"%(prodname, run))

  elif run=="Run2":
    if prodname=="ReprodD":
      if beam==0:
        return 53316949.085000
      else:
        return 48361486.095000

    elif prodname=="DP2023G_reprodD":
      if beam==0:
        return 44310160.965000
      else:
        return 40752975.305000
    elif prodname=="DP2023G_reprodD_Random15Percent":
      if beam==0:
        raise ValueError("[GetICARUSNuMILivetime] Random15Percent on OffBeam is wrong")
      else:
        return 5395844.705


    elif prodname=="DMCP2023F_F":
      if beam==0:
        return 44302293.065000
      else:
        return 41194567.000000
    elif prodname=="DMCP2023F_F_Random15Percent":
      if beam==0:
        raise ValueError("[GetICARUSNuMILivetime] Random15Percent on OffBeam is wrong")
      else:
        #return 5883757.69333333
        return 6.145486905e+6 ## BRUCE


    else:
      raise ValueError("[GetICARUSNuMILivetime] Wrong prodname %s for run %s"%(prodname, run))

  elif run=="Run12":

    if beam==0:
      return 8492620.855000+44302293.065000
    else:
      return 10755359.373333331+41194567.000000

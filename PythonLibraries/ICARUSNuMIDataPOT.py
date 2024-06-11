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
      #return 5.165487279415409e+19 ## BRUCE
      return 4.651603646822754e+19 ## JAESUNG
    elif prodname=="DMCP2023F_F_Random15Percent":
      #return 6824749.08755274E12
      #return 6.983230011348827e+18 ## BRUCE
      return 6.983230011348827e+18 ## JAESUNG

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
      #return 203869890.211324E12 ## BRUCE
      return 1.9571570832099764e+20 ## JAESUNG
    elif prodname=="DMCP2023F_F_Random15Percent":
      #return 29182931.4684785E12 ### ARG commented out at 2024 Feb. 12th, we were using this number for technote plot
      #return 2.9300301931345543e+19 ## BRUCE
      return 2.9300301931345543e+19 ## JAESUNG

    else:
      raise ValueError("[GetICARUSNuMIPOT] Wrong prodname %s for run %s"%(prodname, run))

  else:
    raise ValueError("[GetICARUSNuMIPOT] Wrong run %s"%(run))


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
        #return 8492620.855000
        #return 8347083.895 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240430_InitialBadSpillOnlyRun2 bad spill set
        return 8347083.895000001 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240506_UpdatedBadSpills bad spill set (comment: same as above)
      else:
        #return 9811811.313333
        #return 10755359.373333331 ## BRUCE
        #return 9712335.74 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240430_InitialBadSpillOnlyRun2 bad spill set
        return 9712335.74 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240506_UpdatedBadSpills bad spill set (comment: same as above)
    elif prodname=="DMCP2023F_F_Random15Percent":
      if beam==0:
        raise ValueError("[GetICARUSNuMILivetime] Random15Percent on OffBeam is wrong")
      else:
        #return 1317743.465
        #return 1453270.9883333335 ## BRUCE
        #return 1453270.9883333333 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240430_InitialBadSpillOnlyRun2 bad spill set
        return 1453270.9883333333 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240506_UpdatedBadSpills bad spill set (comment: same as above)

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
        #return 44302293.065000
        #return 42294414.57999999 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240430_InitialBadSpillOnlyRun2 bad spill set
        return 42231883.965 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240506_UpdatedBadSpills bad spill set
      else:
        #return 41194567.000000
        #return 41328565.04666669 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240430_InitialBadSpillOnlyRun2 bad spill set
        return 41209782.31333332 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240506_UpdatedBadSpills bad spill set
    elif prodname=="DMCP2023F_F_Random15Percent":
      if beam==0:
        raise ValueError("[GetICARUSNuMILivetime] Random15Percent on OffBeam is wrong")
      else:
        #return 5883757.69333333
        #return 6.145486905e+6 ## BRUCE
        #return 6145486.905 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240430_InitialBadSpillOnlyRun2 bad spill set
        return 6141553.965 ## JAESUNG with 1) 05/07/2024 GRL + 2) 240506_UpdatedBadSpills bad spill set


    else:
      raise ValueError("[GetICARUSNuMILivetime] Wrong prodname %s for run %s"%(prodname, run))

  elif run=="Run12":

    if beam==0:
      return 8492620.855000+44302293.065000
    else:
      return 10755359.373333331+41194567.000000

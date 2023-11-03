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
    else:
      raise ValueError("[GetICARUSNuMIPOT] Wrong prodname %s for run %s"%(prodname, run))

  elif run=="Run2":
    if prodname=="ReprodD":
      return 243522448.605790E12
    else:
      raise ValueError("[GetICARUSNuMIPOT] Wrong prodname %s for run %s"%(prodname, run))


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
    else:
      raise ValueError("[GetICARUSNuMILivetime] Wrong prodname %s for run %s"%(prodname, run))

  elif run=="Run2":
    if prodname=="ReprodD":
      if beam==0:
        return 53316949.085000
      else:
        return 48361486.095000
    else:
      raise ValueError("[GetICARUSNuMILivetime] Wrong prodname %s for run %s"%(prodname, run))

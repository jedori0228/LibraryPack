import ROOT as rt

def setSBNStyle():

  sbnStyle =  rt.TStyle("sbnStyle","Style for SBN")
  sbnStyle.SetOptStat(0)
  sbnStyle.cd()


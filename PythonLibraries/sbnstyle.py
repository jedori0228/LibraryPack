import ROOT as rt

def setSBNStyle():

  sbnStyle =  rt.TStyle("sbnStyle","Style for SBN")

  sbnStyle.SetCanvasBorderMode(0)
  sbnStyle.SetCanvasColor(rt.kWhite)

  sbnStyle.SetOptStat(0)

  sbnStyle.cd()


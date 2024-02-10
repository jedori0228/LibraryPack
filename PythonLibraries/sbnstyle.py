import ROOT

def setSBNStyle():

  sbnStyle =  ROOT.TStyle("sbnStyle","Style for SBN")

  sbnStyle.SetCanvasBorderMode(0)
  sbnStyle.SetCanvasColor(ROOT.kWhite)

  sbnStyle.SetOptStat(0)

  sbnStyle.cd()

def Draw_ICARUS_Preliminary():

  latex_ICARUS = ROOT.TLatex()
  latex_ICARUS.SetNDC()
  latex_ICARUS.SetTextSize(0.035)

  latex_ICARUS.DrawLatex(0.18, 0.96, "ICARUS #it{#scale[0.8]{Preliminary}}")


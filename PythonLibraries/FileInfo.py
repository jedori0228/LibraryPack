import ROOT

class FileInfo:

  def __init__(self, filepath):
    print("[Utils.FileInfo] Init for filepath = %s"%(filepath))
    self.Filepath = filepath
    self.File = ROOT.TFile(filepath)
    self.POT = self.File.Get("BeamInfo/POT_BeamInfo").GetBinContent(1)
    self.Livetime = self.File.Get("BeamInfo/Livetime_BeamInfo").GetBinContent(1)
    print("[Utils.FileInfo] - POT = %1.2e"%(self.POT))
    print("[Utils.FileInfo] - Livetime = %1.2e"%(self.Livetime))

import ROOT

class TreeInfo:

  def __init__(self, filepath, treename):
    print("[Utils.TreeInfo] Init for filepath = %s"%(filepath))
    self.Filepath = filepath
    self.File = ROOT.TFile(filepath)
    self.Tree = self.File.Get(treename)

    last_separator_index = treename.rfind("/")
    directory_path = treename[:last_separator_index]
    self.POT = self.File.Get("%s/POT"%(directory_path)).GetBinContent(1)
    self.Livetime = self.File.Get("%s/Livetime"%(directory_path)).GetBinContent(1)

    print("[Utils.TreeInfo] - Tree name = %s"%(treename)) 
    print("[Utils.TreeInfo] - POT = %1.2e"%(self.POT))
    print("[Utils.TreeInfo] - Livetime = %1.2e"%(self.Livetime))

    self.Canvas = ROOT.TCanvas("%s/%s"%(filepath, treename, ), "", 1, 1)

  def Draw(self, VarExpr, CutExpr, hist):

    current_canvas = ROOT.gPad.GetCanvas()

    self.Canvas.cd()
    self.Tree.Draw("%s>>%s" % (VarExpr, hist.GetName()), CutExpr)
    current_canvas.cd()

  def AddFriend(self, new_treename):

    print("[Utils.TreeInfo] - Friend tree added: %s"%(new_treename))

    new_tree = self.File.Get(new_treename)
    self.Tree.AddFriend(new_tree)


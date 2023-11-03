import ROOT
from array import array
from mylib import GetProperDecimalString

class VariableInfo:

  def __init__(self, Name, Expr="", Latex="", xMin=0., xMax=100., dx=1, CustomBinning=[], Unit="", IsSpillVar=False):

    self.Name = Name
    self.Expr = Expr
    self.Latex = Latex
    self.Unit = Unit
    self.xMin = xMin
    self.xMax = xMax
    self.dx = dx
    self.nx = round( (xMax-xMin)/dx )
    self.CustomBinning = CustomBinning
    self.IsSpillVar = IsSpillVar

    if self.IsSpillVar:
      self.EventUnit = "Spills"
    else:
      self.EventUnit = "Slices"

    if len(CustomBinning)>0:
      self.xMin = self.CustomBinning[0]
      self.xMax = self.CustomBinning[-1]

  def GetNRebin(self, current_dx):
    current_dx = round(current_dx, 5)
    if current_dx<self.dx:
      #print("self.dx = ", self.dx, "current_dx = ", current_dx, " -> nrebin = ", self.dx/current_dx, int(self.dx/current_dx))
      return round(self.dx/current_dx)
    else:
      return 1

  def GetYaxisTitle(self):

    if len(self.CustomBinning)==0:
      binSizeString = GetProperDecimalString(self.dx)
      if self.Unit=="":
        return "%s/%s"%(self.EventUnit, binSizeString)
      else:
        return "%s/%s%s"%(self.EventUnit, binSizeString,self.Unit)
    else:
      return "%s per bin"%(self.EventUnit)

  def GetEmptyHist(self, name):
    if len(self.CustomBinning)==0:
      return ROOT.TH1D(name, "", self.nx, self.xMin, self.xMax)
    else:
      return ROOT.TH1D(name, "", len(self.CustomBinning)-1, array('d', self.CustomBinning))

  def GetBinArray(self):

    if len(self.CustomBinning)>0:
      return self.CustomBinning
    else:
      out = []
      for i in range(0, self.nx):
        out.append( self.xMin + self.dx*i )
      out.append(self.xMax)
      return out


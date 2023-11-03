import ROOT

class FVTool:

  def __init__(self):

    self.XAVCroy0Lower = -358.489
    self.XAVCroy0Upper = -61.94
    self.XAVCroy1Lower = +61.94
    self.XAVCroy1Upper = +358.489
    self.YAVLower = -181.86
    self.YAVUpper = +134.96
    self.ZAVLower = -894.95
    self.ZAVUpper = +894.85

    self.XMargin=25.
    self.YMargin=25.
    self.ZMarginUp=30.
    self.ZMarginDown=50.

  def GetBoundary(self, coord, cryo, side):

    if coord=="x":
      if cryo==0:
        if side=="l":
          return self.XAVCroy0Lower
        else:
          return self.XAVCroy0Upper
      else:
        if side=="l":
          return self.XAVCroy1Lower
        else:
          return self.XAVCroy1Upper
    elif coord=="y":
      if side=="l":
        return self.YAVLower
      else:
        return self.YAVUpper
    else:
      if side=="l":
        return self.ZAVLower
      else:
        return self.ZAVUpper

  def GetMargin(self, coord, side):

    if coord=="x":
      return self.XMargin
    elif coord=="y":
      return self.YMargin
    elif coord=="z":
      if side=="l":
        return self.ZMarginDown
      else:
        return self.ZMarginUp

  def GetVerticalLine(self, coord, cryo, side, cut=False):

    this_pos = self.GetBoundary(coord, cryo, side)
    if cut:
      if side=="l":
        this_pos += self.GetMargin(coord, side)
      else:
        this_pos -= self.GetMargin(coord, side)

    tmp_xs = [this_pos, this_pos]
    tmp_ys = [1,1E10]

    return ROOT.TGraph(2, array("d", tmp_xs ), array("d", tmp_ys ))

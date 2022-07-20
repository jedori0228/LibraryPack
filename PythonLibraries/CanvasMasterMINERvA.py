import ROOT
import mylib
import array

class CanvasMasterMINERvA:

  def __init__(self, Name, nXPad, nYPad, nPadFilled):

    self.padIndexShift=1000
    self.padIndices = []

    self.Name = Name
    self.nXPad = nXPad
    self.nYPad = nYPad
    self.nPadFilled = nPadFilled

    ## X
    self.X_TITLE_GAP = 2.0
    self.X_LABEL_GAP = 2.0
    self.X_PLOT = 10.
    self.X_PAD_GAP = 2.0
    self.X_RIGHT_MARGIN = 0.6

    ## Y
    self.Y_TITLE_GAP = 2.0
    self.Y_LABEL_GAP = 2.0
    self.Y_PLOT = 7.
    self.Y_PAD_GAP = 2.0
    self.Y_TOP_MARGIN = 1.5

    self.Update()

  def Update(self):

    self.BASE_X_TOTAL = self.X_TITLE_GAP + self.X_LABEL_GAP + self.nXPad * self.X_PLOT + self.X_RIGHT_MARGIN
    self.BASE_Y_TOTAL = self.Y_TITLE_GAP + self.Y_LABEL_GAP + self.nYPad * self.Y_PLOT + self.Y_TOP_MARGIN

  def GetCanvas(self):

    c_Base = ROOT.TCanvas("c_Base_%s"%(self.Name), "", int(self.BASE_X_TOTAL)*100, int(self.BASE_Y_TOTAL)*100)
    c_Base = mylib.RemovePadMargin(c_Base)

    map_index_to_pad = dict()
    self.padIndices = []

    padCounter = 0
    for iy in range(0, self.nYPad):
      for ix in range(0, self.nXPad):

        if padCounter==self.nPadFilled:
          break
        padCounter += 1

        padIndex = ix*self.padIndexShift+iy
        padIndexString = "[%d,%d]"%(ix,iy)
        self.padIndices.append(padIndex)

        this_PAD_X_TOTAL = self.X_PAD_GAP + self.X_PLOT
        this_PAD_X_LEFT_MARGIN = self.X_PAD_GAP
        this_PAD_X_RIGHT_MARGIN = 0.

        this_PAD_Y_TOTAL = self.Y_PAD_GAP + self.Y_PLOT
        this_PAD_Y_TOP_MARGIN = 0.
        this_PAD_Y_BOTTOM_MARGIN = self.Y_PAD_GAP

        this_PAD_X_START_POS = self.X_TITLE_GAP + self.X_LABEL_GAP + ix * (self.X_PLOT) - self.X_PAD_GAP
        this_PAD_Y_START_POS = self.BASE_Y_TOTAL - self.Y_TOP_MARGIN - (iy+1) * (self.Y_PLOT) - self.Y_PAD_GAP 

        this_PAD_X_END_POS = self.X_TITLE_GAP + self.X_LABEL_GAP + (ix+1) * (self.X_PLOT)
        this_PAD_Y_END_POS = self.BASE_Y_TOTAL - self.Y_TOP_MARGIN - iy * (self.Y_PLOT)

        if ix==0:
          this_PAD_X_TOTAL = self.X_LABEL_GAP + self.X_PLOT
          this_PAD_X_LEFT_MARGIN = self.X_LABEL_GAP
          this_PAD_X_START_POS = self.X_TITLE_GAP
        if ix==self.nXPad-1:
          this_PAD_X_TOTAL = self.X_PAD_GAP + self.X_PLOT + self.X_RIGHT_MARGIN
          this_PAD_X_RIGHT_MARGIN = self.X_RIGHT_MARGIN
          this_PAD_X_END_POS = self.BASE_X_TOTAL
        if iy==0:
          this_PAD_Y_TOTAL = self.Y_PAD_GAP + self.Y_PLOT + self.Y_TOP_MARGIN
          this_PAD_Y_TOP_MARGIN = self.Y_TOP_MARGIN
          this_PAD_Y_START_POS = self.BASE_Y_TOTAL - (self.Y_PAD_GAP + self.Y_PLOT + self.Y_TOP_MARGIN)
          this_PAD_Y_END_POS = self.BASE_Y_TOTAL
        if iy==self.nYPad-1:
          this_PAD_Y_TOTAL = self.Y_LABEL_GAP + self.Y_PLOT
          this_PAD_Y_BOTTOM_MARGIN = self.Y_LABEL_GAP
          this_PAD_Y_START_POS = self.Y_TITLE_GAP
          this_PAD_Y_END_POS = self.Y_TITLE_GAP + self.Y_LABEL_GAP + self.Y_PLOT

        map_index_to_pad[padIndex] = ROOT.TPad("map_index_to_pad_%s"%(padIndexString), "",
                                     this_PAD_X_START_POS/self.BASE_X_TOTAL,
                                     this_PAD_Y_START_POS/self.BASE_Y_TOTAL,
                                     this_PAD_X_END_POS/self.BASE_X_TOTAL,
                                     this_PAD_Y_END_POS/self.BASE_Y_TOTAL)
        map_index_to_pad[padIndex] = mylib.RemovePadMargin(map_index_to_pad[padIndex])
        map_index_to_pad[padIndex].SetLeftMargin(this_PAD_X_LEFT_MARGIN/this_PAD_X_TOTAL)
        map_index_to_pad[padIndex].SetRightMargin(this_PAD_X_RIGHT_MARGIN/this_PAD_X_TOTAL)
        map_index_to_pad[padIndex].SetTopMargin(this_PAD_Y_TOP_MARGIN/this_PAD_Y_TOTAL)
        map_index_to_pad[padIndex].SetBottomMargin(this_PAD_Y_BOTTOM_MARGIN/this_PAD_Y_TOTAL)
        map_index_to_pad[padIndex].SetFillColor(0)
        map_index_to_pad[padIndex].SetFillStyle(0)

    c_Base.SetLeftMargin( self.X_TITLE_GAP/self.BASE_X_TOTAL )
    c_Base.SetBottomMargin( self.Y_TITLE_GAP/self.BASE_Y_TOTAL )

    return c_Base, map_index_to_pad

  def GetAxisHists(self, xBins):

    hists_axis = dict()

    padCounter = 0
    ix_Final = self.nPadFilled%self.nXPad
    for iy in range(0, self.nYPad):
      for ix in range(0, self.nXPad):

        if padCounter==self.nPadFilled:
          break
        padCounter += 1

        padIndex = ix*self.padIndexShift+iy
        padIndexString = "[%d,%d]"%(ix,iy)

        hists_axis[padIndex] = ROOT.TH1D('hist_axis_%s'%(padIndexString), '', len(xBins)-1, array.array("d", xBins))
        hists_axis[padIndex].GetXaxis().SetLabelFont(43)
        hists_axis[padIndex].GetXaxis().SetLabelSize(100)
        hists_axis[padIndex].GetXaxis().SetTitleFont(43)
        hists_axis[padIndex].GetXaxis().SetTitleSize(0)

        hists_axis[padIndex].GetYaxis().SetLabelFont(43)
        hists_axis[padIndex].GetYaxis().SetLabelSize(100)
        hists_axis[padIndex].GetYaxis().SetTitleFont(43)
        hists_axis[padIndex].GetYaxis().SetTitleSize(0)

        if ix!=0:
          hists_axis[padIndex].GetYaxis().SetLabelSize(0)

        if iy!=self.nYPad-1 and ( not (iy==self.nYPad-2 and ix>=ix_Final) ):
          hists_axis[padIndex].GetXaxis().SetLabelSize(0)

    return hists_axis

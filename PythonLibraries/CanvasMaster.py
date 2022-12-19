import ROOT
import array
import mylib

class CanvasMaster:

  def __init__(self, Name, Mode):

    self.Name = Name
    self.__Mode = Mode

    ## For single plot
    if self.__Mode==1:

      ## plot
      self.X_PLOT = 12.1
      self.Y_PLOT = 12.5

      ## Gaps
      self.X_TITLE_GAP = 1.5
      self.X_LABEL_GAP = 1.
      self.Y_TITLE_GAP = 1.
      self.Y_LABEL_GAP = 1.

      self.Y_TOP_MARGIN = 0.7
      self.X_RIGHT_MARGIN = 0.6

    ## For rate (up) + ratio (down) plots
    if self.__Mode==2:

      ## Y of Up and Down plots : reference
      self.Up_Y_PLOT = 10
      self.Down_Y_PLOT = 2.

      ## shared
      self.X_PLOT = 12.1
      self.X_TITLE_GAP = 1.5
      self.X_LABEL_GAP = 1.

      ## Base canvas
      self.Y_TOP_MARGIN = 0.7
      self.X_RIGHT_MARGIN = 0.6

      ## Gap between Up and Down pad
      self.PAD_GAP = 0.5

      ## Only for Down pad (y label and title)
      self.Y_TITLE_GAP = 1.
      self.Y_LABEL_GAP = 1.

      self.Update()

  def Update(self):

    if self.__Mode==2:

      ## Now for Up pad
      self.Up_X_PAD = self.X_TITLE_GAP + self.X_LABEL_GAP + self.X_PLOT + self.X_RIGHT_MARGIN
      self.Up_Y_PAD = self.Up_Y_PLOT + self.PAD_GAP +self.Y_TOP_MARGIN

      ## Now for down pad
      self.Down_X_PAD = self.X_TITLE_GAP + self.X_LABEL_GAP + self.X_PLOT + self.X_RIGHT_MARGIN
      self.Down_Y_PAD = self.Y_TITLE_GAP + self.Y_LABEL_GAP + self.Down_Y_PLOT + self.PAD_GAP

  def GetCanvas(self):

    if self.__Mode==1:

      BASE_X_TOTAL = self.X_TITLE_GAP + self.X_LABEL_GAP + self.X_PLOT + self.X_RIGHT_MARGIN
      BASE_Y_TOTAL = self.Y_TITLE_GAP + self.Y_LABEL_GAP + self.Y_PLOT + self.Y_TOP_MARGIN

      c_Base = ROOT.TCanvas(self.Name, "", int(BASE_X_TOTAL*100), int(BASE_Y_TOTAL*100))
      c_Base = mylib.RemovePadMargin(c_Base)
      c_Base.SetTopMargin( (self.Y_TOP_MARGIN)/BASE_Y_TOTAL )
      c_Base.SetBottomMargin( (self.Y_TITLE_GAP + self.Y_LABEL_GAP)/BASE_Y_TOTAL )
      c_Base.SetLeftMargin( (self.X_TITLE_GAP + self.X_LABEL_GAP)/BASE_X_TOTAL )
      c_Base.SetRightMargin( (self.X_RIGHT_MARGIN)/BASE_X_TOTAL )

      return c_Base

    elif self.__Mode==2:

      BASE_X_TOTAL = self.Up_X_PAD
      BASE_Y_TOTAL = self.Down_Y_PAD + self.Up_Y_PLOT + self.Y_TOP_MARGIN

      c_Base = ROOT.TCanvas("c_Base_%s"%(self.Name), "", int(BASE_X_TOTAL*100), int(BASE_Y_TOTAL*100))
      c_Base = mylib.RemovePadMargin(c_Base)

      p_Up = ROOT.TPad("p_Up_%s"%(self.Name), "",
             0.,
             (self.Y_TITLE_GAP + self.Y_LABEL_GAP + self.Down_Y_PLOT)/BASE_Y_TOTAL,
             (self.Up_X_PAD)/BASE_X_TOTAL,
             1.
             )
      p_Up = mylib.RemovePadMargin(p_Up)
      p_Up.SetTopMargin( (self.Y_TOP_MARGIN)/self.Up_Y_PAD )
      p_Up.SetBottomMargin( (self.PAD_GAP)/self.Up_Y_PAD )
      p_Up.SetLeftMargin( (self.X_TITLE_GAP + self.X_LABEL_GAP)/self.Up_X_PAD )
      p_Up.SetRightMargin( (self.X_RIGHT_MARGIN)/self.Up_X_PAD )
      p_Up.SetFillColor(0)
      p_Up.SetFillStyle(0)

      p_Down = ROOT.TPad("p_Down_%s"%(self.Name), "",     
               0.,
               0.,
               (self.Up_X_PAD)/BASE_X_TOTAL,
               (self.Down_Y_PAD)/BASE_Y_TOTAL
               )
      p_Down = mylib.RemovePadMargin(p_Down)
      p_Down.SetTopMargin( (self.PAD_GAP)/self.Down_Y_PAD )
      p_Down.SetBottomMargin( (self.Y_TITLE_GAP + self.Y_LABEL_GAP)/self.Down_Y_PAD )
      p_Down.SetLeftMargin( (self.X_TITLE_GAP + self.X_LABEL_GAP)/(self.Up_X_PAD) )
      p_Down.SetRightMargin( (self.X_RIGHT_MARGIN)/self.Up_X_PAD )
      p_Down.SetFillColor(0)
      p_Down.SetFillStyle(0)

      return c_Base, p_Up, p_Down

  def GetAxisHistCustomBinnings(self, xBins, yBins=[]):

    if self.__Mode==1:

      hist_axis = ROOT.TH1D('hist_axis_up', '', len(xBins)-1, array.array("d", xBins))
      hist_axis.GetXaxis().SetLabelFont(43)
      hist_axis.GetXaxis().SetLabelSize(50)
      hist_axis.GetXaxis().SetTitleFont(43)
      hist_axis.GetXaxis().SetTitleSize(90)
      hist_axis.GetXaxis().SetTitleOffset(0.9)

      hist_axis.GetYaxis().SetLabelFont(43)
      hist_axis.GetYaxis().SetLabelSize(50)
      hist_axis.GetYaxis().SetTitleFont(43)
      hist_axis.GetYaxis().SetTitleSize(100)
      hist_axis.GetYaxis().SetTitleOffset(1.2)

      return hist_axis

    elif self.__Mode==2:

      hist_axis_up = ROOT.TH1D('hist_axis_up', '', len(xBins)-1, array.array("d", xBins))
      hist_axis_down = ROOT.TH1D('hist_axis_down', '', len(xBins)-1, array.array("d", xBins))

      hist_axis_up.SetTitle("")

      ## Up plot

      hist_axis_up.GetXaxis().SetLabelSize(0)

      hist_axis_up.GetYaxis().SetLabelFont(43)
      hist_axis_up.GetYaxis().SetLabelSize(50) # 10
      hist_axis_up.GetYaxis().SetTitleFont(43)
      hist_axis_up.GetYaxis().SetTitleSize(100)
      hist_axis_up.GetYaxis().SetTitleOffset(1.2)
      hist_axis_up.GetYaxis().SetMaxDigits(4)

      ##  Down plot
      hist_axis_down.SetTitle("")

      hist_axis_down.GetXaxis().SetLabelFont(43)
      hist_axis_down.GetXaxis().SetLabelSize(50)
      hist_axis_down.GetXaxis().SetTitleFont(43)
      hist_axis_down.GetXaxis().SetTitleSize(80)
      hist_axis_down.GetXaxis().SetTitleOffset(3.5)


      hist_axis_down.GetYaxis().SetLabelFont(43)
      hist_axis_down.GetYaxis().SetLabelSize(50)
      hist_axis_down.GetYaxis().SetTitleFont(43)
      hist_axis_down.GetYaxis().SetTitleSize(60)
      hist_axis_down.GetYaxis().SetTitleOffset(2.0)


      return hist_axis_up, hist_axis_down

  def GetAxisHist(self, xMin, xMax, dx):

    this_bins = []
    for ix in range(0, int( (xMax-xMin)/dx )):
      this_bins.append( xMin + ix * dx )
    this_bins.append(xMax)

    return self.GetAxisHistCustomBinnings(this_bins)

import os,ROOT,numpy
import math
from array import array

def predefColorCodes():

  colors = [
ROOT.kRed,
ROOT.kMagenta,
ROOT.kOrange,
ROOT.kGreen+2,
ROOT.kCyan,
ROOT.kBlue,
ROOT.kViolet,
ROOT.kGray,
ROOT.kBlack+2,
ROOT.kYellow+2,
]

  return colors

def isclose(a, b, rel_tol=0.001, abs_tol=0.001):
  return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def Rebin1D(hist, nrebin, vec_Xbins):

  hist_out = hist.Clone()
  if nrebin>0:
    hist_out.Rebin(nrebin)
  else:
    hist_out = hist.Rebin(len(vec_Xbins)-1, hist.GetName(), array("d", vec_Xbins) )
  return hist_out


def VariableRebin2D(hist, vec_Xbins, vec_Ybins):

  nXBin = len(vec_Xbins)-1
  nYBin = len(vec_Ybins)-1

  th2_out = ROOT.TH2D(hist.GetName(), '', nXBin, array('d',vec_Xbins), nYBin, array('d',vec_Ybins))

  for iNewBinX in range(1,nXBin+1):

    x_l_New = th2_out.GetXaxis().GetBinLowEdge(iNewBinX)
    x_r_New = th2_out.GetXaxis().GetBinUpEdge(iNewBinX)

    for iNewBinY in range(1,nYBin+1):

      y_l_New = th2_out.GetYaxis().GetBinLowEdge(iNewBinY)
      y_r_New = th2_out.GetYaxis().GetBinUpEdge(iNewBinY)

      thid_new_content = 0

      #print('@@ Filling new bin, x : [%1.2f, %1.2f], y : [%1.2f, %1.2f]'%(x_l_New,x_r_New,y_l_New,y_r_New))

      ## now loop over original histo
      for iOldBinX in range(1,hist.GetXaxis().GetNbins()+1):

        x_l_Old = hist.GetXaxis().GetBinLowEdge(iOldBinX)
        x_r_Old = hist.GetXaxis().GetBinUpEdge(iOldBinX)

        #if x_r_New<x_r_Old:
        #  break

        passX = (x_l_New<x_l_Old or isclose(x_l_New,x_l_Old)) and (x_r_Old<x_r_New or isclose(x_r_Old,x_r_New))

        for iOldBinY in range(1,hist.GetYaxis().GetNbins()+1):

          y_l_Old = hist.GetYaxis().GetBinLowEdge(iOldBinY)
          y_r_Old = hist.GetYaxis().GetBinUpEdge(iOldBinY)

          #if y_r_New<y_r_Old:
          #  break

          passY = (y_l_New<y_l_Old or isclose(y_l_New,y_l_Old)) and (y_r_Old<y_r_New or isclose(y_r_Old,y_r_New))

          #print('@@   Checking old bin, x : [%1.2f, %1.2f], y : [%1.2f, %1.2f]'%(x_l_Old,x_r_Old,y_l_Old,y_r_Old))
          #print('@@     passX',passX,'passY',passY)
          #print('@@     x_l_New<=x_l_Old',x_l_New<=x_l_Old,'x_r_Old<=x_r_New',x_r_Old<=x_r_New,'y_l_New<=y_l_Old',y_l_New<=y_l_Old,'y_r_Old<=y_r_New',y_r_Old<=y_r_New)
          #print('@@     y_r_Old',y_r_Old,'y_r_New',y_r_New)

          if passX and passY:

            #print('@@   --> Merged! Old [%1.4f, %1.4f] -> New [%1.4f, %1.4f]'%(x_l_Old,x_r_Old,x_l_New,x_r_New))

            thid_new_content += hist.GetBinContent(iOldBinX,iOldBinY)

      if thid_new_content==0:
        thid_new_content = 1E-5
      th2_out.SetBinContent(iNewBinX, iNewBinY, thid_new_content)

  return th2_out

def BinWidthNormalizedHistogram(hist, c=1):
  hist_out = hist.Clone()
  for ix in range(0, hist.GetXaxis().GetNbins()):
    iBin = ix+1
    x_l = hist.GetXaxis().GetBinLowEdge(iBin)
    x_r = hist.GetXaxis().GetBinUpEdge(iBin)
    dx = x_r-x_l
    y = hist.GetBinContent(iBin)
    y_err = hist.GetBinError(iBin)
    hist_out.SetBinContent(iBin, y * c/(dx))
    hist_out.SetBinError(iBin, y_err * c/(dx))
  return hist_out

## quantile

def FindQuantile(frac, xs):

  xs.sort()
  N = len(xs)
  h = frac*(N+1)
  h0 = int(math.floor(h))
  h1 = int(math.ceil(h))
  if h0==0:
    return xs[0]
  if h1>N:
    return xs[-1]

  x0 = xs[h0-1]
  x1 = xs[h1-1]

  if h0==h1:
    return x0

  ## Linear interpolation
  return (h1-h)*x0 + (h-h0)*x1

def GetErrorBand(hnom, hunivs):

  ys_Up = []
  ys_Down = []

  g = ROOT.TGraphAsymmErrors()

  for binIdx in range(0,hnom.GetXaxis().GetNbins()+2):

    xnom = hnom.GetXaxis().GetBinCenter(binIdx)
    ynom = hnom.GetBinContent(binIdx)
    g.SetPoint(binIdx, xnom, ynom)

    dx = hnom.GetXaxis().GetBinWidth(binIdx)

    ys = []
    for errhist in hunivs:
      ys.append(errhist.GetBinContent(binIdx))
    y0 = FindQuantile(.5-0.6827/2, ys)
    y1 = FindQuantile(.5+0.6827/2, ys)

    #print('[GetErrorBand] %1.2f + %1.2f - %1.2f '%(ynom, ynom-y0, y1-ynom))

    g.SetPointError(binIdx, dx/2., dx/2., max(ynom-y0, 0.), max(y1-ynom, 0.))

  return g

def GetAsymmError(hist_Nominal, hists_Syst):

  NBin = hist_Nominal.GetXaxis().GetNbins()
  x = []
  x_lerr = []
  x_rerr = []
  y = []
  y_lerr = []
  y_rerr = []

  for i in range(0,NBin):

    x.append( hist_Nominal.GetXaxis().GetBinCenter(i+1) )
    x_lerr.append( x[i] - hist_Nominal.GetXaxis().GetBinLowEdge(i+1) )
    x_rerr.append( hist_Nominal.GetXaxis().GetBinUpEdge(i+1) - x[i] )

    y.append( hist_Nominal.GetBinContent(i+1) )

    this_y_err = 0.
    for hist_Syst in hists_Syst:
      this_y_Syst = hist_Syst.GetBinContent(i+1)
      this_y_diff = this_y_Syst-hist_Nominal.GetBinContent(i+1)

      this_y_err += this_y_diff*this_y_diff

    y_lerr.append( math.sqrt(this_y_err) )
    y_rerr.append( math.sqrt(this_y_err) )

  out = ROOT.TGraphAsymmErrors(NBin, array("d", x), array("d", y),  array("d", x_lerr), array("d", x_rerr), array("d", y_lerr), array("d", y_rerr))
  return out

def convertToGraph(h):

  x = []
  x_err = []
  y = []
  y_err = []

  for ix in range(0,h.GetXaxis().GetNbins()):
    iBin = ix+1
    x_l = h.GetXaxis().GetBinLowEdge(iBin)
    x_r = h.GetXaxis().GetBinUpEdge(iBin)
    x_c = h.GetXaxis().GetBinCenter(iBin)

    x.append(x_c)
    x_err.append(x_r-x_c)
    y.append(h.GetBinContent(iBin))
    y_err.append(h.GetBinError(iBin))

  gr = ROOT.TGraphAsymmErrors(len(x), array('d',x), array('d',y), array('d',x_err), array('d',x_err), array('d',y_err), array('d',y_err) )
  return gr



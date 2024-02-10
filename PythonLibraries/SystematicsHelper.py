import ROOT
import math
import ctypes
import array

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

def GetErrorBandFromUniverse(hnom, hunivs):

  g = ROOT.TGraphAsymmErrors()

  for ix in range(0,hnom.GetXaxis().GetNbins()):

    binIdx = ix+1

    xnom = hnom.GetXaxis().GetBinCenter(binIdx)
    ynom = hnom.GetBinContent(binIdx)
    g.SetPoint(ix, xnom, ynom)

    dx = hnom.GetXaxis().GetBinWidth(binIdx)

    ys = []
    for errhist in hunivs:
      ys.append(errhist.GetBinContent(binIdx))
    y0 = FindQuantile(.5-0.6827/2, ys)
    y1 = FindQuantile(.5+0.6827/2, ys)

    #print('[GetErrorBand] %1.2f + %1.2f - %1.2f '%(ynom, ynom-y0, y1-ynom))

    g.SetPointError(ix, dx/2., dx/2., max(ynom-y0, 0.), max(y1-ynom, 0.))

  return g

def GetErrorBandFromUpDown(hnom, h_up, h_dn):

  g = ROOT.TGraphAsymmErrors()

  for ix in range(0,hnom.GetXaxis().GetNbins()):

    binIdx = ix+1

    xnom = hnom.GetXaxis().GetBinCenter(binIdx)
    ynom = hnom.GetBinContent(binIdx)
    g.SetPoint(ix, xnom, ynom)

    dx = hnom.GetXaxis().GetBinWidth(binIdx)

    ys = []

    y_up = h_up.GetBinContent(binIdx)
    y_dn = h_dn.GetBinContent(binIdx)

    y0 = max( ynom, max(y_up, y_dn) )
    y1 = min( ynom, min(y_up, y_dn) )

    #print('[GetErrorBand] %1.2f, %1.2f, %1.2f '%(ynom, y0, y1))

    g.SetPointError(ix, dx/2., dx/2., max(abs(y1-ynom), 0.), max(abs(ynom-y0), 0.))

  return g

def RemoveErrorFromGraph(gr, name="Graph"):
  # Create a new TGraphAsymmErrors object with the same data points
  new_gr = ROOT.TGraphAsymmErrors(gr.GetN())
  new_gr.SetName(name)

  # Loop through the data points in the original graph
  for i in range(gr.GetN()):
    x = ROOT.Double()
    y = ROOT.Double()
    gr.GetPoint(i, x, y)
    new_gr.SetPoint(i, x, y)
    new_gr.SetPointError(i, gr.GetErrorXlow(i), gr.GetErrorXhigh(i), 0.0, 0.0)

  return new_gr

## SumMode=0: Linearly (100% correlated)
## SumMode=1: Square sum (0% correlated)
def AddGraph(gr1, gr2, SumMode=0, Name="Graph"):

  n1 = 0
  try:
    n1 = gr1.GetN()
  except AttributeError:
    n1 = -1
  n2 = 0
  try:
    n2 = gr2.GetN()
  except AttributeError:
    n2 = -1

  if SumMode!=0 and SumMode!=1:
    raise ValueError("SumMode should be 0:Linearly 1:Square, but %d is given"%(SumMode))

  if n1<0 and n2<0:
    raise ValueError("Both graphs are not TGraph")
  if n1>0 and n2<0:
    return gr1.Clone(Name)
  if n1<0 and n2>0:
    return gr2.Clone(Name)

  # Make sure the graphs have the same number of points
  if n1 != n2:
    raise ValueError("Cannot add TGraphs with different number of points. (n1, n2) = (%d, %d)"%(n1, n2))

  # Create a new TGraph to store the result
  result = ROOT.TGraphAsymmErrors(n1)
  result.SetName(Name)

  # Loop over each point and perform the addition
  for i in range(n1):

    x1, y1 = ctypes.c_double(0.), ctypes.c_double(0.)
    x2, y2 = ctypes.c_double(0.), ctypes.c_double(0.)

    # Get the coordinates of each point in the graphs
    gr1.GetPoint(i, x1, y1)
    gr2.GetPoint(i, x2, y2)

    #if x1.value != x2.value:
    #  raise ValueError("Cannot add TGraphs with different x arrays: (x1, x2) = (%f, %f)"%(x1.value, x2.value))

    x = x1.value
    y_sum = y1.value + y2.value

    # Add the coordinates and set the point in the result graph
    result.SetPoint(i, x, y_sum)

    # Get the asymmetric errors of each point
    x1_err_low = gr1.GetErrorXlow(i)
    x1_err_high = gr1.GetErrorXhigh(i)
    y1_err_low = gr1.GetErrorYlow(i)
    y1_err_high = gr1.GetErrorYhigh(i)

    x2_err_low = gr2.GetErrorXlow(i)
    x2_err_high = gr2.GetErrorXhigh(i)
    y2_err_low = gr2.GetErrorYlow(i)
    y2_err_high = gr2.GetErrorYhigh(i)

    new_y_err_low = (y1_err_low + y2_err_low) if SumMode==0 else math.sqrt(y1_err_low*y1_err_low+y2_err_low*y2_err_low)
    new_y_err_high = (y1_err_high + y2_err_high) if SumMode==0 else math.sqrt(y1_err_high*y1_err_high+y2_err_high*y2_err_high)

    result.SetPointError(
      i,
      x1_err_low,
      x1_err_high,
      new_y_err_low,
      new_y_err_high
    )

  return result

def SumErrorGraphs(dict_KnobName_to_OneSigmaGraph, ToSkip=[]):

  if len(dict_KnobName_to_OneSigmaGraph)==0:
    return 0
  else:

    first_key = next(iter(dict_KnobName_to_OneSigmaGraph))

    N = dict_KnobName_to_OneSigmaGraph[first_key].GetN()

    result = ROOT.TGraphAsymmErrors(N)

    for i in range(N):

      x_nom, y_nom = ctypes.c_double(0.), ctypes.c_double(0.)
      dict_KnobName_to_OneSigmaGraph[first_key].GetPoint(i, x_nom, y_nom)

      x_nom_err_low = dict_KnobName_to_OneSigmaGraph[first_key].GetErrorXlow(i)
      x_nom_err_high = dict_KnobName_to_OneSigmaGraph[first_key].GetErrorXhigh(i)

      thisbin_errsum_low = 0.
      thisbin_errsum_high = 0.

      result.SetPoint(i, x_nom.value, y_nom.value)

      for name in dict_KnobName_to_OneSigmaGraph:

        if name in ToSkip:
          continue
        if dict_KnobName_to_OneSigmaGraph[name]==0:
          continue

        x_syst, y_syst = ctypes.c_double(0.), ctypes.c_double(0.)
        y_syst_err_low = dict_KnobName_to_OneSigmaGraph[name].GetErrorYlow(i)
        y_syst_err_high = dict_KnobName_to_OneSigmaGraph[name].GetErrorYhigh(i)

        thisbin_errsum_low += y_syst_err_low*y_syst_err_low
        thisbin_errsum_high += y_syst_err_high*y_syst_err_high

      thisbin_errsum_low = math.sqrt(thisbin_errsum_low)
      thisbin_errsum_high = math.sqrt(thisbin_errsum_high)

      result.SetPointError(
        i,
        x_nom_err_low,
        x_nom_err_high,
        thisbin_errsum_low,
        thisbin_errsum_high
      )

    return result

def GetFractionalError(gr):

  N = gr.GetN()

  result = ROOT.TGraph(N)

  xs = []
  ys = []

  for i in range(N):

    x, y = ctypes.c_double(0.), ctypes.c_double(0.)
    gr.GetPoint(i, x, y)

    x_err_low = gr.GetErrorXlow(i)
    x_err_high = gr.GetErrorXhigh(i)
    y_err_low = gr.GetErrorYlow(i)
    y_err_high = gr.GetErrorYhigh(i)

    averaged_err = math.sqrt( (y_err_low*y_err_low + y_err_high*y_err_high)/2. )
    if y.value>0:
      averaged_err /= y.value

    result.SetPoint(i, x.value, averaged_err)

    if i==0:
      xs.append( x.value - x_err_low )
    xs.append( x.value + x_err_high )
    ys.append(averaged_err)

  h = ROOT.TH1D("h_FracError_from_"+gr.GetName(), "", len(xs)-1, array.array("d", xs))
  for ix in range(0, len(xs)-1):
    h.SetBinContent(ix+1, ys[ix])


  return h
  #return result

def GetStatisticalError(hnom):

  g = ROOT.TGraphAsymmErrors()

  for ix in range(0,hnom.GetXaxis().GetNbins()):

    binIdx = ix+1

    xnom = hnom.GetXaxis().GetBinCenter(binIdx)
    ynom = hnom.GetBinContent(binIdx)
    g.SetPoint(ix, xnom, ynom)

    dx = hnom.GetXaxis().GetBinWidth(binIdx)

    ys = []

    staterr = hnom.GetBinError(binIdx)

    g.SetPointError(ix, dx/2., dx/2., staterr, staterr)

  return g

def GetRatioPlots(gr_Data, gr_Stat, gr_Sum):

  g_Ratio_Data = ROOT.TGraphAsymmErrors()
  g_Ratio_Stat = ROOT.TGraphAsymmErrors()
  g_Ratio_Sum = ROOT.TGraphAsymmErrors()

  N_Data = gr_Data.GetN()
  N_Stat = gr_Stat.GetN()
  N_Sum = gr_Sum.GetN()

  # Make sure the graphs have the same number of points
  if N_Data!=N_Stat or N_Stat!=N_Sum:
    raise ValueError("Wrong graph points: (%d, %d, %d)"%(N_Data, N_Stat, N_Sum))

  N = N_Data

  for i in range(N):

    x_Data, y_Data = ctypes.c_double(0.), ctypes.c_double(0.)
    gr_Data.GetPoint(i, x_Data, y_Data)
    x_Data = x_Data.value
    y_Data = y_Data.value
    x_err_low_Data = gr_Data.GetErrorXlow(i)
    x_err_high_Data = gr_Data.GetErrorXhigh(i)
    y_err_low_Data = gr_Data.GetErrorYlow(i)
    y_err_high_Data = gr_Data.GetErrorYhigh(i)

    x_Stat, y_Stat = ctypes.c_double(0.), ctypes.c_double(0.)
    gr_Stat.GetPoint(i, x_Stat, y_Stat)
    x_Stat = x_Stat.value
    y_Stat = y_Stat.value
    x_err_low_Stat = gr_Stat.GetErrorXlow(i)
    x_err_high_Stat = gr_Stat.GetErrorXhigh(i)
    y_err_low_Stat = gr_Stat.GetErrorYlow(i)
    y_err_high_Stat = gr_Stat.GetErrorYhigh(i)

    x_Sum, y_Sum = ctypes.c_double(0.), ctypes.c_double(0.)
    gr_Sum.GetPoint(i, x_Sum, y_Sum)
    x_Sum = x_Sum.value
    y_Sum = y_Sum.value
    x_err_low_Sum = gr_Sum.GetErrorXlow(i)
    x_err_high_Sum = gr_Sum.GetErrorXhigh(i)
    y_err_low_Sum = gr_Sum.GetErrorYlow(i)
    y_err_high_Sum = gr_Sum.GetErrorYhigh(i)

    ## check
    #print(x_Data, y_Data, y_Stat, y_Sum, abs(y_Stat-y_Sum))

    ratio = 0.
    ratio_err_low_Data = 0.
    ratio_err_high_Data = 0.
    if y_Stat>0:
      ratio = y_Data/y_Stat
      ratio_err_low_Data = y_err_low_Data/y_Stat
      ratio_err_high_Data = y_err_high_Data/y_Stat
    g_Ratio_Data.SetPoint(i, x_Data, ratio)
    g_Ratio_Data.SetPointError(i, x_err_low_Data, x_err_high_Data, max(0., abs(ratio_err_low_Data)), max(0., abs(ratio_err_high_Data)))

    ratio_err_low_Stat = 0.
    ratio_err_high_Stat = 0.
    if y_Stat>0:
      ratio_err_low_Stat = y_err_low_Stat/y_Stat
      ratio_err_high_Stat = y_err_high_Stat/y_Stat
    g_Ratio_Stat.SetPoint(i, x_Stat, 1.)
    g_Ratio_Stat.SetPointError(i, x_err_low_Data, x_err_high_Data, ratio_err_low_Stat, ratio_err_high_Stat)

    ratio_err_low_Sum = 0.
    ratio_err_high_Sum = 0.
    if y_Sum>0:
      ratio_err_low_Sum = y_err_low_Sum/y_Sum
      ratio_err_high_Sum = y_err_high_Sum/y_Sum
    g_Ratio_Sum.SetPoint(i, x_Sum, 1.)
    g_Ratio_Sum.SetPointError(i, x_err_low_Data, x_err_high_Data, ratio_err_low_Sum, ratio_err_high_Sum)

  return g_Ratio_Data, g_Ratio_Stat, g_Ratio_Sum

def GetBackgroundSubtractedSumErrors(gr_Data, gr_Bkgd_Stat, gr_Bkgd_All):

  N = gr_Data.GetN()

  result_Stat = ROOT.TGraphAsymmErrors(N)
  result_All = ROOT.TGraphAsymmErrors(N)

  for i in range(N):

    ## Data values
    x_Data, y_Data = ctypes.c_double(0.), ctypes.c_double(0.)
    gr_Data.GetPoint(i, x_Data, y_Data)
    x_Data_err_low = gr_Data.GetErrorXlow(i)
    x_Data_err_high = gr_Data.GetErrorXhigh(i)
    y_Data_err_low = gr_Data.GetErrorYlow(i)
    y_Data_err_high = gr_Data.GetErrorYhigh(i)
    ## Stat
    x_Bkgd_Stat, y_Bkgd_Stat = ctypes.c_double(0.), ctypes.c_double(0.)
    gr_Bkgd_Stat.GetPoint(i, x_Bkgd_Stat, y_Bkgd_Stat)
    y_Bkgd_Stat_err_low = gr_Bkgd_Stat.GetErrorYlow(i)
    y_Bkgd_Stat_err_high = gr_Bkgd_Stat.GetErrorYhigh(i)
    ## All (=stat+syst) 
    x_Bkgd_All, y_Bkgd_All = ctypes.c_double(0.), ctypes.c_double(0.)
    gr_Bkgd_All.GetPoint(i, x_Bkgd_All, y_Bkgd_All)
    y_Bkgd_All_err_low = gr_Bkgd_All.GetErrorYlow(i)
    y_Bkgd_All_err_high = gr_Bkgd_All.GetErrorYhigh(i)

    ## Data-bkgd
    y_Subtr = y_Data.value - y_Bkgd_Stat.value

    StatErrorSum_low = math.sqrt( y_Data_err_low*y_Data_err_low + y_Bkgd_Stat_err_low*y_Bkgd_Stat_err_low )
    StatErrorSum_high = math.sqrt( y_Data_err_high*y_Data_err_high + y_Bkgd_Stat_err_high*y_Bkgd_Stat_err_high )

    AllErrorSum_low = math.sqrt( y_Data_err_low*y_Data_err_low + y_Bkgd_All_err_low*y_Bkgd_All_err_low )
    AllErrorSum_high = math.sqrt( y_Data_err_high*y_Data_err_high + y_Bkgd_All_err_high*y_Bkgd_All_err_high )

    result_Stat.SetPoint(i, x_Data.value, y_Subtr)
    result_Stat.SetPointError(
      i,
      x_Data_err_low,
      x_Data_err_low,
      StatErrorSum_low,
      StatErrorSum_high
    )

    result_All.SetPoint(i, x_Data.value, y_Subtr)
    result_All.SetPointError(
      i,
      x_Data_err_low,
      x_Data_err_high,
      AllErrorSum_low,
      AllErrorSum_high
    )

  return result_Stat, result_All

def GetBackgroundSubtractedError(gr_Data, gr_Bkgd_Error):

  N = gr_Data.GetN()

  result = ROOT.TGraphAsymmErrors(N)

  for i in range(N):

    ## Data values
    x_Data, y_Data = ctypes.c_double(0.), ctypes.c_double(0.)
    gr_Data.GetPoint(i, x_Data, y_Data)
    x_Data_err_low = gr_Data.GetErrorXlow(i)
    x_Data_err_high = gr_Data.GetErrorXhigh(i)
    y_Data_err_low = gr_Data.GetErrorYlow(i)
    y_Data_err_high = gr_Data.GetErrorYhigh(i)

    ## Bkgd
    x_Bkgd, y_Bkgd = ctypes.c_double(0.), ctypes.c_double(0.)
    gr_Bkgd_Error.GetPoint(i, x_Bkgd, y_Bkgd)
    y_Bkgd_err_low = gr_Bkgd_Error.GetErrorYlow(i)
    y_Bkgd_err_high = gr_Bkgd_Error.GetErrorYhigh(i)

    ## Data-bkgd
    y_Subtr = y_Data.value - y_Bkgd.value

    result.SetPoint(i, x_Data.value, y_Subtr)
    result.SetPointError(
      i,
      x_Data_err_low,
      x_Data_err_high,
      y_Bkgd_err_low,
      y_Bkgd_err_high
    )

  return result

def GetBackgroundSubtractedDataStatError(gr_Data, gr_Bkgd_Error):

  N = gr_Data.GetN()

  result = ROOT.TGraphAsymmErrors(N)

  for i in range(N):

    ## Data values
    x_Data, y_Data = ctypes.c_double(0.), ctypes.c_double(0.)
    gr_Data.GetPoint(i, x_Data, y_Data)
    x_Data_err_low = gr_Data.GetErrorXlow(i)
    x_Data_err_high = gr_Data.GetErrorXhigh(i)
    y_Data_err_low = gr_Data.GetErrorYlow(i)
    y_Data_err_high = gr_Data.GetErrorYhigh(i)

    ## Bkgd
    x_Bkgd, y_Bkgd = ctypes.c_double(0.), ctypes.c_double(0.)
    gr_Bkgd_Error.GetPoint(i, x_Bkgd, y_Bkgd)
    y_Bkgd_err_low = gr_Bkgd_Error.GetErrorYlow(i)
    y_Bkgd_err_high = gr_Bkgd_Error.GetErrorYhigh(i)

    ## Data-bkgd
    y_Subtr = y_Data.value - y_Bkgd.value

    result.SetPoint(i, x_Data.value, y_Subtr)
    result.SetPointError(
      i,
      x_Data_err_low,
      x_Data_err_high,
      y_Data_err_low,
      y_Data_err_high,
    )

  return result

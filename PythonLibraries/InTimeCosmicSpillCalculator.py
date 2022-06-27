## InTime cosmic MC scaling
class InTimeCosmicSpillCalculator:

  IntimeCosmicMC_Spill = -1

  BeamMC_POT = -1
  BeamMC_Spill = -1

  POTScaleFactorForBeamMC = -1

  def __init__(self, Data_POT, Data_Spill):
    self.Data_POT = Data_POT
    self.Data_Spill = Data_Spill
    self.Data_Intensity = self.Data_POT/self.Data_Spill

  def GetInTimeCosmicSpill(self, f_BeamMC, f_IntimeCosmicMC):

    ## IntimeCosmic info

    self.IntimeCosmicMC_Spill = f_IntimeCosmicMC.Get("BeamInfo/Livetime_BeamInfo").GetBinContent(1)
    print("[mylib.GetInTimeCosmicScaleFactor] Intime cosmic MC has %1.2e spills simulated"%(self.IntimeCosmicMC_Spill))

    ## Beam info

    self.BeamMC_POT = f_BeamMC.Get("BeamInfo/POT_BeamInfo").GetBinContent(1)
    self.BeamMC_Spill = f_BeamMC.Get("BeamInfo/Livetime_BeamInfo").GetBinContent(1)

    ## Scale factor for the BeamMC to match the data POT

    self.POTScaleFactorForBeamMC = self.Data_POT/self.BeamMC_POT
    ## Number of nu-Ar spill simulated from BeamMC;
    ## This number is smaller than data POT
    BeamMC_Spill_Scaled = self.BeamMC_Spill * self.POTScaleFactorForBeamMC

    ## Number of cosmic-only spill we need to match data spill
    IntimeCosmicMC_Spill_ToScale = self.Data_Spill - BeamMC_Spill_Scaled

    return IntimeCosmicMC_Spill_ToScale

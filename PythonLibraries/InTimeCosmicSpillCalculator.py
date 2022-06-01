## InTime cosmic MC scaling
class InTimeCosmicSpillCalculator:

  IntimeCosmicMC_TargetPOT = -1
  BeamMC_TargetPOT = -1

  BeamMC_MCPOT = -1
  BeamMC_MCSpill = -1

  BeamMC_POTScaleFactor = -1
  BeamMCScaledSpill = -1

  def __init__(self, _POTtoNormalize, _nominalIntensity):
    self.POTtoNormalize = _POTtoNormalize
    self.nominalIntensity = _nominalIntensity
    self.nominalSpill = self.POTtoNormalize/self.nominalIntensity

  def GetInTimeCosmicSpill(self, f_BeamMC, f_IntimeCosmicMC):

    ## IntimeCosmic info
    ##   This is necessary to undo the scaling done by ToTH1
    ##   https://github.com/SBNSoftware/sbnana/blob/b085dfe7238dd31ce4ff7b2e791db5f313ed5ac5/sbnana/CAFAna/Core/Spectrum.cxx#L442
    h_IntimeCosmicMC_TargetPOT = f_IntimeCosmicMC.Get("hist_TargetPOT")
    self.IntimeCosmicMC_TargetPOT = h_IntimeCosmicMC_TargetPOT.GetBinContent(1)
    print("[mylib.GetInTimeCosmicScaleFactor] The target POT used for the Intime cosmic MC histograms were %1.2e"%(self.IntimeCosmicMC_TargetPOT))

    ## Beam info
    ##   This is necessary to undo the scaling done by ToTH1
    ##   https://github.com/SBNSoftware/sbnana/blob/b085dfe7238dd31ce4ff7b2e791db5f313ed5ac5/sbnana/CAFAna/Core/Spectrum.cxx#L442
    h_BeamMC_TargetPOT = f_BeamMC.Get("hist_TargetPOT")
    self.BeamMC_TargetPOT = h_BeamMC_TargetPOT.GetBinContent(1)
    self.BeamMC_TargetPOT = 6e20 #TODO hadd 
    print("[mylib.GetInTimeCosmicScaleFactor] The target POT used for the Beam MC histograms were %1.2e"%(self.BeamMC_TargetPOT))

    ## Nominal values
    print("[mylib.GetInTimeCosmicScaleFactor] nominalIntensity = %1.2e"%(self.nominalIntensity))
    print("[mylib.GetInTimeCosmicScaleFactor] -> nominalSpill = POTtoNormalize/nominalIntensity = %1.2e"%(self.nominalSpill))

    ## MC POT/Spill
    ## The POT and Spill used for the MC generation
    h_BeamMC_MCPOT = f_BeamMC.Get('NuMuCC_NoCut/POT_NuMuCC_NoCut')
    h_BeamMC_MCSpill = f_BeamMC.Get('NuMuCC_NoCut/Livetime_NuMuCC_NoCut')
    self.BeamMC_MCPOT = h_BeamMC_MCPOT.GetBinContent(1)
    self.BeamMC_MCSpill = h_BeamMC_MCSpill.GetBinContent(1)
    print("[mylib.GetInTimeCosmicScaleFactor] POT used for the Beam MC generation = %1.2e"%(self.BeamMC_MCPOT))
    print("[mylib.GetInTimeCosmicScaleFactor] Spill used for the Beam MC generation = %1.2e"%(self.BeamMC_MCSpill))

    ## POT scaling
    self.BeamMC_POTScaleFactor = self.POTtoNormalize/self.BeamMC_MCPOT
    print("[mylib.GetInTimeCosmicScaleFactor] -> To normalized the Beam MC to POTtoNormalize (%1.2e), a scale factor = %1.2e will be applied"%(self.POTtoNormalize,self.BeamMC_POTScaleFactor))

    ## Scale the MC spill by the POTtoNormalize
    self.BeamMCScaledSpill = self.BeamMC_MCSpill * self.BeamMC_POTScaleFactor
    print("[mylib.GetInTimeCosmicScaleFactor] -> Then, the Beam MC spill is also scaled; BeamMCScaledSpill = %1.2e"%(self.BeamMCScaledSpill))

    ## Now the cosmic livetime is..
    InTimeCosmicSpill = self.nominalSpill - self.BeamMCScaledSpill
    print("[mylib.GetInTimeCosmicScaleFactor] * The InTime cosmic MC will be scaled to match the spill we need more")
    print("[mylib.GetInTimeCosmicScaleFactor] * nominalSpill - BeamMCScaledSpill = %1.2e"%(InTimeCosmicSpill))

    return InTimeCosmicSpill

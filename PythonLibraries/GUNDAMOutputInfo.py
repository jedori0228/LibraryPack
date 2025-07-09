class GUNDAMOutputInfo:

    def __init__(self, Folder, FitConfig, DataEntry, Latex):

      self.Folder = Folder
      self.FitConfig = FitConfig
      self.DataEntry = DataEntry
      self.Latex = Latex

    def GetFitterFile(self, Var):

      return f'{self.Folder}/Fitter/output_{self.DataEntry}_{self.FitConfig}_{Var}.root'

    def GetCalcXsecFile(self, Var):

      return f'{self.Folder}/CalcXsec/output_{self.DataEntry}_{self.FitConfig}_{Var}.root'

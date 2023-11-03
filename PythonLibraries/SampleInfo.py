class SampleInfo:

  def __init__(self, Key, Name, Latex, Color, Type, Expr="", Weight="1", IsSignal=False):

    self.Key = Key
    self.Expr = Expr
    self.Weight = Weight
    self.Name = Name
    self.Latex = Latex
    self.Color = Color
    self.Type = Type
    self.IsSignal = IsSignal


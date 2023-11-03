class Logger:

  def __init__(self, name, thr_str):

    self.Name = name
    self.Threshold = self.GetLevel(thr_str)

  def GetLevel(self, level_str):
    if level_str=="DEBUG":
      return 0
    elif level_str=="INFO":
      return 1
    elif level_str=="WARN":
      return 2
    elif level_str=="ERROR":
      return 3
    else:
      print("[LOGGER][GetLevel] Wrong level_str: %s"%(level_str))
      raise

  def LOG(self, level_str, msg, subName=""):

    level = self.GetLevel(level_str)
    if level>=self.Threshold:
      header = "[%s][%s]"%(level_str, self.Name) if subName=="" else "[%s][%s][%s]"%(level_str, self.Name, subName)
      print(header, end =" ")
      print(msg)


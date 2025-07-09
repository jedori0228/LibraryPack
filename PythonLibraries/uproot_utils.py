import numpy as np

def RebinUprootHist(bin_edges, contents, nrebin):
    """
    Rebins histogram data by combining nrebin bins into 1.
    
    Parameters:
    bin_edges (numpy.ndarray): The original bin edges.
    contents (numpy.ndarray): The original bin contents.
    nrebin (int): The number of bins to combine into one.
    
    Returns:
    tuple: Tuple containing:
        - new_bin_edges (numpy.ndarray): The rebinned bin edges.
        - new_contents (numpy.ndarray): The rebinned contents.
    """
    # Ensure the number of bins is a multiple of the rebin factor
    if len(contents) % nrebin != 0:
        raise ValueError("Number of bins is not a multiple of the rebin factor")
    
    # Rebin the contents
    new_contents = np.add.reduceat(contents, np.arange(0, len(contents), nrebin))
    
    # Rebin the bin edges
    new_bin_edges = bin_edges[::nrebin]
    
    return new_contents, new_bin_edges

def IntegrateHist(bin_edges, contents, x_min, x_max):

  if len(bin_edges) != len(contents)+1:
    raise ValueError("len(bin_edges) != len(contents)+1")

  bin_indices = np.where((bin_edges[:-1] >= x_min) & (bin_edges[1:] <= x_max))[0]

  # Sum the contents of the selected bins
  integral = np.sum(contents[bin_indices])
    
  return integral

def GetBinIndex(x, edges):
    """
    Return the bin content that the coordinate `x` falls into.

    Underflow/overflow: returns None if x is outside the histogram range.
    """
    # index of the bin (0-based); right edge is *exclusive* except for the last bin
    idx = np.searchsorted(edges, x, side="right") - 1
    if idx<0:
      return -1
    elif idx>=len(edges):
      return len(edges)
    else:
      return idx

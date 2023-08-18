import numpy as np

point = np.array(point)
X = np.asarray(X)


def eucildeanDistance():
  intmdt = ((X - point)**2)
  euclidean = np.round((np.sqrt(np.sum(intmdt, axis =1))), 2)
  return euclidean

def manhattanDistance():
  intmdt = abs((X - point))
  manhattan = np.round(np.sum(intmdt, axis=1), 2)
  return manhattan

def minkowskiDistance(p):
  intmdt = (abs((X - point)))
  minkowski = np.round(np.sum(intmdt ** p, axis=1) ** (1 / p), 2)
  return minkowski

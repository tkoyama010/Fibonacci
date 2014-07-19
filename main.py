import numpy as np
@np.vectorize
def F(n):
  return 1./np.sqrt(5.)*(((1.+np.sqrt(5))/2.)**n-((1.-np.sqrt(5))/2.)**n)
n = np.arange(10)
F = F(n)
np.savetxt("F.txt", F)


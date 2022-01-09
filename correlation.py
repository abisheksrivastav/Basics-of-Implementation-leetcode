from scipy import stats
import numpy as np

def correlation(array1, array2):
   if len(array1) == 0 or len(array2) == 0:
       return 0
   else :
      return (stats.pearsonr(array1, array2)[0], stats.pearsonr(array1, array2)[1])

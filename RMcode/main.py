import RM
#from RMcode.RM import sum_binomial, fill_bit_array, MatrixGenerator, Generation_Gr, Creation_G1
import numpy as np
from itertools import combinations

##matrix = RM.generate_matrix()
##print(matrix)
c=RM.RM(4,2)
message = [0,1,1,0,1,0,1,1,0,1,0]  # 11 бит
##print(c.Encoding42(message))
emessage=c.encode(message)
emessage[2]=1
print(c.decode(emessage))
##print(sum_binomial(4,2))
##print(MatrixGenerator(4,2))
##print(Generation_Gr(Creation_G1(4),2))

"""
1D ARRAY
import numpy as np

one_diamensional_list = [1,2,4]
one_diamensional_arr =np.array(one_diamensional_list)
print("1D array is :", one_diamensional_arr)

2D ARRAY
import numpy as np

two_diamensional_list = [[1,2,3],[4,5,6]]
two_diamensional_arr =np.array(two_diamensional_list)
print("2D array is :", two_diamensional_arr)

import numpy as np

three_diamensional_list = [[[1,2,3],[4,5,6],[7,8,9,]]]
three_diamensional_arr =np.array(three_diamensional_list)
print("3D array is :", three_diamensional_arr)

import numpy as np
ndArray = np.array([1, 2, 3, 4], ndmin=10)
print(ndArray)
print('Dimensions of array:', ndArray.ndim)"""

import numpy as np

p = [45,21,30,29]
q = 3.0
p = np.array(p)
q = np.array(q)
print("Datatype:",p.dtype)
print("Datatype:",q.dtype)

import numpy as np
p = [[10,20,30], [40, 50, 60], [70,80,90]]
q = 3.4
p = np.array(p)
q = np.array(q)
print("Datatype:", p.dtype)
print("Datatype:", q.dtype)

import numpy as np
p = [[[10,20,30], [40, 50, 60], [70,80,90]]]
q = [10,20,30]
p = np.array(p)
q = np.array(q)
print("Dimension of array p:", p.ndim)
print("Dimension of array q:", q.ndim)



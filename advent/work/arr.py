import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d.shape)
print(arr2d.dtype)
print(arr2d.ndim)

# create a 2 by 7 array
arr2by7= np.array([[1, 2, 3,4,6,7,1], [4, 5, 6,1,2,4,2]])

# get a specific element
print(arr2by7.shape)

print(arr2by7[1,5])

print(arr2by7[1,:])
print(arr2by7[:,0])
import numpy as np
import random

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

z = np.concatenate((x, y),axis = 0)

print(z.ndim)

print(z.shape)

print(z.size)

a = np.arange(6)
print(a)

b = a.reshape(3, 2)
print(b) 

a = np.array([1,2,3,4,5,6])
print(a.shape)

a2 = a[np.newaxis, :]
print(a2.shape)  

b = np.array([[1, 1], [2,2]])
a= b.sum(axis=1)
print(a) 

rng = random.Random()

random_number = rng.randint(1, 10)


arr = np.array([11,11,12,13,13,14,15,16,17,17,18])

unique_values = np.unique(a)

unique_values, indices_list = np.unique(arr, return_index=True)

print(indices_list)

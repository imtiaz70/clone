import numpy as np

x = np.arange(0,91,15)
y = np.arange(7)

l = np.array([3,5,7] , dtype=complex)
m = np.array([10,20,30] , dtype=complex)
# x = x.reshape(3,4)
print(l.real)
print(np.angle(m))



# print("Mod of x , y " , np.remainder(l,m))


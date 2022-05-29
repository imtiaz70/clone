import numpy as np

x = np.arange(12).reshape(3,4)
# x = x.reshape(3,4)
print(x)
print(np.amax(x,axis=1))
print(np.amax(x,1))







import numpy as np
import itertools
import matplotlib.pyplot as plt






data = OFDM_dataset(1)

print(data.all_abs)
'''
plt.figure()
plt.plot(data.x, 'x')
plt.show()
'''
plt.figure()
plt.hist(data.all_abs.flatten(), bins=20)
plt.show()


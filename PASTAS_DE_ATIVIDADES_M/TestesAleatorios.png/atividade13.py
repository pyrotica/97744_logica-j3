import matplotlib.pyplot as plt
import numpy as np
val= np.random.randint(1,10,100)
plt.bar(range(len(val)), val)
plt.show()
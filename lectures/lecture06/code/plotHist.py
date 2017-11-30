import numpy as np
import matplotlib.pyplot as plt
mu = 4.0
beta = 0.2
# let's draw 1000 random samples from the Gumbel distribution
samples = np.random.gumbel(mu, beta, 1000)

plt.figure()
plt.hist(samples, bins=30, edgecolor='black', normed=True)
plt.xlabel('sample value')
plt.ylabel('number of occurrences divided by sum of occurences')
plt.show()
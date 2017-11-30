from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

n = 100   # number of trials
p = 1./6. # probability that you win

my_binom = binom(n,p)

n_wins = np.arange(0,40,1)
plt.figure()
plt.plot(n_wins,my_binom.pmf(n_wins), 'o')
plt.show()

# what is the proability that you'll win at least 16 times?
print(my_binom.sf(15))

# what is the probability that you won't win more than 25 times? 
print(my_binom.cdf(24))
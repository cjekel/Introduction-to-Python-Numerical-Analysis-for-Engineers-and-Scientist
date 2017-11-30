from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


np.random.seed(3)
a = np.random.random(10)
b = np.random.normal(size=10)
two_samp = stats.ks_2samp(a,b)
# since the p value is less than 0.05 I reject that the
# two samples came from the same distribution
# with a 95% confidence level.



np.random.seed(121)
binom_mars = stats.binom(100,0.0925)
mars_rv = binom_mars.rvs(10)
print(np.mean(mars_rv))
print(binom_mars.cdf(10))

x = np.arange(0,50,1)
plt.figure()
plt.plot(x, binom_mars.sf(x))
plt.show()


np.random.seed(32332)
# generate 1000 samples from the
rv = stats.laplace.rvs(loc=75, scale=5, size=1000)

# save the random variables as numpy array
np.save('Aluminum_youngs_moduli',rv)



# fit a normal distribion
norm_param = stats.norm.fit(rv)
laplace_param = stats.laplace.fit(rv)
maxwell_param = stats.maxwell.fit(rv)
# vonmises_param = stats.vonmises.fit(rv)
logistic_param = stats.logistic.fit(rv)

x = np.linspace(10,150,200)

plt.figure()
plt.hist(rv, bins=21, normed=True)
plt.plot(x, stats.norm.pdf(x, *norm_param), label='norm')
plt.plot(x, stats.maxwell.pdf(x, *maxwell_param), label='maxwell_param')
# plt.plot(x, stats.vonmises.pdf(x, *vonmises_param), label='vonmises_param')
plt.plot(x, stats.logistic.pdf(x, *logistic_param), label='logistic_param')
plt.plot(x, stats.laplace.pdf(x, *laplace_param), label='laplace')
plt.legend()
plt.show()

plt.figure()
plt.hist(rv, cumulative=True, bins=21, normed=True)
plt.plot(x, stats.norm.cdf(x, *norm_param), label='norm')
plt.plot(x, stats.maxwell.cdf(x, *maxwell_param), label='maxwell_param')
# plt.plot(x, stats.vonmises.pdf(x, *vonmises_param), label='vonmises_param')
plt.plot(x, stats.logistic.cdf(x, *logistic_param), label='logistic_param')
plt.plot(x, stats.laplace.cdf(x, *laplace_param), label='laplace')
plt.legend()
plt.show()

# ks_statistic
ks_norm = stats.kstest(rv, 'norm', norm_param)
ks_laplace = stats.kstest(rv, 'laplace', laplace_param)
ks_maxwell = stats.kstest(rv, 'maxwell', maxwell_param)
ks_logistic = stats.kstest(rv, 'logistic', logistic_param)

# accept either the logistic or laplace!

from __future__ import print_function

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# ========== HW07 SOLUTION [Python2/3] ========== #


# ========== 1 ========== #

a = np.array([0.5507979, 0.70814782, 0.29090474, 0.51082761, 0.89294695, 0.89629309, 0.12558531, 0.20724288, 0.0514672, 0.44080984])
b = np.array([-0.04381817, -0.47721803, -1.31386475, 0.88462238, 0.88131804, 1.70957306, 0.05003364, -0.40467741, -0.54535995, -1.54647732])

# K-S 2 sample test
# null hypothesis: a and b are sampled from the same distribution
kstest = stats.ks_2samp(a, b)
kstest.pvalue < 0.05  # True; reject null hypothesis.
# conclude a and b are NOT from the same distribution.

# a histogram can show visually that they are not from the same distribution.
plt.figure()
plt.hist(a)
plt.hist(b)
plt.show()

# ========== 2 ========== #

np.random.seed(121)
binom_mars = stats.binom(100, 0.0925)
mars_rv = binom_mars.rvs(10)
print(np.mean(mars_rv))
print(binom_mars.cdf(10.0))

# ========== 3 ========== #

rv = np.load('Aluminum_youngs_moduli.npy')
est_loc = np.mean(rv)
est_scale = np.std(rv)

# fitting different distributions
norm_param = stats.norm.fit(rv)
laplace_param = stats.laplace.fit(rv)
maxwell_param = stats.maxwell.fit(rv)
logistic_param = stats.logistic.fit(rv)

# plot PDFs
x = np.linspace(10, 150, 200)
plt.figure()
plt.hist(rv, bins=21, normed=True)
plt.plot(x, stats.norm.pdf(x, *norm_param), label='norm')
plt.plot(x, stats.maxwell.pdf(x, *maxwell_param), label='maxwell_param')
plt.plot(x, stats.logistic.pdf(x, *logistic_param), label='logistic_param')
plt.plot(x, stats.laplace.pdf(x, *laplace_param), label='laplace')
plt.legend()
plt.show()

# plot CDFs
plt.figure()
plt.hist(rv, cumulative=True, bins=21, normed=True)
plt.plot(x, stats.norm.cdf(x, *norm_param), label='norm')
plt.plot(x, stats.maxwell.cdf(x, *maxwell_param), label='maxwell_param')
plt.plot(x, stats.logistic.cdf(x, *logistic_param), label='logistic_param')
plt.plot(x, stats.laplace.cdf(x, *laplace_param), label='laplace')
plt.legend()
plt.show()

# visually, we can eliminate the Maxwell distribution

# K-S tests
ks_norm = stats.kstest(rv, 'norm', norm_param)
ks_laplace = stats.kstest(rv, 'laplace', laplace_param)
ks_maxwell = stats.kstest(rv, 'maxwell', maxwell_param)
ks_logistic = stats.kstest(rv, 'logistic', logistic_param)

# ks_norm.pvalue -> 0.00016185237120902585
# ks_laplace.pvalue -> 0.75696987136141258
# ks_maxwell,pvalue -> 0.0
# ks_logistic.pvalue -> 0.14502969211826544

# with alpha=0.05, accept either the laplace or logistic.
# however, it is clear to be laplace due to the high p-value.

# note that we are looking for a LARGE p-value
# to accept the null hypothesis of coming from that distribution.

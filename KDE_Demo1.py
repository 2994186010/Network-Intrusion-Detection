from KDEpy import FFTKDE
data = norm(loc=0, scale=1).rvs(2**3)
estimator = FFTKDE(kernel='gaussian', bw='silverman')
x, y = estimator.fit(data, weights=None).evaluate()
plt.plot(x, y, label='KDE estimate')

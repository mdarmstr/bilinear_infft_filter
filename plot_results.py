from intrp_infft_1d.intrp_infft_1d import *
from bilinear_nfft_filter import *
import matplotlib.pyplot as plt
import numpy as np

#Script for acquiring and plotting the results.

X,Y = digest_csv('T.Suelo.csv')
Xpred, Xpvls, Fkr, t = validate_data(X,Y)

np.save("Xpred.npy",Xpred)
np.save("Xpvls.npy",Xpvls)
np.save("Fkr.npy",Fkr)
np.save("t.npy",t)

cmap = plt.get_cmap('viridis')

Xpred = np.load("Xpred.npy")
Xpvls = np.load("Xpvls.npy")
X = np.load("t.npy")

idy = 0

df = pd.read_csv('T.Suelo.csv')
Xr = df.iloc[0:,1:].to_numpy()
Ln = Xr.shape[0]

idx = np.invert(np.isnan(X[:,idy]))
t = np.linspace(-0.5,0.5,Ln,endpoint=False)

plt.scatter(t[idx], Xr[idx,idy], c=Xpvls[idx,idy], cmap=cmap, s=1)

idp = np.logical_and(idx,Xpvls[:,idy] < 0.01)

plt.scatter(t[idp], Xr[idp,idy],marker='o',s=2,color='red')
plt.plot(t,Xpred[:,idy])
plt.colorbar()
plt.xlabel('Normalized time $\in$ [-0.5,0.5)')
plt.ylabel('Temperature, C')
plt.title(f'pvals for idx = {idy}; cutoff = 0.01')
plt.show()

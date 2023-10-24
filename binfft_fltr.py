import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds
from scipy.stats import chi2
from infft import *

def validate_data(X,Y,N = 1024,k=2,p=0.05,kernel='sobolev',verbose=True):
    
    if kernel == 'sobolev':
        w = sobk(N,1,2,1e-2)
    elif kernel == 'fejer':
        w = fjr(N)

    Fk = np.zeros((N,X.shape[1]),dtype='complex128')
    mn = np.zeros(X.shape[1])
    Xpred = np.zeros_like(X)
    Xpvls = np.zeros_like(X)
    tnom = np.linspace(-0.5,0.5,X.shape[0],endpoint='False')
    idx = []
    
    for ii in range(X.shape[1]):
        idx.append(np.invert(np.isnan(X[:,ii])))
        mn[ii] = np.mean(X[idx[ii],ii])

        A = ndft_mat(X[idx[ii],ii],N)
        AhA = A.H @ A

        fk, _, _, _ = infft(X[idx[ii],ii], Y[idx[ii],ii] - mn[ii], N, AhA, w, return_adjoint=False, approx=False)
        Fk[:,ii] = fk.copy()
        
        if verbose == True:
            print(f'infft {ii+1} of {X.shape[1]} complete')

    if verbose == True:
        print('inffts complete')

    U,S,V = svds(Fk,k)

    Fkr = U @ np.diag(S) @ V
    
    res = []

    for ii in range(X.shape[1]):
        Xpred[:,ii] = adjoint(tnom,Fkr[:,ii]) + mn[ii]
        #rslt = ttest_1samp(X[idx[ii],ii],Xpred[idx[ii],ii],axis=0)
        res.append(Y[idx[ii],ii] - Xpred[idx[ii],ii])
        # s = np.std(res)
        # df = 1 #np.sum(idx[ii])
        # tt = np.divide(np.sqrt(df)*res, s)
        # Xpvls[idx[ii],ii] = t.cdf(tt,df)

        if verbose == True:
            print(f'performing adjoint transform {ii+1} out of {X.shape[1]}')
            
    s = np.std(np.concatenate(res))
    
    if verbose == True:
        print("calculating pvals")
    
    for ii in range(X.shape[1]):
        Xpvls[idx[ii],ii] = 1 - chi2.cdf((res[ii]/s) ** 2,1)
            
    return Xpred, Xpvls, Fkr, X
    
def digest_csv(name_of_csv, nan_marker=-9999):
    df = pd.read_csv(name_of_csv)
    Ln = df.shape[0]
    Xr = df.iloc[0:,1:].to_numpy()

    Y = np.zeros_like(Xr)
    Y[:] = np.nan
    X = np.zeros_like(Xr)
    X[:] = np.nan
    tl = np.linspace(-0.5, 0.5, Ln, endpoint=False)

    for ii in range(df.shape[1] - 1):
        idx = Xr[:,ii] != nan_marker

        if sum(idx) % 2 != 0:
            idx = change_last_true_to_false(idx)
        
        X[idx,ii] = tl[idx].copy()
        Y[idx,ii] = Xr[idx,ii]

    return X, Y

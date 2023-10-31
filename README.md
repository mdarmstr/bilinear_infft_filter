# Bilinear interpolative inverse Fourier filter

**Please note this routine is in the alpha testing stage, and functionality - including inputs and outputs, are expected to change (as of: 30/10/2023).
**

Anomaly detection of parallel measurements with anticipated gaps and irregular sampling in the time domain. Patterns in the data are found and reconstructed as frequencies using singular value decomposition, and statistical distances are measured relative to the transformed trigonometric polynomial in the time domain.

For a monotonic increasing time series $x$ of dimensions $M \times 1$, a number of observations sampled at $j \in M$ within an $M \times L$ matrix $Y$ of $L$ parallel observations. Let $f(x_j) \in Y_{j,o}$ be the $o^{th}$ measurement in $Y$ for time series $x$ where $o \in L$. The frequencies $\hat{h}_k$ are reconstructed at $j$ times by minimising the following cost function:

$${argmin}_{\hat{h}_k}||f(x_j) - A^H\hat{h}_k||_W$$

Wihtin a matrix of complex values representing the frequencies for each time series measurement, as $H_k \in N,L$, a reconstruction that is robust against time-domain outliers can be reconstructed via:

$$\hat{H}_k = U \Sigma V^H$$

Where $U$ is an $M \times k$ complex matrix of scores, $\Sigma$ is a real-valued $k \times k$ diagonal matrix, and $V^H$ is the Hermitian transpose of the $L \times k$ loadings. The reconstructed data $\hat{Y}$ is recovered using the adjoint transform, represented algebraically as: $A^H$ for each $\hat{y} \in M,1$ for each $\hat{h}_k \in N,1$.

The _p-values_ are a relative measure of statistical agreement with the interpolated signal function. They are derived from the inverser cumulative distribution function for the $\chi^2$ distribution with one degree of freedom, with the expected value as the interpolative function normalised by the standard deviation calculated for the entire dataset.

## Instructions

There are two main functions, `digest_csv` and `validate_data`. The `plot_results` function offers a basic usage case for the sake of example.

### Inputs for `digest_csv`
- `file.csv` as second-order array of $M$ monotonically increasing time measurements, and $O$ stations. The first column is expected to take the time measurements, and typically the first row of the csv contains the names of the time-series variables.
- `nan_maker` _default=-9999_ as a `int` value indicating what placeholder exists to indicate missing data. 

### Outputs for `digest_csv`
- `X` an $M \times L$ numpy array of $M$ measurements and $L$ time-series variables. Missing data is labelled as `np.nan`.
- `Y` an $M \times L$ numpy array of $M$ time points that correspond to $L$ time-series variables. Missing data is indicated as `np.nan`.

### Inputs for `validate_data`
- `X` from the output of `digest_csv`.
- `Y` from the output of `digest_csv`.
- `k` _default=2_ for the number of components in the SVD model.
- `kernel` _default=`sobolev`_ the type of kernel used in the weighted non-uniform interpolative inverse Fast Fourier transform.
- `verbose` _default=`True`_ controls the terminal output of the model. 

### Outputs for `valdiate_data`
- `Xpred` an $M \times L$ numpy array containing the interpolative function for the $o^{th}$ time-series variable.
- `Xpvls` an $M \times L$ numpy array containing the p-values for the $o^{th}$ time-series variable where the data was originally measured. Missing data is indicated as `np.nan`.
- `Fkr` the reconstructed $N \times L$ complex numpy array containing the calculated frequencies for the $o \in L$ time-series variables.
- `X` the original data from the output. 

# Credit
Michael Sorochan Armstrong (mdarmstr@go.ugr.es) and José Camacho Páez (josecamacho@ugr.es) from the Computational Data Science Lab (CoDaS) at the University of Granada. Please, note that the software is provided "as is" and we do not accept any responsibility or liability. Should you find any bug or have suggestions, please contact the authors. For copyright information, please see the license file.

# Installation instructions
In progress - please see `requirements.txt` for a list of dependencies. Requires use of the `intrp_infft_1d` package at `https://github.com/mdarmstr/intrp_infft_1d`






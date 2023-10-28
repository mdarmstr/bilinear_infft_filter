# Bilinear interpolative inverse Fourier filter

Anomaly detection of parallel measurements with anticipated gaps and irregular sampling in the time domain. Patterns in the data are found and reconstructed as frequencies using singular value decomposition, and statistical distances are measured relative to the transformed trigonometric polynomial in the time domain.

For a monotonic increasing time series $x$ of dimensions $M \times 1$, a number of observations sampled at $j \in M$ within an $M \times L$ matrix $Y$ of $L$ parallel observations. Let $f(x_j) \in Y_{j,o}$ be the $o^{th}$ measurement in $Y$ for time series $x$ where $o \in L$. The frequencies $\hat{h}_k$ are reconstructed at $j$ times by minimising the following cost function:

$${argmin}_{\hat{h}_k}||f(x_j) - A^H\hat{h}_k||_W$$

Wihtin a matrix of complex values representing the frequencies for each time series measurement, as $H_k \in N,L$, a reconstruction that is robust against time-domain outliers can be reconstructed via:

$$\hat{H}_k = U \Sigma V^H$$

Where $U$ is an $M \times k$ complex matrix of scores, $\Sigma$ is a real-valued $k \times k$ diagonal matrix, and $V^H$ is the Hermitian transpose of the $L \times k$ loadings. The reconstructed data $\hat{Y} is recovered using the adjoint 

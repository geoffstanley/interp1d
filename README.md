# interp1d
numba accelerated 1D interpolation over last dimension of nD arrays

This provides functions for fast interpolation (or derivatives) of one (or two)
dependent variables in terms of one independent variable, done serially over 
an arbitrary number of such interpolation problems.

Only the minimum amount of data near the evaluation site is accessed, and the 
interpolant is evaluated immediately.

Currently supports linear and PCHIP interpolation.

To add a new interpolation method, the only functions that need to be added
are those which perform the "kernel" of interpolation, which evaluates a single
1D interpolant at a single value that exists within a known interval of the
independent data. See `linear._linterp` for example. Given this "kernel", all
the machinary to broadcast across multiple interpolation problems is provided.

If many interpolations are going to be performed, a faster approach (but
with a higher memory footprint) is to pre-compute the piecewise polynomial 
coefficients once, and then do many evaluations. That is the approach of 
`ppinterp` in [`neutralocean`](https://github.com/geoffstanley/neutralocean).


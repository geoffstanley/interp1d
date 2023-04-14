"""
Functions for interpolation (or derivatives) of one (or two) dependent variables
in terms of one independent variable, done serially over an arbitrary number of such 
interpolation problems.
Only the minimum amount of data near the evaluation site is accessed, and the 
interpolant is evaluated immediately.
If many interpolations are going to be performed, a faster approach (but
with a higher memory footprint) is to pre-compute the piecewise polynomial 
coefficients once, and then do many evaluations. That is the approach of 
`ppinterp` in `neutralocean`.  [https://github.com/geoffstanley/neutralocean]
"""
from .tools import make_interpolator, make_kernel

"""Kernels for linear interpolation"""
import numba as nb


@nb.njit
def _linterp(x, X, Y, i):
    """
    The "kernel" of linear interpolation.

    Parameters
    ----------
    x : float
        The evaluation site

    X : ndarray(float, 1d)
        The independent data.

    Y : ndarray(float, 1d)
        The dependent data.

    i : int
        The interval of `X` that contains `x`. Specifically,
            (a) `i == 1`  and  `X[0] <= x <= X[1]`, or
            (b) `2 <= i <= len(X) - 1` and `X[i-1] < x <= X[i]`.

        These facts about `i` are assumed true; they are not checked.
        (This function will not be called if `x < X[0]` or `X[-1] < x` or
        `x` is nan or `X` are all nan.)

    Returns
    -------
    y : float
        The value of `Y` linearly interpolated to `X` at `x`.

    """

    # dx = (x - X[i-1]) => 0 guaranteed (and == 0 only if x == X[0])
    return (Y[i] - Y[i - 1]) / (X[i] - X[i - 1]) * (x - X[i - 1]) + Y[i - 1]


@nb.njit
def _linterp1(x, X, Y, i):
    """
    The "kernel" of the 1st derivative of linear interpolation.

    Inputs and outputs analogous to `_linterp`.
    """

    return (Y[i] - Y[i - 1]) / (X[i] - X[i - 1])
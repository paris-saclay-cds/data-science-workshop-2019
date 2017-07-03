import numpy as np

from numpy.testing import assert_allclose

from spectra_analysis.regression import fit_params
from spectra_analysis.regression import transform


def test_fit_params():
    X = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1],
                  [2, 2, 2]])

    median, variance = fit_params(X)
    assert_allclose(median, 1.)
    assert_allclose(variance, 0.75)
    assert_allclose(variance,
                    np.percentile(X, 75, axis=0) -
                    np.percentile(X, 25, axis=0))


def test_transform():
    X = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1],
                  [2, 2, 2]])

    median, variance = fit_params(X)
    X_true = np.array([[-1.33333333, -1.33333333, -1.33333333],
                       [-1.33333333, -1.33333333, -1.33333333],
                       [0., 0., 0.],
                       [0., 0., 0.],
                       [0., 0., 0.],
                       [1.33333333, 1.33333333, 1.33333333]])
    assert_allclose(X_true, transform(X, median, variance))

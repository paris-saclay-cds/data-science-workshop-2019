from os.path import dirname, join
import numpy as np
import pandas as pd
from numpy.testing import (assert_allclose, assert_array_equal,
                           assert_raises_regex)
from pandas.testing import assert_frame_equal
from spectra_analysis.preprocessing import read_spectra


def test_read_spectra_error():
    assert_raises_regex(TypeError, "'path_csv' needs to be string.",
                        read_spectra, 1)
    assert_raises_regex(ValueError, "Wrong file format. Expecting csv file",
                        read_spectra, 'file.rnd')


def test_read_spectra():
    module_path = dirname(__file__)
    spectra, concentration, molecule = read_spectra(join(module_path,
                                                         'data', 'data.csv'))
    assert_frame_equal(spectra, pd.DataFrame(np.array([[0.0, 1.0, 2.0],
                                                       [0.0, 2.0, 4.0]])))
    assert_array_equal(concentration, np.array([8000, 500]))
    assert_array_equal(molecule, np.array(['Q', 'B']))

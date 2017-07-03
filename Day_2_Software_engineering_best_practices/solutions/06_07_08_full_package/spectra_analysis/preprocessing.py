# -*- coding: utf-8 -*-
"""
Spectra analysis preprocessing utilities


"""
import six
import pandas as pd
import numpy as np


def read_spectra(path_csv):
    """Read and parse data in pandas DataFrames.

    Parameters
    ----------
    path_csv : str
        Path to the CSV file to read.

    Returns
    -------
    spectra : pandas DataFrame, shape (n_spectra, n_freq_point)
        DataFrame containing all Raman spectra.

    concentration : pandas Series, shape (n_spectra,)
        Series containing the concentration of the molecule.

    molecule : pandas Series, shape (n_spectra,)
        Series containing the type of chemotherapeutic agent.

    """
    if not isinstance(path_csv, six.string_types):
        raise TypeError("'path_csv' needs to be string. Got {}"
                        " instead.".format(type(path_csv)))
    else:
        if not path_csv.endswith('.csv'):
            raise ValueError('Wrong file format. Expecting csv file')

    data = pd.read_csv(path_csv)
    concentration = data['concentration']
    molecule = data['molecule']
    spectra_string = data['spectra']
    spectra = []
    for spec in spectra_string:
        # remove the first and last bracket and convert to a numpy array
        spectra.append(np.fromstring(spec[1:-1], sep=','))
    spectra = pd.DataFrame(spectra)

    return spectra, concentration, molecule

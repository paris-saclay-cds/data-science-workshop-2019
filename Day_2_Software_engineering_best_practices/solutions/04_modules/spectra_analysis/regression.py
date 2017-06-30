# -*- coding: utf-8 -*-
"""
Spectra analysis utilities for regression


"""

import numpy as np

from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import RidgeCV
from sklearn.pipeline import make_pipeline

from .plotting import plot_regression
    

def regression_experiment(X_train, X_test, y_train, y_test):
    """Perform regression experiment.
    
    Build a pipeline using PCA and either a Ridge
    or a RandomForestRegressor model.
    
    Parameters
    ----------
    X_train : pandas DataFrame, shape (n_spectra, n_freq_points)
        DataFrame containing training Raman spectra.
        
    X_test : pandas DataFrame, shape (n_spectra, n_freq_points)
        DataFrame containing testing Raman spectra.
        
    y_training : pandas Serie, shape (n_spectra,)
        Serie containing the training concentrations acting as targets.
        
    y_testing : pandas Serie, shape (n_spectra,)
        Serie containing the testing concentrations acting as targets.
        
    Returns
    -------
    None
    
    """
    for reg in [RidgeCV(), RandomForestRegressor(random_state=0)]:
        pipeline = make_pipeline(PCA(n_components=100), reg)
        y_pred = pipeline.fit(X_train, y_train).predict(X_test)
        plot_regression(y_test, y_pred,
                        'Regression using {}'.format(reg.__class__.__name__))
    
    
def fit_params(data):
    """Compute statistics for robustly scale data.
    
    Compute the median and the variance, i.e. the difference
    between the 75th and 25th percentiles.
    These statistics are used later to scale data.
    
    Parameters
    ----------
    data : pandas DataFrame, shape (n_spectra, n_freq_point)
        DataFrame containing all Raman spectra.
        
    Returns
    -------
    median : ndarray, shape (n_freq_point,)
        Median for each wavelength.
        
    variance : ndarray, shape (n_freq_point,)
        Variance (difference between the 75th and 25th
        percentiles) for each wavelength.
    
    """
    median = np.median(data, axis=0)
    percentile_25 = np.percentile(data, 25, axis=0)
    percentile_75 = np.percentile(data, 75, axis=0)
    return median, (percentile_75 - percentile_25)

    
def transform(data, median, var_25_75):
    """Scale data using robust estimators.
    
    Scale the data by subtracting the median and dividing by the
    variance, i.e. the difference between the 75th and 25th percentiles.
    
    Parameters
    ----------
    data : pandas DataFrame, shape (n_spectra, n_freq_point)
        DataFrame containing all Raman spectra.
        
    median : ndarray, shape (n_freq_point,)
        Median for each wavelength.
        
    var_25_75 : ndarray, shape (n_freq_point,)
        Variance (difference between the 75th and 25th
        percentiles) for each wavelength.
    
    Returns
    -------
    data_scaled : pandas DataFrame, shape (n_spectra, n_freq_point)
        DataFrame containing all scaled Raman spectra.
    
    """
    return (data - median) / var_25_75

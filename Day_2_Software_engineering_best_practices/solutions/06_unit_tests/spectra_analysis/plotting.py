# -*- coding: utf-8 -*-
"""
Spectra analysis plotting utilities


"""

import itertools

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, median_absolute_error


def _apply_axis_layout(ax, title):
    """Apply despine style and add labels to axis."""
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Concentration')
    ax.set_title(title)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.spines['left'].set_position(('outward', 10))
    ax.spines['bottom'].set_position(('outward', 10))

    
def plot_spectra(frequency, spectra, title):
    """Plot a bunch of Raman spectra.
    
    Parameters
    ----------
    frequency : pandas Series, shape (n_freq_points,)
        Frequencies for which the Raman spectra were acquired.
        
    spectra : pandas DataFrame, shape (n_spectra, n_freq_points)
        DataFrame containing all Raman spectra.
        
    title : str
        Title added to the plot.
    
    Returns
    -------
    None
    
    """
    fig, ax = plt.subplots()
    ax.plot(frequency, spectra.T)
    _apply_axis_layout(ax, title)
    
    
def plot_spectra_by_type(frequency, spectra, classes, title):
    """Plot mean spectrum with its variance for a given class.
    
    Parameters
    ----------
    frequency : pandas Series, shape (n_freq_points,)
        Frequencies for which the Raman spectra were acquired.
        
    spectra : pandas DataFrame, shape (n_spectra, n_freq_points)
        DataFrame containing all Raman spectra.
        
    classes : array-like, shape (n_classes,)
        Array contining the different spectra class which will be plotted.
        
    title : str
        Title added to the plot.
        
    Returns
    -------
    None
    
    """
    fig, ax = plt.subplots()
    for label in np.unique(classes):
        label_index = np.flatnonzero(classes == label)
        spectra_mean = np.mean(spectra.iloc[label_index], axis=0)
        spectra_std = np.std(spectra.iloc[label_index], axis=0)
        ax.plot(frequency, spectra_mean, label=label)
        ax.fill_between(frequency,
                        spectra_mean + spectra_std,
                        spectra_mean - spectra_std,
                        alpha=0.2)
    _apply_axis_layout(ax, title)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    

def plot_cm(cm, classes, title):
    """Plot a confusion matrix.
    
    Parameters
    ----------
    cm : ndarray, shape (n_classes, n_classes)
        Confusion matrix.
        
    classes : array-like, shape (n_classes,)
        Array contining the different spectra classes used in the
        classification problem.
        
    title : str
        Title added to the plot.
        
    Returns
    -------
    None
    
    """
    fig, ax = plt.subplots()
    plt.imshow(cm, interpolation='nearest', cmap='bwr')
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

    
def plot_regression(y_true, y_pred, title):
    """Plot actual vs. predicted scatter plot.
    
    Parameters
    ----------
    y_true : array-like, shape (n_samples,)
        Ground truth (correct) target values.

    y_pred : array-like, shape (n_samples,)
        Estimated targets as returned by a regressor.

    title : str
        Title added to the plot.
    
    Returns
    -------
    None
    
    """    
    fig, ax = plt.subplots()
    ax.scatter(y_true, y_pred)
    ax.plot([0, 25000], [0, 25000], '--k')
    ax.set_ylabel('Target predicted')
    ax.set_xlabel('True Target')
    ax.set_title(title)
    ax.text(1000, 20000, r'$R^2$=%.2f, MAE=%.2f' % (
       r2_score(y_true, y_pred), median_absolute_error(y_true, y_pred)))
    ax.set_xlim([0, 25000])
    ax.set_ylim([0, 25000])

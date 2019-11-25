# 2-Day Workshop - Introduction to Data Science in Python

Materials for the Paris-Saclay Center for Data Science python workshop

Data science is gaining attention impacting many scientific fields and applications. Data science encompasses a large number of topics such as data mining, data wrangling, data visualisation, pattern recognition, or machine learning.

This workshop intends to give an introduction to some of these topics using Python and the PyData ecosystem. It is not a course on deep learning.

*Note: the material in this repo is WIP, not the finalized material.*

## Program

### Day 1 -  Data wrangling, exploration, and visualisation

**Goal:** introduce the PyData ecosystem to manipulate, explore, and visualize data.

* Introduction to the basics of numpy, pandas, and matplotlib.

### Day 2 - Machine learning

**Goal:** introduce the basics of machine learning using the  scikit-learn library.

* Get familiar with general principles of machine learning;
* Use these principles by using the scikit-learn library on some toy and real-world data examples.


## Getting started

The course uses Python 3 and some data analysis packages such as Numpy, Pandas, Matplotlib and scikit-learn. To install the required libraries, we highly recommend Anaconda or miniconda (<https://www.anaconda.com/download/>) or another Python distribution that includes the scientific libraries (this recommendation applies to all platforms, so for both Window, Linux and Mac).

### Install Anaconda

For first time users and people not fully confident with using the command line, we advice to install Anaconda, by downloading and installing the Python 3.x version from <https://www.anaconda.com/download/>. Recent computers will require the 64-Bit installer.

For more detailed instructions to install Anaconda, check the [Windows](https://docs.anaconda.com/anaconda/install/windows/), [Mac](https://docs.anaconda.com/anaconda/install/mac-os/) or [linux](https://docs.anaconda.com/anaconda/install/linux/) installation tutorial.

**Note:** When you are already familiar to the command line and Python environments you could opt to use Miniconda instead of Anaconda and download it  from <https://conda.io/miniconda.html>. The main difference is that Anaconda provides a graphical user interface (Anaconda navigator) and a whole lot of scientific packages (e.g <https://docs.anaconda.com/anaconda/packages/py3.6_win-64/>) when installing, whereas for Miniconda the user needs to install all packages using the command line. On the other hand, Miniconda requires less disc space. By choosing Miniconda, create the workshop environment using the `environment.yml` file: `conda env create -f environment.yml`

### Install/check of required packages

This tutorial will require recent installations of

- [NumPy](http://www.numpy.org)
- [SciPy](http://www.scipy.org)
- [matplotlib](http://matplotlib.org)
- [pandas](http://pandas.pydata.org)
- [pillow](https://python-pillow.org)
- [scikit-learn](http://scikit-learn.org/stable/)
- [seaborn](http://seaborn.pydata.org/)
- [IPython](http://ipython.readthedocs.org/en/stable/)
- [Jupyter notebook](http://jupyter.org)


The last one is important and you should be able to type:

```bash
jupyter notebook
```

in your terminal window and see the notebook panel load in your web browser. Try opening and running a notebook from the material to see check that it works. Alternatively you can use Jupyter notebook.

After obtaining the material, we **strongly recommend** you to open and execute the script using `python check_env.py` that is located at the top level of this repository.

We also recommend you to update the scikit-learn the latest release version to ensure best compatibility with the teaching material. Please upgrade already installed packages by executing

```bash
conda update [package-name]
```

Depending on how you installed ``scikit-learn``.


<img src="img/logoUPSayPlusCDS_990.png"/>

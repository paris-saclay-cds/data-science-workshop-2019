# Day 2 - Software engineering best practices for scientists

### 1. Overview of the initial analysis notebook

[exercise/00_initial_script.ipynb](exercise/00_initial_script.ipynb)

### 2. Code style and documentation

[Slides](https://paris-saclay-cds.github.io/python-workshop/Day_2_Software_engineering_best_practices/02_documentation_code_style_slides.html)

**Exercise** Improve the code style of the notebook (you don't need to do the full notebook). Among other things, check for:

- Consistent imports?
- clear variable names?
- PEP8 (whitespace, code layout, maximum line length, ...)

### 3. Reusing code: functions

Notebook about functions: [03_functions.ipynb](03_functions.ipynb)

**Exercise** For those parts of the notebook that are repetitive, refactor this
code into a function and use this function multiple times. For each of the
functions created, add a docstring with: (i) a short description, (ii) a long
description (sometimes optional), (iii) a *Parameters* and *Returns* sections
documenting the input and output parameters.

Eight functions can be created and are listed below. Due to time constraint,
you might want to focus first on the following functions: 1, 2, 3, 4, 7, and 8.

1. Create a function named `read_spectra` which accepts `path_csv` which is the
   path to a csv file and returns `spectra`, `concentration`, and `molecule`
   which are a Dataframe containing the Raman spectra, a Series containing the
   concentration of the molecule, and a Series containing the type of
   chemotherapeutic agent, respectively.
2. Create a function `plot_spectra` which accepts `frequency` and `spectra`
   which need to be plotted. The purpose of this function is to plot a bunch of
   Raman spectra on the same figure.
3. Create a function `plot_spectra_by_type` whith the same parameters as the
   above function. In addition, the `classes` parameters need to be passed to
   group the spectra by category before to compute the mean and standard
   deviation.
4. The two previous `plot_*` functions apply a similar layout style. Create a
   "private" function `_apply_axis_layout` which accepts `ax` and `title` which
   are the matplotlib axis and the title of the plot, respectively. The purpose
   of this function is to add labels and title to the axis and remove the top
   and right border of the axis. Then, you can call this function in the
  `plot_*` functions.
5. Create a function `plot_cm` which takes, `cm`, `classes`, and `title` which
   are the confusion matrix, the classes used in the classification problem, and
   the title of the plot, respectively.
6. Create a function `plot_regression` which takes `y_true`, `y_pred`, and
   `title` which are the true concentration, the predicted concentration, and
   the title to add to the axis, respectively.
7. Create a function `fit_params` which takes `data`, a DataFrame with the Raman
   spectra and return the median and the difference between the 75th percentile
   and the 25th percentile.
8. Create a function `transform` which takes `data`, `median`, and `var_25_75`
   and return the scaled data.

The solutions for this is exercise can be
found [there](solutions/03_code_style.ipynb)

### 4. Reusing code: modules and packages

Notebook: [04_reusing_code_modules.ipynb](04_reusing_code_modules.ipynb)

**Exercise: create a module**

- Open your favorite text editor (with python syntax support). If you don't have a favorite one, a suggestion is to use [Spyder](https://github.com/spyder-ide/spyder), which comes preinstalled with Anaconda
- Move the functions you have written in the previous exercise in the notebook to a stand-alone python file, e.g. `spectra_analysis.py`, located next to the notebook. Import the functions from that file instead of defining them inside the notebook itself (`from spectra_analysis import ...`)

**Synchronization** Before to start the exercise, use the notebook in
[solutions/03_code_style.ipynb](solutions/03_code_style.ipynb). Copy the
notebook in the directory `exercise` to use it now on.

**Exercise: create a package**
- Make a small python package by creating a directory called `spectra_analysis` that contains an empty file named `__init__.py`
- Move the python module inside this directory, and organize the different functions by putting them in different files (e.g. `preprocessing.py`, `plotting.py`, `regression.py`)


### 5. Version control with git

[Slides](https://paris-saclay-cds.github.io/python-workshop/Day_2_Software_engineering_best_practices/05_documentation_git.html)

**Exercise:**

- Install and configure `git`.
- Make the `spectra_analysis` directory into a `git` repository. Refer to the
  slides for the detailed instructions.

### 6. Unit testing

theory notebook with exercises
https://paris-swc.github.io/python-testing-debugging-profiling/

Notebook: [06_unit_testing.ipynb](06_unit_testing.ipynb)

**Exercise**:

- Create a folder `tests` in the directory `spectra_analysis` directory. It
  will contain all the different tests which ensure that our package is robust
  and that nobody will be able to break it.
- Add a file `__init__.py` in `tests` such it is consider as a module.
- Create a file `test_preprocessing.py`. In this file, create two functions:
  - `test_read_spectra_error()` to ensure that the proper error will be raised.
  - `test_read_spectra()` to check that on a toy file, the function is giving
    the expected results.
- Create a file `test_regression.py`. Create two tests function:
  - `test_fit_params` in which we check the right behavior of the function
    `fit_params` with toy data.
  - `test_transform` in which we check the right behavior of the function
    `fit_params` with toy data.
- You can run the tests by running `$ pytest spectral_analysis`.
- Finally, add and commit all those files.

### 7. Redistributable package

Some theory:

- local
- sys.path
- setup.py

**Exercise:**

* make package with setup.py

### 8. GitHub / travis


**Exercise:**

- Before to start this section, you will need to create an account on GitHub by
  clicking [here](https://github.com/join)
- Create you first repository. A guideline can be
  found
  [here](https://help.github.com/articles/creating-a-new-repository/). **Note:
  Create a complete empty repository without initialiazing with any License,
  .gitignore, or README**.
- Follow the instruction in "…or push an existing repository from the command
  line" to add and push your repository.

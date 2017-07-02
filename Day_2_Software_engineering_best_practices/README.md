# Day 2 - Software engineering best practices for scientists

### 1. Overview of the initial analysis notebook

[exercise/00_initial_script.ipynb](exercise/00_initial_script.ipynb)

TODO: put intro from ramp

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

- Create a function named `read_spectra` which accepts `path_csv` which is the
  path to a csv file and returns `spectra`, `concentration`, and `molecule`
  which are a Dataframe containing the Raman spectra, a Series containing the
  concentration of the molecule, and a Series containing the type of
  chemotherapeutic agent, respectively.
- Create a "private" function `_apply_axis_layout` which accepts `ax` and
  `title` which are the matplotlib axis and the title of the plot,
  respectively. The purpose of this function is to add labels and title to the
  axis and remove the top and right border of the axis.
- Create a function `plot_spectra` which accepts `frequency` and `spectra`
  which need to be plotted. In addition, you can pass `title` which will be
  passed to the `_apply_axis_layout` internally to setup the layout of the
  plot. The purpose of this function is to plot a bunch of Raman spectra on the
  same figure.
- Create a function `plot_spectra_by_type` whith the same parameters as the
  above function. In addition, the `classes` parameters need to be passed to
  group the spectra by category before to compute the mean and standard
  deviation.
- Create a function `plot_cm` which takes, `cm`, `classes`, and `title` which
  are the confusion matrix, the classes used in the classification problem, and
  the title of the plot, respectively.
- Create a function `plot_regression` which takes `y_true`, `y_pred`, and
  `title` which are the true concentration, the predicted concentration, and
  the title to add to the axis, respectively.
- Create a function `fit_params` which takes `data`, a DataFrame with the Raman
  spectra and return the median and the difference between the 75th percentile
  and the 25th percentile.
- Create a function `transform` which takes `data`, `median`, and `var_25_75`
  and return the scaled data.


### 4. Reusing code: modules and packages

Notebook: [04_reusing_code_modules.ipynb](04_reusing_code_modules.ipynb)

**Exercise: create a module**

- Open your favorite text editor (with python syntax support). If you don't have a favorite one, a suggestion is to use [Spyder](https://github.com/spyder-ide/spyder), which comes preinstalled with Anaconda
- Move the functions you have written in the previous exercise in the notebook to a stand-alone python file, e.g. `spectra_analysis.py`, located next to the notebook. Import the functions from that file instead of defining them inside the notebook itself (`from spectra_analysis import ...`)

**Exercise: create a package**

- Make a small python package by creating a directory called `spectra_analysis` that contains an empty file named `__init__.py`
- Move the python module inside this directory, and organize the different functions by putting them in different files (e.g. `preprocessing.py`, `plotting.py`, `regression.py`)


### 5. Version control with git

theory
- why version control
- concepts of git: repo, commits = you do changes and then you say: let's save this state = commit (snapshot), history of commits,
- installation how-to if needed


Exercise: (live example by instructor)
- configure git
- make the spectra_analysis dir into a git repo
  git init
- add a readme, add a gitignore and commit
- add the python file

(init, status, log, add commit )


### 6. Unit testing

theory notebook with exercises
https://paris-swc.github.io/python-testing-debugging-profiling/


**Exercise**:

- add a test direcotry, add test_processing.py
- write a test for .... (test with csv file) -> specific steps to do
- running the tests
- add with git to repo

Write unit tests for the functions in `spectra_analysis.py`, and add those tests to the git repo.

- Make a new file `test_spectra_analysis.py`
- Write a test for ... function
- Run the tests using `pytest`


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

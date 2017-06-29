# Day 2 - Software engineering best practices for scientists

### 1. Overview of the initial analysis notebook

[exercise/00_initial_script.ipynb](exercise/00_initial_script.ipynb)

TODO: put intro from ramp

### 2. Code style and documentation

[Slides](https://paris-saclay-cds.github.io/python-workshop/Day_2_Software_engineering_best_practices/02_documentation_code_style_slides.html)

**Exercise** Improve the code style of the notebook (you don't need to do the full notebook)

- Consistent imports?
- clear variable names?
- PEP8 (whitespace, code layout, maximum line length, ...)

### 3. Reusing code: functions

Notebook about functions: [03_functions.ipynb](03_functions.ipynb)

 **Exercise** For those parts of the notebook that are repetitive, refactor
 this code into a function and use this function multiple times.

 - Create functions `alabl` to ...
    which accepts ... and returns ...
 - Create ...

 - Make sure to add docstrings to all functions. Parameters section, return section, ....

specific instructions!


### 4. Reusing code: modules and packages

Some theory -> use notebook (first function) as example -> move to separate file

http://www.scipy-lectures.org/intro/language/reusing_code.html


**Exercise:**

- Move the functions to a stand-alone python file, `spectra_analysis.py`, located next to the notebook. Import the functions from that file instead of defining them inside the notebook itself

Some theory: move python files into directory: package __init__.py

**Exercise:**

- make a package by moving to spectra_analysis dir + reorganize

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

- crate user acocunt
- make repo (empty)
- add existing repo -> add remote to existing repo
- push
- pull requests (only explain, if time do example)

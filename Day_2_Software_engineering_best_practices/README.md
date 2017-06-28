# Day 2 - Software engineering best practices for scientists

1. Overview of the initial analysis notebook

   [00_initial_script.ipynb](00_initial_script.ipynb)

TODO: put intro from ramp

2. Code style and documentation

   [Slides](https://paris-saclay-cds.github.io/python-workshop/Day_2_Software_engineering_best_practices/slides_documentation_code_style.html)

   **Exercise** Improve the code style of the notebook (you don't need to do the full notebook)

        - Consistent imports?
        - clear variable names?
        - PEP8 (whitespace, code layout, maximum line length, ...)

3. Reusable functionality

   Notebook about functions

   **Exercise** For those parts of the notebook that are repetitive, refactor
   this code into a function and use this function multiple times.

   - Create functions `alabl` to ...
      which accepts ... and returns ...
   - Create ...

   - Make sure to add docstrings to all functions. Parameters section, return section, ....

specific instructions!


4. Modular thing
   theory -> use notebook (first function) as example
   -> package __init__.py

   split

  Exercise:

  - Move the functions to a stand-alone python file, `spectra_analysis.py`, located next to the notebook. Import the functions from that file instead of defining them inside the notebook itself

  some theory

  Exercise:
  - make a package by moving to spectra_analysis dir + reorganize

5. Version control with git

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


6. Unit testing

  theory notebook with exercises

  **Exercise**:

  - add a test direcotry, add test_processing.py
  - write a test for .... (test with csv file) -> specific steps to do
  - running the tests
  - add with git to repo

7. Redistributable package

  local
  sys.path
  setup.py

  Exercise:
  * make package with setup.py

8. GitHub / travis

  - make repo
  - push




5. Make a git repository, and add the `spectra_analysis.py` file to this.

6. Write unit tests for the functions in `spectra_analysis.py`, and add those tests to the git repo.

    - Make a new file `test_spectra_analysis.py`
    - Write a test for ... function
    - Run the tests using `pytest`

7. Make this into a package

8. Put this on github + run tests on travis

# Day 2 - Software engineering best practices for scientists

1. Improve the code style of the notebook (you don't need to do the full notebook)

    - Consistent imports?
    - clear variable names?
    - PEP8 (whitespace, ..)

2. For those parts of the notebook that are repetitive, refactor this code into a function and use this function multiple times.

3. Add docstrings for the functions

4. Move the functions to a stand-alone python file, `spectra_analysis.py`, located next to the notebook. Import the functions from that file instead of defining them inside the notebook itself

5. Make a git repository, and add the `spectra_analysis.py` file to this.

6. Write unit tests for the functions in `spectra_analysis.py`, and add those tests to the git repo.

    - Make a new file `test_spectra_analysis.py`
    - Write a test function
    - Run the tests using `pytest`
    
7. Make this into a package

8. Put this on github + run tests on travis

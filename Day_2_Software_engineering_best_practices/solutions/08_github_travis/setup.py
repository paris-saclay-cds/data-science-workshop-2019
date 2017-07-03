from os.path import join
from setuptools import setup, find_packages
from spectra_analysis import __version__
PACKAGES = find_packages()

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "Spectra Analysis: a CDS template for python package"
# Long description will go up on the pypi page
long_description = """

Spectra Analysis
================
Is is a toy example to learn how to make a python package.
"""

NAME = "spectra_analysis"
MAINTAINER = "Center for Data Science"
MAINTAINER_EMAIL = "cdsupsay@gmail.com"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/paris-saclay-cds/python-workshop"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "Center for Data Science"
AUTHOR_EMAIL = "cdsupsay@gmail.com"
PLATFORMS = "OS Independent"
VERSION = __version__
PACKAGE_DATA = {'spectra_analysis': [join('tests', 'data', '*')]}
REQUIRES = ["numpy", "pandas", "scipy", 'scikit-learn', "matplotlib", "six"]

opts = dict(name=NAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            long_description=LONG_DESCRIPTION,
            url=URL,
            download_url=DOWNLOAD_URL,
            license=LICENSE,
            classifiers=CLASSIFIERS,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            platforms=PLATFORMS,
            version=VERSION,
            packages=PACKAGES,
            package_data=PACKAGE_DATA,
            install_requires=REQUIRES)


if __name__ == '__main__':
    setup(**opts)

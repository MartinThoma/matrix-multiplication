from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("library_numpy.pyx", compiler_directives={'language_level' : "3"})
)
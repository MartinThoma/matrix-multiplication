from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("ijk_multiplication_c.pyx", compiler_directives={'language_level' : "3"})
)
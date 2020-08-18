from Cython.Build import cythonize
from setuptools import setup

setup(
    ext_modules=cythonize(
        "library_numpy.pyx", compiler_directives={"language_level": "3"}
    )
)

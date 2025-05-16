from setuptools import setup
from Cython.Build import cythonize



setup(
    ext_modules = cythonize(
        [ "hello.pyx" ]
    )
)

'''
To build the following code use the below command (Linux/MacOS)
         python setup.py build_ext --inplace


python setup.py: Executes the setup.py script.
build_ext: Tells setuptools to build extensions.
--inplace: Tells setuptools to put the compiled .so (Linux/macOS) or .pyd (Windows) file in the same directory as your source files.
'''
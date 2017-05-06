[![Travis](https://travis-ci.org/gatagat/lapjv1.svg?branch=master)](https://travis-ci.org/gatagat/lapjv1/)
[![Appveyor](https://ci.appveyor.com/api/projects/status/github/gatagat/lapjv1?branch=master&svg=true)](https://ci.appveyor.com/project/gatagat/lapjv1/history)
![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)
![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)

python-lapjv1 - Python wrapper of lapjv1
======================================

lapjv1 is an algorithm by Jonker and Volgenant [1] to solve the linear
assignment problem. This repository contains the code by Jonker
(lapjv1/internal) and a Python wrapper (lapjv1).

[1] R. Jonker and A. Volgenant (University of Amsterdam)
"A Shortest Augmenting Path Algorithm for Dense and Sparse Linear Assignment
 Problems", Computing 38, 325-340 (1987)


License
-------

BSD license applies only to the wrapper, the original code cannot be used
commercially, see [lapjv1/internal/README.md](./lapjv1/internal/README.md).


Installation
------------

#### Dependencies

Python-lapjv1 requires:

  * Python (2.7, 3.5, 3.6)
  * NumPy (>=1.10.1)
  * Cython (>=0.21) - to compile the wrapper

#### Using pip

    pip install git+git://github.com/gatagat/lapjv1.git

#### Install from source

  1. Clone

         git clone https://github.com/gatagat/lapjv1.git

  2. Under the root of the repo

         python setup.py build
         python setup.py install

Tested under Linux, OS X, Windows.

Tomas Kazmar, 2012-2017

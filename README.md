python-lapjv1 - Python wrapper of lapjv1
======================================

NOTE: this is a simple fork of [this project](https://github.com/gatagat/lapjv1.git) because of a naming conflict with [this project](https://github.com/src-d/lapjv).

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

    pip install git+git://github.com/dribnet/lapjv1.git

#### Install from source

  1. Clone

         git clone https://github.com/dribnet/lapjv1.git

  2. Under the root of the repo

         python setup.py build
         python setup.py install

Tested under Linux, OS X, Windows.

Tomas Kazmar, 2012-2017

# This file is part of QNET.
#
#    QNET is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#    QNET is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with QNET.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2012-2017, QNET authors (see AUTHORS file)
#
###########################################################################
"""The :mod:`qnet` package exposes all of QNET's functionality for easy
interactive or programmative use.

Specifically, the subpackages for the following parts of QNET are directly
available:

    * Symbolic quantum and circuit algebra as :mod:`qnet.algebra`
    * Printers for symbolic symbolic expressions as :mod:`qnet.printing`
    * A library of circuit components as :mod:`qnet.cc <qnet.circuit_components>`
      (as a shorthand for the :mod:`~qnet.circuit_components` subpackage)
    * Conversion utilities to Sympy and Numpy as :mod:`qnet.convert`
    * Parsing utilities for the QHDL language, as :mod:`qnet.qhdl`
    * Miscellaneous additional tools, as :mod:`qnet.misc`

For interactive usage, the package should be initialized as follows::

    >>> import qnet
    >>> qnet.init_printing()

Note that most subpackages in turn expose their functionality through a "flat"
API. That is, instead of

.. code-block:: python

    from qnet.algebra.operator_algebra import LocalOperator
    from qnet.circuit_components.displace_cc import Displace

the two objects may be more succintly imported from a higher level namespace as

.. code-block:: python

    import qnet  # required for qnet.cc to work
    from qnet.algebra import LocalOperator
    from qnet.cc import Displace

In an interactive context (and only there!), a star import such as

.. code-block:: python

    from qnet.algebra import *

may be useful.

The flat API is defined via the `__all__ <https://docs.python.org/3.5/tutorial/modules.html#importing-from-a-package>`_
attribute of each subpackage (see each package's documentation).

Internally, the flat API (or star imports) must never be used.
"""

import qnet.algebra
import qnet.circuit_components as cc
import qnet.convert
import qnet.misc
import qnet.printing
import qnet.qhdl

from .printing import init_printing

__all__ = ['init_printing']

__version__ = "1.4.3"

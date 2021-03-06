#This file is part of QNET.
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
"""
Component definition file for a coherent field Phasement component.
See documentation of :py:class:`Phase`.
"""
from sympy.core.symbol import symbols
from sympy import exp, I

from qnet.circuit_components.component import Component
from qnet.algebra.circuit_algebra import SLH
from qnet.algebra.matrix_algebra import Matrix


__all__ = ["Phase"]


class Phase(Component):
    r"""Coherent phase shift of the field passing through by real angle
    :math:`\phi`."""

    CDIM = 1

    phi = symbols('phi', real = True)    # Phase angle
    _parameters = ['phi']

    PORTSIN = ["In1"]
    PORTSOUT = ["Out1"]

    def _toSLH(self):

        S = Matrix([[exp(I * self.phi)]])
        L = Matrix([[0]])
        H = 0
        return SLH(S, L, H)

    def _toABCD(self, linearize):
        return self.toSLH().toABCD(linearize)

    def _creduce(self):
        return self

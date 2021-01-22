# --------------------------------------------------------------------------------------
# Copyright 2020 by Oculy Authors, see git history for more details.
#
# Distributed under the terms of the BSD license.
#
# The full license is in the file LICENCE, distributed with this software.
# --------------------------------------------------------------------------------------
"""
"""
from atom.api import Atom, Str, Subclass
from enaml.core.api import Declarative, d_, dfunc


class BasePlot(Atom):
    """"""

    pass


# declarative part for a plot
class Plot:

    #:
    id = d_(Str())

    #:
    @dfunc
    def get_cls(self) -> BasePlot:
        pass

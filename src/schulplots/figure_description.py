from dataclasses import dataclass, field


try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

from .saxes import SAxes
from .sgraph import SGraph, FillBetween
from .lines import VLine, VSpan
from .types import Size
from .sfigure import SFigure
@dataclass
class AxesWithGraphs:
    axes: SAxes
    graphs: list[SGraph] = field(default_factory=list)
    areas: list[FillBetween] = field(default_factory=list)
    vlines: list[VLine] = field(default_factory=list)
    vspans: list[VSpan] = field(default_factory=list)
    left: Size = 0
    bottom: Size = 0
    templates: dict = field(default_factory=dict)
    
    def setup(self):
        for g in self.graphs:
            g.set_saxes(self.axes)
        for a in self.areas:
            a.set_saxes(self.axes)
        for a in self.vlines:
            a.set_saxes(self.axes)
        for a in self.vspans:
            a.set_saxes(self.axes)

@dataclass
class FigureDescription:
    figure: SFigure
    axes_descriptors: list[AxesWithGraphs]
    
    def create_figure(self):
        with self.figure:
            self.figure.set_figure()
            for ax in self.axes_descriptors:
                self.figure.add_axes(ax.axes, left=ax.left, bottom=ax.bottom)
                ax.setup()    

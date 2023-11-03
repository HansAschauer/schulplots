from dataclasses import dataclass, field
from typing import Optional, Any
import numpy as np

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

from .saxes import SAxes
    
@dataclass
class VLineModel:
    x: float = np.inf
    x_var: str = ""
    y_min: float = 0
    y_max: float = 1
    plot_args: dict[str, Any] = field(default_factory=lambda: dict(alpha=0.5))

class VLine(VLineModel):
    _saxes: Optional[SAxes]
    def __init__(self, saxes: SAxes, *args, **kwargs):
        self.set_saxes(saxes)
        #print("XXX", args, kwargs)
        super().__init__(*args, **kwargs)
        #print("YYYY")
    def set_saxes(self, saxes: SAxes):
        self._saxes = saxes
        if self.x != np.inf:
            x = self.x
        else: 
            return
        if self.x_var:
            x = eval(self.x_var, {}, self._saxes.axes_variables)
        self._saxes.axes.axvline(x=x,ymin=self.y_min, ymax=self.y_max, 
                                 **self.plot_args)
@dataclass
class VSpanModel:
    x0: float = 0
    x1: float = 0
    x0_var: str = ""
    x1_var: str = ""
    y_min: float = 0
    y_max: float = 1
    plot_args: dict[str, Any] = field(default_factory=lambda: dict(alpha=0.3, lw=0))

class VSpan(VSpanModel):
    _saxes: Optional[SAxes]
    def __init__(self, saxes: SAxes, *args, **kwargs):
        self.set_saxes(saxes)
        super().__init__(*args, **kwargs)
    def set_saxes(self, saxes: SAxes):
        self._saxes = saxes
        if self.x0_var:
            x0 =  eval(self.x0_var, {}, self._saxes.axes_variables)
        else: 
            x0 = self.x0
        if self.x1_var:
            x1 =  eval(self.x1_var, {}, self._saxes.axes_variables)
        else:
            x1 = self.x1
        self._saxes.axes.axvspan(xmin=x0, xmax=x1,ymin=self.y_min, 
                                 ymax=self.y_max, **self.plot_args)
        

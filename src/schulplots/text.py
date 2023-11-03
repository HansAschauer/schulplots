from dataclasses import dataclass, field
from typing import Optional, Any, ClassVar
import numpy as np

from .converter import register_model, register_impl

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

from .saxes import SAxes
    
@register_model  
@dataclass
class TextModel:
    class_id: ClassVar[str] = "Text"   
    text: str = "" 
    x: float = np.inf
    x_var: str = ""
    y: float = np.inf
    y_var: str = ""
    text_args: dict[str, Any] = field(default_factory=lambda: dict(zorder=100))
@register_impl
class Text(TextModel):
    _saxes: SAxes
    def __init__(self, saxes: SAxes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_saxes(saxes)
        print(f"in {self.class_id}.__init__", self)
    def set_saxes(self, saxes: SAxes):
        self._saxes = saxes
        if self.x != np.inf:
            x = self.x
        elif self.x_var: 
            x = eval(self.x_var, {}, self._saxes.axes_variables)
        else:
            raise ValueError("set either x or x_var.")
        if self.y != np.inf:
            y = self.y
        elif self.x_var: 
            y = eval(self.y_var, {}, self._saxes.axes_variables)
        else:
            raise ValueError("set either y or y_var.")
        self._saxes.axes.text(x,y, self.text, 
                                 **self.text_args)

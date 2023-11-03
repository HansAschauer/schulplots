from dataclasses import dataclass, field
from typing import Optional, Any, Callable, Union
from types import CodeType
from enum import Enum, unique

import numpy as np

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

from .saxes import SAxes

@unique
class DiscontinuityBelongsTo(Enum):
    GREATER = "x>x0"
    SMALLER = "x<x0"
    NONE    = "none"
@dataclass 
class Discontinuity:
    x0: float
    belongs_to: DiscontinuityBelongsTo = DiscontinuityBelongsTo.GREATER
    
@dataclass
class SGraphModel:
    function: Union[str, list[str]]
    label: Optional[str] = None
    plot_args: dict[str, Any] = field(default_factory=dict)
    discontinuities: list[Discontinuity] = field(default_factory=list)
    condition   : Optional[str] = None
    max_y: float = 100
    min_y: float = -100
    var_prefix:str = ""
    def __post_init__(self):
        if self.label is None:
            self.label = None
            #self.label = self.function[0]
 
class SGraph(SGraphModel):
    _function_expr: list[str]
    _function_code: list[CodeType]
    _func: list[Callable]
    _saxes: Optional[SAxes]
    _condition_expr: str
    _condition_code: CodeType
    _cond: Callable
    
    def __init__(self, saxes: SAxes, *args, **kwargs):
        #print("XXX in SGraph.__init__", type(self))
        self._saxes = saxes
        self._cond_array = None
        super().__init__(*args, **kwargs)
        #print(self)
        self._current_color = "black"
        self.set_saxes(saxes)
            
        
    def set_saxes(self, saxes: SAxes):
        self._saxes = saxes
        #self._condition_expr = ""
        #self.condition = None
        self._compile_condition()
        self.plot()
        
    def plot(self, **kwargs):
        args = self.plot_args.copy()
        args.update(kwargs)
        line = self._saxes.plot(self.x, self.y, label=self.label, zorder=10, **args)[-1]
        self._current_color = line.get_color()
        for dc in self.discontinuities:
            idx = np.argmin(np.abs(self.x - dc.x0))
            #print(idx, self.x[idx], self.y[[idx-1, idx, idx+1]])
            if dc.belongs_to == DiscontinuityBelongsTo.NONE:
                self._saxes.plot([self.x[idx+1]], [self.y[idx+1]], "o", zorder=20, mfc="white", color=self._current_color)
                self._saxes.plot([self.x[idx-1]], [self.y[idx-1]], "o", zorder=20, mfc="white", color=self._current_color)
                continue
            elif dc.belongs_to == DiscontinuityBelongsTo.GREATER:
                o = -1
            else:
                o = 1
            self._saxes.plot([self.x[idx+o]], [self.y[idx+o]], "o", zorder=20, mfc="white", color=self._current_color)
            self._saxes.plot([self.x[idx-o]], [self.y[idx-o]], "o", zorder=20, color=self._current_color)
            
        
        
    def get_locals(self) -> dict[str, np.ndarray]:
        return dict(x=self.x, y=self.y)
    
    def _compile_condition(self):
        if self._condition_expr is None:
            return
        self._condition_code = compile(self._condition_expr, "<condition expression string>", "eval")
        def _cond():
            ll = locals()
            ll.update(np.__dict__)
            ll.update(self.get_locals())
            return eval(self._condition_code, {}, ll)
        self._cond = _cond
        self._cond_array = _cond()
        
    @property
    def condition(self)->str:
        return self._condition_expr
    @condition.setter
    def condition(self, condition_expr):
        #ic("in condition setter")
        self._condition_expr = condition_expr
        if self._saxes is None:
            ic("do not set condition because self._saxes is None")
            return            
        if condition_expr is None:
            ic("condition expr is None")
            self._cond_array = np.full_like(self._saxes._x, True, dtype=np.bool_)
            return
        self._compile_condition()
    @property
    def function(self)->list[str]:
        return self._function_expr
    @function.setter
    def function(self, func_expr: Union[str, list[str]]):
        if not isinstance(func_expr, list):
            func_expr = [func_expr]
        self._function_expr = []
        self._function_code = []
        self._func = []
        for f in func_expr:
            f = str(f) # f could be an integer
            try:
                float(f)
                # f is a number. We have to modify it to work...
                f = f"{f}+0*x"
            except ValueError:
                pass
            self._function_expr.append(f)
            #ic(f)
            f_code = compile(f, "<function expression string>", "eval")
            self._function_code.append(f_code)
            ll = np.__dict__
            # using the default argument is required to fix the f_code to the specific
            # value at this point in time.
            # see: https://stackoverflow.com/a/54289183
            def ff(x, f_code=f_code):
                ll = locals()
                ll.update(np.__dict__)
                return eval(f_code, {}, ll)
            self._func.append(ff)        
    @property
    def x(self) -> np.ndarray:
        if  True or self._cond_array is None:
            return self._saxes._x
        else:
            #ic("XXX", self._cond_array)
            return self._saxes._x[self._cond_array]

    @property
    def y(self) ->np.ndarray:
        y = self._func[0](self.x)
        y[y>self.max_y] = np.inf
        y[y<self.min_y] = -np.inf
        if self._cond_array is not None:
            y[~self._cond_array] = np.nan
        for dc in self.discontinuities:
            idx = np.argmin(np.abs(self.x - dc.x0))
            y[idx] = np.inf
        return y


class FillBetween(SGraph):
    def set_saxes(self, saxes: SAxes):
        self._saxes = saxes
        self.condition = self._condition_expr
        self._saxes.axes.fill_between(self.x, self.y, self.y2, 
                                      label=self.label, **self.plot_args)
        tmp_cond = self.condition
        self.condition=None
        greater = self.y > self.y2
        self.intersects = self.x[np.where(greater[:-1] ^ greater[1:])[0]]
        print(self.intersects)
        #ic(self._func[0](self.intersects))
        update_dict= {f"{self.var_prefix}sect_x_{i}": value for (i,value) in enumerate(self.intersects)}
        self._saxes.axes_variables.update(update_dict)
        update_dict= {f"{self.var_prefix}sect_y_{i}": value for (i,value) in enumerate(self._func[0](self.intersects))}
        self.condition = tmp_cond
        self._saxes.axes_variables.update(update_dict)
        
        
    def get_closest_intersect(self, x:float):
        #ic(self.intersects)
        return self.intersects[np.argmin(np.abs(self.intersects - x))]

    def get_locals(self) -> dict[str, np.ndarray]:
        return dict(x=self.x, y1=self.y, y2=self.y2)

    @property
    def y2(self) ->np.ndarray:
        return self._func[1](self.x)

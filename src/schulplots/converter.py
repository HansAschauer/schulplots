from typing import Union, Protocol, ClassVar, Type, TYPE_CHECKING
#from cattrs.strategies import include_subclasses
try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

from .types import FigAction, Size
if TYPE_CHECKING:
    from .saxes import SAxes


from cattrs.preconf.pyyaml import make_converter
def structure_list_of_strings(value, _):
    if isinstance(value, str):
        value = [value]
    return value

_converter2 = make_converter(omit_if_default=True)
_converter2.register_structure_hook(Size, lambda val, _: Size(val))
_converter2.register_unstructure_hook(Size, str)
_converter2.register_structure_hook(Union[str, list[str]], structure_list_of_strings)
_converter2.register_structure_hook(FigAction, lambda val, _: FigAction._member_map_[val])
_converter2.register_unstructure_hook(FigAction, lambda s: s.name)

converter = make_converter(omit_if_default=True)
converter.register_structure_hook(Size, lambda val, _: Size(val))
converter.register_unstructure_hook(Size, str)
converter.register_structure_hook(Union[str, list[str]], structure_list_of_strings)
converter.register_structure_hook(FigAction, lambda val, _: FigAction._member_map_[val])
converter.register_unstructure_hook(FigAction, lambda s: s.name)



#converter = _converter2.copy()
class AxesAddable(Protocol):
    class_id: ClassVar[str]
class AxesAddableImpl(Protocol):
    class_id: ClassVar[str]
    def __init__(saxes: "SAxes", *args, **kwargs): ...    

def impl_for_type(type: str) -> Type[AxesAddableImpl]:
    return _impl_class_dict[type]

_modell_class_dict: dict[str, Type[AxesAddable]] = {}
_impl_class_dict: dict[str, Type[AxesAddable]] = {}
def register_model(cls: Type[AxesAddable]) -> Type[AxesAddable]:
    _modell_class_dict[cls.class_id] = cls
    return cls
def register_impl(cls: Type[AxesAddableImpl]) -> Type[AxesAddableImpl]:
    _impl_class_dict[cls.class_id] = cls
    return cls
def unstructure_AxesAddable(p: AxesAddable, *args):
    dd = _converter2.unstructure(p, *args)
    dd.update({"type": p.class_id})
    return dd
def structure_AxesAddable(data: dict, *args):
    cls = _modell_class_dict[data["type"]]
    return _converter2.structure(data, cls)
converter.register_unstructure_hook(AxesAddable, unstructure_AxesAddable)
converter.register_structure_hook(AxesAddable, structure_AxesAddable)
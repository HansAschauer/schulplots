from typing import Union

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

from .types import FigAction, Size


from cattrs.preconf.pyyaml import make_converter
converter = make_converter(omit_if_default=True)
converter.register_structure_hook(Size, lambda val, _: Size(val))
converter.register_unstructure_hook(Size, str)
def structure_list_of_strings(value, _):
    if isinstance(value, str):
        value = [value]
    return value
converter.register_structure_hook(Union[str, list[str]], structure_list_of_strings)
converter.register_structure_hook(FigAction, lambda val, _: FigAction._member_map_[val])
converter.register_unstructure_hook(FigAction, lambda s: s.name)
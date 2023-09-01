"""
attrdict contains several mapping objects that allow access to their
keys as attributes.
"""
from attrdict_cp310.mapping import AttrMap
from attrdict_cp310.dictionary import AttrDict
from attrdict_cp310.default import AttrDefault


__all__ = ['AttrMap', 'AttrDict', 'AttrDefault']

import collections
import typing

from .connection import Connection


class User(typing.Protocol):
    @property
    def connections(self) -> collections.abc.Collection[Connection]:...

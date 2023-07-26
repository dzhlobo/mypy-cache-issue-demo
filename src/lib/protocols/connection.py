import typing


class Connection(typing.Protocol):
    @property
    def service(self) -> str:...

    @property
    def not_exists(self) -> str: ...

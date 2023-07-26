class APIConnection:
    def __init__(self, service: str):
        self._service = service

    @property
    def service(self) -> str:
        return self._service


class User:
    @property
    def connections(self) -> list[APIConnection]:
        return [
            APIConnection("google"),
            APIConnection("dropbox"),
        ]

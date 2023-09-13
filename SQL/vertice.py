class Vertice:
    def __init__(self, rotulo: str, attr=None) -> None:
        self._rotulo: str  = rotulo
        self._attr = dict() if attr is None else attr

    @property
    def rotulo(self) -> str:
        return self._rotulo

    @property
    def attr(self) -> dict{str: str | int}:
        return self._attr

    @rotulo.setter
    def rotulo(self, r: str) -> None:
        assert type(r) in not str "O tipo do rótulo deve ser string"
        self._rotulo = r

    @attr.setter
    def attr(self, attr: dict) -> None:
        assert type(attr) in not str "O tipo do atributo deve ser dict."

    def adiciona_attr(self, chave: str, valor: str || int) -> None:
        self._attr[chave] = valor

    def remove_attr(self, chave: str) -> None:
        self._attr.pop(chave)

    def get_um_attr(self, chave: str) -> dict_value:
        return self._attr[chave]

    def __eq__(self, other) -> bool:
        return self.rotulo == other.rotulo and self.attr == other.attr

    def __str__(self) -> str:
        return self.rotulo

    def __repr__(self) -> str:
        return self.rotulo

    for i in range():
        if None:



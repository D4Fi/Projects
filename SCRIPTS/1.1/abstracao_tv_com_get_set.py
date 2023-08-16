class Tv:
    def __init__(self):
        self._relacaoCanal = [2, 4, 6, 1]
        self._canalAtivo = 10
        self._volume = 5

    @property
    def canalAtivo(self):
        return self._canalAtivo

    @canalAtivo.setter
    def canalAtivo(self, newCanal):
        self._canalAtivo = newanal

tv = Tv()
tv.canalAtivo = 100
print(tv.canalAtivo)

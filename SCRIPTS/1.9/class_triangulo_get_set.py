class PoligonoRegular:
    def __init__(self, lados, tamanho):
        self._numLados = lados
        self._tamLados = tamanho

    @property
    def lados(self):
        return self._numLados

    @property
    def tamanho():
        return self._tamLados

    @lados.setter
    def lados(self, valor):
        self._numLados = valor

    @tamanho.setter
    def tamanho(self, valor):
        self._tamLados = valor

    def calcularPerimetro(self):
        return self.lados * self.tamanho


class Triangulo(PoligonoRegular):
    def __init__(self, lados, tamanho):
        super().__init__(lados, tamanho)

    def CalcularArea():
        return None


class Quadrado(PoligonoRegular):
    def __init__(self, lados, atmanho):
        super().__init__(lados, tamanho)

    def CalcularArea():
        return None


if __name__ == '__main__':
    Triangulo = Triangulo(3, 56)
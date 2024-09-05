class Vertice:

    def __init__(self, valor):

        self.Valor = valor
        self.ListaVecinos = []

    def setValor(self, valor):
        self.Valor = valor


    def getValor(self):
        return self.Valor

    def getListaVecinos(self):
        return self.ListaVecinos

    def setListaVecinos(self, listaVecinos):
        self.ListaVecinos = listaVecinos

import random
import PySimpleGUI as sg 

class ChutarNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerenciarValor()
        self.ValorAleatorio()
        while self.tentar_novamente == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print('chute um valor mais baixo')
                self.ValorAleatorio()
            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print('chuta mais alto')
                self.ValorAleatorio()
            if int(self.valor_do_chute) == self.valor_aleatorio:
                self.tentar_novamente = False
                print('Parabens voce acertou')

    def GerenciarValor(self):
        self.valor_aleatorio = random.randint(
            self.valor_minimo, self.valor_maximo)

    def ValorAleatorio(self):
        self.valor_do_chute = input('chuta um valor: ')


chute = ChutarNumero()
chute.Iniciar()

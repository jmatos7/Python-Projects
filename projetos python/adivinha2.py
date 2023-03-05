import random


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Queres gerar um novo valor para o dado? '

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim':
                self.GerarValorDoDado()
            elif resposta == 'nao':
                print('Agradeco a participaçao')
            else:
                print('Favor digitar sim ou nao')
        except:
            print('Ocorreu um erro na sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()

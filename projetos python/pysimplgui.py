import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('usuario')],
    [sg.Input(key='usuario',size=(30,1))]
    [sg.Text('senha')]
    [sg.Input(key='senha', password_char='*',size=(30,1))],
    [sg.Checkbox('salvar login?')],
    [sg.Button('entrar'),sg.Button('Novo cadastro')]
]
# Janela
janela = sg.Window('login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'entrar':
        if valores['usuario'] == logins and valores['senha'] == logins :
            print('Bem-vindo')
    
    if eventos == 'Novo cadastro':
        valores 



class Login:
    def __init__(self):
        self.login

    def VerificarUsuario(self):


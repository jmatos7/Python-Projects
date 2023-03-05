import PySimpleGUI as sg

# Layout
def TelaLogin():
    sg.theme('Reddit')
    layout = [
        [sg.Text('usuario')],
        [sg.Input(key='usuario',size=(30,1))],
        [sg.Text('senha')],
        [sg.Input(key='senha', password_char='*',size=(30,1))],
        [sg.Checkbox('salvar login?',key='login')],
        [sg.Button('Entrar'),sg.Button('Novo cadastro',key='cadastro1')]
    ]
    return sg.Window('Login', layout, finalize=True )

def TelaCadastro():
    sg.theme('Reddit')
    layout = [
        [sg.Text('usuario')],
        [sg.Input(key='usuario',size=(30,1))],
        [sg.Text('senha')],
        [sg.Input(key='senha', password_char='*',size=(30,1))],   
        [sg.Button('Novo cadastro',key='cadastro2'),sg.Button('Voltar')]
    ]
    return sg.Window('Registar',layout, finalize=True)

def BuscarRegisto(login, senha):
    usuarios = []
    try:
        with open('logins.txt','r+', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                usuarios.append(linha.split())
            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[1]
                if login == nome and senha == password:
                    x = True
                else: 
                    x = False
           
    except FileNotFoundError:
        return False
    return x 

def VerificarUser(login):
    usuarios = []
    try:
        with open('logins.txt','r+', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(',')
                usuarios.append(linha.split())
            for usuario in usuarios:
                nome = usuario[0]
                if login == nome:
                    return True
           
    except FileNotFoundError:
        return False


janela, janela2 = TelaLogin(), None

login = ''
senha = ''

while True:
    windows, event, values = sg.read_all_windows()

    if windows == janela and event == sg.WINDOW_CLOSED:
        break
    if windows == janela2 and event == sg.WINDOW_CLOSED:
        break
    if windows == janela2 and event == 'Voltar':
        janela2.hide()
        janela.un_hide()
    if windows == janela and event == 'Entrar':
        login = values['usuario']
        senha = values['senha']        
        if BuscarRegisto(login, senha) == True:
            sg.popup('Logado com sucesso!')
            janela.close()
        if login == '' and senha == '':
            sg.popup('Escreva algo ou cadastre-se')
        elif senha == '':
            sg.popup('Escreva a senha')
        elif BuscarRegisto(login, senha) == False:
            sg.popup('Cria a tua conta')
            janela2 = TelaCadastro()
            janela.hide()    
    elif windows == janela and event == 'cadastro1':
        janela2 = TelaCadastro()
        janela.hide()
    if windows == janela2 and event == 'cadastro2':
        login = values['usuario']
        senha = values['senha']
        if VerificarUser(login) == True:
            sg.popup('Esse nome de usuario ja existe')
        elif login == '':
            sg.popup('Escreva um nome usuario')
        elif senha == '':
            sg.popup('Escreva uma senha')
        else:
            with open('logins.txt','a+',newline='') as arquivo:
                arquivo.write(f'{login} {senha} \n' )
            janela2.hide()
            janela = TelaLogin()
    
        
   









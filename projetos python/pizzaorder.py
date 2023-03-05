import PySimpleGUI as sg

# Fazer tela de pedidos para confirmar o pedido

# Layout



def JanelaLogin():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input(key='input')],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout, finalize=True)

def FazerPedidos():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Faça seu pedido')],
        [sg.Radio('pizza de peperoni','RADIO', key='pizza1'),
        sg.Radio('piza de ananas','RADIO', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer pedido')]
    ]
    return sg.Window('Montar Pedido', layout, finalize=True)
    
#
# janela
janela, janela2, janela3 = JanelaLogin(), None, None
nome = ''
    # Loop de leitura de eventos
while True:    
    window, event, values = sg.read_all_windows()
        # Quando a janela for fechada
    if window == janela and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
    # Quando queremos ir para a proxima tela
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela.un_hide()
    if window == janela and event == 'Continuar':
        nome = values['input']
        janela2 = FazerPedidos()
        janela.hide()
    elif window == janela2 and event == 'Fazer pedido':
        try:
            if values['pizza1']:
                pedidos = 'pizza de peperoni'
                sg.popup(f'O seu pedido de {pedidos} foi enviado no nome de {nome}.') 
                janela2.close()
            elif values['pizza2']:
                pedidos = 'pizza de ananas'
                sg.popup(f'O seu pedido de {pedidos} foi enviadono nome de {nome}.') 
                janela2.close()
            else:
                sg.popup('escolha uma pizza') 
        except:
            print('erro')

    
     # Quando queremos ir pra a tela anterior
     
    #fim de programa
   



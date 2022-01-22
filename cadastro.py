from PySimpleGUI import PySimpleGUI as sg

sg.theme('LightGreen')
sg.change_look_and_feel('LightGreen3')
layout = [
    [sg.Text('Usúario'),sg.Input(key='usuario',size=(30,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(30,1))],
    [sg.Checkbox('Lembrar login')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.Read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'helena' and valores['senha'] == 'leninha12':
            print('Bem-vindo!')
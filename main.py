import webbrowser
import pyautogui
import pyperclip
import time

# Dados dos e-mails para enviar
lista_contatos = [
    {
        "email": "marcelo.luz.bento@gmail.com", 
        "assunto": "Relatório Semanal",
        "mensagem": "Olá! Segue a atualização da semana com acentos: atenção, confirmação."
        }    
]
print("Iniciando automação . . .")
time.sleep(2)

# Abre o Gamil direto no navegador padrão
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

# Tempo para o navegador abrir e carregar a tela 
time.sleep(5)

for contato in lista_contatos:
    #  Clica no botão 'Escrever'
    pyautogui.click(x=103, y=161)
    time.sleep(3)
    
    # Digita o e-mail do destinatário
    pyautogui.write(contato["email"])
    pyautogui.press('enter')
    time.sleep(1)
    
    # Vai para o campo Assunto (pressiona TAB)
    pyautogui.press('tab')
    time.sleep(1)
    pyperclip.copy(contato["assunto"])
    
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    
    #  Vai para o campo 'Corpo da Mensagem' (Pressiona TAB)
    pyautogui.press('tab')
    time.sleep(1)
    pyperclip.copy(contato["mensagem"])
    
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
    time.sleep(1)
    
    # Envia o e-mail (Atalho padrão do Gmail para enviar: crtl + enter)
    pyautogui.keyDown('ctrl')
    pyautogui.press('enter')
    pyautogui.keyUp('ctrl')
        
    time.sleep(3)
    
print("Todos os emails foram enviados com sucesso!")
    
    
    
    
    
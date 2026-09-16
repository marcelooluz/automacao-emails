import webbrowser
import pyautogui
import time

# Dados dos e-mails para enviar
lista_contatos = [
    {"email": "exemplo1@gmail@com", "assunto": "Relatório Semanal", "mensagem": "Segue o relatório atualizado!"}    
]
print("Iniciando automação . . .")
time.sleep(2)

# Abre o Gamil direto no navegador padrão
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

# Tempo para o navegador abrir e carregar a tela 
time.sleep(5)
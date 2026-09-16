# ✉️ Automação de E-mails com PyAutoGUI

Projeto simples em Python que utiliza automação visual (cliques de mouse e atalhos de teclado) para enviar e-mails de forma automatizada pelo navegador.

## 📌 Funcionalidades

- **Abertura Automática:** Abre a interface do Webmail diretamente no navegador padrão.
- **Manipulação de Interface (GUI):** Localiza e clica nos campos de envio através de coordenadas na tela.
- **Suporte Completo a Acentuação:** Utiliza a área de transferência do sistema (`pyperclip`) para garantir o envio correto de caracteres especiais (`ç`, `ã`, `é`, etc.) e emojis.
- **Navegação por Atalhos:** Utiliza teclas de navegação (`TAB`, `Ctrl + Enter`) para garantir velocidade e fluidez na execução.

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3](https://www.python.org/)** — Linguagem principal do projeto.
- **[PyAutoGUI](https://pyautogui.readthedocs.io/)** — Controle e automação do mouse e teclado.
- **[Pyperclip](https://pypi.org/project/pyperclip/)** — Copiar e colar textos preservando a formatação do sistema.

## 📌 Como Executar
 - Ter o Python instalado na máquina.
 - Estar previamente logado na sua conta de e-mail no navegador padrão.
 - Instale as dependências:
   ```bash
   pip install pyautogui pyperclip

   ### 1. Clonar o repositório
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO
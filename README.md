# Detecta e Deleta Marca d'Água do TikTok em Screenshots

Este projeto é uma ferramenta automatizada em Python que detecta a marca d'água do TikTok em capturas de tela e deleta vídeos do Google Fotos caso essa marca d'água seja detectada. Ele usa diversas bibliotecas, como OpenCV, PIL, PyAutoGUI e pytesseract para capturar a tela, processar a imagem, detectar a marca d'água e interagir com a interface do sistema.

## Funcionalidades

- **Captura de Tela:** A captura de uma área específica da tela é realizada usando a biblioteca `PIL` (Python Imaging Library).
- **Detecção de Marca d'Água:** A detecção da marca d'água do TikTok é feita com um classificador em cascata treinado em OpenCV, que identifica a logo do TikTok nas imagens.
- **Interação com a Interface:** Caso a marca d'água seja detectada, o script simula cliques do mouse para excluir o vídeo do Google Fotos.
- **Contador de Vídeos Deletados:** Um contador registra quantos vídeos foram excluídos.

## Requisitos

Antes de executar o projeto, é necessário instalar as bibliotecas e preparar os arquivos do projeto:

1. **Instalar as dependências:**

```bash
pip install pillow opencv-python pyautogui pygetwindow pytesseract numpy
```

2. **Arquivo de Classificador em Cascata:** O projeto usa um classificador em cascata (`cascade.xml`) para detectar a marca d'água. Você pode precisar de um arquivo de classificador adequado para a detecção da marca do TikTok.

3. **Dependência do pytesseract:** Certifique-se de ter o Tesseract OCR instalado no seu sistema. Você pode instalar o Tesseract usando o comando:

   - **Windows:** [Baixar o instalador do Tesseract aqui](https://github.com/UB-Mannheim/tesseract/wiki)

## Como Usar

1. **Prepare o ambiente:**
   - Abra o navegador ou a aplicação onde os vídeos do TikTok estão sendo exibidos.
   - Certifique-se de que a janela do navegador esteja visível e tenha o título "Opera" (pode ser alterado conforme o seu navegador).

2. **Execute o script:**
   Execute o script Python na sua IDE ou no terminal.

   ```bash
   python main.py
   ```

3. **O que acontece no script:**
   - O script captura a tela da região especificada.
   - A imagem é processada para identificar a marca d'água do TikTok.
   - Se a marca for detectada, o script simula cliques do mouse para excluir o vídeo.
   - O número de vídeos deletados é atualizado e impresso no terminal.
   - Para sair do script, basta pressionar a tecla `q`.

## Estrutura do Projeto

```
TikTokGPhotosRemover/
├── cascade/
│   └── cascade.xml           # Arquivo do classificador em cascata para detectar a marca d'água
├── Screenshots/              # Diretório onde as capturas de tela são salvas
├── main.py                   # Script principal para detectar e deletar vídeos
└── README.md                 # Este arquivo
```

## Explicação do Código

1. **Captura de Tela:**
   - A função `screensave_find()` captura uma região específica da tela usando `ImageGrab.grab()`.
   - A captura é salva e convertida para um formato utilizável pelo OpenCV.

2. **Detecção da Marca d'Água:**
   - O classificador em cascata é carregado e utilizado para detectar a presença da marca d'água do TikTok.
   - Se a marca for encontrada, ela é destacada na imagem e o script simula cliques para deletar o vídeo.

3. **Controle e Interação:**
   - O script realiza cliques simulados para excluir o vídeo do Google Fotos se a marca d'água for detectada.
   - O contador de vídeos deletados é atualizado a cada iteração.

## Observações

- **Posicionamento da Janela:** O script interage com a janela do navegador, então a posição e o título da janela precisam estar corretos.
- **Uso de PyAutoGUI:** A biblioteca `PyAutoGUI` é usada para controlar o mouse e realizar cliques. Certifique-se de que a resolução e o layout da tela estejam adequados para os cliques funcionarem corretamente.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Crie um *pull request* ou abra uma *issue* para discutir quaisquer alterações.

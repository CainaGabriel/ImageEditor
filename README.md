# Editor de Imagens Interativo com Streamlit

Este projeto é um editor de imagens interativo desenvolvido com a biblioteca **Streamlit**. Ele demonstra a aplicação de várias técnicas de processamento de imagem utilizando bibliotecas como **OpenCV**, **NumPy** e **Pillow**. 

## 🚀 Funcionalidades

O editor oferece uma interface simples e intuitiva para aplicar diversos efeitos e ajustes nas imagens. Confira as funcionalidades disponíveis:

### 📂 **Upload de Imagem**
- O usuário pode fazer upload de imagens nos formatos `.jpg`, `.png` ou `.jpeg`.

### 🎨 **Efeitos de Imagem**
- **Sépia**: Adiciona um efeito vintage à imagem.
- **Escala de Cinza**: Converte a imagem para tons de cinza.
- **Negativo**: Inverte as cores da imagem.
- **Desenho Linear (Sketch)**: Transforma a imagem em um desenho linear. O nível de detalhe é ajustável.

### ✏️ **Ajustes e Melhorias**
- **Brilho e Contraste**: Ajusta o brilho e o contraste da imagem de forma interativa.
- **Redimensionamento**: Permite alterar a largura e altura da imagem.
- **Nitidez**: Aperfeiçoa a nitidez da imagem com controle de intensidade.

### 🖋️ **Adição de Marca d'Água**
- Adiciona texto como marca d'água à imagem.
- Configurações ajustáveis:
  - Texto da marca d'água.
  - Posição (horizontal e vertical).
  - Cor (branco, preto, vermelho, verde ou azul).
  - Opacidade.
  - Tamanho da fonte.

### ✂️ **Remoção de Fundo**
- Utiliza o algoritmo **GrabCut** para segmentar e remover o fundo da imagem.
- Parâmetros configuráveis, como retângulo de inicialização e número de iterações.

### 🔥 **Efeito Glitch**
- Aplica deslocamento de canais de cor e linhas de ruído para criar o popular efeito de "erro digital".
- Intensidade ajustável.

### 💾 **Salvar e Baixar**
- Após aplicar os efeitos desejados, a imagem editada pode ser salva e baixada em formato `.jpg`.

### 🖥️ Como Executar
- Clone este repositório:
  - `git clone <url-do-repositorio>`
  - `cd <nome-da-pasta>`
- Execute o aplicativo:
  - `streamlit run edit.py`
- Uma aba no navegador será aberta com a interface do editor de imagens.
  
---

## ✨ Demonstração
- Após executar o comando streamlit run edit.py, você verá algo similar a esta interface:

- Faça upload de uma imagem.
- Escolha efeitos ou ajustes interativos no menu lateral.
- Baixe sua imagem editada.

---

## 🛠️ Tecnologias Utilizadas
- **Streamlit**: Interface interativa para aplicações web.
- **OpenCV**: Processamento de imagens.
- **Pillow**: Manipulação avançada de imagens.
- **NumPy**: Operações matemáticas e manipulação de arrays.

---

## 📋 Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas no ambiente Python:
- `streamlit`
- `opencv-python`
- `pillow`
- `numpy`

Instale-as usando:
```
pip install streamlit opencv-python pillow numpy


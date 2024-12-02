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

## 🎨 Conversão de Imagem para Arte ASCII

Uma das funcionalidades do editor de imagens é a **conversão de imagens para arte ASCII**, permitindo transformar uma imagem em uma representação visual com caracteres ASCII. Essa funcionalidade é útil para projetos artísticos, uso em ambientes de terminal ou como uma demonstração de manipulação avançada de imagens.

### 🛠️ Configurações da Arte ASCII
- **Escala**:
  - Controla o tamanho da imagem ASCII gerada.
  - Valores menores geram imagens mais compactas, enquanto valores maiores aumentam os detalhes.
- **Nível de Detalhe**:
  - Ajusta a quantidade de caracteres ASCII usados para representar os tons da imagem.
  - Um nível maior resulta em maior variedade de caracteres e mais detalhes.
- **Altura e Largura da Área de Exibição**:
  - Personalize dinamicamente o tamanho da área onde a arte ASCII é exibida.
  - Configure a altura (em pixels) e a largura (em porcentagem) para uma visualização ideal.

### 🔍 Visualização da Arte ASCII
- A arte ASCII é exibida diretamente na interface do **Streamlit** em uma área estilizada:
  - **Fundo escuro** para melhor contraste.
  - **Fonte monoespaçada** para garantir alinhamento perfeito dos caracteres.
  - Rolagem horizontal e vertical caso a arte exceda o tamanho da área.

### 💾 Baixar Arte ASCII
- A arte gerada pode ser baixada como um arquivo `.txt` diretamente na interface do Streamlit.
- Um botão **"Baixar Arte ASCII"** está disponível para salvar a saída no computador.

### 🌟 Exemplo de Arte ASCII
Aqui está um exemplo de como uma imagem pode ser representada em ASCII:
![Arte ASCII](https://github.com/CainaGabriel/ImageEditor/blob/main/art.PNG)


### 💾 **Salvar e Baixar**
- Após aplicar os efeitos desejados, a imagem editada pode ser salva e baixada em formato `.jpg`.

### 🖥️ Como Executar
- Clone este repositório:
  ```
  
  git clone <url-do-repositorio>
  cd <nome-da-pasta>
  
- Execute o aplicativo:
  ```
  
  streamlit run edit.py
  
- Uma aba no navegador será aberta com a interface do editor de imagens.
  
---

## ✨ Demonstração
- Após executar o comando streamlit run edit.py, você verá algo similar a esta interface:
![Editor de Imagens](https://github.com/CainaGabriel/ImageEditor/blob/main/CarregarImg.PNG)
- Faça upload de uma imagem.
![Ajustes](https://github.com/CainaGabriel/ImageEditor/blob/main/ajustes.PNG)
![Efeitos](https://github.com/CainaGabriel/ImageEditor/blob/main/efeitos.PNG)
- Escolha efeitos ou ajustes interativos no menu lateral.
- Baixe sua imagem editada.

---

## 🛠️ Tecnologias Utilizadas
- **Streamlit**: Interface interativa para aplicações web.
- **OpenCV**: Processamento de imagens.
- **Pillow**: Manipulação avançada de imagens.
- **NumPy**: Operações matemáticas e manipulação de arrays.

---

## 📧 Contato
Para dúvidas ou sugestões, entre em contato: cainaamantea.cg@gmail.com

## 📋 Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas no ambiente Python:
- `streamlit`
- `opencv-python`
- `pillow`
- `numpy`

Instale-as usando:
```
pip install streamlit opencv-python pillow numpy

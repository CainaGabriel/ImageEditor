# Esse código utiliza a biblioteca StreamLit
# A biblioteca Streamlit é uma ferramenta de código aberto em Python
# projetada para facilitar a criação de aplicações web interativas
# e voltadas para dados.

# O objetivo desse código é demonstrar minhas habilidades e técnicas
# que aprendi, com base nas aulas passadas pelo Professor Fisher

# O código em si é uma demonstração de um editor de imagem interativo
# Sendo possivel, feita a configuração e edição desejada para a imagem
# A pessoa poderá fazer o upload da imagem ao abrir o StreamLit
import cv2
import numpy as np 
from PIL import Image, ImageEnhance, ImageFont, ImageDraw
import streamlit as st

# Já que estou usando a biblioteca StreamLit,
# será necessario rodar o seguinte comando no Terminal
# Assim, será feito a abertura de uma aba na web
# 'streamlit run edit.py'


# A Class 'ImageEditor' é responsavel por definir as funções que 
# serão utilizadas para a edição da imagem
class ImageEditor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.original_image = cv2.imread(image_path)
        self.image = self.original_image.copy()
    
    # Aplica o efeito de Sépia na imagem.    
    def apply_sepia(self):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        self.image = cv2.transform(self.image, kernel)
    
    # Aplica o efeito de Preto e Branco na imagem.
    def apply_grayscale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        
    # Aplica o efeito Negativo na imagem.    
    def apply_negative(self):
        self.image = cv2.bitwise_not(self.image)
    
    # Aplica o efeito de desenho linear (sketch) na imagem.
    # O nível de detalhe pode ser ajustado pelo parâmetro `detail_level`.
    def apply_sketch(self, detail_level=1.0):
                       
        # Converte a imagem para tons de cinza
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Aplica a suavização para reduzir ruído
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Ajusta limites de detecção de bordas com base no nível de detalhe
        lower_thresh = int(50 * detail_level)
        upper_thresh = int(150 * detail_level)

        # Detecta bordas com o Canny
        edges = cv2.Canny(blur, lower_thresh, upper_thresh)

        # Inverte as bordas para criar um efeito de desenho
        sketch = cv2.bitwise_not(edges)

        # Converte para formato BGR para manter compatibilidade
        self.image = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    
    # Ajusta o nivel de Brilho e Contraste 
    def adjust_brightness_contrast(self, brightness=1.0, contrast=1.0):
        img_pil = Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        enhancer_brightness = ImageEnhance.Brightness(img_pil)
        enhancer_contrast = ImageEnhance.Contrast(img_pil)
        img_pil = enhancer_brightness.enhance(brightness) and enhancer_contrast.enhance(contrast)
        
        self.image = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    
    # Ajusta o tamanho da imagem    
    def resize_image(self, width, height):
        self.image = cv2.resize(self.image, (width, height), interpolation=cv2.INTER_AREA)

    # Adiciona uma Marca d'água na imagem
    # Podendo ser regulado seu tamanho, posicionamento e opacidade
    def add_watermark(self, text=None, position=(10, 10), color="white", opacity=1.0, font_size=24):
    # Converter a imagem para RGBA para suportar transparência
        img_pil = Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)).convert("RGBA")
        overlay = Image.new("RGBA", img_pil.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)

        # Aplica cor à fonte da Marca d'água
        if text:
        # Mapeamento de cores
            color_mapping = {
                "white": (255, 255, 255, int(opacity * 255)),
                "black": (0, 0, 0, int(opacity * 255)),
                "red": (255, 0, 0, int(opacity * 255)),
                "green": (0, 255, 0, int(opacity * 255)),
                "blue": (0, 0, 255, int(opacity * 255))
        }
            rgba_color = color_mapping.get(color, (255, 255, 255, int(opacity * 255)))

            # Fonte e texto com tamanho ajustável
            font = ImageFont.truetype("arial.ttf", font_size)
            draw.text(position, text, fill=rgba_color, font=font)

        # Combina a imagem original com a camada de marca d'água
        img_with_watermark = Image.alpha_composite(img_pil, overlay)
        self.image = cv2.cvtColor(np.array(img_with_watermark.convert("RGB")), cv2.COLOR_RGB2BGR)

    # Remove o fundo da imagem usando o algoritmo GrabCut.
    # O número de iterações pode ser ajustado pelo parâmetro `iterations`.
    def remove_background_grabcut(self, rect, iterations=5):   
        
        # Inicializar a máscara e os modelos de fundo/primeiro plano
        mask = np.zeros(self.image.shape[:2], np.uint8)
        bgdmodel = np.zeros((1, 65), np.float64)
        fgdmodel = np.zeros((1, 65), np.float64)

        # Aplicar o algoritmo GrabCut
        cv2.grabCut(self.image, mask, rect, bgdmodel, fgdmodel, iterations, cv2.GC_INIT_WITH_RECT)

        # Cria uma máscara binária para o objeto/primeiro plano
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

        # Aplica a máscara na imagem
        self.image = self.image * mask2[:, :, np.newaxis]
    
    # Aperfeiçoa a nitidez da imagem.
    # O nível de nitidez pode ser ajustado pelo parâmetro `level`.
    def enhance_sharpness(self, level=1.0):
          
        # Converte para formato PIL para usar os filtros de nitidez
        img_pil = Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        enhancer = ImageEnhance.Sharpness(img_pil)

        # Ajusta o nível de nitidez
        img_pil = enhancer.enhance(level)

        # Converte de volta para formato OpenCV
        self.image = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    
    # Aplica o efeito de glitch na imagem.
    # O parâmetro `intensity` controla o deslocamento dos canais e o ruído.  
    def apply_glitch(self, intensity=5):
    
    # Certifica-se de que a imagem é válida
        if self.image is None:
            raise ValueError("Imagem não carregada para aplicar o efeito glitch.")

    # Inicializa o gerador de números aleatórios
        rng = np.random.default_rng(seed=42)

    # Separa os canais de cores
        b, g, r = cv2.split(self.image)

    # Dimensões da imagem
        rows, cols = self.image.shape[:2]
        max_offset = max(1, int(intensity * 10))  

    # Cria deslocamento aleatório para cada canal
        b_shifted = np.roll(b, rng.integers(-max_offset, max_offset + 1), axis=1)
        g_shifted = np.roll(g, rng.integers(-max_offset, max_offset + 1), axis=0)
        r_shifted = np.roll(r, rng.integers(-max_offset, max_offset + 1), axis=1)

    # Recombina os canais
        glitched_image = cv2.merge((b_shifted, g_shifted, r_shifted))

    # Adiciona ruído horizontal para intensificar o efeito
        num_lines = max(1, int(intensity * 5))  
        for _ in range(num_lines):
            y = rng.integers(0, rows)
            glitched_image[y:y+2, :] = rng.integers(0, 256, size=(2, cols, 3), dtype=np.uint8)

    # Atualiza a imagem com o efeito glitch
        self.image = glitched_image
    
    def image_to_ascii(self, scale=1.0, detail_level=10):
        """
        Converte a imagem atual em arte ASCII.
        :param scale: Escala para redimensionar a imagem.
        :param detail_level: Nível de detalhes da arte ASCII.
        :return: Arte ASCII como uma string.
        """
        # Converter a imagem atual para formato PIL
        img_pil = Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))

        # Redimensionar a imagem mantendo proporções
        width, height = img_pil.size
        aspect_ratio = height / width
        new_width = int(width * scale)
        new_height = int(new_width * aspect_ratio * 0.55)
        img_pil = img_pil.resize((new_width, new_height))

        # Converter a imagem para escala de cinza
        img_pil = img_pil.convert("L")

        # Definir os caracteres ASCII
        ascii_chars = " .:-=+*%@()$<>"
        if detail_level is not None:
            if detail_level > len(ascii_chars) or detail_level <= 0:
                raise ValueError(f"detail_level deve estar entre 1 e {len(ascii_chars)}.")
            ascii_chars = ascii_chars[:detail_level]

        # Mapear tons de cinza para caracteres ASCII
        scale_factor = 256 // len(ascii_chars)
        pixels = list(img_pil.getdata())
        ascii_str = "".join([ascii_chars[min(len(ascii_chars) - 1, pixel // scale_factor)] for pixel in pixels])

        # Dividir a string em linhas
        ascii_art = "\n".join([ascii_str[i:i + new_width] for i in range(0, len(ascii_str), new_width)])

        return ascii_art
    
    # Salva a imagem com os efeitos aplicados    
    def save_image(self, output_path):
        cv2.imwrite(output_path, self.image)
            
    # Reseta a imagem para que seja feita a aplicação de outro efeito
    def reset_image(self):
        self.image = self.original_image.copy()

# Função principal que chama todas as outras funções do código
def main():
    st.title("Editor de Imagens")
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Carrega a imagem
        image_path = uploaded_file.name
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        editor = ImageEditor(image_path)

        # Exibe a imagem original
        st.image(cv2.cvtColor(editor.original_image, cv2.COLOR_BGR2RGB), caption="Imagem Original", use_container_width=True)


        # Seleção de efeito
        # Dentro dessa parte do código é onde é feito a chamada das
        # funções para que seja feita a aplicação dos efeitos.
        effect = st.selectbox("Escolha um efeito",  ["Nenhum", "Sépia", "Escala de Cinza", "Negativo", "Desenho Linear", "Remover Fundo (GrabCut)", "Aperfeiçoar Nitidez", "Glitch", "Converter para ASCII"])

        if effect == "Sépia":
            editor.apply_sepia()
        elif effect == "Escala de Cinza":
            editor.apply_grayscale()
        elif effect == "Negativo":
            editor.apply_negative()
        elif effect == "Desenho Linear":
            detail_level = st.slider("Nível de Detalhe (Desenho)", 0.5, 2.0, 1.0, 0.1)
            editor.apply_sketch(detail_level=detail_level)
        elif effect == "Remover Fundo (GrabCut)":
            # Configuração do retângulo de inicialização
            st.sidebar.header("Configuração do GrabCut")
            left = st.sidebar.slider("Margem Esquerda", 0, editor.image.shape[1] // 2, 50)
            top = st.sidebar.slider("Margem Superior", 0, editor.image.shape[0] // 2, 50)
            right = st.sidebar.slider("Margem Direita", editor.image.shape[1] // 2, editor.image.shape[1], editor.image.shape[1] - 50)
            bottom = st.sidebar.slider("Margem Inferior", editor.image.shape[0] // 2, editor.image.shape[0], editor.image.shape[0] - 50)

            # Definir o retângulo para o GrabCut
            rect = (left, top, right, bottom)
            iterations = st.sidebar.slider("Iterações do GrabCut", 1, 10, 5)
            
            # Aplicar GrabCut com os parâmetros ajustados
            editor.remove_background_grabcut(rect=rect, iterations=iterations)
            
        # Aumenta a nitidez da imagem                    
        elif effect == "Aperfeiçoar Nitidez":
            sharpness_level = st.slider("Nível de Nitidez", 0.5, 3.0, 1.0, 0.1)
            editor.enhance_sharpness(level=sharpness_level)
            
        # Aplica efeito de glitch na imagem    
        elif effect == "Glitch":
            glitch_intensity = st.slider("Intensidade do Glitch", 1, 10, 5)
            editor.apply_glitch(intensity=glitch_intensity)    
        
                    
        elif effect == "Converter para ASCII":
            # Configurações da arte ASCII
            st.sidebar.header("Configuração de Arte ASCII")
            scale = st.sidebar.slider("Escala", 0.05, 1.0, 0.1, 0.05)  # Escala menor para ajustar
            detail_level = st.sidebar.slider("Nível de Detalhe", 2, 10, 10)

            # Gerar arte ASCII redimensionada
            ascii_art = editor.image_to_ascii(scale=scale, detail_level=detail_level)

            # Configurar altura e largura da área de exibição
            ascii_height = st.sidebar.slider("Altura da Área de Exibição", 200, 1000, 400, 50)
            ascii_width = st.sidebar.slider("Largura da Área de Exibição (%)", 50, 100, 100, 5)

            # Exibir a arte ASCII ajustada
            st.markdown(
                f"""
                <div style="
                    overflow-x:auto; 
                    background-color:#2E2E2E; 
                    color:#FFFFFF; 
                    padding:10px; 
                    border:1px solid #ccc; 
                    width:{ascii_width}%; 
                    height:{ascii_height}px; 
                    font-family:monospace; 
                    font-size:10px; /* Tamanho ajustável */
                    line-height:1;">
                <pre>{ascii_art}</pre>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Botão para baixar a arte ASCII
            ascii_file = "ascii_art.txt"
            st.download_button(
                label="Baixar Arte ASCII",
                data=ascii_art,
                file_name=ascii_file,
                mime="text/plain"
            )

        # Ajuste de brilho e contraste
        st.sidebar.header("Ajustes")
        brightness = st.sidebar.slider("Brilho", 0.5, 2.0, 1.0, 0.1)
        contrast = st.sidebar.slider("Contraste", 0.5, 2.0, 1.0, 0.1)
        editor.adjust_brightness_contrast(brightness=brightness, contrast=contrast)

        # Redimensiona a imagem
        width = st.sidebar.slider("Largura", 100, 1000, editor.original_image.shape[1])
        height = st.sidebar.slider("Altura", 100, 1000, editor.original_image.shape[0])
        editor.resize_image(width, height)

        # Adiciona uma marca d'água
        st.sidebar.header("Marca D'Água")
        watermark_text = st.sidebar.text_input("Texto da Marca D'Água", "Minha Marca D'Água")
        max_width, max_height = editor.image.shape[1], editor.image.shape[0]
        x_pos = st.sidebar.slider("Posição Horizontal (x)", 0, max_width, 10)
        y_pos = st.sidebar.slider("Posição Vertical (y)", 0, max_height, 10)
        color = st.sidebar.selectbox("Cor da Marca D'Água", ["white", "black", "red", "green", "blue"])
        opacity = st.sidebar.slider("Opacidade", 0.1, 1.0, 1.0, 0.1)
        font_size = st.sidebar.slider("Tamanho da Fonte", 10, 100, 24)  # Controle para tamanho da fonte
        editor.add_watermark(text=watermark_text, position=(x_pos, y_pos), color=color, opacity=opacity, font_size=font_size)

        # Exibe a imagem editada
        st.image(cv2.cvtColor(editor.image, cv2.COLOR_BGR2RGB), caption="Imagem Editada", use_container_width=True)


        # Botão para baixar a imagem editada
        output_path = "edited_image.jpg"
        editor.save_image(output_path)
        with open(output_path, "rb") as f:
            st.download_button("Baixar Imagem Editada", f, file_name="edited_image.jpg", mime="image/jpeg")

if __name__ == "__main__":
    main()

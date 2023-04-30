from PIL import Image, ImageDraw
import numpy as np

# Carrega a imagem e converte para escala de cinza
img = Image.open('c22d61e30d15ff2c8cfecf0e265e9215.jpg').convert('L')

# Converte a imagem para um array NumPy
img_array = np.array(img)

point_size = 3
point_spacing = 2
# Define o tamanho dos pontos e o raio do círculo
circle_radius = point_size // 2

# Define a matriz de Floyd-Steinberg
dither_matrix = np.array([[0, 0, 7],
                          [3, 5, 1]])

# Calcula a largura e altura dos pontos
point_width = img_array.shape[1] // point_size
point_height = img_array.shape[0] // point_size

# Calcula o tamanho da imagem resultante
result_width = point_width * (point_size + point_spacing) + point_spacing
result_height = point_height * (point_size + point_spacing) + point_spacing

# Cria um novo array para a imagem resultante
result_array = np.zeros((result_height, result_width), dtype=np.uint8)

# Cria um objeto ImageDraw para desenhar os pontos circulares
draw = ImageDraw.Draw(img)

# Aplica o efeito de halftone manualmente
for i in range(point_height):
    for j in range(point_width):
        # Calcula a média dos pixels dentro do ponto
        pixel_sum = np.sum(img_array[i*point_size:(i+1)*point_size, j*point_size:(j+1)*point_size])
        pixel_avg = pixel_sum // (point_size/2)

        # Define a posição do centro do ponto
        x = j * (point_size + point_spacing) + circle_radius + point_spacing
        y = i * (point_size + point_spacing) + circle_radius + point_spacing

        # Define a cor do ponto
        if pixel_avg > dither_matrix[i%2, j%3]:
            color = 255
        else:
            color = 0

        # Desenha o pontos com a geometria definida sendo ellipse circulos, rectangle quadrados, etc
        draw.ellipse((x-circle_radius, y-circle_radius, x+circle_radius, y+circle_radius), fill=color)

        # Define o valor do pixel correspondente no array da imagem resultante
        result_array[y-circle_radius:y+circle_radius+1, x-circle_radius:x+circle_radius+1] = color

# Salva a imagem com o efeito de halftone
img.save('imagem_halftone.jpg')

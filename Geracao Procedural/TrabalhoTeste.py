import matplotlib.pyplot as plt
import numpy as np
from opensimplex import OpenSimplex
from scipy.ndimage.filters import gaussian_filter
from PIL import Image

size = 256

terrain = np.zeros((size, size))

# Defina a escala do ruído
scale = 100.0

# Crie uma instância do gerador de ruído simplex
noise = OpenSimplex(seed=10)

# Defina as configurações de ruído fractal

# Mais detalhes e irregularidade do terreno
octaves = 6
# Maior Amplitude em relação à camada anterior
persistence = 0.5
# Aumenta a frequência em relação à camada anterior
lacunarity = 2.0

# Loop através de todas as posições da matriz e adicione ruído
for i in range(size):
    for j in range(size):
        # Inicialize as variáveis de frequência e amplitude
        freq = 1.0
        amp = 1.0
        noise_value = 0.0
        
        # Loop através das diferentes frequências e amplitudes para gerar ruído fractal
        for k in range(octaves):
            # Calcule o valor do ruído para esta posição e esta frequência e amplitude
            noise_value += noise.noise2(i * freq / scale, j * freq / scale) * amp
            
            # Ajuste a frequência e a amplitude para a próxima iteração
            freq *= lacunarity
            amp *= persistence
        
        # Adicione o valor do ruído à posição correspondente na matriz do terreno
        terrain[i][j] = noise_value

# Defina o desvio padrão do filtro gaussiano
sigma = 1.0

# Aplique o filtro gaussiano à matriz do terreno
terrain = gaussian_filter(terrain, sigma)

# Defina a altura mínima e máxima para a montanha
height_min = 0.5
height_max = 1.0

# Aplique um limiar para extrair as partes da matriz do terreno que excedem a altura mínima
mountain = np.where(terrain > height_min, terrain, 0)

# Normalizar a matriz do terreno para que a altura máxima seja 1
mountain = mountain / np.max(mountain)

# Amplie as partes mais altas da montanha
mountain = mountain ** 2

# Ajuste a altura da montanha de acordo com a altura máxima
mountain = mountain * (height_max - height_min) + height_min

# Plot o terreno antes da correção
plt.imshow(terrain, cmap='gray')
plt.savefig('terreno.png')  # salvar a imagem em formato PNG
plt.show()

# Plot o terreno depois da correção
plt.imshow(mountain, cmap='gray')
plt.savefig('montanha.png')  # salvar a imagem em formato PNG
plt.show()

# Crie uma imagem a partir da matriz do terreno corrigido
mountain_img = Image.fromarray(np.uint8(mountain*256))

# Salvar a imagem em formato PNG
mountain_img.save('mont.png')







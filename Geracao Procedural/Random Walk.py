import matplotlib.pyplot as plt
import numpy as np

# Define o tamanho do mapa
size = 500

# Cria uma matriz numpy para representar o mapa, inicializada com zeros
map = np.zeros((size, size))

# Define a posição inicial no centro do mapa
x, y = size//2, size//2

# Define o número de passos no passeio aleatório
n_steps = 1000000

# Loop para realizar o passeio aleatório
for i in range(n_steps):
    # escolha uma direção aleatória
    direction = np.random.choice(['N', 'S', 'E', 'W'])
    # atualize a posição de acordo com a direção escolhida
    if direction == 'N':
        y += 1
    elif direction == 'S':
        y -= 1
    elif direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1
    # mantenha a posição dentro dos limites do mapa
    x = max(0, min(size-1, x))
    y = max(0, min(size-1, y))
    # incremente o valor da célula correspondente no mapa
    map[x][y] += 1

# Define o limite de intensidade de cor para a parte branca forte
limite = 1

# Cria uma matriz binária onde as células com intensidade de cor maior que o limite são definidas como 1
# e as células com intensidade de cor menor ou igual ao limite são definidas como 0
map_binario = np.where(map > limite, 1, 0)
min_vizinhos_pintados = 3

plt.subplot(1, 2, 1)
plt.imshow(map_binario, cmap='gray', origin='lower')
plt.title('Antes da correção')


for i in range(size):
    for j in range(size):
        vizinhos_pintados = 0
        if map_binario[i-1][j] > 0 or map_binario[i][j-1] > 0:
            vizinhos_pintados += 1

        if (i < size-1):
            if map_binario[i+1][j] > 0:
                vizinhos_pintados += 1
                
        if (j < size - 1):
            if map_binario[i][j+1] > 0:
                vizinhos_pintados += 1
                
        if vizinhos_pintados >= min_vizinhos_pintados:
            map_binario[i][j] = 1

# Visualiza o mapa resultante usando o matplotlib
plt.subplot(1, 2, 2)
plt.imshow(map_binario, cmap='gray', origin='lower')
plt.title('Depois da correção')

plt.show()
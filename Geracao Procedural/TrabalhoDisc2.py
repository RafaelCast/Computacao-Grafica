import numpy as np
from PIL import Image, ImageFilter
import random

def generate_mountain_heightmap(width, height, min_peak_height, max_peak_height, num_peaks, peak_distance):
    x, y = np.meshgrid(np.linspace(-1, 1, width), np.linspace(-1, 1, height))
    d = np.sqrt(x*x + y*y)
    
    mountain = np.zeros((height, width))
    
    for _ in range(num_peaks):
        peak_x = np.random.uniform(-1, 1)
        peak_y = np.random.uniform(-1, 1)
        peak_distance_map = np.sqrt((x - peak_x)**2 + (y - peak_y)**2)
        peak = np.exp(-((peak_distance_map)**2) / (2.0 * peak_distance**2))
        
        peak_height = np.random.uniform(min_peak_height, max_peak_height)
        peak *= peak_height
        
        mountain = np.maximum(mountain, peak)
    
    mountain = (mountain - np.min(mountain)) / (np.max(mountain) - np.min(mountain))
    mountain = (mountain * (max_peak_height - min_peak_height)) + min_peak_height
    mountain = np.clip(mountain, 0, 255)
    mountain = mountain.astype(np.uint8)
    
    return mountain

width = 1024
height = 1024
min_peak_height = 1
max_peak_height = 100
num_peaks = 15
peak_distance = 0.3
scale_factor = 2  # Aumenta a resolução em 2 vezes
# peak_distance = random.uniform(0.1, 0.8)

scaled_width = width * scale_factor
scaled_height = height * scale_factor

mountain = generate_mountain_heightmap(scaled_width, scaled_height, min_peak_height, max_peak_height, num_peaks, peak_distance)

# Redimensiona a imagem para o tamanho original
image = Image.fromarray(mountain)
resized_image = image.resize((width, height))

# Aplica um filtro nítido
sharp_image = resized_image.filter(ImageFilter.SHARPEN)

sharp_image.save('mountain.png')

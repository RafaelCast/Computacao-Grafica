import numpy as np
from PIL import Image

width = 512
height = 512

x, y = np.meshgrid(np.linspace(-1, 1, width), np.linspace(-1, 1, height))
d = np.sqrt(x*x + y*y)
sigma, mu = 1, -30
mountain = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )

mountain = (mountain - np.min(mountain)) / (np.max(mountain) - np.min(mountain)) * 255
mountain = mountain.astype(np.uint8)

i = 7
img = Image.fromarray(mountain)
img.save(f'mountain{i}.png')

random.uniform(0.1, 0.5)

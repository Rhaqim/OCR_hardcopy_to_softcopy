import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('text.png')
nparray = np.array(img)

print(nparray)

plt.imshow(img)
plt.show()


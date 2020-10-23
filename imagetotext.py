import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'D:\Programs\tesseract\tesseract.exe'
from PIL import Image

img = Image.open('text.png')
text = tess.image_to_string(img)

file = open('the_text.txt', 'w')

file.write(f'{text}')
file.close

print(text)
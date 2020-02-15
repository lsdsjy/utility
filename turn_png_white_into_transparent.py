from PIL import Image

img = Image.open('test.png')
data = list(img.getdata())
for i in range(0, len(data)):
    if data[i] == (255, 255, 255, 255):
        data[i] = (255, 255, 255, 0)
img.putdata(data)
img.save('t.png')

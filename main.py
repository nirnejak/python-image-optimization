from PIL import Image

with Image.open("input/4.png") as im:
  im_resized = im.resize((640, 480))
  im_resized.save("output/4.webp")
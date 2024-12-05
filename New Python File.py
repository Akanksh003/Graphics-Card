from PIL import Image

image = Image.open("rickass.png")
pixels = image.load()

out_file = open("finch.bin", "w")

for y in range(256):
  for x in range(128):
    try:
      out_file.write(chr(pixels[x, y]))
    except IndexError:
      out_file.write(chr(0))


import re
from PIL import Image
img = Image.open("oxygen.png")
row = [img.getpixel((x,img.height/2)) for x in range (img.width)]
row = row[::7]
print(row)
print("\n\n")
ords = [r for r,g,b,a in row if r==g==b] ## we just take the pixels that have the same values for RGB
print(ords) ##for every number we take the corrisponding chr in the ascii table through the chr function
nums = re.findall("\d+", "".join(map(chr,ords)))
print("".join(map(chr,map(int, nums)))) ## we must use another map so we can convert every element from string to int

from PIL import Image
im = Image.open("cave.jpg")
(w,h) = im.size

even = Image.new('RGB' , (w // 2 , h // 2))
odd = Image.new('RGB' , ( w // 2 , h // 2))

for i in range(w):             ## this iterates through every pixel like in a matrix
    for j in range(h):
        p = im.getpixel((i,j))  ## given the cordinates it access the pixel
        if(i+j)%2 == 1:
            odd.putpixel ((i //2 , j //2 ),p) ##modifies the pixel at the given cordinates
        else:
           even.putpixel((i // 2, j // 2), p) ## division without the rest
even.save('even.jpg')
odd.save('odd.jpg')

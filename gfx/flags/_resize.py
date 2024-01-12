#!/usr/bin/env python

from PIL import Image
import os
#compare = Image.new('RGBA', (800,600), (0,0,0,0))
overlay = Image.open("../SmallOverlay.png").convert("RGBA") 
#y = 0
for file in os.listdir('.'):
    print(file)
    if "." in file:
        if file.split('.')[1] == 'tga':
            image = Image.open(file)
            image.resize((41, 26)).save('medium/'+file)
            small = image.resize((10, 7)).convert("RGBA")
            #compare.paste(small, (1,1+y*8), small)
            small = Image.alpha_composite(small, overlay)
            #compare.paste(small, (12,1+y*8), small)
            small.save('small/'+file)
            #y += 1
#compare.show()
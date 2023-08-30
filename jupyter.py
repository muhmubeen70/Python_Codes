#Assignment 1: Building a Better Contact Sheet

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

images=[]
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')
img = image.split()
font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 45)
    
#Red
for ratio in (0.1, 0.5, 0.9): 
    R = img[0].point(lambda i: i * ratio)
    G = img[1].point(lambda i: i * 1)
    B = img[2].point(lambda i: i * 1)
    
    img1 = Image.merge("RGB", (R,G,B))
    img2 = img1.crop((0,0,800,img1.height++50))
    
    d = ImageDraw.Draw(img2)
    d.text((5,img2.height-45), "chanel 0 intensity " + str(ratio), font=font, fill = img1.getpixel((0,50)))
        
    images.append(img2)

#Green
for ratio in (0.1, 0.5, 0.9): 
    R = img[0].point(lambda i: i * 1)
    G = img[1].point(lambda i: i * ratio)
    B = img[2].point(lambda i: i * 1)
    
    img1 = Image.merge("RGB", (R,G,B))
    img2 = img1.crop((0,0,800,img1.height++50))
    
    d = ImageDraw.Draw(img2)
    d.text((5,img2.height-45), "chanel 1 intensity " + str(ratio), font=font, fill = img1.getpixel((0,50)))
        
    images.append(img2)

#Blue
for ratio in (0.1, 0.5, 0.9): 
    R = img[0].point(lambda i: i * 1)
    G = img[1].point(lambda i: i * 1)
    B = img[2].point(lambda i: i * ratio)
    
    img1 = Image.merge("RGB", (R,G,B))
    img2 = img1.crop((0,0,800,img1.height++50))
    
    d = ImageDraw.Draw(img2)
    d.text((5,img2.height-45), "chanel 2 intensity " + str(ratio), font=font, fill = img1.getpixel((0,50)))
        
    images.append(img2)

# Contact Sheet
first_image=images[0]

contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    contact_sheet.paste(img, (x, y) ) 
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))

display(contact_sheet)
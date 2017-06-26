from PIL import Image, ImageDraw, ImageFont

image = Image.open("Lenna.png")
fnt = ImageFont.truetype("cour.ttf", 12)
width = image.size[0] 
height = image.size[1] 
bw_image = image.convert("L")
image2 = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image2)
pix_sum = 0
for y in range(height/8):
    for x in range(width/6):
        temp = bw_image.crop((6*x,8*y,6*x+5,8*y+7))
        for i in range(5):
            for j in range(7):
                pix = temp.load()
                pix_sum = pix_sum + pix[i, j]
        pix_sum = pix_sum // 64
        if (pix_sum > 40 and pix_sum <= 55):
            draw.text((6*x,8*y), ".", font=fnt)
        elif (pix_sum > 55 and pix_sum <= 71):
            draw.text((6*x,8*y), ",", font=fnt)
        elif (pix_sum > 71 and pix_sum <= 86):
            draw.text((6*x,8*y), ":", font=fnt)
        elif (pix_sum > 86 and pix_sum <= 101):
            draw.text((6*x,8*y), ";", font=fnt)
        elif (pix_sum > 101 and pix_sum <= 120):
            draw.text((6*x,8*y), "o", font=fnt)            
        elif (pix_sum > 120 and pix_sum <= 145):
            draw.text((6*x,8*y), "0", font=fnt)
        elif (pix_sum > 145 and pix_sum <= 170):
            draw.text((6*x,8*y), "8", font=fnt)
        elif (pix_sum > 170 and pix_sum <= 200):    
            draw.text((6*x,8*y), "*", font=fnt)
        elif (pix_sum > 200 and pix_sum <= 220):
            draw.text((6*x,8*y), "#", font=fnt)            
        elif pix_sum > 220:
            draw.text((6*x,8*y), "@", font=fnt)
image2.show()

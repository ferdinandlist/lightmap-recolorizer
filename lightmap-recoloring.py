from PIL import Image

im = Image.open('lm_0000.tga')
rgb_im = im.convert('RGB')
output = Image.new( mode="RGB", size = im.size );

manipulationThreshold = 175 # pixels with r,g,b values larger than this wont be manipulated
maxDeviance = 40 # the maximum deviance of r,g,b values for a pixel to qualify as grey
targetR = 6
targetG = 9
targetB = 15

#for debuging
#targetR = 150 
#targetG = 0
#targetB = 0

for row in range(im.size[0]) :
	print("row" + str(row))
	for col in range(im.size[1]):
		r, g, b = rgb_im.getpixel((row, col))
		if r+g+b > manipulationThreshold*3:
			output.putpixel( (row,col), ( r, g, b, 255 ) ) # keep the original pixel
		else:
			if abs(r-g) < maxDeviance and abs(r-b) < maxDeviance and abs(g-b) < maxDeviance:
				output.putpixel( (row,col), ( r+targetR, g+targetG, b+targetB, 255 ) ) # store a modified pixel
			else:
				output.putpixel( (row,col), ( r, g, b, 255 ) ) # keep the original pixel

output.save("./output.tga", "TGA")
output.show()


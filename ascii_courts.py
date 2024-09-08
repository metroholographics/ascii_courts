import sys
from wand.image import Image 
from wand.display import display

img_path = "images/test.jpg"

#ascii_map = '''   `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'''
ascii_map = '''  .:-=+*#%@'''

def load_image(img_path):
	try:
		img = Image(filename=img_path)
		print("Successfully loaded image")
		print(f"{img.width} x {img.height}")
	except:
		print("Couldn't open file")
		sys.exit(0)

	return img

def init_pixel_array(img):
	raw_px_list = img.export_pixels(x=0,y=0, width = img.width, height = img.height, channel_map='RGB')
	
	new_arr = []
	for val in range(0, len(raw_px_list), 3):
		new_arr.append((raw_px_list[val], 
						raw_px_list[val + 1],
						raw_px_list[val + 2]))
	return new_arr

def rgb_to_bright(pixel_rgb_list):
	each_px_brightness = []
	for color in pixel_rgb_list:
		each_px_brightness.append(calc_brightness(color))
	return each_px_brightness

def calc_brightness(rgb):
	return  round((rgb[0] + rgb[1] + rgb[2]) / 3)

def bright_to_ascii(bright_list):
	char_list = []
	conversion = 255 / (len(ascii_map) - 1)
	for val in bright_list:
		idx = round(val / conversion)
		#print(len(ascii_map), val,conversion,idx)
		char_list.append(ascii_map[idx])
	return char_list

def display_ascii_image(ascii_char_list):
	for i in range(0, len(ascii_values)):
		if i % img.width == 0:
			print(f"\n{ascii_values[i]}", end="")
		else:
			print(f"{ascii_values[i]}", end = "")
	print("")


if __name__ == '__main__':
	img = load_image(img_path)
	img.sample(100, 50)
	img.format = 'RGB'
	px_rgb_list = init_pixel_array(img)
	px_brightness = rgb_to_bright(px_rgb_list)
	ascii_values = bright_to_ascii(px_brightness)

	display_ascii_image(ascii_values)

	img.destroy()

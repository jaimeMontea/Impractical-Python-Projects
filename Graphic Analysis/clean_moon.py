"""Median pixels in a series of images to produce a single stacked image."""
import os
from PIL import Image
import statistics

print("\nstart stacking images...")
# list images in directory
os.chdir('moon_cropped')
images = os.listdir()

# loop through images and extract RGB channels as separate lists
red_data = []
green_data = []
blue_data = []
for image in images:
    with Image.open(image) as img:
        if image == images[0]:  # get size of 1st cropped image
            img_size = img.size  # width-height tuple to use later
        red_data.append(list(img.getdata(0)))
        green_data.append(list(img.getdata(1)))
        blue_data.append(list(img.getdata(2)))

med_red = [int(statistics.median(x)) for x in zip(*red_data)]
med_blue = [int(statistics.median(x)) for x in zip(*blue_data)]
med_green = [int(statistics.median(x)) for x in zip(*green_data)]

merged_data = [(x) for x in zip(med_red, med_green, med_blue)]
stacked = Image.new('RGB', (img_size))
stacked.putdata(merged_data)
stacked.show()

stacked.save('clean_moon.png', 'PNG')

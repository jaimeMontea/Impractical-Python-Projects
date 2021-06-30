The objectif of this project is to crop, scale, stack, and enhance images to create a clearer photograph of Jupiter. 
The initial images which are going to be treated are in the folder "video_frames" which consist in several frames of a video made of Jupiter. 

The technique used here is called "image stacking", in which many photos—some good, some bad—are averaged together, or stacked, into a single image. 
With enough photos, the persistent, unchanging features (like a planet’s surface) dominate transient features (like a stray cloud). This allows astrophotographers 
to increase magnification limits, as well as compensate for less-than-optimal seeing conditions.

The script "crop_n_scale_images.py" crops the images in the "video_frames" folder to a tightly-fitting box around the planet and saves the results in the "cropped" folder. 
The script "stack_images.py" averages the pixels of the iamges of the previous folder to produce a single stacked image. 
The script "enhance_image.py" runs some enhancement filters (brightness, contrast, color) on an image and then saves the results. The final output is "enhanced.tif". 

Modules used: PIL, shutil, os, sys

The script "clean_moon.py" uses another image-stack technique. It takes all images from the moon_cropped folder and calculates the median value of red, blue and green pixels to remove a nonstationary object. 

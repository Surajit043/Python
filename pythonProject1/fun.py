import imageio
from pathlib import Path

# the path to the source folder of your images
image_path = Path('source_images')
# create a list of all .jpg files
images = list(image_path.glob('*.jpg'))
# read these images and save them to a list
image_list = []
for file_name in images:
    image_list.append(imageio.imread(file_name))

# create the animated image from the list
imageio.mimwrite('animated_from_images.gif', image_list)
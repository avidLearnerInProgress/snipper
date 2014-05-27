import sys
import os.path
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

def check_args():
  if sys.argv[0] == None or sys.argv[1] == None:
    print "You need to supply some parameters!"
    exit()
  if len(sys.argv) < 3:
    print "You need to supply at least two parameters"
    exit()

def open_file(image_to_open):
  picture = Image(filename=image_to_open)
  return picture

def resize_image(image_to_resize, height):
  picture = image_to_resize
  picture.resize(315, height)
  return picture

def print_dimensions(image_to_test):
  picture = image_to_test
  print picture.size

def calculate_height(image_to_calculate):
  picture = image_to_calculate
  height = picture.height
  height = float(height)
  width = picture.width
  width = float(width)
  absolute_width = 315.0
  percent = 100 * (absolute_width / width)
  calculated_height = (percent * height) / 100
  return int(calculated_height)

def check_calculated_height(height_one, height_two):
  if height_one != height_two:
    print "Right now, this script assumes both images are the same height"
    print "This will be changed later on, but in the mean time, sorry. I gotta quit"
    exit()

def create_border(calculated_height):
  if(os.path.isfile('border.png') == False):
    with Color('white') as bg:
      with Image(width=10, height=calculated_height, background=bg) as img:
        img.save(filename='border.png')

def composite_images(image_one, image_two, border):
  img_one = image_one
  img_two = image_two
  img_border = border
  height = img_one.height
  if(os.path.isfile('composite_image.png') == False):
    with Color('white') as bg:
      with Image(height=height, width=640, background=bg) as img:
        img.composite(img_one, left=0, top=0)
        img.composite(img_border, left=315, top=0)
        img.composite(img_two, left=325, top=0)
        img.save(filename='composite_image.png')


def main():
  file_one = sys.argv[1]
  file_two = sys.argv[2]
  check_args()
  image_one = open_file(file_one)
  image_two = open_file(file_two)
  print_dimensions(image_one)
  print_dimensions(image_two)
  calculated_height_one = calculate_height(image_one)
  calculated_height_two = calculate_height(image_two)
  check_calculated_height(calculated_height_one, calculated_height_two)
  image_one = resize_image(image_one, calculated_height_one)
  image_two = resize_image(image_two, calculated_height_two)
  create_border(calculated_height_one)
  border = open_file('border.png')
  print_dimensions(image_one)
  print_dimensions(image_two)
  composite_images(image_one, image_two, border)


if __name__ == '__main__':
  main()

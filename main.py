import sys
from wand.image import Image

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

def resize(image_to_resize):
  picture = image_to_resize
  picture.resize(315)

def main():
  file_one = sys.argv[1]
  file_two = sys.argv[2]
  check_args()
  image_one = open_file(file_one)
  image_two = open_file(file_two)


if __name__ == '__main__':
  main()

import sys
import os
from PIL import ImageOps
from PIL import Image

def main():
    shirt_overlay()

def shirt_overlay():
    # confirm that 2 args were given
    if arg_checker(3) == False:
        sys.exit("Please provide 2 arguments input image and output image.")

    # confirm input extention is .jpg .jpeg or.png
    if exten_checker(sys.argv[1], ["jpg", "jpeg", "png"]) == False:
        sys.exit("Incorrect file type. Please provide either .jpg, .jpeg, or .png ")

    # confirm input file exits
    if os.path.exists(sys.argv[1]) == False:
        sys.exit("File does not exist") 

    # input and output dont have the same file path 
    if sys.argv[1] == sys.argv[2]:
        sys.exit("Input file and output file must be diffrent")

    # open the image
    before = Image.open(sys.argv[1])
    shirt = Image.open("images/shirt.png")
    # resize the image
    before = ImageOps.fit(before, (600,600))
    # paste the shirt image over the input
    before.paste(shirt, shirt)
    # save the image
    before.save(sys.argv[2])
    # shirt.save(sys.argv[2])

def exten_checker(file, extention):
    file = file.split(".")[-1]
    for exten in extention:
        if file == exten:
            return True

# check that proper amounts of args are given
def arg_checker(n):
    if len(sys.argv) == n:
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()
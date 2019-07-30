from PIL import Image
import math
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(imgName):
    im = Image.open(imgName)
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(myImg):
    myImg.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(imgO, new_picture):
    imgO.save(new_picture)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(im):
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    colorpixels = list(im.getdata())
    list_length = len(colorpixels)
    half_pic = int(list_length/2)


    for i in range(half_pic):
        reddef = colorpixels[i][0]
        greendef = colorpixels[i][1]
        bluedef = colorpixels[i][2]
        sum = reddef + greendef + bluedef

        if sum < 182:
            colorpixels[i] = darkBlue
        elif sum > 182 and sum < 364:
            colorpixels[i] = red
        elif sum > 364 and sum < 546:
            colorpixels[i] = lightBlue
        else:
            colorpixels[i] = yellow

    obamapb = im.putdata(colorpixels)
    def save_img(im, obamapb):
        im.save(obamapb)
    save_img(im, "obamapb.jpg")
    newpicture = load_img("obamapb.jpg")
    show_img(newpicture)

def grayscale(im):
    colorpixels = list(im.getdata())
    list_length = len(colorpixels)

    for i in range(list_length):
        reddef = colorpixels[i][0]
        greendef = colorpixels[i][1]
        bluedef = colorpixels[i][2]
        sum = reddef + greendef + bluedef
        average = sum/3
        gray = (int(average), int(average), int(average))

        colorpixels[i] = gray
    graypb = im.putdata(colorpixels)
    def save_img(im, graypb):
        im.save(graypb)
    save_img(im, "graybooks.jpg")
    newpicture = load_img("graybooks.jpg")
    show_img(newpicture)

def emphasize(im):
    red = (217, 26, 33)
    colorpixels = list(im.getdata())
    list_length = len(colorpixels)

    for i in range(list_length):
        reddef = colorpixels[i][0]
        greendef = colorpixels[i][1]
        bluedef = colorpixels[i][2]
        sum = reddef + greendef + bluedef
        average = sum/3
        gray = (int(average), int(average), int(average))

        if greendef < 50 and bluedef < 50:
            colorpixels[i] = red
        else:
            colorpixels[i] = gray

    graypb = im.putdata(colorpixels)
    def save_img(im, graypb):
        im.save(graypb)
    save_img(im, "redbook.jpg")
    newpicture = load_img("redbook.jpg")
    show_img(newpicture)

im = load_img("pb.jpg")
show_img(im)
obamicon(im)
#grayscale(im)
#emphasize(im)

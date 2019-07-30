from PIL import Image

def load_img(imgName):
    im = Image.open(imgName)
    return im

def show_img(myImg):
    myImg.show()

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

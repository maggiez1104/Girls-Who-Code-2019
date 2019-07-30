from PIL import Image

def load_img(imgName):
    im = Image.open(imgName)
    return im

def show_img(myImg):
    myImg.show()

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

im = load_img("books.jfif")
show_img(im)
#obamicon(im)
grayscale(im)
#emphasize(im)

from grandfilters import *

def main():
    #change "file_name_here with your image link"
    myImg = load_img("pb.jpg")
    #pick one of the filters here
    newImg = nat_rainbow(myImg)

    newImg.show()

main()

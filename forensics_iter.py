# This is python 2 only :(
import Image


def def_func(pix_struc):
    print pix_struc
    return pix_struc

def iter_image(path_to_image, cb_func=def_func):
    im = Image.open(path_to_image)
    pix = im.load()
    pixels = []
    pixels_with_cb_func = []
    width = im.size[0]
    height = im.size[1]
    for i in range(0, height):
        for j in range(0, width):
            pixels.append(pix[j,i])
            pixels_with_cb_func.append(cb_func(pix[j,i]))
    return pixels, pixels_with_cb_func

def test_func(pix_struc):
    print chr(pix_struc[0])

iter_image('foo.jpg', test_func)

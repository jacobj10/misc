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

def diff_image(path1, path2):
    im1 = Image.open(path1)
    im2 = Image.open(path2)
    pix1 = im1.load()
    pix2 = im2.load()
    pixel_diff = []
    width1 = im1.size[0]
    width2 = im2.size[0]
    height1 = im1.size[1]
    height2 = im2.size[1]
    width = width1
    height = height1
    if width1 != width2:
        print "Widths not equal, using smaller"
        width = min(width1, width2)
    if height1 != height2:
        print "Heights not equal, using smaller"
        height = min(height1, height2)
    for i in range(0, height):
        for j in range(0, width):
            diffr = pix1[j,i][0] - pix2[j,i][0]
            diffg = pix1[j,i][1] - pix2[j,i][1]
            diffb = pix1[j,i][2] - pix2[j,i][2]
            pixel_diff.append((diffr, diffg, diffb))
    im3 = Image.new(im1.mode, im1.size)
    im3.putdata(pixel_diff)
    im3.save('diff.png')

    return pixel_diff

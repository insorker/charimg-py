from PIL import Image
import argparse as ap
from convertor import Charimg
import os


def initargparse():
    parser = ap.ArgumentParser(description='show image converted to character.')
    parser.add_argument('image', type=str, help='input the path of the image file.')
    parser.add_argument('-s', '--scale', type=int, nargs=2, default=(1, 2), help='input the scale factor. more infomation in readme')
    parser.add_argument('-w', '--towidth', action='store_true', help='draw charimg with the max suitable width(same as the width of the screen)')
    parser.add_argument('-c', '--color', type=int, default=Charimg.Color.GREY, metavar='', help='choose the color type : 0 for grey; 1 for rgb(not available yet)')
    return parser.parse_args()

if __name__ == '__main__':
    args = initargparse()

    with Image.open(args.image) as img:
        cmdinfo = {
            'size': [os.get_terminal_size().columns, os.get_terminal_size().lines],
        }

        charimg = Charimg(img, cmdinfo, args.scale)
        if args.towidth:
            charimg.resize2w()
        else:
            charimg.resize()
        charimg.draw(args.color)
        charimg.print()
        # charimg.save('test1.png')
        # os.system('scp test1.png /mnt/c/Users/qwe/Desktop/test1.png')

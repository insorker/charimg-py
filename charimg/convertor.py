from PIL import Image
from enum import Enum


class Charimg:
    class Color(Enum):
        GREY = 0
        RGB = 1
    ascii_char = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    ascii_char_len = len(ascii_char)
    ascii_char_str = ''
    
    def __init__(self, image, cmdinfo, factor=(1, 2)):
        self.image = image
        self.cmdinfo = cmdinfo
        self.factor = factor
    
    def resize(self):
        img_size = self.image.size
        cmd_size = self.cmdinfo['size']
        factor = [img_size[i] / cmd_size[i] / self.factor[i] for i in range(2)]

        if factor[0] > 1 or factor[1] > 1:
            img_size = [int(length / max(factor)) for length in img_size]
        self.image = self.image.resize(img_size, Image.ANTIALIAS)

    def resize2w(self):
        img_size = self.image.size
        cmd_size = self.cmdinfo['size']
        factor = img_size[0] / cmd_size[0] / self.factor[0]
        img_size = [int(length / factor) for length in img_size]
        self.image = self.image.resize(img_size, Image.ANTIALIAS)

    def draw(self, color=Color.GREY):
        Charimg.ascii_char_str = ''
        w, h = self.image.size

        for j in range(0, h, self.factor[1]):
            for i in range(0, w, self.factor[0]):
                pix = self.image.getpixel((i, j))
                if color == Charimg.Color.GREY:
                    Charimg.ascii_char_str += Charimg.rgb2greychar(*pix)
                elif color == Charimg.Color.RGB:
                    Charimg.ascii_char_str += ''
            Charimg.ascii_char_str += '\n'

        Charimg.ascii_char_str = Charimg.ascii_char_str.rstrip('\n')

    def print(self):
        print(Charimg.ascii_char_str)

    def save(self, name):
        self.image.save(name)

    @staticmethod
    def rgb2greychar(r, g, b, a=256):
        if a == 0:
            return ""

        grey = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        ascii_char_idx = grey * Charimg.ascii_char_len // 255
        return Charimg.ascii_char[ascii_char_idx]

    @staticmethod
    def rgb2rgbchar():
        print("Not yet, building...")
        pass

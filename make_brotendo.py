import os
import random
from PIL import Image, ImageDraw, ImageFont

erics = ['./eric/' + f for f in os.listdir('./eric')]
fonts = []
for fdir in os.listdir('./fonts'):
    for f in os.listdir('./fonts/'+fdir):
        if f.endswith('.ttf'):
            fonts.append(f'./fonts/{fdir}/{f}')


def find_fs(font, text, w):
    print(font)
    w = int(w * 0.5)
    print(w)
    size = 20
    fnt = ImageFont.truetype(font, size)
    while fnt.getsize(text)[0] < w:
        size = int(size * 1.5)
        fnt = ImageFont.truetype(font, size)
    return fnt


def add_caption(im, caption, top):
    W, H = im.size
    font = random.choice(fonts)
    fnt = find_fs(font, caption, W)

    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(caption, font=fnt)
    if top:
        draw.text(((W - w) / 2, (h * 1.2) - h), caption, fill="white", stroke_fill="black", stroke_width=int(W / 200),
                  font=fnt)
    else:
        draw.text(((W - w) / 2, (H - h * 1.2)), caption, fill="white", stroke_fill="black", stroke_width=int(W / 200),
                  font=fnt)


def make_brotendo(TOP_TEXT):
    BOTTOM_TEXT = "brotendo"
    im = Image.open(random.choice(erics))
    add_caption(im, TOP_TEXT, True)
    add_caption(im, BOTTOM_TEXT, False)
    im.save("hello.png", "PNG")


make_brotendo("give me a different eric pls")


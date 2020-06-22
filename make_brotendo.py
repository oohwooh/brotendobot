import os
import random
from io import BytesIO
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
        draw.text(((W - w) / 2, (h * 1) - h), caption, fill="white", stroke_fill="black", stroke_width=int(W / 200),
                  font=fnt)
    else:
        draw.text(((W - w) / 2, (H - h * 1.2)), caption, fill="white", stroke_fill="black", stroke_width=int(W / 200),
                  font=fnt)


from flask import Flask, send_file, request

app = Flask(__name__)

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


@app.route('/<path:path>')
def make_brotendo(path):
    im = Image.open(random.choice(erics))
    add_caption(im, os.path.splitext(path)[0], True)
    add_caption(im, "brotendo", False)
    return serve_pil_image(im)


app.run(host="0.0.0.0", port=3333)

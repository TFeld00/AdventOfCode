from PIL import Image

r = []
DAY = 'img/img'

COLS = {
    '.': (255, 255, 255),
    '#': (0, 0, 0),
}
COLS2 = {p: c for c, p in COLS.items()}

WRITE_IMG = 1
READ_IMG = 1

if WRITE_IMG:
    with open(f'{DAY}.txt', 'r') as F:
        for l in F:
            r += [l.rstrip('\n')]

    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img = Image.new('RGB', (len(r[0]), len(r)), "white")
    pixels = img.load()  # create the pixel map

    for i, l in enumerate(r):
        for j, c in enumerate(l):
            pixels[j, i] = COLS.get(c, (ord(c), 0, 0))

    img.show()

    img.save(f"{DAY}.png")

if READ_IMG:
    r2 = []
    with Image.open(f"{DAY}.png") as img:
        pixels = img.load()
        w, h = img.size
        for i in range(h):
            l = ''
            for j in range(w):
                R, G, B = pixels[j, i]
                l += COLS2.get((R, G, B), chr(R))
            r2 += [l]

    with open(f'{DAY}_2.txt', 'w') as F:
        F.write('\n'.join(r2) + '\n')

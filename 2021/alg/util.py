def parse_with_headers(F):
    d = {}
    n = ''
    r = []
    for l in F:
        if not l:
            d[n] = r
            n = ''
            r = []
        elif l and not n:
            n = l
        elif n:
            r += [l]
    if r:
        d[n] = r
    return d


def parse_no_headers(F):
    d = []
    r = []
    for l in F:
        if not l:
            d += [r]
            r = []
        else:
            r += [l]
    if r:
        d += [r]
    return d


def parse_skip_headers(F):
    d = []
    r = []
    n = ''
    for l in F:
        if not l:
            d += [r]
            n = ''
            r = []
        elif l and not n:
            n = l
        elif n:
            r += [l]
    if r:
        d += [r]
    return d


def get_neigbors_orto(m, y, x):
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        X, Y = x+dx, y+dy
        if 0 <= X < len(m[0]) and 0 <= Y < len(m):
            yield (Y, X, m[Y][X])


def get_neigbors_diag(m, y, x):
    for dx in (-1, 1):
        for dy in (-1, 1):
            X, Y = x+dx, y+dy
            if 0 <= X < len(m[0]) and 0 <= Y < len(m):
                yield (Y, X, m[Y][X])


def get_neigbors_both(m, y, x, includeSelf=False):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == dy == 0 == includeSelf:
                continue
            X, Y = x+dx, y+dy
            if 0 <= X < len(m[0]) and 0 <= Y < len(m):
                yield (Y, X, m[Y][X])

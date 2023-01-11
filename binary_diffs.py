class BinDiff:
    def __init__(self, start: int, end: int, vals: list[int, int]):
        self.start = start
        self.end = end
        self.vals = vals

    def __len__(self):
        return self.end - self.start

    @property
    def val1(self):
        return self.vals[0]

    @property
    def val2(self):
        return self.vals[1]


def diff_find(scroll_nom, codex_nom):
    scroll = open(scroll_nom, "rb")
    codex = open(codex_nom, "rb")
    s, c = b'', b''
    back = {}

    def cont():
        while True:
            s = scroll.read(1)
            c = codex.read(1)
            if not s:
                return False
            if s != c:
                return True

    while cont():
        start = scroll.tell()
        scroll_val, codex_vall = [], []
        while s != c:
            s = scroll.read(1)
            c = codex.read(1)
            scroll_val += s
            codex_vall += c
        end = scroll.tell()
        back[start] = BinDiff(start, end, )
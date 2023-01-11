class BinDiff:
    def __init__(self, start: int, vals: tuple[list[bytes], list[bytes]]):
        self.start = start
        self.vals = vals

    def __len__(self):
        return len(self.vals[0])

    @property
    def end(self):
        return self.start + len(self)

    @property
    def val1(self):
        return self.vals[0]

    @property
    def val2(self):
        return self.vals[1]


def diff_find(scroll_nom: str, codex_nom: str) -> dict[int, BinDiff]:
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
            scroll_val += s
            codex_vall += c
            s = scroll.read(1)
            c = codex.read(1)
        back[start] = BinDiff(start, (scroll_val, codex_vall))
    scroll.close()
    codex.close()
    return back


def diff_reduce(scroll_nom: str, codex_nom: str, diffs: dict[int, BinDiff]):
    scroll = open(scroll_nom, "rb")
    codex = open(codex_nom, "rb")

    for diff in diffs.values():
        scroll.seek(diff.start)
        codex.seek(diff.start)
        s = scroll.read(len(diff))
        c = codex.read(len(diff))
        if s != c:
            del diffs[diff.start]

    return diffs



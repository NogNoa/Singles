import pathlib

def purge(name: str, value: list[dict]):
    for d in value[:-1]:
        filo = blog / (name + '_' + d['hash'] + d['size'] + d['ext'])
        filo.unlink()

blog = pathlib.Path("C:/Users/Noga/downloads/A blog dedicated to all your favorite moments on Tumblr_files")
fili = {}
for filo in blog.iterdir():
    stem, ext = filo.stem, filo.suffix
    tag, _, rest = stem.partition("_")
    name, _, rest = rest.partition("_")
    if not rest:
        continue
    hash, sep, size = rest.partition("_")
    if not size:
        size, hash = hash, ""
    hash += sep
    size = int(size)
    if tag in fili.keys():
        if name in fili[tag].keys():
            fili[tag][name].append({"hash": hash, "size": size, "ext": ext})
        else:
            fili[tag][name] = [{"hash": hash, "size": size, "ext": ext}]
    else:
        fili[tag] = {name: [{"hash": hash, "size": size, "ext": ext}]}
for tag in fili.keys():
    for name in fili[tag].keys():
        fili[tag][name].sort(key=(lambda n: n['size']))  # small first
        purge(f"{tag}_{name}", fili[tag][name])


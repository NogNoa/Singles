import pathlib

def purge(name: str, value: list[dict]):
    for d in value[:-1]:
        filo = blog / f"{name}_{d['hash']}{d['size']}{d['ext']}"
        filo.unlink()

blog = pathlib.Path("C:/Users/Noga/downloads/A blog dedicated to all your favorite moments on Tumblr_files")
fili = {}
for file in blog.iterdir():
    stem, ext = file.stem, file.suffix
    tag, _, rest = stem.partition("_")
    name, _, rest = rest.partition("_")
    if not rest:
        continue
    hash, sep, size = rest.partition("_")
    if not size:
        size, hash = hash, ""
    hash += sep
    size = int(size)
    try:  # to find tag in fili:
        try:  # to find name in fili[tag]:
            fili[tag][name].append({"hash": hash, "size": size, "ext": ext})
        except KeyError:
            fili[tag][name] = [{"hash": hash, "size": size, "ext": ext}]
    except KeyError:
        fili[tag] = {name: [{"hash": hash, "size": size, "ext": ext}]}


for tag in fili.keys():
    tag_dict = fili[tag]
    for name in tag_dict.keys():
        tag_dict[name].sort(key=(lambda n: n['size']))  # small first
        purge(f"{tag}_{name}", tag_dict[name])


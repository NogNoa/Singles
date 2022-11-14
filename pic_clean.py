import pathlib

blog = pathlib.Path("C:/Users/Noga/downloads/A blog dedicated to all your favorite moments on Tumblr_files")
fili = {"other": []}
for file in blog.iterdir():
    stem, ext = file.stem, file.suffix
    tag, _, rest = stem.partition("_")
    name, _, rest = rest.partition("_")
    if not rest:
        fili["other"].append(file.name)
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
with open("fili.txt", "w+") as codex:
    codex.write(str(fili))

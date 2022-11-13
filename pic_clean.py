import pathlib

tumbler = pathlib.Path("C:/Users/Noga/downloads/A blog dedicated to all your favorite moments on Tumblr_files")
fili = {"tumblr": {}, "other": []}
for file in tumbler.iterdir():
    tag, _, rest = file.name.partition("_")
    if tag == "tumblr":
        name, _, rest = rest.partition("_")
        hash, _, rest = rest.partition("_")
        size, _, ext = rest.partition(".")
        size = int(size)
        try:
            fili["tumblr"][name][hash] = {"size": size, "ext": ext}
        except KeyError:
            fili["tumblr"][name] = {hash: {"size": size, "ext": ext}}
    elif rest:
        name, _, rest = rest.partition("_")
        if rest:
            size, _, ext = rest.partition(".")
            size = int(size)
            if tag in fili.keys():
                if name in fili[tag].keys():
                    fili[tag][name].append({"size": size, "ext": ext})
                else:
                    fili[tag][name] = [{"size": size, "ext": ext}]
            else:
                fili[tag] = {name: [size]}
        else:
            fili["other"].append(tag+"_"+name)
    else:
        fili["other"].append(tag)
with open("fili.json","w+") as codex:
    codex.write(str(fili))

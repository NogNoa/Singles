import pathlib

tumbler = pathlib.Path("C:/Users/Noga/downloads/A blog dedicated to all your favorite moments on Tumblr_files")
fili = {}
for file in tumbler.iterdir():
    tag, _, rest = file.name.partition("_")
    if tag == "tumblr":
        name, _, rest = rest.partition("_")
        hash, _, rest = rest.partition("_")
        size = int(rest.partition(".")[0])
        try:
            fili[name] += {hash: size}
        except KeyError:
            fili[name] = {hash: size}
    elif tag == 
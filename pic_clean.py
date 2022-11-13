import pathlib

tumbler = pathlib.Path("C:/Users/Noga/downloads/A blog dedicated to all your favorite moments on Tumblr_files")
fili = {}
for file in tumbler.iterdir():
    name, _, rest = file.name.partition("_")
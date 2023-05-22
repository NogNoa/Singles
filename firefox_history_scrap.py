import os
import json
import datetime

from functools import reduce


def scrap(scroll_nom) -> set:
    with open(f"{scroll_nom}.json", encoding="utf-8", mode="r") as scroll:
        rcvr = json.load(scroll)

    windows = rcvr["windows"] + rcvr["_closedWindows"]
    tabs = [window["tabs"] for window in windows]
    tabs = sum(tabs, [])
    tabs = tuple(filter(lambda tab: tab['entries'], tabs))
    urls = {tab["entries"][-1]["url"] for tab in tabs}
    return urls


def deleuze4(nom: str):
    parts = nom.partition(".jsonlz4")
    return parts[0] + parts[2]


def lz_jsonify(scroll_nom: str):
    codex_nom = scroll_nom + ".json"
    if "upgrade" in scroll_nom:
        scroll_nom = "upgrade.jsonlz4-" + scroll_nom.partition("-")[2]
    elif "bak" in scroll_nom:
        scroll_nom += "lz4"
    else:
        scroll_nom += ".jsonlz4"
    os.system(r"D:\Scripts\mozlz4.exe" + f" {scroll_nom} > {codex_nom}")


if __name__ == "__main__":
    folder = r"C:\Users\Noga\AppData\Roaming\Mozilla\Firefox\Profiles\8e2xs3ha.default-release\sessionstore-backups"
    os.chdir(folder)
    library = tuple(deleuze4(nom) for nom in os.listdir() if ".jsonlz4" in nom) + ("recovery.bak",)
    for scroll_nom in library:
        lz_jsonify(scroll_nom)

    urls_list = [scrap(file) for file in library]

    urls_set = reduce(set.union, urls_list)
    codex_nom = f"urls-{str(datetime.date.today())}.txt"
    with open(codex_nom, "w+") as codex:
        codex.write("\n".join(urls_set))

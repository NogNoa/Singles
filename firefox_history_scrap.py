import os
from functools import reduce
import json


def scrap(scroll_nom) -> set:
    with open(f"{scroll_nom}.json", encoding="utf-8", mode="r") as scroll:
        rcvr = json.load(scroll)

    windows = rcvr["windows"] + rcvr["_closedWindows"]
    tabs = [window["tabs"] for window in windows]
    tabs = sum(tabs, [])
    tabs = tuple(filter(lambda tab: tab['entries'], tabs))
    urls = {tab["entries"][-1]["url"] for tab in tabs}
    return urls


def lz_jsonify(scroll_nom):
    codex_nom = scroll_nom + ".json"
    if "upgrade" in scroll_nom:
        scroll_nom = "upgrade.jsonlz4-" + scroll_nom.partition(".")[2]
    else:
        scroll_nom = scroll_nom + ".jsonlz4"
    os.system(r"D:\Scripts\mozlz4.exe" + f" {scroll_nom} > {codex_nom}")


if __name__ == "__main__":
    library = ["previous", "recovery",
               "upgrade.20230406114409"]
    for scroll_nom in library:
        lz_jsonify(scroll_nom)

    urls_list = [scrap(file) for file in library]
    try:
        with open("urls.txt", "r") as scroll:
            urls_list.append(set(scroll.readlines()))
    except FileNotFoundError:
        pass

    urls_set = reduce(set.union, urls_list)
    with open("urls.txt", "w+") as codex:
        codex.writelines(urls_set)

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
    os.system(r"D:\Scripts\mozlz4.exe " + scroll_nom + ".jsonlz4 > " + scroll_nom + ".json")


if __name__ == "__main__":
    library = ["previous", "recovery", "recovery.bak",
               "upgrade.20230309232128",
               "upgrade.20230214051806",
               "upgrade.20230227191043"]
    for scroll_nom in library:
        lz_jsonify(scroll_nom)

    urls_list = [scrap(file) for file in library]
    try:
        with open("url.txt", "r") as scroll:
            urls_list.extend(scroll.readlines())
    except FileNotFoundError:
        pass

    urls_set = reduce(set.union, urls_list)
    with open("urls.txt", "w+") as codex:
        codex.writelines(urls_set)
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


urls_list = [scrap(file) for file in ["previous", "recovery", "recovery.bak",
                                      "upgrade.20230309232128",
                                      "upgrade.20230214051806",
                                      "upgrade.20230227191043"]]
try:
    with open("url.txt", "r") as scroll:
        urls_list.append(scroll.readlines)
except FileNotFoundError:
    pass

urls_set = reduce(set.union, urls_list)
with open("urls.txt", "w+") as codex:
    codex.writelines(urls_set)

#!/usr/bin/python3
import os
import shutil
from time import sleep

print(r"""
  _  _______  ______  __          ___           _                 ______                     
 | |/ /  __ \|  ____| \ \        / (_)         | |               |___  /                     
 | ' /| |  | | |__     \ \  /\  / / _ _ __   __| | _____      __    / / ___  _ __   ___  ___ 
 |  < | |  | |  __|     \ \/  \/ / | | '_ \ / _` |/ _ \ \ /\ / /   / / / _ \| '_ \ / _ \/ __|
 | . \| |__| | |____     \  /\  /  | | | | | (_| | (_) \ V  V /   / /_| (_) | | | |  __/\__ \
 |_|\_\_____/|______|     \/  \/   |_|_| |_|\__,_|\___/ \_/\_/   /_____\___/|_| |_|\___||___/                                                                                             
""")

shortcuts: dict[str, list[int, int, int, int]] = {}
active = True

while active:

    selection = "1"

    if shortcuts:
        print("(1) Add shortcut")
        print("(2) List shortcuts")
        print("(3) Generate script")
        selection = input("=> ")
        print()

    if selection == "1":

        name = ""
        while not name:
            name = input("Shortcut name (Duplicate name will overwrite old one) => ")

        x_valid = False
        x_start = 0
        x_end = 0
        while not x_valid:
            x_start = ""
            while x_start == "" or not x_start.isdigit() or int(x_start) > 100:
                x_start = input("X-Start (0-100%) => ")

            x_end = ""
            while x_end == "" or not x_end.isdigit() or int(x_end) > 100:
                x_end = input("X-End (0-100%) => ")

            x_start = int(x_start)
            x_end = int(x_end)

            if x_end < x_start:
                print("X-End must be greater than X-Start\n")
                sleep(2)

            else:
                x_valid = True

        y_valid = False
        y_start = 0
        y_end = 0
        while not y_valid:
            y_start = ""
            while y_start == "" or not y_start.isdigit() or int(y_start) > 100:
                y_start = input("Y-Start (0-100%) => ")

            y_end = ""
            while y_end == "" or not y_end.isdigit() or int(y_end) > 100:
                y_end = input("Y-End (0-100%) => ")

            y_start = int(y_start)
            y_end = int(y_end)

            if y_end < y_start:
                print("Y-End must be greater than Y-Start\n")
                sleep(2)

            else:
                y_valid = True

        shortcuts[name] = [x_start, y_start, x_end, y_end]


    elif selection == "2" and shortcuts != {}:

        print("".join(
            [f"{n} | Xs: {shortcuts[n][0]}  Ys: {shortcuts[n][1]}  Xe: {shortcuts[n][2]} Ye: {shortcuts[n][3]}\n"
             for n in shortcuts]
        ))

        input("Press enter to continue...")

    elif selection == "3" and shortcuts != {}:

        shutil.rmtree("temp", True)
        shutil.copytree("template/contents", "contents")
        shutil.copy("template/metadata.desktop", "metadata.desktop")

        with open("contents/code/main.js", "a") as file:

            file.write("\n\n\n\n// CUSTOM ZONES\n")

            for name in shortcuts:
                name_spaceless = name.replace(" ", "")
                x_start, y_start, x_end, y_end = shortcuts[name]

                file.write(
                    f'\nregisterShortcut("kdewindowzones_{name_spaceless}", "KdeWindowZones: {name}", "", function () {{\n'
                    f'   move(workspace, 100, 100, {x_start}, {y_start}, {x_end - x_start}, {y_end - y_start})\n'
                    f'}});\n\n'
                )

        os.system("zip -r CustomKdeWindowZones.kwinscript contents metadata.desktop LICENSE")
        shutil.rmtree("contents")
        os.remove("metadata.desktop")


    else:
        print("INVALID OPTION")
        sleep(2)

    print("\n" * 321)

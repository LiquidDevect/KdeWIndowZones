import os

print(r"""
  _  _______  ______  __          ___           _                 ______                     
 | |/ /  __ \|  ____| \ \        / (_)         | |               |___  /                     
 | ' /| |  | | |__     \ \  /\  / / _ _ __   __| | _____      __    / / ___  _ __   ___  ___ 
 |  < | |  | |  __|     \ \/  \/ / | | '_ \ / _` |/ _ \ \ /\ / /   / / / _ \| '_ \ / _ \/ __|
 | . \| |__| | |____     \  /\  /  | | | | | (_| | (_) \ V  V /   / /_| (_) | | | |  __/\__ \
 |_|\_\_____/|______|     \/  \/   |_|_| |_|\__,_|\___/ \_/\_/   /_____\___/|_| |_|\___||___/                                                                                             
""")
print()

path = os.path.expanduser("~/.config/kglobalshortcutsrc")
kdeglobalshortcutsrc_old = open(path, "r").read()

print("Creating backup...")
open("kglobalshortcutsrc.bak", "w").writelines(kdeglobalshortcutsrc_old)

print("Clearing Shortcuts")
kdeglobalshortcutsrc_old = kdeglobalshortcutsrc_old.strip().split("\n")

kdeglobalshortcutsrc_new = ""

for line in kdeglobalshortcutsrc_old:
    if not line.startswith("kdewindowzones_"):
        kdeglobalshortcutsrc_new += line + "\n"

open(path, "w").write(kdeglobalshortcutsrc_new)

print("Cleared shortcuts!")
print("Please relog/restart to update system settings")
from subprocess import run
from main import ROOT_DIR

"""
File to convert the .ui files to .py
"""

print("COnverting UI to PY...:")

main_window = f"pyuic5 -x '{ROOT_DIR}/core/ui/qtwindow.ui'" \
           f" -o '{ROOT_DIR}/core/ui/qtwindow.py'"

dw_dialog = f"pyuic5 -x '{ROOT_DIR}/downloader/ui/download_dialog.ui'" \
           f" -o '{ROOT_DIR}/downloader/ui/download_dialog.py'"

emulation_config_dialog = f"pyuic5 -x '{ROOT_DIR}/config/ui/emuConfig_dialog.ui'" \
           f" -o '{ROOT_DIR}/config/ui/emuConfig_dialog.py'"
ui_list = [main_window, dw_dialog, emulation_config_dialog]

for ui_convertion in ui_list:
    run(ui_convertion, shell=True)

print("Done.")

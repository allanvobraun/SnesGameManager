from subprocess import run
from os import getcwd


root = getcwd()  # /home/allan/PycharmProjects/pyqt


# arquivo temporario que transforma de .ui para .py
comando1 = f"pyuic5 -x '{root}/core/ui/qtwindow.ui'" \
           f" -o '{root}/core/ui/qtwindow.py'"

comando2 = f"pyuic5 -x '{root}/downloader/ui/download_dialog.ui'" \
           f" -o '{root}/downloader/ui/download_dialog.py'"

run(comando1, shell=True)
run(comando2, shell=True)

print("Os aquivos foram convertidos.")


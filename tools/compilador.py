from subprocess import run

# arquivo temporario que transforma de .ui para .py
comando1 = "pyuic5 -x '/home/allan/PycharmProjects/pyqt/core/ui/qtwindow.ui'" \
           " -o '/home/allan/PycharmProjects/pyqt/core/ui/qtwindow.py'"

comando2 = "pyuic5 -x '/home/allan/PycharmProjects/pyqt/core/ui/download_dialog.ui'" \
           " -o '/home/allan/PycharmProjects/pyqt/core/ui/download_dialog.py'"

run(comando1, shell=True)
run(comando2, shell=True)



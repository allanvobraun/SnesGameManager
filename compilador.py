from subprocess import run

comando1 = "pyuic5 -x '/home/allan/PycharmProjects/pyqt/qtwindow.ui' -o '/home/allan/PycharmProjects/pyqt/qtwindow.py'"
comando2 = "pyuic5 -x '/home/allan/PycharmProjects/pyqt/download_dialog.ui'" \
           " -o '/home/allan/PycharmProjects/pyqt/download_dialog.py'"

run(comando1, shell=True)
run(comando2, shell=True)



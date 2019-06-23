from subprocess import run

comando = "pyuic5 -x '/home/allan/PycharmProjects/pyqt/qtwindow.ui' -o '/home/allan/PycharmProjects/pyqt/qtwindow.py'"

run(comando, shell=True)



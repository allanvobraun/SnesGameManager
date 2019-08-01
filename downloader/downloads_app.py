from time import sleep
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QDialog
from math import floor
from downloader.thread_fix import nongui
from downloader.ui.download_dialog import *
from downloader.format_download import download_cover
from main import ROOT_DIR
"""
Faz todo o processo para baixar as capas dos games
"""


class Flager(QObject):  # Classe para se criar gatilhos de eventos, ou signals
    downloaded = pyqtSignal()  # Sinaliza que um download foi completo


class DowloadThread(QThread):  # Classe para gerenciar o processo de download

    def __init__(self, roms):
        QThread.__init__(self)
        self.break_loop = False
        self.roms = roms
        self.flare = Flager()

    def __del__(self):
        print("Tread finished")
        self.wait()

    def break_thread(self):
        self.break_loop = True
        self.quit()

    def run(self):
        self.work()

    @nongui
    def work(self):
        for rom in self.roms:
            if self.break_loop:
                break
            download_cover(rom, out_path=f"{ROOT_DIR}/covers")
            self.flare.downloaded.emit()


class DownloadDialog(QDialog, Ui_DownloadDialog):  # Classe do popup de download
    def __init__(self, roms, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # atributos
        self.roms = roms
        self.roms_amount = len(self.roms)
        self.completed = 0
        self.percent = 0
        self.progressBar.setValue(self.percent)
        self.th = DowloadThread(self.roms)

        # conexões
        self.btCancel.clicked.connect(self.cancel)
        self.th.flare.downloaded.connect(self.add_progress)

    def start_download(self):  # começa a fazer o downlaod
        self.show()
        self.th.run()

    def cancel(self):  # quebra o processo de download
        self.th.break_thread()
        self.close()

    def add_progress(self):  # Lida com a barra de progresso
        self.completed += 1
        self.percent = floor((self.completed / self.roms_amount) * 100)
        self.progressBar.setValue(self.percent)

        if self.percent == 100:
            self.change_label("Download complete")
            sleep(0.5)
            self.close()

    def change_label(self, txt):  # Troca o texto do dialog
        self.label.setText(txt)

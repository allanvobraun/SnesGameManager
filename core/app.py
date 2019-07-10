import glob  # Usado para pegar o caminho do arquivo mais facilmente
from json import dump, load
from os import mkdir
from os.path import expanduser
from shutil import copy2
from subprocess import run

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtWidgets import QDesktopWidget, QFileDialog, QAbstractItemView


from downloader.downloads_app import DownloadDialog
from core.ui.qtwindow import *
from downloader.format_download import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)  # construtor do qtwidgets
        self.setupUi(self)  # setup do front end
        self.resize(750, 450)
        self.center()

        # atributos

        # tipos de arquivos suportados pelo emulador
        self.roms_extensions = ("7z", "bin", "bs", "fig", "mgd", "sfc", "smc", "swc", "zip")
        self.root = ROOT_DIR  # detect the current working directory
        self.imgs_folder = self.root + "/" + "covers"
        self.resources_folder = f"{ROOT_DIR}/resources"
        self.games_folder = ""
        self.roms_path = []  # caminho das roms carregadas pelo list_roms
        self.roms = []  # nomes das roms
        self.select_game = ""  # rom selecionada
        self.model = None  # modelo dos items da lista
        self.dwnl_dialog = DownloadDialog(self.roms, parent=self)
        self.app_icon = QtGui.QIcon()
        self.app_icon.addFile(f'{self.resources_folder}/icon.png', QtCore.QSize(256, 256))
        QtWidgets.QMainWindow.setWindowIcon(self, self.app_icon)
        self.setWindowIcon(self.app_icon)

        # conectores de widgets para metodos
        self.listGamesbox.setEditTriggers(QAbstractItemView.NoEditTriggers)  # torna a lista de games não editavel
        self.btPlay.clicked.connect(self.play_game)  # botão jogar
        self.actionOpen_roms_folder.triggered.connect(self.get_folder)  # ação para abrir o folder
        self.actionDownload_Game_Covers.triggered.connect(self.download_game_covers)  # baixar as capas
        self.btReload.clicked.connect(self.update_listbox)  # botao de recarregar
        self.listGamesbox.clicked.connect(self.game_selected)  # seletor de games

        # chamadas de função
        QtCore.QTimer.singleShot(50, self.load_folder)  # carrega informações do json
        QtCore.QTimer.singleShot(50, self.create_img_dir)  # cria diretorio
        QtCore.QTimer.singleShot(50, self.copy_df_img)  # copia a imagem padrão para o diretorio

    def download_game_covers(self):  # Requisita o download de cada capa da rom
        self.dwnl_dialog.set_roms(self.roms)
        self.dwnl_dialog.start_download()
        self.update_listbox()

    def play_game(self):  # roda o game selecionado
        if self.select_game != "":
            game = self.games_folder + "/" + self.select_game
            # run("snes9x-gtk '{}'".format(game), shell=True)
            run("zsnes '{}'".format(game), shell=True)

    def create_img_dir(self):  # cria o diretorio dascovers somente se não exixtir
        try:
            mkdir(self.imgs_folder)
        except FileExistsError:
            pass

    def copy_df_img(self):  # copia imagem padrão de capa para o diretorio de imagens
        file_path = f"{self.resources_folder}/none.png"
        copy2(file_path, self.imgs_folder)
        self.update_listbox()

    def save_folder(self):  # salva o caminho do arquivo
        with open(f'{ROOT_DIR}/save_path.json', 'w') as arquivo:
            dump({"path": self.games_folder}, arquivo)  # Grava o caminho em um json

    def load_folder(self):  # carrega o caminho especificado pelo json
        try:
            with open(f"{ROOT_DIR}/save_path.json", "r") as json_file:
                data = load(json_file)
                self.games_folder = data["path"]
        except (ValueError, OSError):
            self.games_folder = ""

        self.update_listbox() 

    def get_folder(self):  # Função para procurar uma pasta
        self.games_folder = QFileDialog.getExistingDirectory(self,  # Abre o explorador de arquivos
                                                             'Select a folder:',
                                                             expanduser("~"),  # abre o home do usuario como padrão
                                                             QFileDialog.ShowDirsOnly)  # mostre somente diretorios
        print(self.games_folder)
        self.save_folder()
        self.update_listbox()

    def list_roms(self):  # lista as roms contidas na pasta

        for file_type in self.roms_extensions:  # Adiciona o caminho absoluto de cada rom a lista
            self.roms_path.extend(glob.glob(self.games_folder + "/*." + file_type))

        self.roms = path_to_roms(self.roms_path)  # salva somente o nome das roms

        # print(self.roms_path)
        # print(self.roms)

    def display_listing_games(self):  # Coloca os games da pasta no listGamesbox
        self.model = QStandardItemModel(self.listGamesbox)

        for item in self.roms:
            img_file_path = ROOT_DIR + "/covers/" + format_gamename(item)

            if exists(img_file_path):
                game_icon = QIcon(img_file_path)
            else:
                game_icon = QIcon(ROOT_DIR + "/" + "covers/none.png")

            game = QStandardItem(game_icon, item)
            self.model.appendRow(game)
        self.model.sort(Qt.AscendingOrder)

        self.listGamesbox.setModel(self.model)

    def update_listbox(self):  # da um update das roms no listbox
        self.roms.clear()
        self.roms_path.clear()
        self.list_roms()
        self.display_listing_games()

    def game_selected(self, idx):  # identifica o game selecionado da lista
        # item = idx.row()
        self.select_game = self.model.itemFromIndex(idx).text()
        print(self.select_game)

    def center(self):  # centraliza a janela
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

# if __name__ == "__main__":
#     my_app = QtWidgets.QApplication([])
#     window = MainWindow()
#     window.show()
#     my_app.exec_()


def run_app():
    my_app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    my_app.exec_()

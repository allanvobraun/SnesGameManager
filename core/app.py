from PyQt5.QtWidgets import QDesktopWidget, QFileDialog, QAbstractItemView
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtCore import Qt
from core.ui.qtwindow import *
from core.ui.download_dialog import *
from os import getcwd, mkdir
from os.path import expanduser
from subprocess import run
import glob  # Usado para pegar o caminho do arquivo mais facilmente
from json import dump, load

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
        self.root = getcwd()   # detect the current working directory
        self.imgs_folder = self.root + "/" + "covers"
        self.games_folder = ""
        self.roms_path = []  # caminho das roms carregadas pelo list_roms
        self.roms = []  # nomes das roms
        self.select_game = ""  # rom selecionada
        self.model = None  # modelo dos items da lista

        # conectores de widgets para metodos
        self.listGamesbox.setEditTriggers(QAbstractItemView.NoEditTriggers)  # torna a lista de games não editavel
        self.btPlay.clicked.connect(self.play_game)  # botão jogar
        self.actionOpen_roms_folder.triggered.connect(self.get_folder)  # ação para abrir o folder
        self.actionDownload_Game_Covers.triggered.connect(self.get_game_covers)  # baixar as capas
        self.btReload.clicked.connect(self.update_listbox)  # botao de recarregar
        self.listGamesbox.clicked.connect(self.game_selected)  # seletor de games

        # chamadas de função
        QtCore.QTimer.singleShot(50, self.load_folder)  # carrega informações do json
        QtCore.QTimer.singleShot(50, self.create_img_dir)  # cria diretorio

    def get_game_covers(self):  # Faz o dowload de cada capa da rom
        for rom in self.roms:
            download_cover(rom, out_path="covers", allow_dups=False)
        self.update_listbox()

    def play_game(self):  # roda o game selecionado
        if self.select_game != "":
            game = self.games_folder + "/" + self.select_game
            run("snes9x-gtk '{}'".format(game), shell=True)

    def create_img_dir(self):  # cria o diretorio dascovers somente se não exixtir
        try:
            mkdir(self.imgs_folder)
        except FileExistsError:
            pass

    def save_folder(self):  # salva o caminho do arquivo
        with open('save_path.json', 'w') as arquivo:
            dump({"path": self.games_folder}, arquivo)  # Grava o caminho em um json

    def load_folder(self):  # carrega o caminho especificado pelo json
        try:
            with open("save_path.json", "r") as json_file:
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

        print("Caminho das roms = {}".format(self.roms_path))
        self.roms = self.format_rom_names(self.roms_path)  # salva somente o nome das roms

        # print(self.roms_path)
        # print(self.roms)

    def display_listing_games(self):  # Coloca os games da pasta no listGamesbox
        self.model = QStandardItemModel(self.listGamesbox)

        for item in self.roms:
            img_file_path = "covers/" + format_gamename(item)

            if exists(img_file_path):
                game_icon = QIcon(img_file_path)
            else:
                game_icon = QIcon("covers/none.png")

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

    @staticmethod
    def format_rom_names(rom_list):  # Função para extrair os nomes das roms de cada caminho
        extracted_names = []
        for path in rom_list:
            name = path.split("/")[-1]
            extracted_names.append(name)
        return extracted_names


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

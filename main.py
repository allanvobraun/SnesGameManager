from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QAbstractItemView
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from qtwindow import *

from os.path import expanduser
from subprocess import run
import glob  # Usado para pegar o caminho do arquivo mais facilmente
from json import dump, load

from format_download import download_cover


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)  # construtor do qtwidgets
        self.setupUi(self)  # setup do front end
        QtCore.QTimer.singleShot(50, self.load_folder)

        # atributos

        # tipos de arquivlos suportados pelo emulador
        self.roms_extensions = ("7z", "bin", "bs", "fig", "mgd", "sfc", "smc", "swc", "zip")
        self.games_folder = ""
        self.roms_path = []  # caminho das roms carregadas pelo list_roms
        self.roms = []  # nomes das roms
        self.select_game = ""  # rom selecionada

        # conectores de widgets para metodos
        self.listGamesbox.setEditTriggers(QAbstractItemView.NoEditTriggers)  # torna a lista de games não editavel
        self.btPlay.clicked.connect(self.play_game)  # botão jogar
        self.actionOpen_roms_folder.triggered.connect(self.get_folder)  # ação para abrir o folder
        self.actionDownload_Game_Covers.triggered.connect(self.get_game_covers)  # baixar as capas
        self.btReload.clicked.connect(self.update_listbox)  # botao de recarregar
        self.listGamesbox.clicked.connect(self.game_selected)  # seletor de games

    def get_game_covers(self):
        for rom in self.roms:
            print(rom)
            download_cover(rom, out_path="covers")

    def play_game(self):  # roda o game selecionado
        if self.select_game != "":
            game = self.games_folder + "/" + self.select_game
            print("snes9x '{}'".format(game))
            run("snes9x '{}'".format(game), shell=True)

    def save_folder(self):  # salva o caminho do arquivo
        with open('save_path.json', 'w') as arquivo:
            dump({"path": self.games_folder}, arquivo)  # Grava o caminho em um json

    def load_folder(self):
        try:
            with open("save_path.json", "r") as json_file:
                data = load(json_file)
                self.games_folder = data["path"]
        except (ValueError, OSError):
            self.games_folder = ""

        self.update_listbox()

    def get_folder(self):  # Função para procurar uma pasta
        print("get")

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

        # self.roms_path = glob.glob(self.games_folder + "/*.smc")  # separa as rom .smc da pasta
        print("Caminho das roms = {}".format(self.roms_path))
        self.roms = self.format_rom_names(self.roms_path)  # salva somente o nome das roms

        # print(self.roms_path)
        # print(self.roms)

    def display_listing_games(self):  # Coloca os games da pasta no listGamesbox
        model = QStandardItemModel(self.listGamesbox)  # modelo dos items

        for item in self.roms:
            game = QStandardItem(item)

            # Add the item to the model
            model.appendRow(game)

        self.listGamesbox.setModel(model)

    def update_listbox(self):  # da um update das roms no listbox
        self.list_roms()
        self.display_listing_games()

    def game_selected(self, idx):  # identifica o game selecionado da lista
        item = idx.row()
        self.select_game = self.roms[item]
        print(self.select_game)

    @staticmethod
    def format_rom_names(rom_list):  # Função para extrair os nomes das roms de cada caminho
        extracted_names = []
        for path in rom_list:
            name = path.split("/")[-1]
            extracted_names.append(name)
        return extracted_names


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

#  /home/allan/snes/teste.smc

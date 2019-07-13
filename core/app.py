import glob  # Usado para pegar o caminho do arquivo mais facilmente
from os import mkdir
from os.path import expanduser
from shutil import copy2
from subprocess import run
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtWidgets import QDesktopWidget, QFileDialog, QAbstractItemView, QMenu

from config.json_handler import get_obj_value, write_folder
from downloader.downloads_app import DownloadDialog
from config.emuConfig_app import EmuConfigDialog, EmulatorConfigs
from core.ui.qtwindow import *
from downloader.format_download import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)  # construtor do qtwidgets
        self.setupUi(self)  # setup do front end

        # configurações
        self.resize(750, 450)
        self.center()

        # atributos

        # tipos de arquivos suportados pelo emulador
        self.roms_extensions = ("7z", "bin", "bs", "fig", "mgd", "sfc", "smc", "swc", "zip")
        self.root = ROOT_DIR  # pasta raiz do projeto
        self.imgs_folder = self.root + "/" + "covers"
        self.resources_folder = f"{ROOT_DIR}/resources"
        self.games_folder = ""
        self.roms_path = []  # caminho das roms carregadas pelo list_roms
        self.roms = []  # nomes das roms
        self.select_game = ""  # rom selecionada
        self.model = None  # modelo dos items da lista
        self.default_emulator_config = EmulatorConfigs("Zsnes")
        self.emulators_list = get_obj_value("emulators")

        self.dwnl_dialog = DownloadDialog(self.roms, parent=self)  # Caixa popup de download
        self.emu_dialog = None  # Caixa popup de configurações do emulador

        # icone
        self.app_icon = QtGui.QIcon()
        self.app_icon.addFile(f'{self.resources_folder}/icon.png', QtCore.QSize(256, 256))
        QtWidgets.QMainWindow.setWindowIcon(self, self.app_icon)
        self.setWindowIcon(self.app_icon)

        self.listGamesbox.setEditTriggers(QAbstractItemView.NoEditTriggers)  # torna a lista de games não editavel

        # conectores de widgets para metodos
        self.btPlay.clicked.connect(lambda: self.play_game(emulator="Default"))  # botão jogar
        self.actionOpen_roms_folder.triggered.connect(self.get_folder)  # ação para abrir o folder
        self.actionDownload_Game_Covers.triggered.connect(self.download_game_covers)  # baixar as capas
        self.actionEmulator_config.triggered.connect(self.configurate_emulator)  # configurações do emulador
        self.btReload.clicked.connect(self.update_listbox)  # botao de recarregar
        self.listGamesbox.clicked.connect(self.game_selected)  # seletor de games
        self.listGamesbox.pressed.connect(self.game_selected)

        # chamadas de função
        QtCore.QTimer.singleShot(50, self.load_folder)  # carrega informações do json
        QtCore.QTimer.singleShot(50, self.create_img_dir)  # cria diretorio
        QtCore.QTimer.singleShot(50, self.copy_df_img)  # copia a imagem padrão para o diretorio

    def contextMenuEvent(self, event):  # Função do menu de click direito
        ctx_menu = QMenu(self)
        ctx_menu.addAction("Run")
        ctx_menu.addSeparator()
        for emulator in self.emulators_list:
            ctx_menu.addAction(f"Run with {emulator}")
        ctx_menu.triggered.connect(self.ctx_menu_click)
        ctx_menu.exec_(self.mapToGlobal(event.pos()))

    def ctx_menu_click(self, action):  # Evento acionado quando uma opção do ctxmenu é pressionada
        # Precisa ser melhorado para funcinar de forma mais generalizada
        action_tag = action.text()
        swich_case = {"Run": "Default", "Run with Zsnes": "Zsnes",
                      "Run with Higan": "Higan", "Run with Snes9x": "Snes9x",
                      "Run with Custom": "Custom"}
        self.play_game(emulator=swich_case[action_tag])

    def configurate_emulator(self):  # Abre a janela de configurações do emulador
        self.emu_dialog = EmuConfigDialog(parent=self)
        self.emu_dialog.exec_()

    def download_game_covers(self):  # Requisita o download de cada capa da rom
        self.dwnl_dialog.set_roms(self.roms)
        self.dwnl_dialog.start_download()
        self.update_listbox()

    def update_default_emulator(self):  # Define qual é o emulador default pelo json
        for emulator in self.emulators_list:
            if EmulatorConfigs(emulator).default_emulator:
                self.default_emulator_config = EmulatorConfigs(emulator)
                print(self.default_emulator_config.emulator)

    def play_game(self, emulator="Default"):  # roda o game selecionado
        if self.select_game != "":
            if emulator == "Default":
                self.update_default_emulator()
                run_command = self.default_emulator_config.actual_command
            else:
                run_command = EmulatorConfigs(emulator).actual_command

            game = self.games_folder + "/" + self.select_game
            run(f"{run_command} '{game}'", shell=True)

    def create_img_dir(self):  # cria o diretorio dascovers somente se não exixtir
        try:
            mkdir(self.imgs_folder)
        except FileExistsError:
            pass

    def copy_df_img(self):  # copia imagem padrão de capa para o diretorio de imagens
        file_path = f"{self.resources_folder}/none.png"
        copy2(file_path, self.imgs_folder)
        self.update_listbox()

    def save_folder(self):  # salva o caminho da pasta de roms
        write_folder(self.games_folder)

    def load_folder(self):  # carrega o caminho especificado pelo json
        self.games_folder = get_obj_value("roms_path")
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
        print("selecionado")
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

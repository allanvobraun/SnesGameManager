import glob  # Usado para pegar o caminho do arquivo mais facilmente
from os import mkdir
from os.path import expanduser
from shutil import copy2
from subprocess import run
from PyQt5.QtCore import Qt, QFile, QTextStream
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon, QPixmap
from PyQt5.QtWidgets import QDesktopWidget, QFileDialog, QAbstractItemView, QMenu, QAction

from config.json_handler import get_obj_value, write_folder
from downloader.downloads_app import DownloadDialog
from config.emuConfig_app import EmuConfigDialog
from config.themeConfig_app import ThemeConfigDialog
from config.settings import EmulatorConfigs, ThemeConfigs
from core.ui.qtwindow import *
from downloader.format_download import *
from themes.breeze import breeze_resources


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
        self.model = QStandardItemModel(self.listGamesbox)  # modelo dos items da lista
        self.default_emulator_config = EmulatorConfigs("Zsnes")
        self.emulators_list = get_obj_value("emulators")

        self.dwnl_dialog = None  # Caixa popup de download
        self.emu_dialog = None  # Caixa popup de configurações do emulador
        self.theme_dialog = None
        self.ctx_menu = MainCtxMenu(self.play_game, parent=self.listGamesbox)  # Menu de botão direito

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
        self.actionChange_Theme.triggered.connect(self.configurate_theme)
        self.btReload.clicked.connect(self.update_listbox)  # botao de recarregar
        self.listGamesbox.clicked.connect(self.game_selected)  # seletor de games
        self.listGamesbox.pressed.connect(self.game_selected)
        self.listGamesbox.customContextMenuRequested.connect(self.ctx_menu.show_menu)

        # chamadas de função
        QtCore.QTimer.singleShot(50, self.load_folder)  # carrega informações do json
        QtCore.QTimer.singleShot(50, self.create_img_dir)  # cria diretorio
        QtCore.QTimer.singleShot(50, self.copy_df_img)  # copia a imagem padrão para o diretorio

        self.change_theme()

    def change_theme(self):  # Muda o tema padrão
        main_theme = get_obj_value("theme_config", "Main_theme")
        file_name = ThemeConfigs(main_theme).file
        if file_name is not None:
            file = QFile(file_name)
            file.open(QFile.ReadOnly | QFile.Text)
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        else:
            self.setStyleSheet("")

    def configurate_theme(self):  # Abre a janela de configurações do emulador
        self.theme_dialog = ThemeConfigDialog(parent=self)
        self.theme_dialog.exec_()
        self.change_theme()

    def configurate_emulator(self):  # Abre a janela de configurações do emulador
        self.emu_dialog = EmuConfigDialog(parent=self)
        self.emu_dialog.exec_()

    def download_game_covers(self):  # Requisita o download de cada capa da rom

        self.dwnl_dialog = DownloadDialog(self.roms, parent=self)
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

    def create_img_dir(self):  # cria o diretorio das covers somente se não exixtir
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

    def display_listing_games(self):  # Coloca os games da pasta no listGamesbox
        self.model = QStandardItemModel(self.listGamesbox)

        for item in self.roms:
            img_file_path = ROOT_DIR + "/covers/" + format_gamename(item)

            if exists(img_file_path):  # Caution QIcon can cause memory leak
                game_icon = QIcon(QPixmap(img_file_path))
            else:
                game_icon = QIcon(QPixmap(ROOT_DIR + "/" + "covers/none.png"))

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


class MainCtxMenu(QMenu):  # Classe do menu de botão direito
    def __init__(self, play_function,  parent=None):
        super().__init__(parent)
        self.parent = parent

        # actions
        self.action_run = QAction("Run")
        self.action_zsnes = QAction("Run with Zsnes")
        self.action_higan = QAction("Run with Higan")
        self.action_custom = QAction("Run with Custom")
        self.action_list = [self.action_zsnes, self.action_higan, self.action_custom]

        self.addAction(self.action_run)
        self.addSeparator()
        self.addActions(self.action_list)

        # trigers
        self.action_run.triggered.connect(lambda: play_function("Default"))
        self.action_zsnes.triggered.connect(lambda: play_function("Zsnes"))
        self.action_higan.triggered.connect(lambda: play_function("Higan"))
        self.action_custom.triggered.connect(lambda: play_function("Custom"))

    def show_menu(self, pos):  # Execute the menu
        self.exec_(self.parent.mapToGlobal(pos))


def run_app():
    my_app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    my_app.exec_()

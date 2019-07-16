from PyQt5.QtWidgets import QDialog
from config.settings import ThemeConfigs
from config.ui.themeConfig_dialog import *
from config.json_handler import get_obj_value
from main import ROOT_DIR


class ThemeConfigDialog(QDialog, Ui_themeDialog):  # Classe de config do tema
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # atributos

        self.themes = list(get_obj_value("theme_config").keys())[:-1]  # Lista de temas
        self.themes_configurations = {}  # Dicionario que guarda as instancias de configurações
        for theme in self.themes:
            self.themes_configurations[theme] = ThemeConfigs(theme)

        self.themeBox.addItems(self.themes)  # Adiciona items ao combobox
        self.selected_theme = self.themeBox.currentText()  # Tema selecionado
        self.selected_theme_config = self.themes_configurations[self.selected_theme]  # COnfiguração do tema selecionado

        # configurações

        self.link_label.setOpenExternalLinks(True)  # Permite links
        self.display_main_theme()
        self.set_label()
        self.set_preview()

        # conexões
        self.themeBox.currentTextChanged.connect(self.themebox_change)
        self.btApply.clicked.connect(self.apply_changes)  # Botão de aplicar
        self.btCancel.clicked.connect(self.close)

    def set_label(self):  # Muda o link da label
        link = self.selected_theme_config.source
        if link is not None:
            self.link_label.setText(f'<a href="{link}">Source: BreezeStyleSheets</a>')
        else:
            self.link_label.setText("")

    def set_preview(self):  # Muda a imagem da preview
        image = QtGui.QPixmap(f"{ROOT_DIR}/{self.selected_theme_config.image}")
        self.preview_label.setPixmap(image)

    def apply_changes(self):  # Aplica as configurações de cada emulador e salva no json
        for obj in self.themes_configurations.values():
            obj.save_configs()
        self.close()

    def themebox_change(self):  # Mudança do thema
        self.selected_theme = self.themeBox.currentText()
        self.selected_theme_config = self.themes_configurations[self.selected_theme]
        self.update_main_theme()
        self.set_preview()
        self.set_label()

    def update_main_theme(self):  # Atualiza qual vai ser o tema padrão
        for theme in self.themes_configurations.values():
            theme.default_theme = False
        self.selected_theme_config.default_theme = True

    def display_main_theme(self):  # Mostra o tema utilizado primeiro
        for theme in self.themes:
            if ThemeConfigs(theme).default_theme:
                self.selected_theme = ThemeConfigs(theme).theme
                self.selected_theme_config = self.themes_configurations[self.selected_theme]
                self.themeBox.setCurrentIndex(self.themes.index(self.selected_theme))  # Ajusta a combobox
                self.set_preview()
                self.set_label()


if __name__ == '__main__':
    my_app = QtWidgets.QApplication([])
    dialog = ThemeConfigDialog()
    dialog.show()
    my_app.exec_()


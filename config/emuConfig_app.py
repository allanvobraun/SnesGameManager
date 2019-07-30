from PyQt5.QtWidgets import QDialog, QFileDialog
from config.json_handler import get_obj_value
from config.ui.emuConfig_dialog import *
from config.settings import EmulatorConfigs
from os.path import expanduser


class EmuConfigDialog(QDialog, Ui_emuDialog):  # Classe do popup de configurações
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # atributos
        self.emulators = get_obj_value("emulators")  # Carrega a lista de emuladores do json

        # dicionario contendo objetos das configurações de cada emulador
        self.emulators_configurations = {}
        for emulator in self.emulators:
            self.emulators_configurations[emulator] = EmulatorConfigs(emulator)

        self.emuBox.addItems(self.emulators)  # Adiciona items ao combobox
        self.current_emulator = None
        self.display_default_emulator()
        self.current_config = self.emulators_configurations[self.current_emulator]  # configuração do emulador atual

        self.update_txtbox()

        # configs
        self.txtBox.setReadOnly(True)

        # conexões
        self.emuBox.currentTextChanged.connect(self.update_txtbox)  # Caixa de seleção
        self.btApply.clicked.connect(self.apply_changes)  # Botão de aplicar
        self.btCancel.clicked.connect(self.close)
        self.btSearch.clicked.connect(self.search_emulator)

    def search_emulator(self):
        execu_path = QFileDialog.getOpenFileName(self,  # Abre o explorador de arquivos
                                                 'Select the emulator .exe file',
                                                 expanduser("~"),  # abre o home do usuario como padrão
                                                 "Executable (*.exe)")  # mostre somente executaveis
        self.current_config.exe_path = execu_path[0]
        self.update_txtbox()

    def display_default_emulator(self):  # Mostra na combox o emulador default primeiro
        for emulator in self.emulators:
            if EmulatorConfigs(emulator).default_emulator:
                self.current_emulator = EmulatorConfigs(emulator).emulator
                self.emuBox.setCurrentIndex(self.emulators.index(self.current_emulator))  # Ajusta a combobox
                print(self.current_emulator)

    def apply_changes(self):  # Aplica as configurações de cada emulador e salva no json
        for obj in self.emulators_configurations.values():
            obj.save_configs()
        self.close()

    def update_selected_emulator(self):  # Atualiza qual é o emulador atual selecionado pela emubox
        self.current_emulator = self.emuBox.currentText()
        self.current_config = self.emulators_configurations[self.current_emulator]
        self.update_default_emulator()

    def update_txtbox(self):  # Atualiza o comando exibido na command box
        self.update_selected_emulator()
        file_name = self.current_config.exe_name

        self.txtBox.setText(file_name)  # troca o texto da caixa

    def update_default_emulator(self):  # Atualiza qual vai ser o emulador padrão utilizado para rodar os jogos
        for emulator in self.emulators_configurations.values():
            emulator.default_emulator = False
        self.current_config.default_emulator = True


if __name__ == '__main__':
    my_app = QtWidgets.QApplication([])
    emu_dialog = EmuConfigDialog()
    emu_dialog.show()
    my_app.exec_()

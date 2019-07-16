from PyQt5.QtWidgets import QDialog
from config.json_handler import get_obj_value
from config.ui.emuConfig_dialog import *
from config.settings import EmulatorConfigs


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

        self.update_commandbox()

        # configs
        self.commandBox.setReadOnly(True)

        # conexões
        self.emuBox.currentTextChanged.connect(self.update_commandbox)  # Caixa de seleção
        self.checkBox.stateChanged.connect(self.check_event)  # Caixa de marcar o check
        self.commandBox.editingFinished.connect(self.update_command)  # Caixa de escrever o comando
        self.btApply.clicked.connect(self.apply_changes)  # Botão de aplicar
        self.btCancel.clicked.connect(self.close)

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

    def check_event(self):  # Quando a checkbox mudar de estado mude o estado de read-only
        self.update_selected_emulator()
        checked = 2
        unchecked = 0

        if self.checkBox.checkState() == checked:
            self.commandBox.setReadOnly(True)
            self.current_config.use_default_command = True

        elif self.checkBox.checkState() == unchecked:
            self.commandBox.setReadOnly(False)
            self.current_config.use_default_command = False

        self.update_commandbox()

    def update_command(self):  # Atualiza o comando designado ao emulador
        self.current_config.custom_command = self.commandBox.text()

    def update_selected_emulator(self):  # Atualiza qual é o emulador atual selecionado pela emubox
        self.current_emulator = self.emuBox.currentText()
        self.current_config = self.emulators_configurations[self.current_emulator]
        self.update_default_emulator()

    def update_checkbox_state(self):  # Atualiza a checkbox de acordo com a configuração booleana
        self.update_selected_emulator()
        self.checkBox.setChecked(self.current_config.use_default_command)

    def update_commandbox(self):  # Atualiza o comando exibido na command box
        self.update_selected_emulator()
        if self.current_emulator == "Custom":
            self.checkBox.setChecked(False)
            self.checkBox.setEnabled(False)  # trava a checkbox
            command = self.current_config.custom_command
        else:
            self.checkBox.setEnabled(True)
            if self.current_config.use_default_command:  # booleano para trocar entre default e custom
                command = self.current_config.default_command
            else:
                command = self.current_config.custom_command

        self.commandBox.setText(command)  # troca o texto da caixa
        self.update_checkbox_state()

    def update_default_emulator(self):  # Atualiza qual vai ser o emulador padrão utilizado para rodar os jogos
        for emulator in self.emulators_configurations.values():
            emulator.default_emulator = False
        self.current_config.default_emulator = True


if __name__ == '__main__':
    my_app = QtWidgets.QApplication([])
    emu_dialog = EmuConfigDialog()
    emu_dialog.show()
    my_app.exec_()


from config.json_handler import get_obj_value, write_config

"""
Classes for change and consult configurations from the Json file
"""


class Config:  # Classe pai de configuração geral
    def __init__(self, json_key):
        self.json_key = json_key
        self.json_obj = get_obj_value(self.json_key)

    def save_to_json(self):  # salva as configs no json
        write_config(self.json_key, self.json_obj)

    def overwrite_save(self, key, values):  # Troca as informações
        self.json_obj = get_obj_value(self.json_key)
        self.json_obj[key] = values
        self.save_to_json()


class EmulatorConfigs(Config):  # Classe que carrega e salva as configurações de cada emulador do json para a memória
    def __init__(self, emulator):
        super().__init__("emulators_config")
        self.emulator_obj = self.json_obj[emulator]

        self.emulator = emulator  # nome do emulador
        self._default_command = self.emulator_obj["default_command"]  # comando padrão para rodar os jogos
        self._custom_command = self.emulator_obj["custom_command"]  # comando personalizado
        self._use_default_command = self.emulator_obj["use_default_command"]  # booleano
        self._default_emulator = self.emulator_obj["default_emulator"]  # booleano, este é o emulador padrão?
        # comando a ser utilizado
        self._actual_command = self.default_command if self.use_default_command else self.custom_command

    def save_configs(self):  # salva as configurações
        data_dict = {
                "default_command": self.default_command,
                "custom_command": self.custom_command,
                "use_default_command": self.use_default_command,
                "default_emulator": self.default_emulator}
        self.overwrite_save(self.emulator, data_dict)

    @property
    def use_default_command(self):
        return self._use_default_command

    @property
    def actual_command(self):
        return self._actual_command

    @property
    def custom_command(self):
        return self._custom_command

    @property
    def default_command(self):
        return self._default_command

    @property
    def default_emulator(self):
        return self._default_emulator

    @default_command.setter
    def default_command(self, value):
        self._default_command = value

    @custom_command.setter
    def custom_command(self, value):
        self._custom_command = value

    @use_default_command.setter
    def use_default_command(self, value):
        self._use_default_command = value

    @default_emulator.setter
    def default_emulator(self, value):
        self._default_emulator = value


class ThemeConfigs(Config):  # Classe que carrega e salva as configurações de cada tema do json para a memória
    def __init__(self, theme):
        super().__init__("theme_config")
        self.theme_obj = self.json_obj[theme]

        self.theme = theme  # nome do tema
        self._source = self.theme_obj["source"]  # link de origem do tema
        self._image = self.theme_obj["image"]  # imagem de preview do tema
        self._default_theme = self.theme_obj["default_theme"]  # booleano
        self._file = self.theme_obj["file"]  # arquivo qss para carregar o tema

    def save_configs(self):
        data_dict = {
            "source": self.source,
            "image": self.image,
            "default_theme": self.default_theme,
            "file": self.file}
        self.save_main_theme()
        self.overwrite_save(self.theme, data_dict)

    def save_main_theme(self):  # Salva qual vai ser o tema principal
        if self.default_theme:
            self.overwrite_save("Main_theme", self.theme)

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def default_theme(self):
        return self._default_theme

    @default_theme.setter
    def default_theme(self, value):
        self._default_theme = value

    @property
    def file(self):
        return self._file

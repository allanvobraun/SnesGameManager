import sys
import os


def path_to_roms(rom_list):  # Função para extrair os nomes das roms de cada caminho
    extracted_names = []
    for path in rom_list:
        name = path.split("/")[-1]
        extracted_names.append(name)
    return extracted_names


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



from main import ROOT_DIR
from json import dump, load

"""
Read and save configs to a json file
"""


def write(data):  # Sobrescreve as alterações  no json
    with open(f'{ROOT_DIR}/user_config.json', 'w') as json_file:
        dump(data, json_file, indent=2)


def write_emulator_config(emulator, new_data):
    with open(f'{ROOT_DIR}/user_config.json', "r") as json_file:
        data = load(json_file)
        data["emulators_config"][emulator] = new_data
    write(data)


def write_command(emulator, command):  # Escreve o comando de emulador no json
    with open(f'{ROOT_DIR}/user_config.json', "r") as json_file:
        data = load(json_file)
        data["emulators_config"][emulator]["custom_command"] = command
    write(data)


def write_folder(games_folder):  # Escreve o folder de games no json

    with open(f'{ROOT_DIR}/user_config.json', "r") as json_file:
        data = load(json_file)
        data["roms_path"] = games_folder

    write(data)


def get_obj_value(key, *subkeys):  # Carrega um valor especifico do json
    try:
        with open(f"{ROOT_DIR}/user_config.json", "r") as json_file:
            data = load(json_file)
            data_value = data[key]
            for subkey in subkeys:
                data_value = data_value[subkey]

            return data_value
    except (ValueError, OSError):
        print(f"ERROR -> Cant find {key}")
        return ""

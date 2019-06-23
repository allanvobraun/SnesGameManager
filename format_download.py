from urllib.error import HTTPError
from wget import download


# Modulo usado para baixar os arquivos de imagem, confome a demanda, do github
# exemplo:
# ACME Animation Factory.smc
# https://raw.githubusercontent.com/ZeroSuf3r/nintendo-games-icons/master/A/ACME%20Animation%20Factory%20(USA).png


def rm_extension(rom_name):  # formata a string para remover a extensão do arquivo. Ex: "potato.smc" -> "potato"
    end = rom_name.find(".", len(rom_name) - 4)
    new_rom_name = rom_name.replace(rom_name[end:], "")
    return new_rom_name


def rm_espaces(rom_name):  # remove espaços redudantes
    removed_double_spaces = rom_name.replace("  ", " ")
    clean_rom_name = removed_double_spaces.replace(" .", ".")
    return clean_rom_name


def rm_regions(rom_name):  # remove a tag de região
    if rom_name.find("(") == -1:
        return rom_name

    start = rom_name.find("(")
    end = rom_name.find(")", start) + 1
    removed_region = rom_name.replace(rom_name[start:end], "")
    return removed_region


def format_gamename(rom_name):  # Formata o nome do game para ser competivel com o nome da imagem
    semi_formated_name = rm_espaces(rm_extension(rm_regions(rom_name)))
    formated_name = rm_espaces(semi_formated_name + " (USA)")
    return formated_name + ".png"


def get_first_letter(rom_name):  # Pega a primeira letra do arquivo, será o folder do github
    if rom_name[0].isdigit():
        return "0-9"
    else:
        return rom_name[0].upper()


def generate_link(rom_name):  # gera o link de download da imagem da rom
    file = format_gamename(rom_name)
    folder = get_first_letter(rom_name)
    base_link = "https://raw.githubusercontent.com/ZeroSuf3r/nintendo-games-icons/master"
    final_link = "{}/{}/{}".format(base_link, folder, file)
    return final_link


# função de alto nivel que faz download da capa do game, tendo em base o nome da rom não-formatado
def download_cover(rom_name, out_path=None):
    img_link = generate_link(rom_name)
    try:
        download(img_link, out=out_path)

    except HTTPError as error:

        if error.code == 404:
            return "ERROR 404 - LINK NOT FOUND"



# download_cover("dawd.txt")
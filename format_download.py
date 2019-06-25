from urllib.error import HTTPError
from wget import download
from os.path import exists


# Modulo usado para baixar os arquivos de imagem, confome a demanda, do github
# exemplo:
# ACME Animation Factory.smc
# https://raw.githubusercontent.com/ZeroSuf3r/nintendo-games-icons/master/A/ACME%20Animation%20Factory%20(USA).png


def rm_extension(rom_name):  # formata a string para remover a extensão do arquivo. Ex: " potato (U).smc" -> "potato"
    end = rom_name.rindex(".")
    new_rom_name = rom_name.replace(rom_name[end:], "")
    return new_rom_name


def rm_espaces(rom_name):  # remove espaços redudantes
    if rom_name[0] == " ":
        clean_rom_name = rom_name[1:]
    else:
        clean_rom_name = rom_name

    while clean_rom_name.count("  ") != 0:
        removed_double_spaces = clean_rom_name.replace("  ", " ")
        clean_rom_name = removed_double_spaces.replace(" .", ".")
    return clean_rom_name


def rm_brackets(rom_name):  # remove os [] e seus conteudos
    if rom_name.count("(") == 0:
        return rom_name
    new_name = rom_name

    while new_name.count("[") + new_name.count("]") != 0:
        start = new_name.index("[")
        end = new_name.index("]", start) + 1
        new_name = new_name.replace(new_name[start:end], "")

    return new_name


def rm_parenthesis(rom_name):  # remove os parenteses e seus conteudos
    if rom_name.count("(") == 0:
        return rom_name
    new_name = rom_name

    while new_name.count("(") + new_name.count(")") != 0:
        start = new_name.index("(")
        end = new_name.index(")", start) + 1
        new_name = new_name.replace(new_name[start:end], "")
    return new_name


def wipe_name(rom_name):  # Aplica diversas funções para limpar caracteres indesejaveis
    clean = rm_espaces(rm_extension(rm_parenthesis(rm_brackets(rom_name))))
    return clean


def format_gamename(rom_name):  # Formata o nome do game para ser competivel com o nome da imagem
    semi_formated_name = wipe_name(rom_name)
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


def has_duplicate(rom_name, path):

    file = format_gamename(rom_name)
    if exists(path + "/" + file):
        return True
    else:
        return False


# função de alto nivel que faz download da capa do game, tendo em base o nome da rom não-formatado
def download_cover(rom_name, out_path=None, allow_dups=True):

    if (out_path is not None) and (not allow_dups):  # Se não permitir arquivos duplicados
        dup_flag = has_duplicate(rom_name, out_path)  # teste se tiver duplicatas
    else:
        dup_flag = False

    if not dup_flag:  # se tudo ok, baixe, se nao existe uma duplicata não permetida
        img_link = generate_link(rom_name)

        try:
            download(img_link, out=out_path)

        except HTTPError as error:
            if error.code == 404:
                print("ERROR 404 - LINK NOT FOUND")
                return "ERROR 404 - LINK NOT FOUND"
            else:
                print("ERROR unknown")
                return "ERROR unknown"
    else:
        print("Error duplicate file")
        return "Error duplicate file"

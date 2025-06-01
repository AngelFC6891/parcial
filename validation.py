from constants import *


def is_integer(string : str) -> bool:
    '''
    Description: Verifica si una cadena representa a un número entero positivo o negativo.\n
    Argument/s:
        string: cadena.\n
    Return: True si la cadena representa a un número entero, caso contrario devuelve False.
    '''
    output = len(string) > 0
    
    for i in range(len(string)):
        ascii = ord(string[i])

        if i == 0 and ascii == 45:
            if len(string) > 1:
                continue
            else:
                output = False
                break
         
        if ascii < 48 or ascii > 57:
            output = False
            break
    
    return output


def is_letter(char : str) -> bool:
    '''
    Description: Verifica si un caracter es una letra.\n
    Argument/s:
        i: caracter.\n
    Return: True si el caracter es una letra, caso contrario devuelve False.
    '''
    output = True
    ascii = ord(char)
    
    if not (ascii >= 65 and ascii <= 90) and not (ascii >= 97 and ascii <= 122):
        output = False

    return output


def is_word(word : str):
    '''
    Description: Verifica si una cadena contiene solo letras.\n
    Argument/s:
        word: cadena.\n
    Return: True si la cadena contiene solo letras, caso contrario devuelve False.
    '''
    is_word = True

    for i in word:
        if not is_letter(i):
            is_word = False
            break

    return is_word


def is_name(name : str) -> bool:
    '''
    Description: Verifica si una cadena es un nombre válido (con un mínimo de letras iniciales y un espacio intermedio).\n
    Argument/s:
        name: cadena.\n
    Return: True si la cadena es un nombre válido, caso contrario devuelve False.
    '''
    is_name = True
    i = get_space_index(name)

    if not i in [-1, 0, len(name)-1]:
        if not (is_word(name[:i]) and len(name[:i]) >= LETTERS_QTY):
            is_name = False
        else:
            if not is_word(name[i+1:]):
                is_name = False
    else:
        if i == 0:
            name = name[1:]
        elif i == len(name)-1:
            name = name[:len(name)-1]

        if not (is_word(name) and len(name) >= LETTERS_QTY):
            is_name = False

    return is_name


def is_score(string : str) -> bool:
    '''
    Description: Verifica si una cadena es un puntaje válido (debe ser convertible a entero y pertenecer a un rango de puntaje).\n
    Argument/s:
        string: cadena.\n
    Return: True si la cadena es un puntaje válido, caso contrario devuelve False.
    '''
    output = False

    if is_integer(string):
        if int(string) >= SCORE_MIN and int(string) <= SCORE_MAX:
            output = True

    return output


def is_match(string : str, pattern : str, chars_qty : int) -> bool:
    '''
    Description: Verifica si una cadena coincide con un patrón de búsqueda.\n
    Argument/s:
        string: cadena.\n
        pattern: patrón de búsqueda.\n
        chars_qty: cantidad de caracteres a comparar.\n
    Return: True si la cadena coincide con el patrón, caso cotrario devuelve False.
    '''
    output = len(pattern) >= chars_qty

    if output:
        for i in range(chars_qty):
            if not ord(string[i]) in [ord(pattern[i]), ord(pattern[i]) + 32, ord(pattern[i]) - 32]:
                output = False
                break

    return output


def get_space_index(string : str) -> int:
    '''
    Description: Verifica si la cadena contiene un caracter espacio.\n
    Argument/s:
        string: cadena.\n
    Return: el índice en el cual se encuentra el espacio, de no haber devuelve -1.
    '''
    index = -1

    for i in range(len(string)):
        if ord(string[i]) == SPACE_ASCII:
            index = i
            break

    return index
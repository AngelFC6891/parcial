from constants import *
from validation import *
import os
import copy


def get_option() -> str | int:
    '''
    Description: Solicita ingresar un opción numérica, la valida y la convierte a entero.\n
    Argument/s: No requiere.\n
    Return: Un entero si la opción es válida, caso contrario devuelve una cadena.
    '''
    print(TITLE, MENU)
    option = input(OPTION)

    if is_integer(option):
        option = int(option)

    return option


def press_enter() -> None:
    '''
    Description: Solicita presionar la tecla enter para continuar con el programa, y además limpia la consola.\n
    Argument/s: No requiere.\n
    Return: No tiene.
    '''
    _ = input(PRESS_ENTER)
    os.system(CLEAR)


def create_array(qty : int, value_init : any=0) -> list:
    '''
    Description: Inicializa un array unidimensional.\n
    Argument/s:
        qty: cantidad de elementos.
        value_init: valor inicial que se usará para todos los elementos.\n
    Return: array unidimensional.
    '''
    return [value_init] * qty


def create_matrix(rows : int, cols : int, value_init : any=0) -> list[list]:
    '''
    Description: Inicializa un array bidimensional.\n
    Argument/s:
        rows: cantidad de filas.
        cols: cantidad de columnas.
        value_init: valor inicial que se usará para todos los elementos.\n
    Return: array bidimensional.
    '''
    matrix = create_array(rows, value_init)
    
    for i in range(rows):
        matrix[i] = create_array(cols, value_init)

    return matrix


def accumulate_array(array : list) -> int | float:
    '''
    Description: Suma todos los elementos de un array unidimensional.\n
    Argument/s:
        array: array unidimensional.\n
    Return: la suma total, ya sea entero o flotante.
    '''
    total = 0

    for i in array:
        total += i

    return total


def accumulate_col(matrix : list, col : int) -> int | float:
    '''
    Description: Suma todos los elementos de una columna de un array bidimensional.\n
    Argument/s:
        matrix: array bidimensional.\n
        col: índice de la columna.\n
    Return: la suma total, ya sea entero o flotante.
    '''
    total = 0
    
    for row in range(len(matrix)):
        total += matrix[row][col]
    
    return total


def get_average(total : float, qty : int) -> float | None:
    '''
    Description: Divide dos números para obtener un promedio.\n
    Argument/s:
        total: es la suma total correspondiente al numerador del promedio.\n
        qty: es la cantidad total de elementos correspondiente al denominador del promedio.\n
    Return: la razón entre ambos valores, de tipo flotante.
    '''
    return total / qty if not qty == 0 else None


def get_averages_parts(scores : list[list]) -> list[float]:
    '''
    Description: Calcula el puntaje promedio de cada participante y lo almacena en un array unidimensional.\n
    Argument/s:
        scores: matriz de puntajes.\n
    Return: array unidimensional de flotates.
    '''
    averages = create_array(len(scores))

    for i in range(len(scores)):
        averages[i] = get_average(accumulate_array(scores[i]), len(scores[i])) 

    return averages


def get_averages_jurys(matrix : list[list]) -> list[float]:
    '''
    Description: Calcula el promedio de los puntajes asignados de cada jurado y los almacena en un array unidimensional.\n
    Argument/s:
        scores: matriz de puntajes.\n
    Return: array unidimensional de flotates.
    '''
    averages_jurys = create_array(len(matrix[0]))

    for i in range(len(matrix[0])):
        averages_jurys[i] = get_average(accumulate_col(matrix, i), len(matrix))

    return averages_jurys


def sort_arrays(arrays : list[list], upward : bool=True) -> None:
    '''
    Description: Permite ordenar, de manera ascendente o descendente, un array o varios arrays paralelos. En el segunto caso, toma como referencia para el ordenamiento al primer array del parámetro arrays.\n
    Argument/s:
        arrays: array de arrays.\n
        upward: booleano (define el tipo de ordamiento: True para ascendente o de lo contrario False).\n
    Return: No tiene.
    '''
    array_ref = arrays[0]

    for i in range(len(array_ref)-1):
        for j in range(i+1, len(array_ref)):
            if (upward and array_ref[i] > array_ref[j]) or (not upward and array_ref[i] < array_ref[j]):
                array_ref[i], array_ref[j] = array_ref[j], array_ref[i]

                if len(arrays) > 1:
                    for k in range(1, len(arrays)):
                        arrays[k][i], arrays[k][j] = arrays[k][j], arrays[k][i]


def get_info_part(data : str, names : list[str], averages : list[float], scores : list[list], i : int) -> str:
    '''
    Description: Permite obtener toda la información de un participante: nombre, puntaje por jurado y puntaje promedio.\n
    Argument/s:
        data: cadena donde se almacenará la información.\n
        names: array unidimensional con los nombres de los participantes.\n
        averages: array unidimensional con los promedios de los participantes.\n
        scores: matriz de puntajes.\n
        i: índice del participante de interés.
    Return: cadena.
    '''
    data = f'{data}\n{PARTICIPANT_NUM}{i+1}: {names[i]}'

    for j in range(len(scores[i])):
        data = f'{data}\n{SCORE_JURY}{j+1}: {scores[i][j]}'

    data = f'{data}\n{AVERAGE_SCORE}{averages[i]:.2f}/{SCORE_MAX}\n'

    return data


def show_info_parts(names : list[str], averages : list[float], scores : list[list]) -> None:
    '''
    Description: Muestra por consola la información de todos los participantes: sus nombres, sus puntajes por jurado y sus puntajes promedio.\n
    Argument/s:
        names: array unidimensional con los nombres de los participantes.\n
        averages: array unidimensional con los promedios de los participantes.\n
        scores: matriz de puntajes.\n
    Return: No tiene.
    '''
    data = VOID_STR
    for i in range(len(scores)):
        data = get_info_part(data, names, averages, scores, i)
    
    print(data)


def show_parts_by_average(names : list[str], averages : list[float], ref : float, above_below : str=ABOVE) -> None:
    '''
    Description: Muestra por consola a todos los participantes cuyo promedio sea superior o inferior a un valor de referencia.\n
    Argument/s:
        names: array unidimensional con los nombres de los participantes.\n
        averages: array unidimensional con los promedios de los participantes.\n
        ref: valor flotante de referencia.\n
        above_below: cadena ('above' si la comparación es por encima del valor de referencia, de lo contrario 'below')
    Return: No tiene.
    '''
    data = VOID_STR

    for i in range(len(averages)):
        if (above_below == ABOVE and averages[i] > ref) or\
            (above_below == BELOW and averages[i] < ref):
            data = f'{data}\n{PARTICIPANT_NUM}{i+1}: {names[i]} - {AVERAGE_SCORE}{averages[i]:.2f}/{SCORE_MAX}'

    if data == VOID_STR : data = NOT_EXISTS
    print(data)


def show_averages_jurys(averages : list[float]) -> None:
    '''
    Description: Muestra por consola a cada jurado con su promedio de puntajes asignados.\n
    Argument/s:
        averages: array unidimensional de los promedios de cada jurado.\n
    Return: No tiene.
    '''
    data = VOID_STR

    for i in range(len(averages)):
        data = f'{data}\n{AVERAGE_JURY}{i+1}: {averages[i]:.2f}/{SCORE_MAX}'

    print(data)


def show_strictest_jurys(averages : list[float]) -> None:
    '''
    Description: Muestra por consola a aquellos jurados que tuvieron el menor promedio de puntajes asignados.\n
    Argument/s:
        averages: array unidimensional de los promedios de cada jurado.\n
    Return: No tiene.
    '''
    data = VOID_STR

    averages_copy = copy.deepcopy(averages)
    sort_arrays([averages_copy])
    min_average = averages_copy[0]

    for i in range(len(averages)):
        if averages[i] == min_average:
            data = f'{data}\n{JURY_NUM}{i+1} - {AVERAGE_SCORE}{averages[i]:.2f}/{SCORE_MAX}'

    print(data)


def search_parts_by_name(names : list[str], averages : list[float], scores : list[list]) -> None:
    '''
    Description: Busca participantes por su nombre y muestra su información por consola.\n
    Argument/s:
        names: array unidimensional con los nombres de los participantes.\n
        averages: array unidimensional con los promedios de los participantes.\n
        scores: matriz de puntajes.\n
    Return: No tiene.
    '''
    data = VOID_STR
    pattern = input(ENTER_NAME)
    
    if is_word(pattern):
        for i in range(len(names)):
            if is_match(names[i], pattern, LETTERS_QTY):
                data = get_info_part(data, names, averages, scores, i)

    if data == VOID_STR : data = NO_MATCHES
    print(data)


def show_parts_by_best_average(names : list[str], averages : list[float], top : int=1) -> None:
    '''
    Description: Muestra por consola a los participantes con mayor puntaje promedio.\n
    Argument/s:
        names: array unidimensional con los nombres de los participantes.\n
        averages: array unidimensional con los promedios de los participantes.\n
        top: entero (determina el podio de posiciones: solo 1er puesto, 1er y 2do puesto, etc.)
    Return: No tiene.
    '''
    data = VOID_STR
    names_copy = copy.deepcopy(names)
    averages_copy = copy.deepcopy(averages)
    sort_arrays([averages_copy, names_copy], upward=False)
    i = 0

    for j in range(1, top+1):
        if i < len(averages_copy):
            average_ref = averages_copy[i]
            init = i

            for k in range(init, len(averages_copy)):
                if averages_copy[k] == average_ref:
                    data = f'{data}\n#{j}. {PARTICIPANT}: {names_copy[k]} - {AVERAGE_SCORE}{averages_copy[k]:.2f}/{SCORE_MAX}'
                    i = k+1
                else:
                    break
        else:
            break

    print(data)


def show_parts_by_alphabetic_order(names : list[str], averages : list[float], scores : list[list]) -> None:
    '''
    Description: Ordena alfabéticamente los nombres de los participantes y luego los muestra por consola con toda su información.\n
    Argument/s:
        names: array unidimensional con los nombres de los participantes.\n
        averages: array unidimensional con los promedios de los participantes.\n
        scores: matriz de puntajes.\n
    Return: No tiene.
    '''
    names_copy = copy.deepcopy(names)
    averages_copy = copy.deepcopy(averages)
    scores_copy = copy.deepcopy(scores)
    sort_arrays([names_copy, averages_copy, scores_copy])
    show_info_parts(names_copy, averages_copy, scores_copy)


def reset(names : list[str], scores : list[list], value_init : any=0) -> None:
    '''
    Description: Resetea el array de nombres y la matriz de puntajes de los participantes.\n
    Argument/s:
        names: array unidimensional con los nombres de los participantes.\n
        scores: matriz de puntajes.\n
        value_init: valor inicial que se usará para todos los elementos.
    Return: No tiene.
    '''
    for i in range(len(names)):
        names[i] = value_init
        row = scores[i]

        for j in range(len(row)):
            row[j] = value_init

    print(RESET_OK)


def show_alert(names_ok : bool, scores_ok : bool) -> None:
    '''
    Description: Muestra por consola un alerta en caso de que no se haya efectuado la carga de datos de los participantes.\n
    Argument/s:
        names_ok: booleano (True si los nombres fueron cargados, caso contrario False).\n
        scores_ok: booleano (True si los puntajes fueron cargados, caso contrario False).\n
    Return: No tiene.
    '''
    alert = None

    if not names_ok and scores_ok:
        alert = NAMES_NOT_EXIST
    elif not scores_ok and names_ok:
        alert = SCORES_NOT_EXIST
    elif not (names_ok and scores_ok):
        alert = DATA_NOT_EXIST

    print(alert)
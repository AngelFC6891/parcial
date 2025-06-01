from constants import *
from validation import *


def load_names(array : list) -> bool:
    '''
    Description: Solicita ingresar un nombre, lo valida y lo carga en un array unidimensional.\n
    Argument/s:
        array: array unidimensional.\n
    Return: True una vez finalizado el proceso.
    '''

    for i in range(len(array)):
        print(f'\n{PARTICIPANT_NUM}{i+1}')
        array[i] = input(ENTER_NAME)

        while True:
            if not is_name(array[i]):
                print(INVALID_NAME)
                array[i] = input(ENTER_NAME)
            else:
                print(NAME_OK)
                break

    return True


def load_scores(matrix : list[list]) -> bool:
    '''
    Description: Solicita ingresar un puntaje, lo valida y lo carga en un array bidimensional.\n
    Argument/s:
        matrix: array bidimensional.\n
    Return: True una vez finalizado el proceso.
    '''
    
    for i in range(len(matrix)):
        print(f'\n{PARTICIPANT_NUM}{i+1}')

        for j in range(len(matrix[i])):
            print(f'{JURY_NUM}{j+1}')
            score = input(ENTER_SCORE)

            while True:
                if not is_score(score):
                    print(INVALID_SCORE)
                    score = input(ENTER_SCORE)
                else:
                    matrix[i][j] = int(score)
                    print(SCORE_OK)
                    break

    return True
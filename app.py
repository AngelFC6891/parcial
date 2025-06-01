from library import *
from inputs import *


def execute():
    '''
    Description: Ejecuta el programa.\n
    Argument/s: No requiere.\n
    Return: No tiene.
    '''
    
    names = create_array(PARTS_QTY) # parts is participants
    scores = create_matrix(PARTS_QTY, JURYS_QTY)
    names_ok = False
    scores_ok = False
    
    while True:
        option = get_option()
        
        if not (names_ok and scores_ok):
            
            match option:

                case 1:
                    if not names_ok:
                        names_ok = load_names(names)
                    else:
                        print(NAMES_EXIST)

                case 2:
                    if not scores_ok:
                        scores_ok = load_scores(scores)
                    else:
                        print(SCORES_EXIST)

                case 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
                    data_alert(names_ok, scores_ok)

                case 11:
                    if names_ok or scores_ok:
                        names_ok = False
                        scores_ok = False
                        reset(names, scores)
                    else:
                        print(DATA_NOT_EXIST)

                case 0:
                    break

                case _:
                    print(INVALID_OPTION)
        else:
            match option:

                case 1 | 2:
                    print(DATA_EXIST)

                case 3:
                    averages_parts = get_averages_parts(scores)
                    show_info_parts(names, averages_parts, scores)

                case 4:
                    show_parts_by_average(names, averages_parts, 4)

                case 5:
                    show_parts_by_average(names, averages_parts, 7)

                case 6:
                    averages_jurys = get_averages_jurys(scores)
                    show_averages_jurys(averages_jurys)

                case 7:
                    show_strictest_jurys(averages_jurys)

                case 8:
                    search_parts_by_name(names, averages_parts, scores)

                case 9:
                    show_parts_by_best_average(names, averages_parts, top=3)

                case 10:
                    show_parts_by_alphabetic_order(names, averages_parts, scores)

                case 11:
                    names_ok = False
                    scores_ok = False
                    reset(names, scores)

                case 0:
                    break

                case _:
                    print(INVALID_OPTION)

        press_enter()
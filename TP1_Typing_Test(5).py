#!/usr/bin/env python3
from readchar import readkey
from colorama import Fore, Style
from time import time, ctime
from collections import namedtuple
from pprint import pprint
import argparse, random


def main():

    #-----VARIABLES------
    Inputs = namedtuple('Input', ['requested', 'received','duration'])

    my_dict = {
        'accuracy': 0,
        'inputs': [],
        'number_of_hits': 0,
        'number_of_types': 0,
        'test_durantion': 0,
        'test_end': 0,
        'test_start': 0,
        'type_average_duration': 0,
        'type_hit_average_duration': 0,
        'type_miss_average_duration': 0
    }

    #-----PLAYER's CHOOSEN ARGUMENTS-----
    parser = argparse.ArgumentParser(description='Typing Test')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.')
    parser.add_argument('-mv', '--max_value', type=int, required=False, default=0, help='Max number of seconds for time mode or maximum number of inputs for number of inputs mode.')

    args = vars(parser.parse_args())
    print(args)

    if args['use_time_mode']:
        print('Test running up to ' + str(args['max_value']) + ' seconds\n')
    else:
        print('Test running up to ' + str(args['max_value']) + ' inputs\n')

    print(Fore.BLUE + "PARI" + Style.RESET_ALL + " Typing Test, Grupo 6," + str(ctime(time())) + Style.RESET_ALL )
    print('Press any key to start the test')
    readkey()

    #----GAME START------
    start_time = time()
    my_dict['test_start'] = ctime(start_time) #STORE TIME START

    #----DYNAMIC CYCLE----
    while True:
        
        rand_letter = chr(random.randrange(97,123)) #CHOOSE A RANDOM LETTER
        print('Type letter ' + Fore.BLUE + Style.BRIGHT + rand_letter + Style.RESET_ALL)
        
        cycle_type_time = time() #INITIATE TIMER
        typed_letter = readkey()

        cycle_type_time = time() - cycle_type_time #CALCULATE TIME OF TYPING
        my_dict['type_average_duration'] += cycle_type_time #STORE BY ADDING PREVIOUS VALUE


        if typed_letter == rand_letter: #IF PLAYER HITS
            my_dict['number_of_hits'] += 1 #STORE THE HIT
            my_dict['type_hit_average_duration'] += cycle_type_time #ADD CYCLE TIME

            print('You typed letter ' + Fore.GREEN + Style.BRIGHT + typed_letter + Style.RESET_ALL)
        
        elif ord(typed_letter) == 32: #PLAYER TYPE 'SPACE' TO STOP THE TEST
            print('Typing game stopped.')
            break
        else:
            my_dict['type_miss_average_duration'] += cycle_type_time #ADD CYCLE TIME

            print('You typed letter ' + Fore.RED + Style.BRIGHT + typed_letter + Style.RESET_ALL)
        

        my_dict['number_of_types'] += 1 #STORE THE HIT

        my_dict['test_durantion'] = time() - start_time #CALCULATE AND STORE THE TEST DURATION
        my_dict['inputs'].append(Inputs(rand_letter,typed_letter,cycle_type_time)) #STORE CYCLE DATA

        if args['use_time_mode'] and args['max_value'] < my_dict['test_durantion']: #IF TIME IS OFF
            print('Current test duration (' + str(my_dict['test_durantion']) + ') exceeds maximum of ' + str(args['max_value']))
            break

        elif not args['use_time_mode'] and args['max_value'] == my_dict['number_of_types']: #IF MAX INPUTS LIMIT IS REACHED
            print('Current test inputs (' + str(my_dict['number_of_types']) + ') are equal to ' + str(args['max_value']))
            break
    
    print(Fore.BLUE + "Test finished!! Good JOB !!! " + Style.RESET_ALL)

    #-----STATISTICS-----
    my_dict['accuracy'] = my_dict['number_of_hits']/my_dict['number_of_types'] #CALCULATE ACCURACY
    my_dict['test_end'] = ctime()   #STORE END DATE
    my_dict['type_average_duration'] /= my_dict['number_of_types'] #CACULATE TYPE AVERAGE DURATION
    if my_dict['number_of_hits'] > 0: #IF PLAYER NEVER HIT
        my_dict['type_hit_average_duration'] /= my_dict['number_of_hits'] #CACULATE TYPE HIT AVERAGE DURATION

    if my_dict['number_of_hits'] != my_dict['number_of_types']: #IF PLAYER FAILED
        my_dict['type_miss_average_duration'] /= (my_dict['number_of_types'] - my_dict['number_of_hits']) #CACULATE TYPE MISS AVERAGE DURATION

    pprint(my_dict)

if __name__ == "__main__":
    main()
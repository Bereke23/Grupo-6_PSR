import argparse
from operator import truediv
import readchar
from queue import Empty
import time
from colorama import Fore, Back, Style
import random
from collections import namedtuple
from pprint import pprint

#Variaveis gerais usadas
Tempo_maximo = 5
init = time.time()
fin = 0
my_dict = {}
Inputs = namedtuple('Input', ['requested', 'received','duration'])


def argumentosetrada():
    # Definição dos argumentos de entrada:
    parser = argparse.ArgumentParser(description='Modo de funcionamento')
    parser.add_argument('-utm','--use_time_mode', action='store_true' ,
                    help='Max number of secs for time mode or maximum number os inputs mode.')
    parser.add_argument('-mv','--max_value',type = int, required= True,
                    help='Max number of secs for time mode or maximum number os inputs mode.')
    args = vars(parser.parse_args())
    valor_max = args['max_value']
    temporizador = args['use_time_mode']
    if valor_max > 0:
        print(args)
        teclainicial(valor_max,temporizador)
    print('Numero invalido de inputs tente outra vez')
    exit(0)
    
    

def teclainicial(numero_maximo, temporizador):
    # Definição da parte inicial do teste:
    seconds = time.time()
    local_time = time.ctime(seconds)
    print(Fore.BLUE + "PARI" + Style.RESET_ALL + " Typing Test, Grupo 6," + local_time + Style.RESET_ALL ) 
    if temporizador:
        print("Test runnig up to " + str(Tempo_maximo) + "s")
    else:
        print("Test runnig up to " + str(numero_maximo) + " inputs" )
    print("Press any key to star the test")
    my_dict['test_start'] = local_time
    key = readchar.readkey()
    if key is not Empty:
        modofuncionamento(numero_maximo,temporizador)
    

def modofuncionamento(numero_maximo,temporizador):
    # Escolha do tipo do funcionamento:
    types = []
    type_average_duration = []
    number_of_types = 0
    number_of_hits = 0
    type_hit_average_duration = []
    type_miss_average_duration = []
    if temporizador:
        inicio = time.time()
        intervalo = 0
        while intervalo < Tempo_maximo:
            i1 = time.time()
            randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
            print("Type letter " + randomLowerLetter)
            tecla = readchar.readkey()
            if randomLowerLetter == tecla:
                fi2 = time.time()
                print('The key pressed ' + Fore.GREEN + tecla + Style.RESET_ALL)
                number_of_hits +=1
                number_of_types +=1
                dif1 = fi2 - i1
                type_hit_average_duration.append(dif1)
            else:
                fi3 = time.time()
                print('The key pressed ' + Fore.RED+ tecla + Style.RESET_ALL)
                number_of_types +=1
                dif2 = fi3 - i1 
                type_miss_average_duration.append(dif2)
            f1 = time.time()
            inte1= f1 - i1
            type_average_duration.append(inte1)
            types.append(Inputs(randomLowerLetter, tecla,inte1)) 
            if tecla == chr(32) :
                dicionario(types,intervalo,type_average_duration,number_of_hits,number_of_types,type_hit_average_duration,type_miss_average_duration)
            fim = time.time()
            intervalo = fim - inicio
        print( "Current test duration " + "(" + str(intervalo)+ ")" + " exceeds maximum of "+ str(Tempo_maximo))
        dicionario(types,intervalo,type_average_duration,number_of_hits,number_of_types,type_hit_average_duration,type_miss_average_duration)
    else:
        inicio = time.time()
        intervalo = 0
        for letras in range(1,numero_maximo+1):
            i1 = time.time()
            randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
            print("Type letter " + randomLowerLetter)
            tecla = readchar.readkey()
            if randomLowerLetter == tecla:
                fi2 = time.time()
                print('The key pressed ' + Fore.GREEN + str(tecla) + Style.RESET_ALL)
                number_of_hits +=1
                number_of_types +=1
                dif1 = fi2 - i1
                type_hit_average_duration.append(dif1)
            else:
                fi3 = time.time()
                print('The key pressed ' + Fore.RED+ str(tecla) + Style.RESET_ALL)
                number_of_types +=1
                dif2 =  fi3 - i1
                type_miss_average_duration.append(dif2)
            f1 = time.time()
            inte1= f1 - i1
            type_average_duration.append(inte1)
            types.append(Inputs(randomLowerLetter, tecla,inte1))
            if tecla == chr(32) :
                dicionario(types,intervalo,type_average_duration,number_of_hits,number_of_types,type_hit_average_duration,type_miss_average_duration)
        fim = time.time()
        intervalo = fim - inicio
        print( "Current test duration " + "(" + str(intervalo)+ ")")
        dicionario(types,intervalo,type_average_duration,number_of_hits,number_of_types,type_hit_average_duration,type_miss_average_duration)


def dicionario(types,intervalo,type_average_duration,number_of_hits,number_of_types,type_hit_average_duration,type_miss_average_duration):
    segundos = time.time()
    fim_tempo = time.ctime(segundos)
    accuracy = number_of_hits/number_of_types
    if sum(type_hit_average_duration) == 0:
        typehit_average_duration = 0
    else: 
        typehit_average_duration = sum(type_hit_average_duration)/len(type_hit_average_duration)
    if sum(type_miss_average_duration) == 0:
        typemiss_average_duration = 0
    else:
        typemiss_average_duration = sum(type_miss_average_duration)/len(type_miss_average_duration)

    if sum(type_average_duration) == 0:
        type_averageduration = 0
    else:
        type_averageduration = sum(type_average_duration)/len(type_average_duration)
    my_dict['test_end'] = fim_tempo
    my_dict['test_duration'] =intervalo
    my_dict['inputs'] = types
    my_dict['number_of_types'] = number_of_types
    my_dict['number_of_hits'] = number_of_hits
    my_dict['accuracy'] = accuracy
    my_dict['type_average_duration'] = type_averageduration
    my_dict['type_hit_average_duration'] = typehit_average_duration
    my_dict['type_miss_average_duration']= typemiss_average_duration
    pprint(my_dict)
    print(Fore.BLUE + "Test finished!! Good JOB !!! " + Style.RESET_ALL)
    exit(0)

import os 
from common import Quit_Exception
from volume_calculator import calculate
from card_trick import trick
from pig_latin import translate
while True:
    os.system('clear')
    print('\n 1. pig latin translator \n\n 2. card trick \n\n 3. area/volume calculator')
    choice=input('\nchoose one\n')
    os.system('clear')
    try:
        if choice=='1':
            while True:    
                translate()
        if choice=='2':
            while True:    
                trick()
        if choice=='3':
            while True:
                calculate()
    except Quit_Exception as qe:
        print('')

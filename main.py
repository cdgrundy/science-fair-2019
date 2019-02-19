import os 
from common import Quit_Exception
from calculator import calculator
from volume_calculator import calculate
from card_trick import trick
from pig_latin import translate
while True:
    os.system('clear')
    print('\n 1. traducteur de pig latin \n\n 2. tour de cartes \n\n 3. calculateur de l\'aire / volume')
    choice=input('\nchoisi un\n')
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
        if choice=='4':
            while True:
                calculator()
    except Quit_Exception as qe:
        print('')

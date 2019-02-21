from common import Quit_Exception, ready_to_quit
from triangle import triangulate
from square import squared
from circle import circulate
import os
def calculate():
    print('Tapez Q pour quitter')
    print('Je peut calculer l\'aire \n\n 1. rectangle \n\n 2. triangle \n\n 3. cercle')
    choice=input('\nchoisi\n')
    os.system('clear')
    ready_to_quit(choice)
    if choice=='1':
        squared()
    if choice=='2':
        triangulate()
    if choice=='3':
        circulate()

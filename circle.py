from common import Quit_Exception, ready_to_quit
import math
def circulate():
    
    radius=None
    print('Je peut calculer l\'aire d\'une cercle pour toi')
    
    while not isinstance(radius,float):
        try:
            radius=input('c\'est quoi vos rayons')
            radius=float(radius)
        except ValueError:
            print('s\'il vous plait entrer un numéro')
        except SyntaxError:
            print('s\'il vous plait entrer un numéro')
    answer=radius*radius*math.pi
    print('l\'aire du cercle est {}\n\n\n'.format(answer))

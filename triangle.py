from common import Quit_Exception, ready_to_quit
def triangulate():
    
    base=None
    height=None
    print('Je peut calculer l\'aire d\'une triangle pour toi')
    
    while not isinstance(base,float):
        try:
            base=input('\nc\'est quoi vos base')
            base=float(base)
        except ValueError:
            print('s\'il vous plait entrer un numéro')
        except SyntaxError:
            print('s\'il vous plait entrer un numéro')
    
    while not isinstance(height,float):
        try:
            height=input('c\'est quoi vos hauteur')
            height=float(height)
        except ValueError:
            print('s\'il vous plait entrer un numéro')
        except SyntaxError: 
            print('s\'il vous plait entrer un numéro')
    answer=base*height/2
    print('l\'aire du triangle est {}\n\n\n'.format(answer))

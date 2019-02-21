from common import Quit_Exception, ready_to_quit
def squared():
    
    length=None
    width=None
    print('Je peut calculer l\'aire d\'une rectangle pour toi')
    
    while not isinstance(length,float):
        try:
            length=input('c\'est quoi vos longeur')
            length=float(length)
        except ValueError:
            print('s\'il vous plait entrer un numéro')
        except SyntaxError: 
            print('s\'il vous plait entrer un numéro')
    
    while not isinstance(width,float):
        try:
            width=input('c\'est quoi vos largeur')
            width=float(width)
        except ValueError:
            print('s\'il vous plait entrer un numéro')
        except SyntaxError: 
            print('s\'il vous plait entrer un numéro')
    answer=length*width
    print('l\'aire du rectangle est {}\n\n\n'.format(answer))

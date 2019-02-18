from common import Quit_Exception, ready_to_quit
def calculate():
        print('Tapez Q pour quitter')
        print('Je peut calculer l\'aire ou le volume')
        try:
            length=input('Longueur=')
        except NameError:
            print('Veuillez entrer un numéro entier:')
        except SyntaxError:
            print('Veuillez entrer un numéro entier:')
            ready_to_quit(length) 
            
        try:
            width=input('largeur=')
        except NameError:
            print('Veuillez entrer un numéro entier:')
        except SyntaxError:
            print('Veuillez entrer un numéro entier:')
            ready_to_quit(width)
            
        try:
            height=input('(Si tu veut calculer l\'aire, mis la taille a 1)\n la taille=')
        except NameError:
            print('Veuillez entrer un numéro entier:')
        except SyntaxError:
            print('Veuillez entrer un numéro entier:')
            ready_to_quit(height)
        print('Le reponse est {}.'.format(int(length)*int(height)*int(width)))

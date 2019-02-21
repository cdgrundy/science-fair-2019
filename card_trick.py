import os
import time
from common import Quit_Exception, ready_to_quit

d=u'\u2666'
h=u'\u2665'
s=u'\u2660'
c=u'\u2663'

delay=5


def handle_suit(suit):
        left={'droit','d'}
        right={'gauche','g'}
        print('{0}. Choix interessant. Maintenant, ne pense pas au {0} et choisi un direction au hasard. droit   gauche'.format(suit))
        dire=input().lower()
        while dire not in left and dire not in right:
            print('S\'il vous plait, entre un direction \n')        
            dire=input().lower()
        if dire in left:
            handle_side('droit') 
        if dire in right:
            handle_side('gauche')


def handle_side(side):
        print(f'{side}, bon choix, maintenant choisi un carte mentalement, mais ne tapez pas! J{d}  Q{c}  J{s}  Q{h}  K{c}  K{d}')
        time.sleep(delay)
        print('maintenant frappé le retour')
        finish=input().lower()
        os.system('clear')
        print('pense a ton carte et dit a voix haute') 
        time.sleep(delay)
        print('maintenant frappé le retour')
        finished=input().lower()
        print(f'on a enlevé to carte, J{h}  Q{s}  Q{d}  K{s}  K{h}')
        time.sleep(delay*3)


def trick():
    spade={'pique','piques','p'}
    heart={'coeurs','coeur','c'}
    club={'clubs','club','cl'}
    diamond={'diamants','diamant','d'}
    print('Tapez Q pour quitter')
    print('\ncette astuce va vous étonner, choisissez un costume, pique, cœurs, clubs, diamants')
    choice=input().lower()
    ready_to_quit(choice)
    if choice in spade:
        handle_suit('piques')
    if choice in heart: 
        handle_suit('coeurs')
    if choice in club:
        handle_suit('clubs')
    if choice in diamond:
        handle_suit('diamants')

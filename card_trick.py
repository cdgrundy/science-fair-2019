import time
from common import Quit_Exception, ready_to_quit

d=u'\u2666'
h=u'\u2665'
s=u'\u2660'
c=u'\u2663'

delay=5


def handle_suit(suit):
        left={'left','l'}
        right={'right','r'}
        print('{0}. interesting choice. now, don\'t think of {0} and randomly pick a direction. left   right'.format(suit))
        dire=input().lower()
        while dire not in left and dire not in right:
            print('Please enter a direction \n')        
            dire=input().lower()
        if dire in left:
            handle_side('left') 
        if dire in right:
            handle_side('right')


def handle_side(side):
        print(f'{side}, good choice, now mentaly select a card, but don\'t type it! J{d}  Q{c}  J{s}  Q{h}  K{c}  K{d}')
        time.sleep(delay)
        print('now hit return')
        finish=input().lower()
        print('think about your card and say it aloud twice') 
        time.sleep(delay)
        print('now hit return')
        finished=input().lower()
        print(f'we\'ve removed your card, J{h}  Q{s}  Q{d}  K{s}  K{h}')
        time.sleep(delay*3)


def trick():
    spade={'spades','spade','s'}
    heart={'hearts','heart','h'}
    club={'clubs','club','c'}
    diamond={'diamonds','diamond','d'}
    print('type Q to quit')
    print('\nthis trick will blow your mind, pick a suit, spades  hearts  clubs  diamonds')
    choice=input().lower()
    ready_to_quit(choice)
    if choice in spade:
        handle_suit('spades')
    if choice in heart: 
        handle_suit('hearts')
    if choice in club:
        handle_suit('clubs')
    if choice in diamond:
        handle_suit('diamonds')

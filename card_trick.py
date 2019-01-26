from common import Quit_Exception, ready_to_quit
def handle_suit(suit):
        left={'left','l'}
        right={'right','r'}
        print('{0}. interesting choice. now, don\'t think of {0} and randomly pick a direction. left   right'.format(suit))
        dire=raw_input().lower()
        if dire in left:
            handle_side('left')
        if dire in right:
            handle_side('right')
def handle_side(side):
                done1={'done',''}
                print('{}, good choice, now mentaly select a card, but don\'t type it! Jd  Qc  Js  Qh  Kc  Kd'.format(side))
                finish=raw_input().lower()
                if finish in done1:
                        print('think about your card and say it aloud twice')
                        finished=raw_input().lower()
                        if finished in done1:
                                print('we\'ve removed your card, Jh  Qs  Qd  Ks  Kh')
def trick():
    spade={'spades','spade','s'}
    heart={'hearts','heart','h'}
    club={'clubs','club','c'}
    diamond={'diamonds','diamond','d'}
    print('this trick will blow your mind, pick a suit, spades  hearts  clubs  diamonds')
    choice=raw_input().lower()
    ready_to_quit(choice)
    if choice in spade:
	handle_suit('spade')
    if choice in heart: 
	handle_suit('heart')
    if choice in club:
	handle_suit('club')
    if choice in diamond:
	handle_suit('diamond')

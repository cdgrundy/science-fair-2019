from common import Quit_Exception, ready_to_quit
from addition import addition
from subtraction import subtraction
from multiplication2 import multiplication
from division import division
def calculator():
    print('\n1. addition\n\n2. sutraction\n\n3. multiplication\n\n4. division')
    choice=input('\nchoisi un\n')
    ready_to_quit(choice)
    if choice=='1':
        addition()
    if choice=='2':
        subtraction()
    if choice=='3':
        multiplication()
    if choice=='4':
        division()
        

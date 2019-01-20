from volume_calculator import calculate
from card_trick import trick
from pig_latin import translate
print('\n 1. pig latin translator \n\n 2. card trick \n\n 3. area/volume calculator')
choice=input('choose one')
if choice==1:
    translate()
if choice==2:
    trick()
if choice==3:
    calculate()

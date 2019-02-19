def addition():
    number1=None
    number2=None
    print('Je peux additioné deux nombres pour vous')
    while not isinstance(number1,float):
        try:
            number1=input('C\'est quoi vos numéro premier')
            number1=float(number1)
        except ValueError:
            print('S\'il vous plait entrer un numéro')
        except SyntaxError:
            print('S\'il vous plait entrer un numéro')
    while not isinstance(number2,float):
        try:
            number2=input('C\'est quoi vos deuxieme numéro?')
            number2=float(number2)
        except ValueError:
            print('S\'il vous plait entrer un numéro')
        except SyntaxError:
            print('S\'il vous plait entrer un numéro')
    answer=number1+number2
    print('{}+{}={}'.format(number1,number2,answer))

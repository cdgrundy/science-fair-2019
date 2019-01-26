class Quit_Exception(Exception):
    pass

def ready_to_quit(input):
    quit=('q','quit','','exit')
    if input in quit:
	raise Quit_Exception('We\'re done here')
   

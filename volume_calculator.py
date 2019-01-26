from common import Quit_Exception, ready_to_quit
def calculate():
	print('I can calculate area or volume for you')
	length=raw_input('length=')
        ready_to_quit(length)
	width=raw_input('width=')
        ready_to_quit(width)
	height=raw_input('(if you wish to calculate area, set height to 1)\n height=')
	ready_to_quit(height)
	print('the answer is {}'.format(int(length)*int(height)*int(width)))


from common import Quit_Exception, ready_to_quit
def calculate():
		print('I can calculate area or volume for you')
		try:
			length=raw_input('length=')
		except NameError:
			print('please input a whole nunber')
		except SyntaxError:
			print('please input a whole number')
        	        ready_to_quit(length)
        		width=raw_input('width=')
		except NameError:
			print('please input a whole number')
		except SyntaxError:
			print('please input a whole number')
			ready_to_quit(width)
	       		height=raw_input('(if you wish to calculate area, set height to 1)\n height=')
		except NameError:
			print('please input a whole number')
		except SyntaxError:
			print('please input a whole number')
          		ready_to_quit(height)
        		print('the answer is {}'.format(int(length)*int(height)*int(width)))


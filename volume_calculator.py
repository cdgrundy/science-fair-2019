def calculate():
	print('I can calculate area or volume for you')
	length=input('length=')
	width=input('width=')
	height=input('(if you wish to calculate area, set height to 1)\n height=')
	print('the answer is {}'.format(length*height*width))

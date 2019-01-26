from __future__ import print_function
from common import Quit_Exception, ready_to_quit
puncuation=[',', '.', '?', '!']
vowels=['a','e','i','o','u']
blends=['br','bl','cr','cl','ch','cz','dr','dj','dw','fr','fl','gr','gl','gn','gw','kn','kl','kr','ll','mn','pn','ps','pl','pr','pt','qu','sh','sl','sc','sk','sm','sn','sp','st','sv','sw','sch','scl','scr','spr','squ','str','tr','th','ts','wr','wh'
]
def translate():
    sentence=raw_input('pig latin translator: ')
    ready_to_quit(sentence)
    words=sentence.split()
    for word in words:
    	if word[0] in vowels: 
    		print(word+'way',end=' ')
    	elif word[0:3] in blends:
    		print(word[3:]+word[0:3]+'ay',end=' ')
    	elif word[0:2] in blends:
    		print(word[2:]+word[0:2]+'ay',end=' ')
    	else:
    		print(word[1:]+word[0]+'ay',end=' ')
    print('\n')	

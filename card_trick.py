done2={'done',''}
done1={'done',''}
left={'left','l'}
right={'right','r'}
spade={'spades','spade','s'}
heart={'hearts','heart','h'}
club={'clubs','club','c'}
diamond={'diamonds','diamond','d'}
print('this trick will blow your mind, pick a suit, spades  hearts  clubs  diamonds')
choice=raw_input().lower()
if choice in spade:
	print('spades. interesting choice. now, don\'t think of spades and randomly pick a direction. left   right')
	dire=raw_input().lower()
	if dire in left:
		print('left, good choice, now mentaly select a card, but don\'t type it! J♢  Q♧  J♤  Q♡  K♧  K♢')
		finish=raw_input().lower()
		if finish in done1:
			print('think about your card and say it aloud twice')
			finished=raw_input().lower()
			if finished in done2:
				print('we\'ve removed your card, J♡  Q♤  Q♢ K♤  K♡') 
	if dire in right:
		print('right, good choice, now mentaly select a card, but don\'t type it! J♢  Q♧  J♤  Q♡  K♧  K♢')
		finish=raw_input().lower()
		if finish in done1:
			print('think about your card and say it aloud twice')
			finished=raw_input().lower()
			if finished in done2:
				print('we\'ve removed your card, J♡  Q♤  Q♢ K♤  K♡')
if choice in heart:
	print('hearts. interesting choice. now, don\'t think of hearts and randomly pick a direction. left   right')
	dire=raw_input().lower()
	if dire in left:
		print('left, good choice, now mentaly select a card, but don\'t   type it! J♢  Q♧  J♤  Q♡  K♧  K♢')
		finish=raw_input().lower()
		if finish in done1:
			print('think about your card and say it aloud twice')
			finished=raw_input().lower()
			if finished in done2:
				print('we\'ve removed your card, J♡  Q♤  Q♢ K♤  K♡') 
	if dire in right:
		print('right, good choice, now mentaly select a card, but don\'t type it! J♢  Q♧  J♤  Q♡  K♧  K♢')
		finish=raw_input().lower()
		if finish in done1:
			print('think about your card and say it aloud twice')
			finished=raw_input().lower()
			if finished in done2:
				print('we\'ve removed your card, J♡  Q♤  Q♢ K♤  K♡')

if choice in club:
	print('clubs. interesting choice. now, don\'t think of clubs and randomly pick a direction. left   right')
	dire=raw_input().lower()
	if dire in left:
		print('left, good choice, now mentaly select a card, but don\'t   type it! J♢  Q♧  J♤  Q♡  K♧  K♢')
		finish=raw_input().lower()
		if finish in done1:
			print('think about your card and say it aloud twice')
			if choice in done2:
				print('we\'ve removed your card, J♡  Q♤  Q♢ K♤  K♡') 
	if dire in right:
		print('right, good choice, now mentaly select a card, but don\'t itype it! J♢  Q♧  J♤  Q♡  K♧  K♢')
		finish=raw_input().lower()
		if finish in done1:
			print('think about your card and say it aloud twice')
			finished=raw_input().lower()
			if finished in done2:
				print('we\'ve removed your card, J♡  Q♤  Q♢ K♤  K♡')
if choice in diamond:
	print('diamonds. interesting choice. now, don\'t think of diamonds and randomly pick a direction. left   right')
	dire=raw_input().lower()
	if dire in left:
		print('left, good choice, now mentaly select a card, but don\'t  type it! J♢  Q♧  J♤  Q♡  K♧  K♢')
		finish=raw_input().lower()
		if finish in done1:
			print('think about your card and say it aloud twice')
			finished=raw_input().lower()
			if finished in done2:
				print('we\'ve removed your card, J♡  Q♤  Q♢ K♤  K♡')
	if dire in right:
		print('right, good choice, now mentaly select a card, but don\'t type it! J♢  Q♧  J♤  Q♡  K♧  K♢')
		finish=raw_input().lower()
		if finish in done1:
			print('think about your card and say it aloud twice')
			finished=raw_input().lower()
			if finished in done2:
				print('we\'ve removed your card, J♡  Q♤  Q♢ K♤  K♡')

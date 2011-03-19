class Card(object):
	def __init__(self,string):
		if string[0] == 'A':
			self.val = 14
		elif string[0] == 'K':
			self.val = 13
		elif string[0] == 'Q':
			self.val = 12
		elif string[0] == 'J':
			self.val = 11
		elif string[0] == 'T':
			self.val = 10
		elif:
			self.val = int(string[0])
		self.suit = string[1]

def is_straight(hand):
	hand.sort(key=lambda x: x.val)
	cur = hand[0].val - 1
	for card in hand:
		if card.val != cur+1:
			return False
	return True

def is_flush(hand):
	type = hand[0].suit
	for card in hand:
		if card.suit != type:
			return False
	return True

def identify_hand(x):
	if 

def compare_hands(x,y):
	identify_hand(x)
	flush = [false,false]
	straight = [false,false]
	highest_run = [0,0]
	for hand in x,y:


def get_hands(string):
	hands = map(Card,string.split())
	hand1 = hands[0:5]
	hand2 = hands[5:]
	return hand1,hand2

cardfile = open("data/poker.txt")
for line in cardfile:
	wins = 0
	if compare_hands(*(get_hands(line))):
		wins += 1

print wins

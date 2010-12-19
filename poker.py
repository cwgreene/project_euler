def is_royal_flush(hand):
	def hand_has(hand,values):
		for card in values.split(','):
			if card not in hand:
				return false
		return true

	if is_flush(hand):
		hand_has(hand,"T,J,Q,K,A")
	return False	

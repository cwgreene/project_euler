import itertools as it
import string
import re

def decrypt(key,msg):
	res = []
	key = map(ord,key)
	for k,m in it.izip(it.cycle(key),msg):
		res.append(k^m)
	res=map(chr,res)
	return "".join(res)

def count_word(string,word):
	return len(re.findall(word,string))

def search_key_space(msg):
	lower = string.ascii_lowercase
	for x in lower:
		for y in lower:
			for z in lower:
				res = decrypt(x+y+z,msg)
				if count_word(res," the ") > 5:
					print res,x+y+z

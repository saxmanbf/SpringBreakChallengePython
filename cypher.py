
	# normalizes that input text

def normalize(text):
	
	text = text.lower()
	text = text.replace(" ","")
	
	import re
	text = re.sub(r'\W+', '',text)
	
	return text


	# splits the normalized text into rows that make up the necessary 'square'

def square(text):
	import math
	rows = []
	for i in range( 0,len(text),int(math.ceil(math.sqrt(len(text)))) ):
		rows.append( text[i:i+int(math.ceil(math.sqrt(len(text))))] )
	return rows


def encrypt(rows):

	return newRows
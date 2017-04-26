
	# normalizes the input text

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

	# pads the rows with temporary puncuation to avoid
	# out of index errors in the encrypt function

def pad(rows):
	while len(rows[0]) != len(rows[-1]):
		rows[-1] += '!'
	return rows
	
	# reorders the squared rows into the encrypted rows

def encrypt(rows):
	output = []
	for i in range(len(rows[0])):
		word = []
		for j in range(len(rows)):
			word += rows[j][i]
		output += word
	return ''.join(output)

	# condenses all of the above functions into one function 
	# to fully encrypt the input message

def encryptComplete(text):
	message = normalize(encrypt(pad(square(normalize(text)))))
	return message
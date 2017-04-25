def normalize(text):
	
	text = text.lower()
	text = text.replace(" ","")
	
	import re
	text = re.sub(r'\W+', '',text)
	
	return text

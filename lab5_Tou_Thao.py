"""



"""


def main():
	
	


	DecodeWord()





#Your code goes here.
def DecodeWord() :
	ne = ''
	encodedWord = "WBLARF8TTS"
	# encodedWord = "L8KAOUL"
	# encodedWord = "E8N8N8"
	# encodedWord = "8TRA8DY T8LA"
	# encodedWord = "8TT LHA TILLTA LIMAS"	
	# encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	# encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	# encodedWord = "UUHO"  		#Used for Bonus
	# encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	for i in range(1, len(encodedWord)+1) :
		if encodedWord[i-1:i] == "L":
			ne = ne+"T"
		elif encodedWord[i-1:i] == "T":
			ne = ne+"L"
		elif encodedWord[i-1:i] == "8":
			ne = ne+"A"
		elif encodedWord[i-1:i] == "B":
			ne = ne+"A"
		elif encodedWord[i-1:i] == "A":
			ne = ne+"E"
		elif encodedWord[i-1:i] == "E":
			ne = ne+"B"
		elif encodedWord[i-1:i] == "U":
			if encodedWord[i-1:i+1] == "UU" :
				ne = ne+"W"
		else:
			ne = ne+encodedWord[i-1:i]
		
	print(ne)

	







#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()


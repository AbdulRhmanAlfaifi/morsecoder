import sys

lookUpTable = {"A" : ".-","B" : "-...","C" : "-.-.","D" : "-..","E" : ".","F" : "..-.","G" : "--.","H" : "....","I" : "..","J" : ".---","K" : "-.-","L" : ".-..","M" : "--","N" : "-.","O" : "---","P" : ".--.","Q" : "--.-","R" : ".-.","S" : "...","T" : "-","U" : "..-","V" : "...-","W" : ".--","X" : "-..-","Y" : "-.--","Z" : "--..","0" : "-----","1" : ".----","2" : "..---","3" : "...--","4" : "....-","5" : ".....","6" : "-....","7" : "--...","8" : "---..","9" : "----."}



def printHelpMessage():
	msg = '''
  \x1b[31m=====================================================\x1b[0m
  Developed By AbdulRhman Alfaifi (Twitter @A__ALFAIFI) 
  \x1b[31m=====================================================\x1b[0m

  \x1b[34mUsage:\x1b[0m python morsecoder.py [-e | -d] [Message | CodedMessage]

  -e		Encode mode. Used to encode the message from readable 
		string to morsecode encoded message.

  -d		Decode mode. Used to decode the encoded message 
		from morsecode encoded message to readable message.

  \x1b[34mExamples:\x1b[0m

  \x1b[33mCommand :\x1b[0m python morsecoder.py -e 'AbdulRhman'
  \x1b[32mOutput :\x1b[0m .- -... -.. ..- .-.. .-. .... -- .- -.

  \x1b[33mCommand :\x1b[0m python morsecoder.py -d '.- -... -.. ..- .-.. .-. .... -- .- -.'
  \x1b[32mOutput\x1b[0m : ABDULRHMAN
	'''
	print(msg)


def encode(message):
	results = ""
	message = message.upper()
	for char in message:
		if char == " ":
			results += "/ "
		else:
			try:
				results+=lookUpTable[char]+" "
			except KeyError:
				print('ERROR: Invalid Character.')
				print('Letters and numbers only.')
				sys.exit()
	return results[0:-1]



def decode(coded):
	results = ""
	for code in coded.split(' '):
		if code == '/':
			results += ' '
		else:
			reverseLookUpTable = {v: k for k, v in lookUpTable.items()}
			try:
				results += reverseLookUpTable[code]
			except KeyError:
				print('ERROR: Invalid Character OR wrong morse code.')
				print('Allowed characters are ".", "-" and "/" for space.')
				sys.exit()
	return results


if len(sys.argv) < 3:
	printHelpMessage()
	sys.exit()
if sys.argv[1] == '-e':
	print(encode(sys.argv[2]))
elif sys.argv[1] == '-d':
	print(decode(sys.argv[2]))
else:
	printHelpMessage()

# morsecoder
Command line tool to encode message to morse code and decode morse code to clear message.

# Installing
```
git clone https://github.com/AbdulRhmanAlfaifi/morsecoder.git
cd morsecoder
python morsecoder.py
```
or download 'morsecode.py' file from the browser and run it using ```python morsecoder.py```.

# Usage:
```
  =====================================================
  Developed By AbdulRhman Alfaifi (Twitter @A__ALFAIFI) 
  =====================================================

  Usage: python morsecoder.py [-e | -d] [Message | CodedMessage]

  -e		Encode mode. Used to encode the message from readable 
		string to morsecode encoded message.

  -d		Decode mode. Used to decode the encoded message 
		from morsecode encoded message to readable message.

  Examples:

  Command : python morsecoder.py -e 'AbdulRhman'
  Output : .- -... -.. ..- .-.. .-. .... -- .- -.

  Command : python morsecoder.py -d '.- -... -.. ..- .-.. .-. .... -- .- -.'
  Output : ABDULRHMAN

```

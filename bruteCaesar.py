#!/usr/bin/env python
#title		:bruteCaesar.py
#description	:brute force 
#author		:PwnEIP
#email		:pwneip@gmail.com
#date		:18 Oct 2017
#updates        :
#version	:1.0
#usage		:bruteCaesar.py [-h] <string>
#notes		:
#python_version	:3
#dependencies   :guess_language
#==============================================================================

import sys, getopt, string
from guess_language import guess_language

def usage():
	print("usage: bruteCaesar.py <string>")
	print("\t -h, this menu")
	sys.exit(2)

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    shifted_alphabet = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift] + string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def main(argv):
	try:                                
		opts, args = getopt.getopt(argv, "h", ["help"])
	except getopt.GetoptError:
		usage()
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
	if len(args) > 0:
		for i in range(1,26):
                    plaintext = caesar(' '.join(args), i)
                    language = guess_language(plaintext)
                    if language == "en":
                        print("ROT:" + '{:2}'.format(i) + " " + plaintext + "<----english---") 
                    else:
                        print("ROT:" + '{:2}'.format(i) + " " + plaintext)
		sys.exit(0)
	else:
		usage()

if __name__ == "__main__":
    main(sys.argv[1:])

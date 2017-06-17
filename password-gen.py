#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Generates passwords.
#
# TODO: Add commandline parsing, allow user to decide whether
# to select duplicate or look alike characters.
#

import os
import random
import string

def password_generator(size, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation):
	return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

def main():
	try:
		# Gets user's desired password length. Has error checking and prevention. Goodie!
		password_length = 0
		while(password_length < 8):
			try:
				password_length = int(input("Length of password (Min 8, Max 64): "))
			except ValueError:
				print("Numbers only please.\n")

			if(password_length < 8):
				print("Password length not long enough, try again.")
			elif(password_length > 64):
				print("Password length too large.\nYeah, like you're going to remember it.")
			else:
				break

		password_string = password_generator(password_length)
		print("\nYour password: "+str(password_string))

	except KeyboardInterrupt:
		print("\nKeyboard interrupt, exiting")
	except EOFError:
		print("\n\nEOF Error.")

if __name__ == '__main__':
    main()

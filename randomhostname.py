#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This script is for generating random hostnames. Useful for in situtations
# where you need to hide some details about your computer e.g. wifi hotspots.
#
# TODO: add mac address randomization as an option.

import os
import random
import string

def hostname_generator(size=random.randint(6,12), chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

def main():
	random = hostname_generator()
	print("Changing system hostname to random letters and numbers...")
	command = "hostnamectl set-hostname " + random
	os.system(command)
	print("New Hostname: "+random)

if __name__ == '__main__':
    main()

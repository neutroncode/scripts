#!/usr/bin/env python3
#encoding:utf-8
import ipaddress # Checks for valid IP address
import argparse
import sys
import os

# changeProxy.py
# Changes second proxy chain in privoxy.
# 2 modes
# Interactive and command-line
# If -i (--interactive) flag set, enter Interactive
# mode regardless of the other flags
#
# INTERACTIVE MODE:
# ask for type of proxy, then ip:port,
# then ask if want to save settings
# After save, loop back until keyboard interrupt
#
# COMMAND LINE:
# changeProxy.py [options] ip:port
# -s4 (--socks4) Socks4 proxy
# -s5 (--socks5) Socks5 proxy
#
# TODO:
# Fix the buggy commandline.


class colors:
    BAD = '\033[91m'
    OK = '\033[93m'
    GOOD = '\033[92m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Misc values
class progVariables:
    i = 0;
    configFilepath = "/etc/config/privoxy"

def checkRoot():
    uid = os.getuid()
    if uid != 0:
        print('usage: changeProxy.py [-h] [-i | -s | -I] config')
        sys.stderr.write(colors.BAD + colors.BOLD + "Error: this app needs to be rooted.\n" + colors.ENDC)
        sys.exit(1)

# Edits config file.
# For better editing, use with(open)
def editConfig(socksType,ipAndPort):
    replacementIP = "forward-socks" + str(socksType) + " / " + str(ipAndPort[0]) + ":" + str(ipAndPort[1])

    # Read file to find string to replace
    configFileHandle = open(progVariables.configFilepath,"r+")
    configFile = configFileHandle.readlines()
    for i in range(0,len(configFile)):
        if(configFile[i].find("forward-socks5t") != -1):
            print("") # just a placeholder
        elif(configFile[i].find("forward-socks5") != -1):
            configFile[i] = replacementIP + " .\n"
        elif(configFile[i].find("forward-socks4") != -1):
            configFile[i] = replacementIP + " .\n"

    configFileHandle.close()

    # Write to file
    configFileHandle = open(progVariables.configFilepath,"w")
    configFileHandle.writelines(configFile)
    configFileHandle.close()

# Obtains parameters from command line
def commandLine():
    # Parses the variables on the command line.
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", dest="config", help="Specifies config file.", default="/etc/privoxy/config")
    # IP and socks type
    parser.add_argument("-i", "--ip-port", dest="ipAndPort", help="Sets IP and port. Format your ip and port like this: <ip>:<port>")
    parser.add_argument("-s", "--socks", dest="socksType", help="Specifies socks type.")
    # Whether interactive is wanted
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-I", "--interactive", dest="interactive", help="Enters into interactive mode.", action="store_true")
    args = parser.parse_args()

    # Setting the variables
    # First sets config file before checking
    # for the interactive flag. This is to
    # ensure that the config file can be
    # changed before entering interactive mode.
    if(args.config != ''):
        progVariables.configFilepath = args.config

    if(args.interactive):
        return 0

    editConfig(args.socksType,args.ipAndPort)
    sys.exit(0)
    # check argument variables
    # return error if variables incorrect.

# Opens an interactive shell for the user.
def interactive():
    # ASCII art here!
    try:
        print('Interactive mode. To exit, press Ctrl+C')
        while(1):
            # Reset values
            socksType = 0
            ipAndPort = 0

            while(socksType != 4 or socksType != 5):
                try:
                    socksType = int(input(colors.OK + colors.BOLD + '\nSOCKS Proxy type: ' + colors.ENDC + ' \n[' + colors.BOLD + '4' + colors.ENDC + ' for Socks4] \n['+ colors.BOLD + '5' + colors.ENDC + ' for Socks5] \n> '))
                except ValueError:
                    print("Numbers only please.")

                if(socksType == 4 or socksType == 5):
                    break
                else:
                    print("Select [4] or [5] only.")

            while(ipAndPort != 1):
                try:
                    ipAndPort = str(input(colors.OK + colors.BOLD + '\nEnter IP and Port: ' + colors.ENDC + ' \nLike so: <ip-address>:<port> \n> '))
                    ipAndPort = ipAndPort.split(':')
                    if(ipaddress.ip_address(str(ipAndPort[0]).lower()) != ValueError):
                        break
                except ValueError:
                    print("Enter in IP address and port like this:\n<ip-address>:<port>")

            print("You chose Socks" + str(socksType) + " and IP address " + str(ipAndPort[0]) + ":" + str(ipAndPort[1]))
            if(str(input("\nSave? [Y/n]: ")).lower() == 'y'):
                editConfig(socksType,ipAndPort)
                print(colors.GOOD + colors.BOLD + "Saved!" + colors.ENDC)
            else:
                print(colors.BAD + colors.BOLD + "Not saved." + colors.ENDC)

            progVariables.i = progVariables.i+1
            print("\n+=======+ " + str(progVariables.i) + " +=======+")

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt, exiting")
        sys.exit(0)

def main():
    checkRoot()
    commandLine()
    interactive()

if __name__ == '__main__':
    main()
    # Keyboard interrupt handling here

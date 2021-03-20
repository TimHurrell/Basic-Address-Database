

####!/usr/bin/env python3
####!/usr/bin/python3
#!c:/Python39/python.exe
import getopt, sys
full_cmd_arguments = sys.argv

argument_list = full_cmd_arguments[1:]
print (argument_list)

short_options = "ho:v"
long_options = ["help", "output=", "verbose"]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

# Evaluate given options
for current_argument, current_value in arguments:
    if current_argument in ("-v", "--verbose"):
        print ("Enabling verbose mode")
    elif current_argument in ("-h", "--help"):
        print ("Displaying help")
    elif current_argument in ("-o", "--output"):
        print (("Enabling special output mode (%s)") % (current_value))
#! python3
# mapIt.py - Launches a map in the web browswer using an address from the
#    command line or clipboard

#import webbroswer for launching the browser and import sys for reading
#    the potential command line arguments and pyperclip from copying from
#    the clipboard
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    #Get address from clipboard
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)

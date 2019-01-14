#! python3

# amazonItemTop5ByReview.py

# This program will complete the following tasks;
#     1)Take item of interest from command line or clipboard
#     2)Take item of interest text and search Amazon.com for results
#     3)Return results from Amazon search sorted by Avg. Cust Review
#         -minimum of 100 review for each item returned, if possible
#     4)Take the top 5 results from Avg. Cust Review search and open
#     a new tab in the browser for each

import bs4, pyperclip, requests, sys, webbrowser

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# display text while downloading the Amazon search results page
print('Finding the best reviewed items on Amazon...')

# Download the page details for the target Amazon results search page
res = requests.get('https://www.amazon.com/s/field-keywords=' + address)
res.raise_for_status

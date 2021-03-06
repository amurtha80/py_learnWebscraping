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
# 2019-02-12
# Below code is commented as traditional reqeuests function c=all no longer works with Amazon. One now needs
# an Amazon.com Product API key to access product data from the site
# ACTION: Create Amazon.com Product account and create API Key to access Amazon.com Product data
##res = requests.get('https://www.amazon.com/s/field-keywords=' + replace("address", ' ', '%20') + '&sort=review-count-rank')
##res.raise_for_status

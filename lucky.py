#! python3
# lucky.py - Opens several Google search results

# Gets search keywords from the command line arguments
# Retrieves the search results page
# Opens a browser tab for each result
# Details:
# Read the command line arguments from sys.argv
# Fetch the search result page with the requests module
# Find the links to each search result
# Call the webrowser.open() function to open the web browser

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status

# TODO: Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# TODO: Open a browser tab for each result
# assign an object with the selector element we want. Returns a
#     list of all the elements that matched our selector.
linkElems = soup.select('.r a')

# Open a browser tab for each result
#     store the min of either 5 or the number of links whichever are
#     fewer
numOpen = min(5, len(linkElems))
# Loop through the number of links (value stored in numOpen)
for i in range(numOpen):
    # Open a new tab in the browser. Need to use the initial
    # http://google.com part as that is not in the href attribute
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

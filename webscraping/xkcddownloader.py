# xkcddownloader.py
# automated download of xkcd comics from web

# Does not work with comic 1525

import os
import requests
import bs4

# setup the url for xkcd
url = "https://xkcd.com"

# create a folder to store the comics
os.makedirs("xkcd_pictures", exist_ok=True)

# loop to download all the comics
while not url.endswith("#"): #since the last page has # at end of url
    # Download the page (html)
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of picture using bs4
    comic_elem = soup.select("#comic img") #list

    if comic_elem == []:
        print("\tCan't find the image...")
    else:
        # comic_url -> "https://img.xkcd..."
        if comic_elem[0].get("src").startswith("/2067/"):
            comic_url = "https://xkcd.com" + comic_elem[0].get("src")
        else:
            comic_url = "https:" + comic_elem[0].get("src")

        # Download the image
        res = requests.get(comic_url)
        print(f"\tDownloading image at {comic_url}...")

        # Save the image
        image_file = open(os.path.join("xkcd_pictures", os.path.basename(comic_url)), "wb") #open (file name) binary
        for chunk in res.iter_content(1000000):
            image_file.write(chunk)
        image_file.close()

    # get the Previous button URL
    prev_link = soup.select('a[rel="prev"]')[0] # "/2396/"
    url = "https://xkcd.com" + prev_link.get("href")

print ("Done")
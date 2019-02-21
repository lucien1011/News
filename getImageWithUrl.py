from WebScraper.WebScraper import WebScraper
from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.request import HTTPError 
import argparse

# ________________________________________________________________________ ||
parser = argparse.ArgumentParser()
parser.add_argument('--in_url',action='store',default="https://www.nytimes.com/")
parser.add_argument('--out',action='store',default="DownloadedImg/")

option = parser.parse_args()

# ________________________________________________________________________ ||
url             = option.in_url
output_folder   = option.out
lineDivider     = "="*100

# ________________________________________________________________________ ||
scraper     = WebScraper()

# ________________________________________________________________________ ||
raw_html = scraper.simple_get(url)
html = BeautifulSoup(raw_html,'html.parser')

# ________________________________________________________________________ ||
folder_path = os.path.abspath(output_folder)
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for i,p in enumerate(html.select('img')):
    print(lineDivider)
    numberStr = '{0:02d}'.format(i)
    print("Downloading image "+numberStr)
    try:
        urllib.request.urlretrieve(p['src'],os.path.join(folder_path,'img'+numberStr+'.jpg'))
    except HTTPError:
        print("Error downloading this image: "+p['src'])

#Importing essential libraries
import urllib
import re
from bs4 import BeautifulSoup
import time

file_path = '/content/drive/MyDrive/Kaggle/Portrait/Data' #Path of my google drive where I will be storing the scraped images
base_url = 'https://www.wikiart.org' #Will be scraping the images from wiki-art
portrait_url = base_url + '/en/artists-by-genre/portrait' 

portrait_soup = BeautifulSoup(urllib.request.urlopen(portrait_url), "lxml")
portrait_list_main = portrait_soup.find("main")
lis = portrait_list_main.find_all("li")

for c in range(ord('a'), ord('z')+1):
    char = chr(c)
    artist_list_url = base_url + '/en/Alphabet/' + char + '/text-list'

    genre_soup = BeautifulSoup(urllib.request.urlopen(artist_list_url), "lxml")
    artist_list_main = genre_soup.find("main")
    lis = artist_list_main.find_all("li")
    for li in lis: 
        born = 0
        died = 0
        for line in li.text.splitlines():
            if line.startswith(",") and "-" in line:
                parts = line.split('-')
                if len(parts) == 2:
                    born = int(re.sub("[^0-9]", "",parts[0]))
                    died = int(re.sub("[^0-9]", "",parts[1]))
        if born>1850 and died>0 and (born<1900 or died<1950):
            link = li.find("a")
            artist = link.attrs["href"]
            artist_url = base_url + artist
            artist_soup = BeautifulSoup(urllib.request.urlopen(artist_url), "lxml")
            if "Portrait" in artist_soup.text or "Portrait" in artist_soup.text or "self-portrait" \
                in artist_soup.text or "Self-portrait" in artist_soup.text:
                print(artist + " " + str(born) + " - " + str(died))

                url = base_url + artist + '/all-works/text-list'
                artist_work_soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")

                artist_main = artist_work_soup.find("main")
                image_count = 0
                artist_name = artist.split("/")[2]

                lis = artist_main.find_all("li")

                for li in lis:
                    link = li.find("a")

                    if link != None:
                        painting = link.attrs["href"]

                        url = base_url + painting
                        print(url)
                        try:
                            painting_soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")

                        except:
                            print("error retreiving page")
                            continue

                        if "Public domain" in painting_soup.text:

                            genre = painting_soup.find("span", {"itemprop":"genre"})
                            if genre != None and (genre.text == "portrait" or genre.text == "self-portrait"):

                                og_image = painting_soup.find("meta", {"property":"og:image"})
                                image_url = og_image["content"].split("!")[0] # ignore the !Large.jpg at the end
                                print(image_url)

                                save_path = file_path + "/" + artist_name + "_" + str(image_count) + ".jpg"

                                try:
                                    print("downloading to " + save_path)
                                    time.sleep(0.2)  # try not to get a 403                    
                                    urllib.request.urlretrieve(image_url, save_path)
                                    image_count = image_count + 1
                                except Exception as e:
                                    print("failed downloading " + image_url, e) 
#importing libraries
from bs4 import *
import requests
import re


class AparatPage():
    def __init__(self,page):
        self.page = page
        self.all_links = self.qualities()

    def qualities(self):
        #Download page's source
        pagesource = requests.get(self.page)
        #putting page source in a soup!
        soup = BeautifulSoup(pagesource.text, "html.parser")
        #trying to extract links
        souplinks = soup.find_all("a", {"class": "link"})
        linklist = []
        linkandquality = {}

        for link in souplinks:
            #finding urls and putting them into a list
            linklist.append(link["href"])

        for link in linklist:
            #fidning video qualities with regex
            quality = re.findall(r'https:\/\/.*.*\/.*-(\d{3,4}p).*.\d', link)
            linkandquality[quality[0]] = link

        print(linkandquality)
        return linkandquality

    def downloadvideo(self,quality,filename):
        #cheking the users desired quality
        if(quality == "144" or quality == "144p"):
            download_file(self.all_links["144p"], filename)

        elif(quality == "240" or quality == "240p"):
            download_file(self.all_links["240p"], filename)

        elif(quality == "360" or quality == "360p"):
            download_file(self.all_links["360p"], filename)

        elif(quality == "720" or quality == "720p"):
            download_file(self.all_links["720p"], filename)

        elif(quality == "1080" or quality == "1080p"):
            download_file(self.all_links["1080p"], filename)


#defining a funtion to download the file
def download_file(url, name):
    #cheking if user want to put the default name in the file's name
    if(name == "!default"):
        name = url.split('/')[-1]
    #cheking if user wants to name the file !default
    elif(name == "\!default"):
        #fiding file extension/format
        name = url.split('/')[-1]
        name = name.split('.')
        name = name[-1]
        name = "!default" + "." + name
    #checking if user want to put desired name on the file
    elif(name != "\!default" and name != "!default"):
        #fiding file extension/format
        fileformat = url.split('/')[-1]
        fileformat = fileformat.split('.')
        name = name + "." + fileformat[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return name
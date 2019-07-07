#importing libraries
from bs4 import *
import requests
import re
from colorama import *

#defining a funtion to download the file
def download_file(url,name):
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

def main():
    #getting page's url and it's source
    requestespage = input("What is your video's page?\n")
    page = requests.get(requestespage)
    #putting page source in a soup!
    soup = BeautifulSoup(page.text, "html.parser")
    #trying to extract links
    souplinks = soup.find_all("a", {"class": "link"})
    linklist = []
    links_with_qualities = {}

    for link in souplinks:
        #finding urls and putting them into a list
        linklist.append(link["href"])

    for link in linklist:
        #fidning video qualities with regex
        quality = re.findall(r'https:\/\/.*.*\/.*-(\d{3,4}p).*.\d', link)
        print("New video quality found:" + quality[0])
        links_with_qualities[quality[0]] = link

    #asking user the desired quality
    downloadquality = input("Which quality do you want?\n")
    downloadname = input(
        "What do you want to name it? You can user '!default' for the default name or you can use a new name\n")

    #cheking the users desired quality
    if(downloadquality == "144" or downloadquality == "144p"):
        download_file(links_with_qualities["144p"], downloadname)

    elif(downloadquality == "240" or downloadquality == "240p"):
        download_file(links_with_qualities["240p"], downloadname)

    elif(downloadquality == "360" or downloadquality == "360p"):
        download_file(links_with_qualities["360p"], downloadname)

    elif(downloadquality == "720" or downloadquality == "720p"):
        download_file(links_with_qualities["720p"], downloadname)

    elif(downloadquality == "1080" or downloadquality == "1080p"):
        download_file(links_with_qualities["1080p"], downloadname)

if __name__ == "__main__":
    main()

#this is a regex to find url's/video's quality:
#re.find(r'https:\/\/.*.*\/.*-(\d{3,4}p).*.\d', link)

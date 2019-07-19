#importing libraries
from bs4 import *
import requests
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
from colorama import *

class AparatPage():
    def __init__(self,page):
        self.page = page
        checkurl = self.qualities()
        if("False" in checkurl):
            splittedcheckurl = checkurl.split(" ")
            print("Error occured! The code is: " + splittedcheckurl[1])
            self.validurl = False
        
        self.all_links = checkurl

    def qualities(self):
        #Download page's source
        print("Attemping to get the page.")
        pagesource = requests.get(self.page)
        if(pagesource.status_code == 200):
            pass
        elif(pagesource.status_code != 200):
            return "False" + " " + str(pagesource.status_code)
        
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
        return linkandquality

    def download_video(self,quality,filename):
        try:
            #cheking the users desired quality
            if(quality == "144" or quality == "144p"):
                self.__download_file(self.all_links["144p"], filename)
                
            elif(quality == "240" or quality == "240p"):
                self.__download_file(self.all_links["240p"], filename)

            elif(quality == "360" or quality == "360p"):
                self.__download_file(self.all_links["360p"], filename)
                
            elif(quality == "480" or quality == "480p"):
                self.__download_file(self.all_links["480p"], filename)

            elif(quality == "720" or quality == "720p"):
                self.__download_file(self.all_links["720p"], filename)

            elif(quality == "1080" or quality == "1080p"):
                self.__download_file(self.all_links["1080p"], filename)
            else:
                print("Invalid input for quality!")
        except:
            print("Error happened for finding the quality!")

    def find_playlist_videos(self):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=r"./chromedriver_win32.exe",chrome_options=options)
        driver.get(self.page)
        source = driver.page_source
        # with open("file.txt","w+",encoding="utf-8") as f:
        #     f.write(source)
        soup = BeautifulSoup(source, "html.parser")
        div = soup.find("div", attrs={"class": "playlist-body ss-container"})
        playlist = div
        playlistsoup = BeautifulSoup(str(playlist), "html.parser")
        links = playlistsoup.find_all("a", {"class": "title"})
        urls = []
        for link in links:
            urls.append(link.get("href"))
        for link in urls:
            currentindex = urls.index(link)
            fulllink = "https://aparat.com"+link
            urls[currentindex] = fulllink
        return urls

    #defining a funtion to download a file
    def __download_file(self,url,name):
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
        #Without progress bar:
        # with requests.get(url, stream=True) as r:
        #     r.raise_for_status()
        #     with open("downloads/" + name, 'wb') as f:
        #         for chunk in tqdm(r.iter_content(chunk_size=8192),r.headers.get("content-length")):
        #             if chunk:  # filter out keep-alive new chunks
        #                 f.write(chunk)
        #                 # f.flush()
        
        #And with progress bar:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open("downloads/" + name, 'wb') as f:
                pbar = tqdm(total=int(r.headers['Content-Length']))
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        pbar.update(len(chunk))
        return name

    def all_album_videos(self):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(self.page)
        source = driver.page_source
        # with open("file.txt","w+",encoding="utf-8") as f:
        #     f.write(source)
        soup = BeautifulSoup(source, "html.parser")
        div = soup.find("div", attrs={"class": "playlist-body ss-container"})
        playlist = div
        playlistsoup = BeautifulSoup(str(playlist), "html.parser")
        links = playlistsoup.find_all("a", {"class": "title"})
        urls = []
        for link in links:
            urls.append(link.get("href"))
        for link in urls:
            currentindex = urls.index(link)
            fulllink = "https://aparat.com"+link
            urls[currentindex] = fulllink
        return urls

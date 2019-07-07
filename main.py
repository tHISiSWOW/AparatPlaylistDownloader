try:
    from apget import *
    import os
    import sys
    import selenium_tool
    from colorama import *
    init(autoreset=True)
    def isjustspace(string):
        flag_justspace = None
        for char in string:
            if char != " ":
                flag_justspace = False
        if(flag_justspace == False):
            return False
        else:
            flag_justspace = True
            return True

    def checkinput(inputstring):
        splittedinputstring = (inputstring.lower()).split(" ")
        if(inputstring == "1" or"download" and "album" in splittedinputstring or "album" in splittedinputstring or inputstring.lower() == "1. Download an album" or "download" and "playlist" in splittedinputstring or "download" and "playlist" in splittedinputstring):
            return "downloadplaylist"

        elif(inputstring == "single" or inputstring.lower() == "download a single video" or "single" in splittedinputstring or "single video" in splittedinputstring or "video" in splittedinputstring or inputstring == "2" or "2" in inputstring):
            return "downloadsinglevideo"

        elif(inputstring == "save"):
            pass

        elif(isjustspace(inputstring)):
            return "justspace"

        elif(inputstring == ""):
            return "blank"

        elif(inputstring == "help"):
            return "help"

        elif(inputstring == "quit"):
            return "quit"

        else:
            return "wronginput"

    def isaparaturl(url):
        slashsplittedurl = None
        if("/" in url):
            slashsplittedurl = url.split("/")
        else:
            if("aparat.com" not in url):
                return False
        for member in slashsplittedurl:
            if(member == ""):
                slashsplittedurl.remove(member)
        if(hasscheme(url)):
            dotsplittedurl = slashsplittedurl[1].split(".")
            try:
                if(len(dotsplittedurl) == 3):
                    if(dotsplittedurl[0] == "www" and dotsplittedurl[1] == "aparat" and dotsplittedurl[2] == "com"):
                        return True
                elif(len(dotsplittedurl) == 2):
                    if(dotsplittedurl[0] == "aparat" and dotsplittedurl[1] == "com"):
                        return True
                elif(len(dotsplittedurl) > 3):
                    if(dotsplittedurl[1] == "aparat" and dotsplittedurl[2] == "com"):
                        return True
                    elif(dotsplittedurl[2] == "aparat" and dotsplittedurl[3] == "com"):
                        return True
                    elif(dotsplittedurl[3] == "aparat" and dotsplittedurl[4] == "com"):
                        return True
            except:
                return "nofiltermatched"

        elif(hasscheme(url) == False):
            dotsplittedurl = slashsplittedurl[0].split(".")
            try:
                if(len(dotsplittedurl) == 3):
                    dotsplittedurl = slashsplittedurl[0].split(".")
                    if(dotsplittedurl[0] == "www" and dotsplittedurl[1] == "aparat" and dotsplittedurl[2] == "com"):
                        return True
                elif(len(dotsplittedurl) == 2):
                    dotsplittedurl = slashsplittedurl[0].split(".")
                    if(dotsplittedurl[0], dotsplittedurl[1] == "aparat", "com"):
                        return True
                elif(len(dotsplittedurl) > 3):
                    if(dotsplittedurl[1] == "aparat" and dotsplittedurl[2] == "com"):
                        return True
                    elif(dotsplittedurl[2] == "aparat" and dotsplittedurl[3] == "com"):
                        return True
                    elif(dotsplittedurl[3] == "aparat" and dotsplittedurl[4] == "com"):
                        return True
            except:
                return "nofiltermatched"

        else:
            return False


    def hasscheme(url):
        splittedurl = url.split("/")
        if(splittedurl[0] == "http:" or splittedurl[0] == "https:" and splittedurl[1] == ""):
            return True
        else:
            return False


    def main():
        #print(Style.BRIGHT + "Trying to install the required libraries...")
        #import required_libraries
        selenium_tool.start()
        os.system("cls")
        flag_stay = True
        print(Style.BRIGHT + Fore.MAGENTA + '''
                 _____    _____  
         /\     |  __ \  |  __ \ 
        /  \    | |__) | | |  | |
       / /\ \   |  ___/  | |  | |
      / ____ \  | |      | |__| |
     /_/    \_\ |_|      |_____/ 
                             
                             ''')
        print(Style.BRIGHT + Fore.CYAN + "Hi! And wellcome to Aparat Playlist Downloader")
        print(Style.BRIGHT + Fore.CYAN + "This is the first version and I hope you enjoy it.")
        print(Style.BRIGHT + Fore.CYAN + "This program is made by Aidin Hosseinzadeh.")
        print(Style.BRIGHT + Fore.CYAN + "I'll be happy to receive any bug report or suggestion.")
        print(Style.BRIGHT + Fore.CYAN + "Email: aidinpvm@gmail.com\n")
        print(Style.BRIGHT + Fore.CYAN + "Confused?! Type help to get some!")
        try:
            while(flag_stay == True):
                
                job = input(Style.BRIGHT)
                if(checkinput(job) == "downloadplaylist"):
                    url = input(Style.BRIGHT + "Enter the page's url: ")
                    if(isaparaturl(url)):
                        if(hasscheme(url) == False):
                            url = "https://" + url
                    else:
                        print(Style.BRIGHT + Fore.RED + "It looks that the entered url is wrong.")
                    try:
                        if(hasscheme(url) and isaparaturl(url) == True):
                            flag_defaultquality = False
                            flag_defaultname = False
                            defaultquality = None
                            defaultname = None
                            defaultqualityisvalid = None
                            primarypage = AparatPage(url)
                            albumlinks = primarypage.find_playlist_videos()
                            defaultqualityinput = input(Style.BRIGHT + "Do you want to set a default quality for all the videos?(y/n)")

                            defaultnameinput = input(Style.BRIGHT + "Do you want to let the program automatically set a name for videos by a base name?(y/n)")
                            
                            if(defaultqualityinput.lower() == "y"):
                                flag_defaultquality = True
                                defaultquality = input(Style.BRIGHT + "Which quality do you want to choose for all the videos?")

                            if(defaultnameinput.lower() == "y"):
                                flag_defaultname = True
                                defaultname = input(Style.BRIGHT + "What would be the base name for all the videos?")

                            flag_counter = 0
                            for link in albumlinks:
                                page = AparatPage(link)
                                desiredname = None
                                desiredquality = None
                                flag_validquality = None
                                alternativequality = ""
                                flag_validalternativequality = None
                                if(flag_defaultquality != True):
                                    print("Video qualities are:")
                                    for quality in page.all_links:
                                        print(Style.BRIGHT + quality)
                                    desiredquality = input(Style.BRIGHT + "Which quality do you want to download?\n")
                                if(flag_defaultname != True):
                                    desiredname = input(Style.BRIGHT + "What do you want to name it?(Enter !default to put the default name)\n")
                                if(flag_counter == 0):
                                    print(Style.BRIGHT + "Trying to download the 1st video!")
                                elif(flag_counter == 1):
                                    print(Style.BRIGHT + "Trying to download the 2nd video!")
                                elif(flag_counter == 2):
                                    print(Style.BRIGHT + "Trying to download the 3rd video!")
                                elif(flag_counter > 2):
                                    print(Style.BRIGHT + "Trying to download the {}th video!".format(flag_counter + 1))
                                for quality in page.all_links:
                                    if(str(defaultquality).replace("p", "") + "p" == quality):
                                        flag_validquality = True
                                
                                while(flag_validquality != True and flag_defaultquality == True):
                                    if(flag_validalternativequality == True):
                                        break
                                    else:
                                        alternativequality = input(Style.BRIGHT + Fore.YELLOW + "The default quality looks to be not available for this video. Please choose another quality.\n")

                                        for quality in page.all_links:
                                            if(alternativequality.replace("p", "") + "p" == quality):
                                                flag_validalternativequality = True
                                
                                page.download_video(defaultquality if flag_defaultquality == True and flag_validquality == True else alternativequality if flag_validalternativequality == True else desiredquality if flag_defaultquality != True else desiredquality, defaultname if flag_defaultname == True and flag_counter == 0 else defaultname + str(flag_counter) if flag_defaultname == True and flag_counter > 0 else desiredname if flag_defaultname != True else desiredname)

                                print(Style.BRIGHT + Fore.GREEN + "\nFinished downloading!")
                                
                                flag_counter += 1
                    #Defining the exceptions to avoid the mess!
                    except requests.exceptions.MissingSchema:
                        print(Style.BRIGHT + Fore.RED + "You entered a wrong url. Perhaps you have missed http://")
                    except requests.exceptions.ConnectionError:
                        print(Style.BRIGHT + Fore.RED + "There was a connection error.")
                    except:
                        print(Style.BRIGHT + Fore.RED + "Something went wrong.")

                elif(checkinput(job) == "downloadsinglevideo"):
                    url = input(Style.BRIGHT + "Enter the page's url: ")
                    if(isaparaturl(url)):
                        if(hasscheme(url) == False):
                            url = "https://" + url
                    else:
                        print(Style.BRIGHT + Fore.RED + "It looks that you have entered a wrong url.")
                    try:
                        if(isaparaturl(url)):
                            if(hasscheme(url)):
                                page = AparatPage(url)
                                print(Style.BRIGHT + "Video qualities are:")
                                for quality in page.all_links:
                                    print(quality)
                                desiredquality = input(Style.BRIGHT + "Which quality do you want to download?\n")
                                desiredname = input(Style.BRIGHT + "What do you want to name it?(Enter !default to put the default name)\n")
                                page.download_video(desiredquality, desiredname)
                                print(Style.BRIGHT + Fore.GREEN + "\nFinished downloading!")

                    #Defining the exceptions to avoid the mess!
                    except requests.exceptions.MissingSchema:
                        print(Style.BRIGHT + Fore.RED + "You entered a wrong url. Perhaps you have missed http://")
                    except requests.exceptions.ConnectionError:
                        print(Style.BRIGHT + Fore.RED + "There was a connection error.")
                    except:
                        print(Style.BRIGHT + Fore.RED + "Something went wrong.")

                elif(checkinput(job) == "blank" or checkinput(job) == "justspace"):
                    pass

                elif(checkinput(job) == "help"):
                    print(Style.BRIGHT + "1. Download a playlist.")
                    print(Style.BRIGHT + "2. Download a single video.")

                elif(checkinput(job) == "wronginput"):
                    print(Style.BRIGHT + Fore.RED + "Wrong input.")

                elif(checkinput(job) == "quit"):
                    sys.exit()
        except:
            print(Style.BRIGHT + Fore.RED + "An unknown error occurred.")
        input()
except:
    print(Style.BRIGHT + Fore.RED + "An unknown error occurred.")
if __name__ == "__main__":
    main()

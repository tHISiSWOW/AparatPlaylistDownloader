try:
    from apget import *
    import os
    import sys
    import selenium_tool
    from colorama import *
    from tkinter import *
    from tkinter import ttk
    from tkinter.ttk import Progressbar
    from configparser import ConfigParser

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
                            if(primarypage.validurl != False):
                                albumlinks = primarypage.find_playlist_videos()
                                defaultqualityinput = input(Style.BRIGHT + "Do you want to set a default quality for all the videos?(y/n)")

                                defaultnameinput = input(Style.BRIGHT + "Do you want to let the program automatically number videos videos by a base name?(y/n)")
                                
                                if(defaultqualityinput.lower() == "y"):
                                    flag_defaultquality = True
                                    defaultquality = input(Style.BRIGHT + "What would be the default quality?")

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
                            else:
                                pass
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
                                print(Style.BRIGHT + "Availabe video qualities are:")
                                for quality in page.all_links:
                                    print(quality)
                                desiredquality = input(Style.BRIGHT + "Enter your desired quality.\n")
                                desiredname = input(Style.BRIGHT + "Enter your desired name.(Enter !default to put the default name)\n")
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

    def popupmsg(msg):
        try:
            t_check.join()
        except:
            pass
        global popup
        popup = Tk()
        popup.wm_title("اخطار")
        NORM_FONT = ("IRANSans 8")
        global po_label
        po_label = Label(popup, text=msg, font=NORM_FONT,fg="gray25",bg="white")
        po_label.pack(side=TOP, fill="x",padx=10,pady=10)
        global B1
        B1 = Button(popup,bd=1, font=NORM_FONT, text="باشه",fg="white",bg="gray25", command = popup.destroy)
        B1.pack(side=TOP,padx=10,pady=10)
        popup.geometry("260x100")
        popup.config(bg="white")
        try:
            popup.wm_iconbitmap(r'./icon/down_arrow_J6h_icon.ico')
        except:
            pass
        popup.resizable(width=False, height=False)
        popup.mainloop()

    def downlod_playlist():
        pass

    def save_playlist():
        config['optins'] = {
            'name_entry': list_name,
            'name_url': list_name,
            'url': link_name,
            'number': list_number
        }
        with open(r"./save_palylist.ini","w") as s:
            config.write(s)

    def show_info():
        popupmsg('''this program has been written by:\nHamidreza Zangoie Known as hamid_1856\nEmail: hrzangoie@gmail.com\nTelegram Chanel: @Sour_software\nversion: 0.0.1 alfa''')   

    def exit_event():
        
        try:
            popup.destroy()
        except:
            pass
        window.destroy()

    def load_playlist():
        pass

    def language():
        pass

    Bd = 1
    bg_color = "medium spring green"
    fg_color = "snow2"
    font_ = "IRANSans 9"

    window = Tk()
    window.title("Aparat Playlint Downloader | by Aidin & Hamids")
    

    config = ConfigParser()
    parser = ConfigParser()

    nb = ttk.Notebook(window)

    page1 = Frame(nb)
    page2 = Frame(nb)

    nb.add(page1, text=' صفحه اصلی ')
    nb.add(page2, text=' تنظیمات ')




    frame1 = LabelFrame(page1,bd=0)
    frame1.pack(pady=(5,5),padx=(5,5),fill=BOTH)
    frame2 = LabelFrame(page1,bd=0)
    frame2.pack(pady=(5,0),padx=(5,5),expand=1,fill=BOTH)
    frame4 = LabelFrame(frame2,bd=0)
    frame4.pack(side=TOP,anchor=W,expand=1,fill=BOTH)
    frame3 = LabelFrame(frame2,bd=0)
    frame3.pack(side=TOP,anchor=W,fill=BOTH)

    progress = Progressbar(frame3, orient=HORIZONTAL,length=100,  mode='determinate')
    progress.pack(side=TOP,anchor=W,padx=(5,5),pady=(5,5),fill=BOTH,expand=1)

    p_p = Label(progress,text="%0",bg='gray90')
    p_p.pack(anchor='center',padx=(0,5),pady=(5,5))

    listbox = Listbox(frame4,width=87,bd=Bd,height=12,fg=fg_color,bg=bg_color,font=font_)
    listbox.pack(side=TOP,anchor=N,padx=(5,5),pady=5,fill=BOTH)

    Label(frame1,text="آدرس:",font=font_).pack(side=LEFT,anchor=W,padx=(5,0),pady=(5,5))

    url_entry = Entry(frame1,font=font_,bd=Bd)
    url_entry.pack(side=LEFT,anchor=N,padx=(5,0),pady=(5,5),expand=1,fill=BOTH)

    btn_search = Button(frame1,text="جوست و جو",fg=fg_color,bg=bg_color,font=font_,bd=Bd)
    btn_search.pack(side=LEFT,anchor=E,padx=(5.5),pady=(5,5))

    Label(page2,text="کیفیت",font=font_).pack(side=TOP,anchor=W)

    cb = ttk.Combobox(page2,state='readonly',font=font_,values=("پایین ترین","بالا ترین"))
    cb.set("پایین ترین")
    cb.pack(side=TOP,anchor=W,padx=5,pady=(0,5))

    D_button = Button(frame3,text="دانلود پلی لیست",state='disabled',fg=fg_color,bg=bg_color,font=font_,bd=Bd)
    D_button.pack(side=RIGHT,anchor=NW,padx=(5,5),pady=(5,5))

    S_button = Button(frame3,text="ذخیره پلی لیست",state='disabled',fg=fg_color,bg=bg_color,font=font_,bd=Bd)
    S_button.pack(side=RIGHT,anchor=NW,padx=(5,5),pady=(5,5))

    # create a toplevel 
    # menu
    menubar = Menu(window)

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="بارگذاری پلی لیست", command=load_playlist)
    filemenu.add_command(label="ذخیره پلی لیست", command=save_playlist)
    filemenu.add_separator()
    filemenu.add_command(label="خروج", command=exit_event)
    menubar.add_cascade(label="فایل", menu=filemenu)


    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="اطلاعات")
    helpmenu.add_separator()
    helpmenu.add_command(label="درباره")
    menubar.add_cascade(label="کمک", menu=helpmenu)

    window .config(menu=menubar)

    nb.pack(expand=1, fill="both",padx=5,pady=5)


except:
    print(Style.BRIGHT + Fore.RED + "An unknown error occurred.")

if __name__ == "__main__":
    window.protocol("WM_DELETE_WINDOW", exit_event)
    window.iconbitmap(r"./icon/down_arrow_J6h_icon.ico")
    window.resizable(width=False,height=False)
    #window.geometry("700x500")
    window.mainloop()
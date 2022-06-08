# import module 
import subprocess
import os 
import json
import sys
import requests 
from colorama import Fore 

class MusicDownload:



    # Platoform 
    def soundcloud(self, url):
        filename = subprocess.check_output(
            ['youtube-dl', '--get-filename', url]
        )


        subprocess.call(
            ['youtube-dl', url]
        )

        json_files = [pop_json for pop_json in os.listdir(os.path.dirname(os.path.realpath('__file__'))) if pop_json.endswith('.json')]
        print(Fore.YELLOW+ "Download Pleas Wait... \n")

        with open(json_files[0], 'r') as fp:
            data = json.load(fp)
            
        url=data['url']
        thumb = data['thumbnail']
        title = data['fulltitle']

        test1 = os.path.join(f"{title.mp3}", self.path)
        print("*"* 20)
        print(self.path)
        fp =  open(test1, "w")
        # fp.write(requests.get(url, stream=True).content)
        fp.write(requests.get(url, stream=True).content)
        print(Fore.BLUE+ f"Downlaod {title} is finished, Follow Mehras Dreams on GitHub")


    def spotify(self):
        print(Fore.RED+ "This platform is developing...")

    
    def youtube(self):
        print(Fore.RED+ "This platform is developing...")

def clear_terminal():
    try:
        os.system('clear')
    except:
        os.system('cls')

# Client inputs 
# path_directory = input(Fore.YELLOW+ "Enter your path you want download the music (Press Enter to save music in here) :>> ")
 
clear_terminal()

# if not path_directory:
#     print("")
#     path_directory = os.getcwdb()

platform_input = str(input(Fore.GREEN+ "\nEnter your platform you want download from that\n\n1[SoundCloud] \n2[YouTube]\n3[Spotify]\n\n:>>"))

if not platform_input:
    raise ValueError('You should select the platform')

# Create the object
msdonwlaoder = MusicDownload()

# Download the music from our object


if platform_input == str(1):
    clear_terminal()
    link_input = input(Fore.BLUE+"Enter your song url: ")
    msdonwlaoder.soundcloud(url=link_input)

elif platform_input == str(2):
    clear_terminal()
    print(Fore.RED+ "Is developing :(")
    sys.exit()


if platform_input == str(3):
    clear_terminal()
    print(Fore.RED+ "Is developing :(")
    sys.exit()

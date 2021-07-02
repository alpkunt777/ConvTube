from pytube import YouTube
import __future__
import youtube_dl
import os
from colorama import init,Fore,Back,Style

os.system("clear")
init()

options = input(f"{Fore.YELLOW}DownTube is a Youtube video forwarding program.\nMy Discord: Alpkunt#4620\n\n{Fore.GREEN}[1] {Fore.CYAN}Convert mp3\n{Fore.GREEN}[2] {Fore.CYAN}Convert mp4\n{Fore.GREEN}\n{Fore.LIGHTRED_EX}downtube >>> {Style.RESET_ALL}")


if options == "1":
	url = input(f"\n{Fore.YELLOW}Please paste the url of the youtube video you want to convert.\n\n{Fore.LIGHTRED_EX}downtube >>> {Style.RESET_ALL}")

	os.system("clear")

	ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

	youtube_dl.YoutubeDL(ydl_opts).download([url])
    	
	print(f"{Fore.YELLOW}\n\nConvert is complated succesfully! Pleasee check DownTube directory.")


if options == "2":
	url = input(f"\n{Fore.YELLOW}Please paste the url of the youtube video you want to convert.\n\n{Fore.LIGHTRED_EX}downtube >>> {Style.RESET_ALL}")

	YouTube(url).streams.first().download()
	print(f"{Fore.YELLOW}\n\nConvert is complated succesfully! Pleasee check DownTube directory.")

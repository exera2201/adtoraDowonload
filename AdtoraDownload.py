import youtube_dl
from pystyle import *

System.Title('AdtoraDownload by exera2201')

ydl_opts = {}

Adtora = """
 █████  ██████  ████████  ██████  ██████   █████  ██████   ██████  ██     ██ ███    ██ ██       ██████   █████  ██████  
██   ██ ██   ██    ██    ██    ██ ██   ██ ██   ██ ██   ██ ██    ██ ██     ██ ████   ██ ██      ██    ██ ██   ██ ██   ██ 
███████ ██   ██    ██    ██    ██ ██████  ███████ ██   ██ ██    ██ ██  █  ██ ██ ██  ██ ██      ██    ██ ███████ ██   ██ 
██   ██ ██   ██    ██    ██    ██ ██   ██ ██   ██ ██   ██ ██    ██ ██ ███ ██ ██  ██ ██ ██      ██    ██ ██   ██ ██   ██ 
██   ██ ██████     ██     ██████  ██   ██ ██   ██ ██████   ██████   ███ ███  ██   ████ ███████  ██████  ██   ██ ██████  
                                                                                                                        
"""
print(Colorate.Vertical(Colors.blue_to_purple, Adtora))


def dl_vid():
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([zxt])
        
        
channel = 1
while channel == int(1):
        link = input(Col.blue +"Entre l'url de la vidéo->")
        zxt = link.strip() 
        
        dl_vid()
        
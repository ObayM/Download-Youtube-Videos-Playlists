from importlib.resources import path
from django.shortcuts import render

import pafy
from pytube import Playlist
import pytube
# from .models import Login

# Create your views here.



def index(request):
    if request.method == "POST":
        url = request.POST.get("name_url")
        DOWNLOAD_DIR = request.POST.get("path")
        type = request.POST.get("type")
        quality = request.POST.get("quality")
#Download video
        if type == "2": 
            
            url_video = pafy.new(url)
            
            if quality == "2": #Download video with quallity 720p

                my_list = []

                for video in url_video.allstreams:
                    my_list.append(str(video))
                i  = 0
                while i != len(my_list):
                        if "normal:mp4@" in my_list[i] and "720" in my_list[i]:
                                print("ok "+ my_list[i] +" "+ str(my_list.index(my_list[i])))
                                quallity_video = my_list.index(my_list[i])
                        i +=1
                url_video.allstreams[quallity_video].download(filepath=DOWNLOAD_DIR)


            elif quality == "1": #Download video with quallity 720p

                my_list = []

                for video in url_video.allstreams:
                    my_list.append(str(video))
                i  = 0
                while i != len(my_list):
                        if "normal:mp4@" in my_list[i] and "720" in my_list[i]:
                                print("ok "+ my_list[i] +" "+ str(my_list.index(my_list[i])))
                                quallity_video = my_list.index(my_list[i])
                        i +=1
                url_video.allstreams[quallity_video].download(filepath=DOWNLOAD_DIR)
        
        if type == "3":
            if quality == "1":
                
                ur_rP = Playlist(url)
                c=0
                while c != len(ur_rP.video_urls):
                        url_video = pafy.new(ur_rP.video_urls[c])


                        my_list = []

                        for video in url_video.allstreams:
                                my_list.append(str(video))
                        i  = 0
                        while i != len(my_list):
                                if "normal:mp4@" in my_list[i] and "360" in my_list[i]:
                                        print("ok "+ my_list[i] +" "+ str(my_list.index(my_list[i])))
                                        quallity_video = my_list.index(my_list[i])
                                i +=1
                        url_video.allstreams[quallity_video].download(filepath=DOWNLOAD_DIR)
                        c+=1
            elif quality == "2":

                ur_rP = Playlist(url)
                c=0
                while c != len(ur_rP.video_urls):
                        url_video = pafy.new(ur_rP.video_urls[c])


                        my_list = []

                        for video in url_video.allstreams:
                                my_list.append(str(video))
                        i  = 0
                        while i != len(my_list):
                                if "normal:mp4@" in my_list[i] and "720" in my_list[i]:
                                        print("ok "+ my_list[i] +" "+ str(my_list.index(my_list[i])))
                                        quallity_video = my_list.index(my_list[i])
                                i +=1
                        url_video.allstreams[quallity_video].download(filepath=DOWNLOAD_DIR)
                        c+=1
                
        elif type=="1":
            audio = pafy.new(url)
            audio.getbestaudio().download(filepath=DOWNLOAD_DIR)


    return render(request,"pages/index.html")
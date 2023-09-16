from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Videos,Playliststory,Story,Videoplaylist,Vcomment,Scomment
from django.views.generic.edit import CreateView# Create your views here.
from .forms import CantactForm,StoryConnectForm
from django.db.models import Q
import random
def home(request):
    return render(request,"index.html")

def videos(request):
    videos=Videos.objects.filter(first_youtuber=False).order_by('-time_stamp')[0:8]
    fant=Videos.objects.filter(genres='Fantasy',first_youtuber=False).order_by('-time_stamp')[0:8]
    comedy=Videos.objects.filter(genres='Comedy',first_youtuber=False).order_by('-time_stamp')[0:8]
    moral=Videos.objects.filter(genres='Moral',first_youtuber=False).order_by('-time_stamp')[0:8]
    horror=Videos.objects.filter(genres='Horror',first_youtuber=False).order_by('-time_stamp')[0:8]
    action=Videos.objects.filter(genres='Action',first_youtuber=False).order_by('-time_stamp')[0:8]
    suspence=Videos.objects.filter(genres='Suspence',first_youtuber=False).order_by('-time_stamp')[0:8]
    scici=Videos.objects.filter(genres='Sci-Fi',first_youtuber=False).order_by('-time_stamp')[0:8]
    english=Videos.objects.filter(language='English',first_youtuber=False).order_by('-time_stamp')[0:8]
    telugu=Videos.objects.filter(language='Telugu',first_youtuber=False).order_by('-time_stamp')[0:8]
    video_playlist=Videoplaylist.objects.filter(first_youtuber=False)[0:8]
    context={
        'videos':videos,
        'fant':fant,
        'comedy':comedy,
        'moral':moral,
        'horror':horror,
        'action':action,
        'suspence':suspence,
        'scici':scici,
        'english':english,
        'telugu':telugu,
        'video_playlist':video_playlist

    }
    return render(request,"videos.html",context)

def play_video(request,slug):
    print(slug)
    video=Videos.objects.get(slug=slug)
    value=video.genres
    count=5
    slice = random.random() * (count - 5)
    videos=Videos.objects.filter(genres=value)[slice: slice+5]
    comments=Vcomment.objects.filter(slug=Videos.objects.get(slug=slug))
    context={
        'video':video,
        'videos':videos,
        'slug':slug,
        'comments':comments
    }
    return render(request,"video.html",context)

def story(request):
    playlist=Playliststory.objects.filter(story_connect=False)
    short_storys=Story.objects.filter(subtitle__isnull=True,story_connect=False)
    context={
        'playlist':playlist,
        'short_storys':short_storys
    }
    return render(request,"StoryPlanes.html",context)

class ContactUs(CreateView):
    template_name="About.html"
    form_class=CantactForm

    def form_valid(self, form):
        form.save()
        return redirect('/')
    
class SendStory(CreateView):
    template_name="SendPlanes.html"
    form_class=StoryConnectForm

    def form_valid(self, form):
        form.save()
        return redirect("/")

def soon(request):
    return render(request,"soon.html")


def storyplaylist(request,slug):
    storylist=Story.objects.filter(plalist=Playliststory.objects.get(slug=slug))
    comments=Scomment.objects.filter(slug=Playliststory.objects.get(slug=slug))
    context={
        'storylist':storylist,
        'slug':slug,
        'comments':comments
    }
    return render(request,"storyplaylist.html",context)

def videos_all(request,value):
    videos=Videos.objects.filter(Q(genres=value )| Q(language=value))
    context={
        'videos':videos,
        'value':value
    }
    return render(request,"videos_all.html",context)

def video_playlist(request,slug):
    playlists=Videos.objects.filter(playlist=Videoplaylist.objects.get(slug=slug))
    print(playlists)
    context={
        'playlists':playlists,
    }
    return render(request,"video_playlist.html",context)

def story_connect(request):
    playlist=Playliststory.objects.filter(story_connect=True)
    short_storys=Story.objects.filter(subtitle__isnull=True,story_connect=True)
    context={
        'playlist':playlist,
        'short_storys':short_storys
    }
    return render(request,"story_connect.html",context)

def first_youtuber(request):
    videos=Videos.objects.filter(first_youtuber=True).order_by('-time_stamp')[0:8]
    fant=Videos.objects.filter(genres='Fantasy',first_youtuber=True).order_by('-time_stamp')[0:8]
    comedy=Videos.objects.filter(genres='Comedy',first_youtuber=True).order_by('-time_stamp')[0:8]
    moral=Videos.objects.filter(genres='Moral',first_youtuber=True).order_by('-time_stamp')[0:8]
    horror=Videos.objects.filter(genres='Horror',first_youtuber=True).order_by('-time_stamp')[0:8]
    action=Videos.objects.filter(genres='Action',first_youtuber=True).order_by('-time_stamp')[0:8]
    suspence=Videos.objects.filter(genres='Suspence',first_youtuber=True).order_by('-time_stamp')[0:8]
    scici=Videos.objects.filter(genres='Sci-Fi',first_youtuber=True).order_by('-time_stamp')[0:8]
    english=Videos.objects.filter(language='English',first_youtuber=True).order_by('-time_stamp')[0:8]
    telugu=Videos.objects.filter(language='Telugu',first_youtuber=True).order_by('-time_stamp')[0:8]
    video_playlist=Videoplaylist.objects.filter(first_youtuber=True)[0:8]
    list_quary=[
        videos,
        fant,
        comedy,
        moral,
        horror,
        action,
        suspence,
        scici,
        english,
        telugu,
        video_playlist
    ]
    context={
        'videos':videos,
        'fant':fant,
        'comedy':comedy,
        'moral':moral,
        'horror':horror,
        'action':action,
        'suspence':suspence,
        'scici':scici,
        'english':english,
        'telugu':telugu,
        'video_playlist':video_playlist,
        'list_quary':list_quary

    }
    return render(request,"frist_youtuber.html",context)

def top_rated(request):
    playlist=Playliststory.objects.filter(top_rated=True)
    short_storys=Story.objects.filter(subtitle__isnull=True,top_rated=True)
    video_playlist=Videoplaylist.objects.filter(top_rated=True)
    videos=Videos.objects.filter(top_rated=True)

    context={
        'playlist':playlist,
        'short_storys':short_storys,
        'video_playlist':video_playlist,
        'videos':videos
    }
    return render(request,"top_rated.html",context)

def vcomments(request):
    if request.method=="POST":
        comment=request.POST['comment']
        video=request.POST['video']
        videoinfo=Videos.objects.get(slug=video)
        comment=Vcomment.objects.create(msg=comment,slug=videoinfo)

        return redirect('/videoinfo/'+video)
    else:
        return redirect('/')
    
def scommnet(request):
    if request.method=="POST":
        comment=request.POST['comment']
        story=request.POST['story']
        print(comment,story)
        playlistinfo=Playliststory.objects.get(slug=story)
        comment=Scomment.objects.create(msg=comment,slug=playlistinfo)

        return redirect('/storyplaylist/'+story)
    else:
        return redirect('/')
    

def search(request):
    if request.method=="POST":
        search=request.POST['search']
        playlist=Playliststory.objects.filter(playlist_name__icontains=search)  
        short_storys=Story.objects.filter(title__icontains=search)
        video_playlist=Videoplaylist.objects.filter(playlist_name__icontains=search)
        videos=Videos.objects.filter(title__icontains=search)

        context={
        'playlist':playlist,
        'short_storys':short_storys,
        'video_playlist':video_playlist,
        'videos':videos
        }
        return render(request,"search.html",context)
    else:
        return redirect('/')
    
def terms(request):
    return render(request,"Privacy.html")

def credits(request):
    return render(request,"Credits.html")
        
    

        
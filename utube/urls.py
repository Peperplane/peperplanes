from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('videos/',views.videos,name="videos"),
    path('videoinfo/<str:slug>/',views.play_video,name="videoinfo"),
    path('story',views.story,name="story"),
    path('about',views.ContactUs.as_view(),name="about"),
    path('all/<str:value>/',views.videos_all,name="all"),
    path('sendstory',views.SendStory.as_view(),name="sendstory"),
    path('soon',views.soon,name="soon"),
    path('storyplaylist/<str:slug>/',views.storyplaylist,name="storyplaylist"),
    path('videoplaylist/<str:slug>/',views.video_playlist,name="videoplaylist"),
    path('storyconnect',views.story_connect,name="storyconnect"),
    path('firstyoutube',views.first_youtuber,name="firstyoutube"),
    path('toprated/',views.top_rated,name="toprated"),
    path('vcomment/',views.vcomments,name="vcomment"),
    path('scomment/',views.scommnet,name="scomment"),
    path('search/',views.search,name="search"),
    path('terms',views.terms,name="terms"),
    path('credits',views.credits,name="credits"),
    
]
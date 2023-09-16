from django.db import models
from autoslug import AutoSlugField
import uuid
# Create your models here.

class Videoplaylist(models.Model):
    playlist_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="playlist_video",blank=True,null=True)
    first_youtuber=models.BooleanField(default=False)
    top_rated=models.BooleanField(default=False)
    slug=AutoSlugField(populate_from='playlist_name',primary_key=True,editable=None,blank=False,null=False)
    

    def __str__(self) -> str:
        return self.playlist_name

class Videos(models.Model):
    title=models.CharField(max_length=50)
    sub_title=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(upload_to='video_imgs')
    desc=models.TextField()
    url=models.CharField(max_length=150)
    time_stamp=models.DateField(auto_now_add=True)
    genres=models.CharField(max_length=30,null=True,blank=True)
    language=models.CharField(max_length=50,default="Telugu")
    playlist=models.ForeignKey(Videoplaylist,on_delete=models.SET_NULL,blank=True,null=True)
    top_rated=models.BooleanField(default=False)
    first_youtuber=models.BooleanField(default=False)
    slug=AutoSlugField(populate_from='title',primary_key=True,editable=None,blank=False,null=False)

    def __str__(self) -> str:
        return self.title
    
class ContactUs(models.Model):
    id=models.UUIDField(primary_key=True,unique=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    message=models.TextField()
    image=models.ImageField(upload_to='contact_imges',blank=True,null=True)

    def __str__(self) -> str:
        return self.email
    
class StoryConnect(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=50,blank=True,null=True)
    story=models.TextField()
    image=models.ImageField(upload_to='storyconnect_imges',blank=True,null=True)
    url=models.CharField(max_length=150,blank=True,null=True)
    slug=AutoSlugField(populate_from='title',primary_key=True,editable=None,blank=False,null=False)

    def __str__(self) -> str:
        return self.email

    
class Playliststory(models.Model):
    playlist_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="playlist_story",blank=True,null=True)
    story_connect=models.BooleanField(default=False)
    top_rated=models.BooleanField(default=False)
    slug=AutoSlugField(populate_from='playlist_name',primary_key=True,editable=None,blank=False,null=False)

    def __str__(self) -> str:
        return self.playlist_name
       
class Story(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=50, blank=True,null=True)
    image=models.ImageField(upload_to='story_imges',blank=True,null=True)
    story_info=models.TextField()
    time_stamp=models.DateField(auto_now_add=True)
    plalist=models.ForeignKey(Playliststory,on_delete=models.SET_NULL,blank=True,null=True)
    story_connect=models.BooleanField(default=False)
    top_rated=models.BooleanField(default=False)
    slug=AutoSlugField(populate_from='title',primary_key=True,editable=None,blank=False,null=False)
    

    def __str__(self) -> str:
        return self.title
    
class Vcomment(models.Model):
    id=models.UUIDField(primary_key=True,unique=True, default=uuid.uuid4, editable=False)
    msg=models.TextField()
    slug=models.ForeignKey(Videos,on_delete=models.CASCADE)

    
class Scomment(models.Model):
    id=models.UUIDField(primary_key=True,unique=True, default=uuid.uuid4, editable=False)
    msg=models.TextField()
    slug=models.ForeignKey(Playliststory,on_delete=models.CASCADE)

    




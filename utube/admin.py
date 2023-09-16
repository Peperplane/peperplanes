from django.contrib import admin
from .models import Videos,ContactUs,StoryConnect,Story,Playliststory,Videoplaylist,Vcomment,Scomment
# Register your models here.
class VideosAdmin(admin.ModelAdmin):
    list_display=['title','sub_title','playlist','language','genres','top_rated','first_youtuber','time_stamp']
    search_fields=['title','language','genres','time_stamp']
    list_filter=['playlist','genres','language','top_rated','first_youtuber']
    list_editable=['top_rated','first_youtuber']

class VideoPlaylistAdmin(admin.ModelAdmin):
    list_display=['playlist_name','first_youtuber','top_rated']
    search_fields=['playlist_name']
    list_filter=['playlist_name','first_youtuber','top_rated']
    list_editable=['first_youtuber','top_rated']

class StoryAdmin(admin.ModelAdmin):
    list_display=['title','subtitle','plalist','top_rated','story_connect','time_stamp']
    search_fields=['title','time_stamp']
    list_filter=['plalist','top_rated','story_connect','time_stamp']
    list_editable=['top_rated','story_connect']

class StoryPlaylistAdmin(admin.ModelAdmin):
    list_display=['playlist_name','story_connect','top_rated']
    search_fields=['playlist_name']
    list_filter=['playlist_name','story_connect','top_rated']
    list_editable=['story_connect','top_rated']

class ContactusAdmin(admin.ModelAdmin):
    list_display=['name','email','message']
    search_fields=['name','email']
    list_filter=['name','email']

class StoryconnectAdmin(admin.ModelAdmin):
    list_display=['name','email','title','url']
    search_fields=['name','email','title']
    list_filter=['name','email']

class VcommentsAdmin(admin.ModelAdmin):
    list_display=['slug','msg']
    search_fields=['msg']
    list_filter=['slug']

class ScommentsAdmin(admin.ModelAdmin):
    list_display=['slug','msg']
    search_fields=['msg']
    list_filter=['slug']


admin.site.register(Videos,VideosAdmin)
admin.site.register(ContactUs,ContactusAdmin)
admin.site.register(StoryConnect,StoryconnectAdmin)
admin.site.register(Story,StoryAdmin)
admin.site.register(Playliststory,StoryPlaylistAdmin)
admin.site.register(Videoplaylist,VideoPlaylistAdmin)
admin.site.register(Vcomment,VcommentsAdmin)
admin.site.register(Scomment,ScommentsAdmin)


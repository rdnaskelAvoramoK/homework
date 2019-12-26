from django.contrib import admin
from .models import User, Video, Comment, Channel, Hystory, Playlist


class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(User)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Channel)
admin.site.register(Hystory)
admin.site.register(Playlist)
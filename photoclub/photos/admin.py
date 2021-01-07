from django.contrib import admin

# Register your models here.
from photoclub.photos.models import Photo, Like, Comment


# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'title', 'date',)
    list_filter = ('type', 'date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'photo_id')


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Like)
admin.site.register(Comment, CommentAdmin)

from django.contrib import admin
from django.contrib.auth.models import Group, User

from apps.models import Friend


#
# @admin.register(Category)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name']


# class CommentStackedInline(admin.StackedInline):
#     model = Comment
#     fields = ['name', 'body']
#
#
# @admin.register(Post)
# class PostModelAdmin(admin.ModelAdmin):
#     inlines = [CommentStackedInline]
#
#
# class PhotosStackedInline(admin.StackedInline):
#     model = Photo
#     fields = ['title', 'url']
#
#
# @admin.register(Album)
# class AlbumModelAdmin(admin.ModelAdmin):
#     inlines = [PhotosStackedInline]
#
#
@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'profession')


admin.site.unregister(Group)
admin.site.unregister(User)

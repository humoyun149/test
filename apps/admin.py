from django.contrib import admin
from django.contrib.auth.models import Group, User

from apps.models import Blog, Category

admin.site.register(Blog)
admin.site.register(Category)


admin.site.unregister(Group)

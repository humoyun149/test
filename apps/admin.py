from django.contrib import admin

from apps.models import People


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    pass

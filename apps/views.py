from django.shortcuts import render

from apps.models import Friend


def index_views(request):
    friends = Friend.objects.all()
    context = {
        'friends': friends
    }
    return render(request, 'apps/index.html', context)

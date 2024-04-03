from django.shortcuts import render

from apps.models import People


def index_views(request):
    context = {
        'people': People.objects.all()
    }
    return render(request, 'apps/index.html', context)

from django.shortcuts import render

from .models import Note


def index(request):
    pass


def page_not_found(request, exception=None):
    return render(
        request, 'misc/404.html',
        {'path': request.path}, status=404
    )


def server_error(request, exception=None):
    return render(request, 'misc/500.html', status=500)

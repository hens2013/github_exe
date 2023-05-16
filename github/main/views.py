# views.py file
from django.http import HttpResponse

from .models import PullRequest


def index(request):
    PullRequest.objects.create(title='asd', url='asd')
    return HttpResponse("Tech with tim!")

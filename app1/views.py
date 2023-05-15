from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Topic, Comment

# Create your views here.

def index(request):
    topic_list=Topic.objects.all()
    topic_dic={'topics':topic_list}
    return render(request, 'index.html', context=topic_dic)
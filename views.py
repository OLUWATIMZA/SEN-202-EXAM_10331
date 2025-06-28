from django.shortcuts import render
from models import post


def home(request):
    posts= post.objects,all().order_by('created at')
    return render(request," employess/home.html",{"post", post})

def manager(request):
     posts= post.objects,all()
     return render(request," employess/manager.html",{"post", post})


def intern(request):
     posts= post.objects,all()
     return render(request," employess/intern.html",{"post", post})

# Create your views here.

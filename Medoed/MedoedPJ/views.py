from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, "MedoedPJ/index.html", {"post": post})
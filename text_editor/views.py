from tkinter import YES
from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'text_editor/index.html')

def save_text(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        print(title, description)
        data = Editor.objects.create(title=title, text=description)
    return render(request, 'text_editor/show.html')

def show_data(request):
    return render(request, 'text_editor/show.html')
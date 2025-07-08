from django.shortcuts import render, redirect
from .models import *
from .forms import EditorForm

# Create your views here.

def index(request):
    form = EditorForm()
    return render(request, 'text_editor/index.html', {'form': form})

def save_text(request):
    if request.method == 'POST':
        description = request.POST['description']
        print(description)
        data = Editor.objects.create(text=description)  #ignore objects there is no error
    return render(request, 'text_editor/show.html')

def show_data(request):
    return render(request, 'text_editor/show.html')
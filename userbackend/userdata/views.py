from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import UploadedImage

def home(request):
    images = UploadedImage.objects.all()
    return render(request, 'home.html', {'images': images})

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})


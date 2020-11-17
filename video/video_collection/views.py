from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoForm, SearchForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models.functions import Lower

# Create your views here.

def home(request):
    app_name = 'Linguistics Videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})


# add a video
def add(request):
    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        
        if new_video_form.is_valid():
            try:
                new_video_form.save() # save if form is valid
                return redirect('video_list')
            except ValidationError:
                messages.warning(request, 'Invalid YouTube URL')
            except IntegrityError:
                messages.warning(request, 'Video already added')
            
        messages.warning(request, 'Invalid! Check your data!')
        
        # show page with previously entered form data
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})
        
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})


# display list of saved Videos
def video_list(request):
    
    search_form = SearchForm(request.GET)
    
    if search_form.is_valid():
        # only list videos matching the search term
        search_term = search_form.cleaned_data['search_term']
        videos = Video.objects.filter(name__icontains=search_term).order_by(Lower('name'))
        
    else:
        search_form = SearchForm()
        videos = Video.objects.order_by(Lower('name'))
        
    return render(request, 'video_collection/video_list.html', {'videos': videos, 'search_form': search_form})


# display detail about a video
def video_detail(request, video_pk):
    video = get_object_or_404(Video, pk=video_pk)
    return render(request, 'video_collection/video_detail.html', {'video': video})

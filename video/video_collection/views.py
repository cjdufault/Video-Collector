from django.shortcuts import render

# Create your views here.

def home(request):
    app_name = 'Linguistics Videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

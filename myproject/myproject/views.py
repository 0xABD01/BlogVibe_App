# from django.http import HttpResponse

from django.shortcuts import render
from posts.models import Post


def home(request):
    latest_posts = Post.objects.order_by('-date')[:5]  # Adjust number as needed
    return render(request, 'home.html', {
        'latest_posts': latest_posts,
    })
def about(request):
    return render(request, 'about.html')  # Render the about.html template

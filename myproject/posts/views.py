from django.shortcuts import render, redirect  
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms   

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'posts/posts_list.html', {'posts': posts})  # Pass the posts to the template

def post_page(request, slug):
    post = Post.objects.get(slug=slug)  # Fetch the post with the given slug from the database
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url='/users/login/') 
def post_new(request):
    if request.method == 'POST':                             
        form = forms.CreatePost(request.POST, request.FILES)  ## Create an instance of the form with the POST data
        if form.is_valid():  
            newPost = form.save(commit=False)     ## Create a new Post instance without saving it to the database yet
            newPost.author = request.user         ## Set the author of the post to the currently logged-in user
            newPost.save()                        ## Save the new Post instance to the database                               
            return redirect('posts:list')      ## Redirect to the post list
    else:                                                    ## If the request method is not POST, create a new form instance
        form = forms.CreatePost()                               ## Create an instance of the form
    return render(request, 'posts/post_new.html', {'form': form})
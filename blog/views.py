from django.shortcuts import render
from .models import Post

# posts = [
  # Dummy Data
#   {
#     'author'      : 'Seanw', 
#     'title'       : 'blog post 1',
#     'content'     : 'First Post',
#     'date_posted' : 'Sept 21, 2018'
#   },
#   {
#     'author'      : 'Seanw', 
#     'title'       : 'blog post 2',
#     'content'     : 'Second Post Post',
#     'date_posted' : 'Sept 21, 2018'
#   }
# ]
# Create your views here.

def home(request):
  context = {
    'posts': Post.objects.all
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})
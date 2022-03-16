from django.shortcuts import render

# здесь настраивается отображение д-х
from post.models import Post


def post_list(request):
    posts = Post.objects.all()   #select * from Post
    return render(request, 'blog/blog.html', context={'post': posts})


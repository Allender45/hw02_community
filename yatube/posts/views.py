from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    return render(request, 'index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    latest = group.posts.all()[:13]
    return render(request, 'group.html', {'posts': latest, 'group': group, })

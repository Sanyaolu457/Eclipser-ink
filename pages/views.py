from django.shortcuts import render,get_object_or_404
from posts.models import Tag, POST

def home(request):
    posts = POST.objects.all().prefetch_related('tags', 'mentions').order_by('-created_at')
    all_tags = Tag.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
        'all_tags': all_tags
    })

def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = POST.objects.filter(tags=tag).prefetch_related('tags', 'mentions').order_by('-created_at')
    all_tags = Tag.objects.all()
    return render(request, 'posts_by_tag.html', {'posts': posts, 'tag': tag, 'all_tags': all_tags})

def post_detail(request, slug):
    post = get_object_or_404(POST, slug=slug)

    related_posts = POST.objects.filter(
        tags__in=post.tags.all()
    ).exclude(pk=post.pk).distinct()[:4]

    return render(request, 'post_detail.html', {
        'post': post,
        'related_posts': related_posts,
    })
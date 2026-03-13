from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm
from authentication.models import Participant
from .models import POST

@login_required(login_url='login')
def create_post(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.save()
           form.save_m2m()
           return redirect ('home')
        
    else:
        form = PostForm()

    return render(request, 'create_post.html', {
        'form': form
    })

def user_profile(request, username):
    participant = get_object_or_404(Participant, username = username)
    posts = POST.objects.filter(author=participant).order_by('-created_at')
    return render (request, 'profile.html', {
        'participant': participant,
        'posts': posts
    })

@login_required(login_url='login')
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile.bio = request.POST.get('bio', '')
        if request.FILES.get('image'):
            profile.image = request.FILES['image']
        profile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('user_profile', username=request.user.username)
    return render(request, 'edit_profile.html', {'profile': profile})

@login_required(login_url='login')
def delete_account(request):
    request.user.delete()
    return redirect('home')

from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from .models import Song, Type
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .form import RegisterUserForm, AddMusic
from django.contrib import messages


def home(request):
    single = Song.objects.filter()[:3]
    best = Song.objects.filter()[:5]
    songs = Song.objects.all()
    type = Type.objects.all()
    user = request.user
    content = {
        'songs':songs,
        'single':single,
        'best':best,
        'type':type,
        'user':user
    }

    return render(request, 'audio/index.html', content )

def list(request):
    song = Song.objects.all()
    content = {
        'song':song
    }

    return render(request, 'audio/song_list.html', content)

def detail(request, pk):
    song = Song.objects.get(id=pk)
    content = {
        'song':song
    }
    return render(request, 'audio/detail.html', content)
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        music = Song.objects.filter(title__contains=searched)
        return render(request, 'audio/search.html', {'searched':searched, 
        'music':music})
    else:
        return render(request, 'audio/search.html', {})

def like_post(request, pk):
    user = request.user
    song = get_object_or_404(Song,id=request.POST.get('song_id'))
    liked = False
    if song.like.filter(id=user.id).exists():
        song.like.remove(request.user)
        liked = False
    else:
        song.like.add(request.user)
        liked=True


    return HttpResponseRedirect(reverse('home'))

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('login')
    else:
        return render(request, 'audio/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logged Out, Try Logging Again..."))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'audio/register.html', {'form':form})


def create_music(request):
    if request.method == 'POST':
        form = AddMusic(request.POST )
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddMusic()

    context = {'form':form}
    return render(request, 'audio/upload.html', context)


def CategoryView(request, cats):
    genre = Song.objects.filter(genre=cats)
    return render(request, 'audio/categories.html', {'cats':cats, 'genre':genre})

def CountryView(request, cats):
    country = Song.objects.filter(country=cats)
    return render(request, 'audio/countries.html', {'cats':cats, 'country':country})
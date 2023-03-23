from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def index(request):
    G = Genre.objects.all()
    F = Film.objects.all()

    context = {
        'Genre': G,
        'Film': F
    }
    return render(request, 'base.html', context)


def get_genre(request, genre_id):
    g = Genre.objects.all()
    F = Film.objects.filter(genre_id = genre_id).all()

    context = {
        'Genre': g,
        'Film': F
    }

    return render(request, 'genre.html', context)


def get_film(request, film_id):
    f = Film.objects.get(id = film_id)
    g = Genre.objects.all()
    A = Answer.objects.all()

    f_view=f.view
    Film.objects.filter( id = film_id ).update( view = f_view + 1 )

    if Actor.objects.filter(film_id = film_id):
        a = Actor.objects.filter(film_id = film_id).all()
    else:
        a = None

    if request.method == 'POST':

        if Review.objects.filter(review_author = str(request.user.username),
                                 review_text = request.POST.get("review-text"),
                                 film_id = film_id):
            pass
        else:
            if request.POST.get("review-id", None):
                if Answer.objects.filter(answer_author = str(request.user.username),
                                         answer_text = request.POST.get("review-text"),
                                         reviews_id = request.POST.get("review-id")):
                    pass
                else:
                    Answer.objects.create(answer_author = str(request.user.username),
                                          answer_text = request.POST.get("review-text"),
                                          reviews_id = request.POST.get("review-id")).save()
            else:
                Review.objects.create(review_author = str(request.user.username),
                                      review_text = request.POST.get("review-text"),
                                      film_id = film_id).save()

    context = {
        'Film': f,
        'Genre': g,
        'Actor': a,
        'Answer': A,

    }

    return render(request, 'film.html', context)


def user_register(request):
    g = Genre.objects.all()

    if request.method == 'POST':

        reg_user = UserRegisterForm(request.POST)
        if reg_user.is_valid():

            reg_user.save()

            username = request.POST.get('username')
            password = request.POST.get('password1')
            log_user = authenticate(username = username, password = password)
            login(request, log_user)

            if UserDescription.objects.filter(user_id = log_user.id, description = request.POST.get('description')):
                pass
            else:
                UserDescription.objects.create(user_id = log_user.id,
                                               description = request.POST.get('description')).save()

            return redirect('/')

    else:
        reg_user = UserRegisterForm()

    context = {
        'user': reg_user,
        'Genre': g
    }
    return render(request, 'register.html', context)


def liked_films(request, film_id):
    if not LikedFilms.objects.filter(user = request.user, films_id = film_id):
        LikedFilms.objects.create(user = request.user, films_id = film_id).save()




    return redirect(f'/film/{film_id}')


def user_profile(request):
    if UserPhoto.objects.filter(user = request.user):
        userphoto = UserPhoto.objects.get(user = request.user)
    else:
        userphoto = ''

    if UserDescription.objects.filter(user = request.user):
        userdesc = UserDescription.objects.get(user = request.user)
    else:
        userdesc = ''

    if request.method == 'POST':

        if request.POST.get('desc-text'):
            if UserDescription.objects.filter(user = request.user) is not True:
                UserDescription.objects.create(user = request.user, description = request.POST.get('desc-text')).save()
                return redirect('/profile')

        if request.FILES.get('profile-image'):
            if UserPhoto.objects.filter(user = request.user) is not True:
                UserPhoto.objects.create(user = request.user, photo = request.FILES.get('profile-image')).save()
                return redirect('/profile')

    context = {
        'user': request.user,
        'userphoto': userphoto,
        'desc': userdesc
    }

    return render(request, 'profile.html', context)


def user_login(request):
    g = Genre.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_user = authenticate(username = username, password = password)

        if login_user is not None:
            login(request, login_user)

            return redirect('/')

    context = {
        'Genre': g
    }
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('/')


def search(request):
    search = request.POST.get('search')
    g = Genre.objects.all()
    f = Film.objects.filter(name__icontains = search).all()

    context = {
        'Genre': g,
        'Film': f
    }
    return render(request, 'search.html', context)

def create_film(request):

    G = Genre.objects.get(genre=request.POST.get('genre'))
    Film.objects.create(
        name=request.POST.get('name'),
        producer=request.POST.get('produser'),
        rating=request.POST.get('rating'),
        warning_age=request.POST.get('warning_age'),
        description=request.POST.get('desc'),
        img=request.FILES.get('img'),
        genre=G, path_video=request.FILES.get('path_video')
    ).save()
    F = Film.objects.get(name=request.POST.get('name'))
    UserCreatedFilms.objects.create( user = request.user, films_id = F.id).save()

    return redirect('/profile')
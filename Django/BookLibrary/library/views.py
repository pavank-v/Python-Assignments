from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SearchBook, UserLoginForm, UserRegisterForm
from .models import Book, SearchHistory, Users
from .scrapping import BookDetails


def home(request):
    if request.user.is_authenticated:
        return render(request, 'library/home.html')
    else:
        return render(request, 'library/signin.html')
    
@login_required(login_url='signin') 
def search_books(request):
    if request.method == 'POST':
        form = SearchBook(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            details = BookDetails(title)
            amazon_url = details.amazon_link
            flipkart_url = details.flipkart_link
            good_reads_review = details.good_reads_review
            cover_image = details.cover_image
            
            # Record search history
            if not SearchHistory.objects.filter(title=title).exists():
                SearchHistory.objects.create(
                    title=title,
                    cover_image=cover_image,
                    amazon_url=amazon_url,
                    flipkart_url=flipkart_url,
                    good_reads_review=good_reads_review
                )
            context = {
                'title':title,
                'amazon_url':amazon_url,
                'flipkart_url':flipkart_url,
                'good_reads_review':good_reads_review,
                'cover_image':cover_image,
            }
            return render(request, 'library/search_result.html', context)
    else:
        form = SearchBook()
        
    return render(request, 'library/base.html', {'form':form})

@login_required(login_url='signin')
def add_to_favorites(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        cover_image = request.POST.get('cover_image')
        amazon_url = request.POST.get('amazon_url')
        flipkart_url = request.POST.get('flipkart_url')
        good_reads_review = request.POST.get('good_reads_review')
        
        if not Book.objects.filter(title=title).exists():
            Book.objects.create(
                    user=user,
                    title=title,
                    cover_image=cover_image,
                    amazon_url=amazon_url,
                    flipkart_url=flipkart_url,
                    good_reads_review=good_reads_review,
                )
        return redirect('favourites') 

    return redirect('home')

@login_required(login_url='signin')
def favourites(request):
    books = Book.objects.all()
    return render(request, "library/favourites.html",{'books':books})

@login_required(login_url='signin')
def base(request):
    form = SearchBook()
    return render(request, 'library/base.html', {'form': form})

@login_required(login_url='signin')
def search_history(request):
    search_history = SearchHistory.objects.all()
    return render(request, 'library/search_history.html', {'search_history': search_history})


def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r, )
        if user:
            login(request, user)
            return render(request, 'library/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'library/signup.html', context)
    else:
        return render(request, 'library/signup.html', context)


def signin(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            login(request, user)
            # username = request.session['username']
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'library/base.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'library/signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'library/signin.html', context)


def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'library/signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'library/success.html', context)

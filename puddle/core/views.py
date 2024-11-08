from django.shortcuts import render, redirect
from item.models import Catergory, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Catergory.objects.all()
    context = {
        'categories': categories,
        'items': items,
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(requset):
    return render(requset, 'about.html')


# def login(request):
#     return render(request, 'login.html')
#

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.urls import reverse

from .forms import RegistrationForm
from .models import User


def list(request):
    users = User.objects.all()
    template = loader.get_template('users/list.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    return render(request, 'users/index.html')


def add(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.save(email, password)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = RegistrationForm()
    return render(request, 'users/add.html', {'form': form})

from django.shortcuts import render, redirect
import random


def home(request):
    return render(request, 'generator/home.html', {})


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        for i in range(len(characters)):
            characters.append(characters[i].upper())
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length'))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def refresh(request):
    redirect('password/')

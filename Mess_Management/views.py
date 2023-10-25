from django.shortcuts import render, redirect, reverse

def HomePage(request):
    return render(request, 'home.html')
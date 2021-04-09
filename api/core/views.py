from django.shortcuts import render, redirect


def index(request):
    context = {

    }
    return render(request, 'core/index.html', context=context)

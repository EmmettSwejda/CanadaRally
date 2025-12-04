from django.shortcuts import render, redirect
from .forms import locationForm


def home(request):
    return render(request, 'base.html')


def createLocation(request):
    if request.method == "POST":
        sv = locationForm(request.POST)
        if sv.is_valid():
            sv.save()
            return redirect("home")
    else:
        form = locationForm()

    return render(request, 'createLocation.html', {'form': form})
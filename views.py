# views.py
from django.shortcuts import render

def index(request):
    """View function for the index page of the website."""
    return render(request, 'index.html')
"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Pupil

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def list(request):
    """Renders the list page."""
    assert isinstance(request, HttpRequest)
    pupils = Pupil.objects.all()
         
    return render(
        request,
        'app/list.html',
        {
            'pupils': pupils,
            'title':'Список',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def portfolio(request):
    """Renders the portfolio page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/portfolio.html',
        {
            'title':'Портфолио',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

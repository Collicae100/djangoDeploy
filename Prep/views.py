from django.shortcuts import render
from django.utils import timezone
from .models import Starter

def post_list(request):
    starter = Starter.objects.all()
    return render(request, 'Prep/app.html', {'starter': starter})

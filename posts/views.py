from django.shortcuts import render
from django.views.generic.list import ListView
from . import models

# Create your views here.
class BlogListView(ListView):
    queryset = models.Entry.objects.published()
    paginate_by = 20

def index(request):
    return render(request, 'posts/index.html')

def post(request,slug):
    return render(request, 'posts/index.html')

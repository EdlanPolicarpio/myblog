from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from . import models
from . import forms

# Create your views here.
class EntryListView(ListView):
    queryset = models.Entry.objects.published()
    paginate_by = 20

def index(request):
    return render(request, 'posts/index.html')

def entry(request,slug):
    entry = get_object_or_404(models.Entry, slug=slug)
    context = {"entry":entry}
    return render(request, 'posts/entry.html', context)

def create(request):
    if request.method == 'POST':
        #create form
        form = forms.EntryForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/entries')
    else:
        form = forms.EntryForm() 
    context = {'form':form}
    return render(request, 'posts/create.html',context)

def edit(request,slug):
    entry = get_object_or_404(models.Entry, slug=slug)
    if request.method == 'POST':
        form = forms.EntryForm(instance = entry, data = request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/entries')
    else:
        init = {"title":entry.title, "body":entry.body, 
	"published":entry.published, "slug":entry.slug}
        form = forms.EntryForm(instance = entry, initial = init)

    context = {"form":form, "entry":entry}
    return render(request, 'posts/edit.html', context)

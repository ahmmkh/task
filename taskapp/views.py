# -*- coding: utf-8 -*-
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import redirect

#from __future__ import unicode_literals
from django.shortcuts import render
from .models import Task
from .forms import add_form
import timeago

def index(request):
    all_tasks = Task.objects.all()
   # count = all_tasks.count()
    #undone = Task.objects.filter(done=False).count()
    context = {'objects':all_tasks}
    return render(request, "dd.html",context = context)
def not_finshed(request):
    all_tasks = Task.objects.all().filter   (done=False)
   # count = all_tasks.count()
    #undone = Task.objects.filter(done=False).count()
    context = {'objects':all_tasks}
    return render(request, "dd.html",context = context)
def add_task(request):
    if request.method == 'POST':
        form = add_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            done = form.cleaned_data['done']
            try:
                val = int(done) ==1
                print val
            except ValueError:
                print("not value")
            
            task = Task.objects.create(title = title, desc = desc , done= val)
            return redirect("index")
    else:
        return render(request,"add.html")
def edit_task(request,task_id):
    if request.method == 'POST':
        form = add_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            done = form.cleaned_data['done']
            try:
                val = int(done)
            except ValueError:
                print("That's not an int!")
            task = Task.objects.get(id=task_id)
            task.title = title
            task.desc = desc
            task.done = val
            task.save()
            return redirect("index")
    else:
        task = Task.objects.get(id=task_id)
        context = {'task_to_edit':task}
        return render(request,"edit.html",context=context)
def delete(request,task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("index")
# Create your views here.

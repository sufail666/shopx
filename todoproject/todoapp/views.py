from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.models import Task

from .forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class listview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'

class detailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class updateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cdetail',kwargs={'pk':self.object.id})

class deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


def home(request):
    task=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task2=Task(name=name,priority=priority,date=date)
        task2.save()

    return render(request,'index.html',{'task':task})

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id1):
    task=Task.objects.get(id=id1)
    form=todoform(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})

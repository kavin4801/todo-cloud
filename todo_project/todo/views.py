from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.is_completed = 'is_completed' in request.POST
        task.save()
        return redirect('task_list')
    return render(request, 'todo/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

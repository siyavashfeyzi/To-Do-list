from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from . models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todolist/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        """""
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        completed = request.POST.get('completed', False)
        create_at = timezone.now()
        last_update = timezone.now()
        Task.objects.create(title=title, description=description,
                            completed=completed, create_at=create_at, last_update=last_update)
        """""
        task = Task()
        task.title = request.POST.get('title', '')
        task.description = request.POST.get('description', '')
        task.completed = request.POST.get('completed', False)
        task.create_at = timezone.now()
        task.last_update = timezone.now()
        task.save()
        return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
